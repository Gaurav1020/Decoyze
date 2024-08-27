import socket
import requests
import json
import logging
from ipaddress import ip_address, AddressValueError

# Configure logging to securely log information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the IP address and port on which to listen
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 4444      # Choose your desired port

# Function to get geolocation information for an IP address
def get_geolocation(ip):
    try:
        # Validate the IP address
        ip_address(ip)

        # Fetch geolocation data from a trusted source
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        
        # Ensure the response is valid
        if response.status_code == 200:
            return response.json()
        else:
            logging.warning(f"Failed to fetch geolocation data for {ip}. Status code: {response.status_code}")
            return None
    except (requests.RequestException, AddressValueError) as e:
        logging.error(f"Error fetching geolocation data for {ip}: {e}")
        return None

# Function to parse HTTP headers and extract the data
def parse_http_request(data):
    try:
        # Decode the received bytes to a string
        decoded_data = data.decode('utf-8', errors='ignore')
        
        # Split headers and body
        headers_part, body_part = decoded_data.split("\r\n\r\n", 1)
        
        # Parse headers into a dictionary
        headers_lines = headers_part.split("\r\n")
        headers = {}
        for header in headers_lines[1:]:  # Skip the first line (Request Line)
            key, value = header.split(":", 1)
            headers[key.strip()] = value.strip()

        # Parse the body into a dictionary (if it's JSON)
        try:
            body = json.loads(body_part)
        except json.JSONDecodeError:
            body = body_part  # If it's not JSON, just return the raw body

        return headers, body
    except Exception as e:
        logging.error(f"Error parsing HTTP request: {e}")
        return None, None

# Function to safely handle incoming data and drop the connection afterward
def handle_client(client_socket, client_address):
    ip, port = client_address
    logging.info(f"Connection received from {ip}:{port}")

    try:
        # Receive the data from the client
        data = client_socket.recv(1024)  # 1024 is the buffer size
        if data:
            # Parse the HTTP request to extract headers and body
            headers, body = parse_http_request(data)
            
            if headers:
                # Log all headers
                logging.info(f"Headers: {json.dumps(headers, indent=2)}")

                # Extract the X-Forwarded-For header if it exists
                x_forwarded_for = headers.get('X-Forwarded-For')
                if x_forwarded_for:
                    logging.info(f"X-Forwarded-For header found: {x_forwarded_for}")

                    # Optionally geolocate the X-Forwarded-For IP address
                    geolocation_data = get_geolocation(x_forwarded_for.split(",", 1)[0])
                    if geolocation_data:
                        logging.info(f"Geolocation data for X-Forwarded-For {x_forwarded_for}: {json.dumps(geolocation_data, indent=2)}")
                else:
                    logging.info("X-Forwarded-For header not found in the request.")

            if body:
                # Log the body data
                logging.info(f"Body: {json.dumps(body, indent=2) if isinstance(body, dict) else body}")
                
    except socket.error as e:
        logging.error(f"Error receiving data from {ip}:{port}: {e}")
    finally:
        # Drop the connection
        logging.info(f"Dropping connection from {ip}:{port}")
        client_socket.close()

# Main server loop
def start_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Set socket options to reuse the address
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Bind the socket to the address and port
            server_socket.bind((HOST, PORT))
            
            # Start listening for incoming connections
            server_socket.listen()
            logging.info(f"Listening securely on {HOST}:{PORT}...")

            while True:
                # Accept a new connection
                client_socket, client_address = server_socket.accept()
                handle_client(client_socket, client_address)
    except Exception as e:
        logging.critical(f"Server encountered a critical error: {e}")

# Run the server
if __name__ == "__main__":
    start_server()

