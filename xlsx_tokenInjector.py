from zipfile import ZipFile
import os
import sys
import datetime
import logging
import argparse
import modules.processing as proc
import modules.crypt as crypt

if __name__ == "__main__":
    datetimenow = datetime.datetime.now()
    templatePath = "./templates/ExcelTemplate.xlsx"
    outputFolder = "./output/"
    workfolder = "./workfolder/"
    outputfilexl = f"{outputFolder}{datetimenow}.xlsx"
    outputfilezip = f"{outputFolder}{datetimenow}"
    nulls = ["", "\n", " ", "\r\n"]

    # Argument Parser Configuration
    description = "Placeholder Description"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '-u', '--url', 
        help='Provide listener IP/URL', 
        type=str,
        required=True
    )
    parser.add_argument(
        '-t', '--tags', 
        help='Provide tags associated with the file', 
        type=str,
        required=False
    )
    parser.add_argument(
        '-v', '--verbose', 
        help='Provide tags associated with the file', 
        default=0,
        action='store_true',
        required=False
    )
    args=parser.parse_args()

    # Logger Configuration
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    if args.verbose:
        console_handler.setLevel(logging.DEBUG)

    # Parse and validate listener
    listener = str(args.url)
    if(proc.validateURL(listener)):
        logging.info(f"URL validation for {listener} successful")
    else:
        raise TypeError("Invalid url format\n Please enter url in formats: http(s)://domain.tld:port OR http(s)://IP:port\nPort is optional unless using non-standard ports for http(80) and https(443) protocols")
    # Pending: integrate some identifier for file

    outputTags = args.tags
    if (outputTags in nulls):
        outputTags="None"
    logging.info(f"Proceeding with listener: {listener} and tags: {outputTags}")

    proc.emptyFolder(workfolder=workfolder)
    proc.unzip(template=templatePath, workfolder=workfolder)
    embedFilePath = "workfolder/xl/drawings/_rels/drawing1.xml.rels"
    proc.embedListener(listener=listener, placeholder_val="REPLACEMENTURI", file_path=embedFilePath)
    proc.zip(output=outputfilezip,workfolder=workfolder)
    logging.debug(f"Renaming file to {outputfilexl}")

 

    os.rename(outputfilezip+".zip", outputfilexl)
    fileHashmd5 = crypt.summd5(outputfilexl)
    fileHashsha1 = crypt.sumsha1(outputfilexl)
    fileHashsha256 = crypt.sumsha256(outputfilexl)
    os.rename(outputfilexl, f"{outputFolder}{fileHashmd5}.xlsx")
    logging.info(f"Decoy creation successful...\nFile stored in : {outputfilexl}\nMD5 Sum: {fileHashmd5}\nSHA1 Sum: {fileHashsha1}\nSHA256 Sum: {fileHashsha256}")
    proc.emptyFolder(workfolder=workfolder)
