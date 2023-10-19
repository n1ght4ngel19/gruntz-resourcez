import os
import shutil
import subprocess
import sys


def rename_anims(type):
    path = f"./{type}GRUNT"

    for folder in os.listdir(path):
        if folder == "DEATH":
            subprocess.run(["convert", "+append", f"{path}/{folder}/*.png", f"{type}Grunt_Death.png"])
        else:
            directionpath = f"{path}/{folder}"
            for subfolder in os.listdir(directionpath):
                subprocess.run(["convert", "+append", f"{directionpath}/{subfolder}/*.png", f"{type}Grunt_{subfolder}_{folder}.png"])
        # if folder == "CRUMBLEWATERBRIDGE":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Bridge_Water_Crumble.png"])
        # if folder == "DEATHBRIDGE":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Bridge_Death.png"])
        # if folder == "WATERBRIDGE":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Bridge_Water.png"])
        # if folder == "TOGGLEDEATHBRIDGE":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Bridge_Death_Toggle.png"])
        # if folder == "TOGGLEWATERBRIDGE":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Bridge_Water_Toggle.png"])
        # if folder == "MUD":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Mud_01.png"])
        # if folder == "DIRT":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Dirt_01.png"])
        # if folder == "FORT":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Fort_01.png"])
        # if folder == "ROCKBREAK":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}RockBreak_01.png"])
        # if folder == "FORTSPLASH":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Splash_Fort_01.png"])
        # if folder == "DEATHSPLASH":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Splash_Death_01.png"])
        # if folder == "WATER1":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Water_01.png"])
        # if folder == "WATER2":
        #     subprocess.run(["convert", "+append", f"{path}{folder}/*.png", f"{path}Water_02.png"])


def rename_items(num):
    path = "/mnt/e/Editing/GruntzREZ/INGAMEICONZ/"
    toolz_path = f"{path}TOOLZ/"
    toyz_path = f"{path}TOYZ/"
    powerupz_path = f"{path}POWERUPZ/"

    # for tool in os.listdir(toolz_path):
    #     tool_name = tool[0].upper() + tool[1:].lower()
    #     subprocess.run(["convert", "+append", f"{toolz_path}{tool}/*.png", f"{toolz_path}{tool_name}_Rotating.png"])

    for toy in os.listdir(toyz_path):
        toy_name = toy[0].upper() + toy[1:].lower()
        subprocess.run(["convert", "+append", f"{toyz_path}{toy}/*.png", f"{toyz_path}{toy_name}_Rotating.png"])

    for powerup in os.listdir(powerupz_path):
        powerup_name = powerup[0].upper() + powerup[1:].lower()
        subprocess.run(
            ["convert", "+append", f"{powerupz_path}{powerup}/*.png", f"{powerupz_path}{powerup_name}_Rotating.png"])


if __name__ == '__main__':
    # rename_items(sys.argv[1])
    rename_anims(sys.argv[1])
