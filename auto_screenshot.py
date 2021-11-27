import pyautogui
import time
import os
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import numpy as np

num_of_minutes = int(input('Enter duration of lecture (minutes): '))
lecture_title = ((input('Enter name of lecture: ')).replace(' ', '_'))
wait_beetwen_screen = float(input('How long to wait between next screenshot (for example 5) (seconds): '))

if not os.path.exists(lecture_title):
    os.mkdir(lecture_title)
    print("Directory " , lecture_title ,  " Created ")
else:
    print("This directory " , lecture_title ,  " Already exist. I will overwitten it and files in that directory. Are you sure to continue?")
    answer = input('[yes]/[no]: ')
    if answer == 'no':
        quit()

i = 1
status = True

stop_cond = num_of_minutes*60/wait_beetwen_screen

while status:
    if i == stop_cond:
        status = False
    elif i == 1:
        # time.sleep(3)  # wait 3 seconds before first screenshot
        my_screen_shot = pyautogui.screenshot()
        file_num = str(i)
        my_screen_shot.save(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')
        print('screenshot saved')

        i += 1
        time.sleep(wait_beetwen_screen)


    else:
        my_screen_shot = pyautogui.screenshot()
        file_num = str(i)
        previous_file_num = str(i-1)
        my_screen_shot.save(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')

        # compare if screenshot have changed
        previous_img = (np.asarray(Image.open(f'{lecture_title}/{str(lecture_title)}_{previous_file_num}.png')))
        current_img = (np.asarray(Image.open(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')))

        # percentage comparision of similarity
        similarity = np.sum(np.equal(previous_img, current_img)) / np.ma.size(current_img)
        # print(similarity)

        similarity_treshold = 0.998
        if similarity > similarity_treshold:
            os.remove(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')
            print('identical screenshot deleted')

        else:
            print('screenshot saved')
            i += 1

        time.sleep(wait_beetwen_screen)


print('Remember to copy screenshots to safe location. You may accidentaly overwrite it.')
