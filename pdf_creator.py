from os import listdir
from os.path import isfile, join
import os
from PIL import Image

directory_path = os.getcwd()
# print("My current directory is : " + directory_path)
folder_name = os.path.basename(directory_path)
# print("My directory name is : " + folder_name)

imagelist = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
imagelist.remove('pdf_creator.py')
imagelist.remove(f'{folder_name}.pdf')
imagelist.sort(key=lambda x: os.path.getmtime(x))


print(imagelist)

imagelist_opened = [Image.open(image) for image in imagelist]


pdf1_filename = f'{folder_name}.pdf'

imagelist_opened[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=imagelist_opened[1:])