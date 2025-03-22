#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Shared Variables

import customtkinter as ctk
import glob
from PIL import Image  # library for image handling
from .JsonFunctions import json_reader

# path when on raspberry pi for the .desktop execution file to work
main_pi_location = "/home/admin/Schweisspruefung/Optimierung-einer-Schweisspruefanlage/Assets/Scripts/"
#w1temp_base_dir = "/sys/bus/w1/devices/"
#device_folder = glob.glob(w1temp_base_dir + "28*")[0]
#w1temp_location = device_folder + "/w1_slave"


# path when on PyCharm
#main_pi_location = ""
#w1temp_location = "../default_temp.txt"


# Startup variables----------------------------------------
class GetStartupVariables:
    name_of_app = json_reader("startup_var", "name_of_app", main_pi_location + "../JSON/")
    color_SET_blue = json_reader("startup_var", "color_SET_blue", main_pi_location + "../JSON/")
    color_SET_gray = json_reader("startup_var", "color_SET_gray", main_pi_location + "../JSON/")
    text_color_SET = json_reader("startup_var", "text_color_SET", main_pi_location + "../JSON/")
    start_window = json_reader("startup_var", "start_window", main_pi_location + "../JSON/")
    appearance_mode = json_reader("startup_var", "appearance_mode", main_pi_location + "../JSON/")
    save_path = json_reader("startup_var", "save_path", main_pi_location + "../JSON/")
    code_testing = json_reader("startup_var", "code_testing", main_pi_location + "../JSON/")


# Personal variables----------------------------------------
class GetPersonalVariables:
    last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", main_pi_location + "../JSON/")
    personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                                          main_pi_location + "../JSON/")
    examiner_list = json_reader("personal_var", "examiner_list", main_pi_location + "../JSON/")


# Item variables----------------------------------------
class GetItemVariables:
    last_chosen_item = json_reader("item_var", "last_chosen_item", main_pi_location + "../JSON/")
    infos_item = json_reader("item_var", f"infos_item_{last_chosen_item}", main_pi_location + "../JSON/")
    item_list = json_reader("item_var", "item_list", main_pi_location + "../JSON/")


# Exam Parameter variables----------------------------------------
class GetExamParameterVariables:
    last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list",
                                             main_pi_location + "../JSON/")
    parameter_list = json_reader("exam_parameter_var", f"parameter_list_{last_chosen_parameter_list}",
                                 main_pi_location + "../JSON/")
    parameter_list_indexes = json_reader("exam_parameter_var", "parameter_list_indexes", main_pi_location + "../JSON/")


# Pictures----------------------------------------
start_image = ctk.CTkImage(Image.open(main_pi_location + "../Images/Placeholder.png"), size=(600, 600))
back_arrow_image = ctk.CTkImage(dark_image=Image.open(main_pi_location + "../Images/Back_Arrow.png"), size=(1, 1))
pruefstueck_image = ctk.CTkImage(dark_image=Image.open(main_pi_location + "../Images/Pruefstueck_Dark.png"),
                                 light_image=Image.open(main_pi_location + "../Images/Pruefstueck_Light.png"),
                                 size=(16, 9))
