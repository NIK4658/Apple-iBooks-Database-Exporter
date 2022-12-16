import shutil
import getpass
import os
import glob

# Get the username of the current user
USERNAME = getpass.getuser()

# Set the source path of the database files
SRC_ANNOTATION_DB_PATH = "/users/"+USERNAME+"/Library/Containers/com.apple.iBooksX/Data/Documents/AEAnnotation/"
SRC_BOOK_DB_PATH = "/users/"+USERNAME+"/Library/Containers/com.apple.iBooksX/Data/Documents/BKLibrary/"

# Set the destination path of the database files
DST_ANNOTATION_PATH = "./Output/Annotations.sqlite"
DST_BOOKS_PATH = "./Output/Books.sqlite"

# Get the database files
ANNOTATION_DATABASE_FILE = glob.glob(os.path.join(SRC_ANNOTATION_DB_PATH, "*.sqlite"))
BOOKS_DATABASE_FILE = glob.glob(os.path.join(SRC_BOOK_DB_PATH, "*.sqlite"))

# Check if the database files are found
if(len(ANNOTATION_DATABASE_FILE) == 0 or len(BOOKS_DATABASE_FILE) == 0):
    print("Error: Database file not found")
    exit()
else:
    print("Database file found")
    # Get the path of the database files
    ANNOTATION_DATABASE_FILE_PATH = str(ANNOTATION_DATABASE_FILE[0])
    BOOKS_DATABASE_FILE_PATH = str(BOOKS_DATABASE_FILE[0])
    # Copy the database files to the destination path
    shutil.copyfile(ANNOTATION_DATABASE_FILE_PATH, DST_ANNOTATION_PATH)
    shutil.copyfile(BOOKS_DATABASE_FILE_PATH, DST_BOOKS_PATH)
    print("Database copied")
