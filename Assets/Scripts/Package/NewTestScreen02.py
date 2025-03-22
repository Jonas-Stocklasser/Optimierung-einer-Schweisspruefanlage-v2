#!/usr/bin/python3
# Date: 18.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 2; ID=1.1
from tkinter import messagebox

import customtkinter as ctk
import tkcalendar as tkc
import math
import os
from datetime import datetime
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader, json_creator


class NewTestScreen02(ctk.CTkFrame):  # class for the NewTestScreen02 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size * 0.8, font_size * 0.8))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 2:" +
                                                " persönliche Daten des Prüflings eingeben"),
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
                                         command=lambda: self.master.confirm_go_back("1.0"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        corner_radius=20,
                                        width=window_geometry[0] / 4.5,
                                        height=font_size * 11)
        self.entry_frame.place(x=0,
                               y=font_size * 2)

        # first name entry------------------------------------------------------------
        self.first_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   corner_radius=10,
                                                   text="Vorname",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size),
                                                   width=window_geometry[0] / 4.5 - 20,
                                                   height=font_size * 1.5)
        self.first_name_entry_label.place(x=10,
                                          y=10)

        self.first_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                             placeholder_text="Vorname",
                                             font=("bold", font_size),
                                             width=window_geometry[0] / 4.5 - 20
                                             )
        self.first_name_entry.place(x=10,
                                    y=font_size * 1.5 + 15)

        # last name entry------------------------------------------------------------
        self.last_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                  fg_color=GetStartupVariables.color_SET_blue,
                                                  corner_radius=10,
                                                  text="Nachname",
                                                  text_color=GetStartupVariables.text_color_SET,
                                                  font=("bold", font_size),
                                                  width=window_geometry[0] / 4.5 - 20,
                                                  height=font_size * 1.5)
        self.last_name_entry_label.place(x=10,
                                         y=2 * font_size * 1.5 + 25)

        self.last_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                            placeholder_text="Nachname",
                                            font=("bold", font_size),
                                            width=window_geometry[0] / 4.5 - 20
                                            )
        self.last_name_entry.place(x=10,
                                   y=3 * font_size * 1.5 + 30)

        # birth date entry------------------------------------------------------------
        self.birth_date_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   corner_radius=10,
                                                   text="Geburtsdatum",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size),
                                                   width=window_geometry[0] / 4.5 - 20,
                                                   height=font_size * 1.5)
        self.birth_date_entry_label.place(x=10,
                                          y=4 * font_size * 1.5 + 40)

        self.birth_date_entry = tkc.DateEntry(master=self.entry_frame,
                                              font=("bold", int(math.floor(font_size / 1.5))),
                                              date_pattern='dd.mm.yyyy',
                                              year=2000,
                                              month=1,
                                              day=1,
                                              state="readonly")
        self.birth_date_entry.place(x=10,
                                    y=5 * font_size * 1.5 + 45)

        # save and continue button------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=font_size * 6 + 20 + font_size * 5 + 10)
        self.button_frame.place(x=0,
                                y=font_size * 2 + font_size * 11 + 10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         command=self.save_entry_data_examinee,
                                         height=font_size * 1.5,
                                         width=font_size * 6)
        self.save_button.place(x=10,
                               y=10)

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="disabled",
                                             command=self.continue_button_function,
                                             height=font_size * 1.5,
                                             width=font_size * 5)
        self.continue_button.place(x=font_size * 6 + 20,
                                   y=10)

    def continue_button_function(self):  # method for the button actions
        self.master.switch_window("1.2")
        self.create_examinee_folder_and_json()

    def save_entry_data_examinee(self):  # method to save the entry data
        personal_infos_examinee = [self.first_name_entry.get(),
                                   self.last_name_entry.get(),
                                   self.birth_date_entry.get()]
        if len(personal_infos_examinee[0].strip()) >= 1 and len(personal_infos_examinee[1].strip()) >= 1:  # integrity evaluation
            self.continue_button.configure(state="normal")  # unlock the continue button
            json_writer("personal_var", "personal_infos_examinee", personal_infos_examinee,
                        main_pi_location + "../JSON/")
        else:
            self.continue_button.configure(state="disabled")  # lock the continue button
            if len(personal_infos_examinee[0].strip()) < 1:
                print("Please provide first name")
                messagebox.showinfo("Eingabefehler", "Bitte Vornamen eingeben!")
            elif len(personal_infos_examinee[1].strip()) < 1:
                print("Please provide last name")
                messagebox.showinfo("Eingabefehler", "Bitte Nachnamen eingeben!")

    def reset_input_new_test(self):
        self.first_name_entry.delete(0, "end")
        self.first_name_entry.configure(placeholder_text="Vorname")
        self.last_name_entry.delete(0, "end")
        self.last_name_entry.configure(placeholder_text="Nachname")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    @staticmethod
    def create_examinee_folder_and_json():  # create a new folder for all the created files for the examinee
        personal_infos_examinee = json_reader("personal_var", "personal_infos_examinee", main_pi_location + "../JSON/")
        exam_date = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
        error_append = ""
        error_num = 0
        save_path = json_reader("startup_var", "save_path", main_pi_location + "../JSON/")
        new_folder = f"{save_path}/{personal_infos_examinee[1]}_{personal_infos_examinee[0]}" + error_append
        while True:
            try:
                os.mkdir(new_folder)
                break
            except FileExistsError:
                error_num += 1
                error_append = str(error_num)
                new_folder = f"{save_path}/{personal_infos_examinee[1]}_{personal_infos_examinee[0]}{error_append}"

        json_creator(f"{personal_infos_examinee[1]}_{personal_infos_examinee[0]}", f"{new_folder}/",
                     "personal_infos_examinee", personal_infos_examinee)
        json_writer("personal_var", "personal_folder_path",
                    f"{new_folder}/", main_pi_location + "../JSON/")
        json_writer("personal_var", "personal_json_name",
                    f"{personal_infos_examinee[1]}_{personal_infos_examinee[0]}", main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "exam_date", exam_date, personal_folder_path)
