from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PIL.ExifTags import TAGS
import os
import shutil
import io
import whatimage



def check_img(img):
    okay = ["jpg","JPG","jpeg","JPEG"]
    if img.split(".")[-1] in okay:
        return True
    else:
        return False


def sort_imgs(root_src_dir):

    for src_dir, dirs, files in os.walk(root_src_dir): #os.walkthrough
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            if check_img(src_file): #check the image with the programm check_img

                _TAGS_r = dict(((v, k) for k, v in TAGS.items())) # Get Metadates
                with Image.open(src_file) as im:  # open and close file
                    exifdata = im.getexif()
                keys = list(exifdata.keys())
                keys = [k for k in keys if k in TAGS] # get a list with all tags
                datetime = "\n".join([str((TAGS[k], exifdata[k])) for k in keys if TAGS[k] == "DateTime"]) # check date
                year = datetime.split(", '")[-1].split(":")[0] # get year

                if year == "": ## if no year exists, get archived
                    shutil.copy(src_file,"F:\\Sicherung Google Fotos\\Ohne_Datum")
                    print(f"{src_file} has no Date and has been moved to F:\\Sicherung Google Fotos\\Ohne_Datum")
                    os.remove(src_file)
                else: ## if there's a year, create a folder and move it into
                    if year in os.listdir(f"{root_src_dir}"):
                        pass
                    else:
                        os.mkdir(f"{root_src_dir}\\{year}")

                    try:
                        shutil.copy(src_file, f"{root_src_dir}\\{year}")
                        print(f"{src_file} has been moved to {year}")
                        os.remove(src_file)
                    except shutil.SameFileError:
                        continue


def get_heic(root_src_dir):
    try:
        os.mkdir(f"F:\\Sicherung Google Fotos\\heic")
    except FileExistsError:
        pass
    counter = 0
    for src_dir, dirs, files in os.walk(root_src_dir): #os.walkthrough
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            if src_file.split(".")[-1] in ["heic","HEIC"]: #check the image with the programm check_img
                try:
                    shutil.copy(src_file,f"F:\\Sicherung Google Fotos\\heic")
                    os.remove(src_file)
                    print("converted.")
                    counter += 1
                except shutil.SameFileError:
                    continue
    print(f"moved {counter} .heic's")

get_heic("F:\\Sicherung Google Fotos\\Alle Einzeln")
#sort_imgs("F:\\Sicherung Google Fotos\\Google Fotos\\Archiv")

