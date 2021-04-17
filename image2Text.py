''' 
This  script expects 2 arguments: 
 1 - A folder containing jpg or  png images from paper document scans
 2 - A folder,  where text generated from images will be stored 
'''
import os 
from os import path
import sys
import logging
arguments = sys.argv
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


#method to test if folder exists
def folder_exists(absolute_path):
    return path.exists(absolute_path) and path.isdir(absolute_path)
    
def exit_program_with_error (err_message):
    logging.error(err_message)
    logging.info('exiting the program ...')
    exit(1)

def main():
    #for this example , we support only png and jpg files , but feel free to extend supported formats
    supported_ext = ['.jpg','.png']
    if  len(arguments)< 3 :
        exit_program_with_error('This  script expects 2 arguments :\n 1- A folder containing jpg or  png images from paper document scans \n 2 - A folder,  where text generated from images will be stored ')
    else :
        imagesDir = sys.argv[1]
        textDir = sys.argv[2]
        if not folder_exists(imagesDir):
            exit_program_with_error('the image input folder does not exist')

        image_files = os.listdir(imagesDir)
    
        #supported_files = [image_file   for image_file in image_files if len(os.path.splitext(image_file)) == 2 ]
        supported_files = [image_file   for image_file in image_files if len(os.path.splitext(image_file)) == 2 and (os.path.splitext(image_file)[1]) in supported_ext ]
        logging.info(str(len(supported_files)) +' support files found in '+ imagesDir)
        if not os.path.exists(textDir) :
            logging.info("creating folder :" + textDir)
            os.makedirs(textDir)
        for supported_file in supported_files :
            filename = os.path.splitext(supported_file)[0]
            logging.info('converting '+ supported_file+' to text ...' )
            absolutepath2file = os.path.join(imagesDir,supported_file)
            logging.info(absolutepath2file)
            text = pytesseract.image_to_string(Image.open(absolutepath2file))
            f = open(os.path.join(textDir,filename+".txt"), "w")
            f.write(text)
            f.close()

if __name__== "__main__":
   main()