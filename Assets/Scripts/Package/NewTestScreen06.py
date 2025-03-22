#!/usr/bin/python3
# Date: 29.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 6; ID=1.5
import string
from tkinter import messagebox

import customtkinter as ctk
import tkinter as tk
import math
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetExamParameterVariables, back_arrow_image, main_pi_location

font_size = 1
window_geometry_glob = None


class NewTestScreen06(ctk.CTkFrame):  # class for the NewTestScreen06 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        global font_size
        global window_geometry_glob

        window_geometry_glob = window_geometry
        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size * 0.8, font_size * 0.8))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 6:" +
                                                " Prüfparameter einstellen"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w",
                                          width=window_geometry[0] - 30 - font_size * 1.5,
                                          height=font_size * 1.5)
        self.indicator_bar.place(x=0,
                                 y=0)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         corner_radius=10,
                                         text="",
                                         anchor="center",
                                         image=back_arrow_image,
                                         command=lambda: self.master.confirm_go_back("1.4"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # options menu parameter------------------------------------------------------------
        self.parameter_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                        corner_radius=20,
                                                        width=window_geometry[0] / 4.5,
                                                        height=font_size * 3 + 20)
        self.parameter_option_menu_frame.place(x=0,
                                               y=font_size * 2)

        self.parameter_option_menu_label = ctk.CTkLabel(master=self.parameter_option_menu_frame,
                                                        fg_color=GetStartupVariables.color_SET_blue,
                                                        corner_radius=10,
                                                        text="Voreinstellungen",
                                                        text_color=GetStartupVariables.text_color_SET,
                                                        font=("bold", font_size),
                                                        width=window_geometry[0] / 4.5 - 20,
                                                        height=font_size * 1.5)
        self.parameter_option_menu_label.place(x=10,
                                               y=10)

        self.options_menu_parameter = ctk.CTkOptionMenu(master=self.parameter_option_menu_frame,
                                                        font=("bold", font_size),
                                                        dropdown_font=("bold", font_size),
                                                        corner_radius=10,
                                                        variable=tk.StringVar(
                                                            value=GetExamParameterVariables.last_chosen_parameter_list),
                                                        values=GetExamParameterVariables.parameter_list_indexes,
                                                        command=self.parameter_list_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_parameter.place(x=10,
                                          y=font_size * 1.5 + 15)
        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        corner_radius=20,
                                        width=font_size * 15 + 20,
                                        height=font_size * 4)
        self.entry_frame.place(x=0,
                               y=font_size * 2 + font_size * 3 + 30)

        # pressure entry------------------------------------------------------------
        self.pressure_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                 fg_color=GetStartupVariables.color_SET_blue,
                                                 corner_radius=10,
                                                 text="Maximaler Prüfdruck [bar]",
                                                 text_color=GetStartupVariables.text_color_SET,
                                                 font=("bold", font_size),
                                                 width=font_size * 15,
                                                 height=font_size * 1.5)
        self.pressure_entry_label.place(x=10,
                                        y=10)

        self.pressure_entry = ctk.CTkEntry(master=self.entry_frame,
                                           font=("bold", font_size),
                                           state="disabled",
                                           width=font_size * 15
                                           )
        self.pressure_entry.place(x=10,
                                  y=font_size * 1.5 + 15)

        self.pressure_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                         corner_radius=10,
                                                                         width=font_size * 15,
                                                                         height=font_size * 1.5)
        self.pressure_entry_unchanged_overlay_label_frame.place(x=10,
                                                                y=font_size * 1.5 + 15)

        self.pressure_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.pressure_entry_unchanged_overlay_label_frame,
            text=f"{GetExamParameterVariables.parameter_list[0]}",
            font=("bold", font_size))
        self.pressure_entry_unchanged_overlay_label.place(x=10,
                                                          rely=0.1)

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=font_size * 5 + font_size * 6 + 40 + font_size * 5)
        self.button_frame.place(x=0,
                                y=font_size * 2 + font_size * 3 + 40 + font_size * 4)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", font_size),
                                           state="normal",
                                           command=lambda: self.change_entry_data_exam_parameter(),
                                           height=font_size * 1.5,
                                           width=font_size * 5)
        self.change_button.place(x=10,
                                 y=10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # save button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_exam_parameter(),
                                         height=font_size * 1.5,
                                         width=font_size * 6)
        self.save_button.place(x=font_size * 5 + 20,
                               y=10)

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="normal",
                                             command=self.continue_button_function,
                                             height=font_size * 1.5,
                                             width=font_size * 5)
        self.continue_button.place(x=font_size * 5 + font_size * 6 + 30,
                                   y=10)

    def continue_button_function(self):
        self.master.switch_window("2.0")
        self.write_personal_json()

    def change_entry_data_exam_parameter(self):
        self.pressure_entry_unchanged_overlay_label.place_forget()
        self.pressure_entry_unchanged_overlay_label_frame.place_forget()
        """self.control_time_entry_unchanged_overlay_label.place_forget()
        self.control_time_entry_unchanged_overlay_label_frame.place_forget()"""

        self.pressure_entry.configure(state="normal", placeholder_text="Druck in Bar")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_exam_parameter(self):
        global window_geometry_glob
        parameter_list = [self.pressure_entry.get()]
        last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list",
                                                 main_pi_location + "../JSON/")

        allowed_characters = set(string.digits + ".")

        if len(parameter_list[0].strip()) >= 1 and set(parameter_list[0]) <= allowed_characters:
            self.continue_button.configure(state="normal")
            json_writer("exam_parameter_var", ("parameter_list_" + last_chosen_parameter_list),
                        parameter_list, main_pi_location + "../JSON/")

            self.pressure_entry_unchanged_overlay_label_frame.place(x=10,
                                                                    y=font_size * 1.5 + 15)
            self.pressure_entry_unchanged_overlay_label.place(x=10,
                                                              rely=0.1)
            self.update_labels(parameter_list)

            self.pressure_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        elif len(parameter_list[0].strip()) < 1:
            self.continue_button.configure(state="disabled")
            print("Please provide pressure")
            messagebox.showinfo("Eingabefehler", "Bitte maximalen Prüfdruck eigeben!")
        elif not set(parameter_list[0]) <= allowed_characters:
            self.continue_button.configure(state="disabled")
            print("Please only input [1 2 3 4 5 6 7 8 9 0 .]")
            print(parameter_list)
            messagebox.showinfo("Eingabefehler", "Bitte nur erlaubte Zeichen eingeben!\n[1 2 3 4 5 6 7 8 9 0 .]")

    def update_labels(self, infos):
        self.pressure_entry_unchanged_overlay_label.configure(text=f"{infos[0]}")

    def parameter_list_select(self, which):
        json_writer("exam_parameter_var", "last_chosen_parameter_list", which, main_pi_location + "../JSON/")
        parameter_list = json_reader("exam_parameter_var", f"parameter_list_{which}", main_pi_location + "../JSON/")
        self.update_labels(parameter_list)

    def reset_input_new_test(self):
        self.save_button.configure(state="disabled")
        self.continue_button.configure(state="normal")
        self.change_button.configure(state="normal")

    @staticmethod
    def write_personal_json():
        last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list",
                                                 main_pi_location + "../JSON/")
        parameter_list = json_reader("exam_parameter_var", f"parameter_list_{last_chosen_parameter_list}",
                                     main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "exam_parameter", parameter_list, personal_folder_path)
