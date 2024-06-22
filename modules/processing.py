import os, shutil
from zipfile import ZipFile
import logging
import validators
import re

def emptyFolder(workfolder="./workfolder"):
    logging.debug("Attempting to clean workfolder...")
    for filename in os.listdir(workfolder):
        file_path = os.path.join(workfolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logging.exception(f'Failed to delete {file_path}. Reason: {e}')
    logging.debug("Cleanup Successful\n")

def unzip(template="",workfolder=""):
    logging.debug(f"Starting unzipping {template} to {workfolder}...")
    try:
        with ZipFile(template, 'r') as zObj: 
            zObj.extractall(path=workfolder) 
    except Exception as e:
        logging.exception("Unzipping failed for the template\n-------Exception encountered-------\n",e)
    logging.debug(f"Unzip Successful\n")

def zip(output="",workfolder=""):
    logging.debug("Attempting to reassemble the components of the decoy...")
    try:
        archived = shutil.make_archive(output, 'zip', workfolder)
        logging.debug(archived) 
    except Exception as e:
        logging.exception("Error zipping/compressing the file.\n",e)
    logging.debug("Reassembly Successful\n")

def embedListener(listener="", placeholder_val="REPLACEMENTURI", file_path=""):
    logging.debug("Attempting to embed the listener into file...")
    try:
        with open(file_path, 'r') as f:
            temp = f.read().replace(placeholder_val,listener)
        with open(file_path, 'w') as f:
            temp = f.write(temp)
    except Exception as e:
        logging.exception(f"Failed embedding listener ({listener}) into the file for the given placeholder ({placeholder_val}) in the template. Error:\n{e}")
    logging.debug(f"Successfully embedded listener ({listener}) to the decoy\n")

def validateURL(url):
    # Taken from https://stackoverflow.com/a/7995979 Thank you :)
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return (url is not None and validators.url(url) or regex.match(url) )