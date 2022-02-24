#!/usr/bin/env python3

import os
import shutil


# make 26 folders, each named for each skill level [0,26]
# for each folder, iterate through roll levels [3,18]
# if the roll is 3 or 4, copy critical_success
# if the roll is 5 and the folder is 15+, copy critical_success
# if the roll is 6 and the folder is 16+, copy critical_success
# if the roll is <= the folder, copy success_image
# if the roll is 17 or 18, copy critical_failure
# else copy failure

top = os.path.abspath(os.getcwd())
fail_image = os.path.join(top, "failure_small.png")
success_image = os.path.join(top, "success_small.png")
critical_success_image = os.path.join(top, "critical_success_small.png")
critical_fail_image = os.path.join(top, "critical_fail_small.png")


for skill in range(30):
    dir_name = "skill_" + str(skill)
    if os.path.isdir(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.chdir(dir_name)
    
    for roll in range(3,19):
        new_file_name = "roll_" + str(roll) + ".png"
        if (roll == 3) or (roll == 4) or (roll == 5 and skill >=15) or (roll == 6 and skill >= 16):
            shutil.copyfile(critical_success_image, new_file_name)
        elif (roll == 17) or (roll == 18):
            shutil.copyfile(critical_fail_image, new_file_name)
        elif roll <= skill:
            shutil.copyfile(success_image, new_file_name)
        else:
            shutil.copyfile(fail_image, new_file_name)
    os.chdir(top)
    
    