#!/usr/bin/python3
# Date: 21.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 3; ID=1.2
from tkinter import messagebox

import customtkinter as ctk
import tkinter as tk
import math
import tkcalendar as tkc
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetPersonalVariables, back_arrow_image, main_pi_location

font_size = 1


class NewTestScreen03(ctk.CTkFrame):  # class for the NewTestScreen03 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")
        global font_size
        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size * 0.8, font_size * 0.8))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 3:" +
                                                " persönliche Daten des Prüfers eingeben"),
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
                                         command=lambda: self.master.confirm_go_back("1.1"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # option menu examiner------------------------------------------------------------
        self.examiner_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                       corner_radius=20,
                                                       width=window_geometry[0] / 4.5,
                                                       height=2 * font_size * 1.5 + 20)
        self.examiner_option_menu_frame.place(x=0,
                                              y=font_size * 2)

        self.examiner_option_menu_label = ctk.CTkLabel(master=self.examiner_option_menu_frame,
                                                       fg_color=GetStartupVariables.color_SET_blue,
                                                       corner_radius=10,
                                                       text="Voreinstellungen",
                                                       text_color=GetStartupVariables.text_color_SET,
                                                       font=("bold", font_size),
                                                       width=window_geometry[0] / 4.5 - 20,
                                                       height=font_size * 1.5)
        self.examiner_option_menu_label.place(x=10,
                                              y=10)

        self.options_menu_examiner = ctk.CTkOptionMenu(master=self.examiner_option_menu_frame,
                                                       font=("bold", font_size),
                                                       dropdown_font=("bold", font_size),
                                                       corner_radius=10,
                                                       variable=tk.StringVar(
                                                           value=GetPersonalVariables.last_chosen_examiner),
                                                       values=GetPersonalVariables.examiner_list,
                                                       command=self.examiner_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_examiner.place(x=10,
                                         y=font_size * 1.5 + 15)

        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        corner_radius=20,
                                        width=window_geometry[0] / 4.5,
                                        height=font_size * 11)
        self.entry_frame.place(x=0,
                               y=font_size * 2 + 2 * font_size * 1.5 + 30)

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
                                             font=("bold", font_size),
                                             state="disabled",
                                             height=font_size * 1.5,
                                             width=window_geometry[0] / 4.5 - 20
                                             )
        self.first_name_entry.place(x=10,
                                    y=font_size * 1.5 + 15)

        self.first_name_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                           corner_radius=10,
                                                                           width=window_geometry[0] / 4.5 - 20,
                                                                           height=font_size * 1.5)
        self.first_name_entry_unchanged_overlay_label_frame.place(x=10,
                                                                  y=font_size * 1.5 + 15)

        self.first_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.first_name_entry_unchanged_overlay_label_frame,
            text=GetPersonalVariables.personal_infos_examiner[0],
            font=("bold", font_size))
        self.first_name_entry_unchanged_overlay_label.place(x=10,
                                                            rely=0.1)

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
                                            font=("bold", font_size),
                                            state="disabled",
                                            height=font_size * 1.5,
                                            width=window_geometry[0] / 4.5 - 20)
        self.last_name_entry.place(x=10,
                                   y=3 * font_size * 1.5 + 30)

        self.last_name_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                          corner_radius=10,
                                                                          width=window_geometry[0] / 4.5 - 20,
                                                                          height=font_size * 1.5)
        self.last_name_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=3 * font_size * 1.5 + 30)

        self.last_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.last_name_entry_unchanged_overlay_label_frame,
            text=GetPersonalVariables.personal_infos_examiner[1],
            font=("bold", font_size))
        self.last_name_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)

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
                                              year=1976,
                                              month=2,
                                              day=1,
                                              state="readonly")
        self.birth_date_entry.place(x=10,
                                    y=5 * font_size * 1.5 + 45)

        self.birth_date_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                           corner_radius=10,
                                                                           width=window_geometry[0] / 4.5 - 20,
                                                                           height=font_size * 1.5)
        self.birth_date_entry_unchanged_overlay_label_frame.place(x=10,
                                                                  y=5 * font_size * 1.5 + 45)

        self.birth_date_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.birth_date_entry_unchanged_overlay_label_frame,
            text=GetPersonalVariables.personal_infos_examiner[2],
            font=("bold", font_size))
        self.birth_date_entry_unchanged_overlay_label.place(x=10,
                                                            rely=0.1)

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=font_size * 5 + font_size * 6 + 40 + font_size * 5)
        self.button_frame.place(x=0,
                                y=font_size * 2 + 2 * font_size * 1.5 + 30 + font_size * 11 + 10)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", font_size),
                                           state="normal",
                                           command=lambda: self.change_entry_data_examiner(),
                                           height=font_size * 1.5,
                                           width=font_size * 5)
        self.change_button.place(x=10,
                                 y=10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_examiner(),
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
        self.master.switch_window("1.3")
        self.write_personal_json()

    def change_entry_data_examiner(self):  # make the entries typeable
        last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", main_pi_location + "../JSON/")
        infos = json_reader("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                                              main_pi_location + "../JSON/")
        self.first_name_entry_unchanged_overlay_label.place_forget()
        self.first_name_entry_unchanged_overlay_label_frame.place_forget()
        self.last_name_entry_unchanged_overlay_label.place_forget()
        self.last_name_entry_unchanged_overlay_label_frame.place_forget()
        self.birth_date_entry_unchanged_overlay_label.place_forget()
        self.birth_date_entry_unchanged_overlay_label_frame.place_forget()

        self.first_name_entry.configure(state="normal")
        self.first_name_entry.delete(0, ctk.END)
        self.first_name_entry.insert(0, f"{infos[0]}")
        self.last_name_entry.configure(state="normal")
        self.last_name_entry.delete(0, ctk.END)
        self.last_name_entry.insert(0, f"{infos[1]}")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_examiner(self):
        personal_infos_examiner = [self.first_name_entry.get(),
                                   self.last_name_entry.get(),
                                   self.birth_date_entry.get()]
        last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", main_pi_location + "../JSON/")

        if len(personal_infos_examiner[0].strip()) >= 1 and len(personal_infos_examiner[1].strip()) >= 1:
            self.continue_button.configure(state="normal")
            json_writer("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                        personal_infos_examiner, main_pi_location + "../JSON/")

            self.first_name_entry_unchanged_overlay_label_frame.place(x=10,
                                                                      y=font_size * 1.5 + 15)
            self.first_name_entry_unchanged_overlay_label.place(x=10,
                                                                rely=0.1)
            self.last_name_entry_unchanged_overlay_label_frame.place(x=10,
                                                                     y=3 * font_size * 1.5 + 30)
            self.last_name_entry_unchanged_overlay_label.place(x=10,
                                                               rely=0.1)
            self.birth_date_entry_unchanged_overlay_label_frame.place(x=10,
                                                                      y=5 * font_size * 1.5 + 45)
            self.birth_date_entry_unchanged_overlay_label.place(x=10,
                                                                rely=0.1)
            self.update_labels(personal_infos_examiner)

            self.first_name_entry.configure(state="disabled")
            self.last_name_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        else:
            self.continue_button.configure(state="disabled")
            if len(personal_infos_examiner[0].strip()) < 1:
                print("Please provide first name")
                messagebox.showinfo("Eingabefehler", "Bitte Vornamen eingeben!")
            elif len(personal_infos_examiner[1].strip()) < 1:
                print("Please provide last name")
                messagebox.showinfo("Eingabefehler", "Bitte Nachnamen eingeben!")

    def update_labels(self, infos):
        self.first_name_entry_unchanged_overlay_label.configure(text=infos[0])
        self.last_name_entry_unchanged_overlay_label.configure(text=infos[1])
        self.birth_date_entry_unchanged_overlay_label.configure(text=infos[2])

    def examiner_select(self, which):
        json_writer("personal_var", "last_chosen_examiner", which, main_pi_location + "../JSON/")
        personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{which}",
                                              main_pi_location + "../JSON/")
        self.update_labels(personal_infos_examiner)

    def reset_input_new_test(self):
        self.save_button.configure(state="disabled")
        self.continue_button.configure(state="normal")
        self.change_button.configure(state="normal")

    @staticmethod
    def write_personal_json():
        last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", main_pi_location + "../JSON/")
        personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                                              main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "personal_infos_examiner", personal_infos_examiner, personal_folder_path)
