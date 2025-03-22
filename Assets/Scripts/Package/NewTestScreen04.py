#!/usr/bin/python3
# Date: 23.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 4; ID=1.3
import re
import string
from tkinter import messagebox

import customtkinter as ctk
import tkinter as tk
import math
import tkcalendar as tkc
from datetime import datetime
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetItemVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader

font_size = 1


class NewTestScreen04(ctk.CTkFrame):  # class for the NewTestScreen04 window
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
                                          text=("Neuer Test - Schritt 4:" +
                                                " Daten des Prüfstückes überprüfen"),
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
                                         command=lambda: self.master.confirm_go_back("1.2"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # options menu item------------------------------------------------------------
        self.item_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                   corner_radius=20,
                                                   width=window_geometry[0] / 4.5,
                                                   height=font_size * 3 + 20)
        self.item_option_menu_frame.place(x=0,
                                          y=font_size * 2)

        self.item_option_menu_label = ctk.CTkLabel(master=self.item_option_menu_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   corner_radius=10,
                                                   text="Voreinstellungen",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size),
                                                   width=window_geometry[0] / 4.5 - 20,
                                                   height=font_size * 1.5)
        self.item_option_menu_label.place(x=10,
                                          y=10)

        self.options_menu_item = ctk.CTkOptionMenu(master=self.item_option_menu_frame,
                                                   font=("bold", font_size),
                                                   dropdown_font=("bold", font_size),
                                                   corner_radius=10,
                                                   variable=tk.StringVar(
                                                       value=GetItemVariables.last_chosen_item),
                                                   values=GetItemVariables.item_list,
                                                   command=self.item_select
                                                   )
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_item.place(x=10,
                                     y=font_size * 1.5 + 15)

        # entry frame 1------------------------------------------------------------
        self.entry_frame1 = ctk.CTkFrame(master=self,  # frame for the entries
                                         corner_radius=20,
                                         width=font_size * 25 + 20,
                                         height=4 * (15 + font_size * 3) + 10)
        self.entry_frame1.place(x=0,
                                y=font_size * 2 + font_size * 3 + 30)

        # entry frame 2------------------------------------------------------------
        self.entry_frame2 = ctk.CTkFrame(master=self,  # frame for the entries
                                         corner_radius=20,
                                         width=font_size * 25 + 20,
                                         height=4 * (15 + font_size * 3) + 10)
        self.entry_frame2.place(x=font_size * 25 + 30,
                                y=font_size * 2 + font_size * 3 + 30)

        # title entry------------------------------------------------------------
        self.title_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="Werkstoff",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.title_entry_label.place(x=10,
                                     y=10)

        self.title_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        font=("bold", font_size),
                                        state="disabled",
                                        width=window_geometry[0] / 6
                                        )
        self.title_entry.place(x=10,
                               y=font_size * 1.5 + 15)

        self.title_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      corner_radius=10,
                                                                      width=window_geometry[0] / 6,
                                                                      height=font_size * 1.5)
        self.title_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=font_size * 1.5 + 15)

        self.title_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.title_entry_unchanged_overlay_label_frame,
            text=GetItemVariables.infos_item[0],
            font=("bold", font_size))
        self.title_entry_unchanged_overlay_label.place(x=10,
                                                       rely=0.1)

        # info1 entry------------------------------------------------------------
        self.info1_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="Umfangsspannung σ [MPa]",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.info1_entry_label.place(x=10,
                                     y=2 * font_size * 1.5 + 25)

        self.info1_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        font=("bold", font_size),
                                        state="disabled")
        self.info1_entry.place(x=10,
                               y=3 * font_size * 1.5 + 30)

        self.info1_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      corner_radius=10,
                                                                      width=window_geometry[0] / 6,
                                                                      height=font_size * 1.5)
        self.info1_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=3 * font_size * 1.5 + 30)

        self.info1_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info1_entry_unchanged_overlay_label_frame,
            text=GetItemVariables.infos_item[1],
            font=("bold", font_size))
        self.info1_entry_unchanged_overlay_label.place(x=10,
                                                       rely=0.1)

        # info2 entry------------------------------------------------------------
        self.info2_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="SDR",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.info2_entry_label.place(x=10,
                                     y=4 * font_size * 1.5 + 40)

        self.info2_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        font=("bold", font_size),
                                        state="disabled"
                                        )
        self.info2_entry.place(x=10,
                               y=5 * font_size * 1.5 + 45)

        self.info2_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      corner_radius=10,
                                                                      width=window_geometry[0] / 6,
                                                                      height=font_size * 1.5)
        self.info2_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=5 * font_size * 1.5 + 45)

        self.info2_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info2_entry_unchanged_overlay_label_frame,
            text=GetItemVariables.infos_item[2],
            font=("bold", font_size))
        self.info2_entry_unchanged_overlay_label.place(x=10,
                                                       rely=0.1)

        # info3 entry------------------------------------------------------------
        self.info3_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="Nenn-Außendurchmesser des Rohres dₙ [mm]",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.info3_entry_label.place(x=10,
                                     y=10 + (5 * font_size * 1.5 + 45) + (font_size * 1.5))

        self.info3_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        font=("bold", font_size),
                                        state="disabled"
                                        )
        self.info3_entry.place(x=10,
                               y=15 + (5 * font_size * 1.5 + 45) + (2 * font_size * 1.5))

        self.info3_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      corner_radius=10,
                                                                      width=window_geometry[0] / 6,
                                                                      height=font_size * 1.5)
        self.info3_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=15 + (5 * font_size * 1.5 + 45) + (2 * font_size * 1.5))

        self.info3_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info3_entry_unchanged_overlay_label_frame,
            text=GetItemVariables.infos_item[3],
            font=("bold", font_size))
        self.info3_entry_unchanged_overlay_label.place(x=10,
                                                       rely=0.1)

        # info4 entry------------------------------------------------------------
        self.info4_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="Prüfdauer (Regelung) [min]",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.info4_entry_label.place(x=10,
                                     y=10)

        self.info4_entry = ctk.CTkEntry(master=self.entry_frame2,
                                        font=("bold", font_size),
                                        state="disabled"
                                        )
        self.info4_entry.place(x=10,
                               y=15 + font_size * 1.5)

        self.info4_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame2,
                                                                      corner_radius=10,
                                                                      width=window_geometry[0] / 6,
                                                                      height=font_size * 1.5)
        self.info4_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=15 + font_size * 1.5)

        self.info4_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info4_entry_unchanged_overlay_label_frame,
            text=GetItemVariables.infos_item[4],
            font=("bold", font_size))
        self.info4_entry_unchanged_overlay_label.place(x=10,
                                                       rely=0.1)

        # info5 entry------------------------------------------------------------
        self.info5_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="Lieferform",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.info5_entry_label.place(x=10,
                                     y=25 + (2 * font_size * 1.5))

        self.info5_entry = ctk.CTkEntry(master=self.entry_frame2,
                                        font=("bold", font_size),
                                        state="disabled",
                                        width=window_geometry[0] / 6
                                        )
        self.info5_entry.place(x=10,
                               y=30 + (3 * font_size * 1.5))

        self.info5_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame2,
                                                                      corner_radius=10,
                                                                      width=window_geometry[0] / 6,
                                                                      height=font_size * 1.5)
        self.info5_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=30 + (3 * font_size * 1.5))

        self.info5_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info5_entry_unchanged_overlay_label_frame,
            text=GetItemVariables.infos_item[5],
            font=("bold", font_size))
        self.info5_entry_unchanged_overlay_label.place(x=10,
                                                       rely=0.1)

        # info6 entry------------------------------------------------------------
        self.info6_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="Herstellungsverfahren",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.info6_entry_label.place(x=10,
                                     y=40 + (4 * font_size * 1.5))

        self.info6_entry = ctk.CTkEntry(master=self.entry_frame2,
                                        font=("bold", font_size),
                                        state="disabled",
                                        width=window_geometry[0] / 6
                                        )
        self.info6_entry.place(x=10,
                               y=45 + (5 * font_size * 1.5))

        self.info6_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame2,
                                                                      corner_radius=10,
                                                                      width=window_geometry[0] / 6,
                                                                      height=font_size * 1.5)
        self.info6_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=45 + (5 * font_size * 1.5))

        self.info6_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info6_entry_unchanged_overlay_label_frame,
            text=GetItemVariables.infos_item[6],
            font=("bold", font_size))
        self.info6_entry_unchanged_overlay_label.place(x=10,
                                                       rely=0.1)

        # info7 entry------------------------------------------------------------
        self.info7_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=10,
                                              text="Herstellungsdatum",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size),
                                              width=font_size * 25,
                                              height=font_size * 1.5)
        self.info7_entry_label.place(x=10,
                                     y=55 + (6 * font_size * 1.5))

        self.manufacturing_date_entry = tkc.DateEntry(master=self.entry_frame2,
                                                      font=("bold", int(math.floor(font_size / 1.5))),
                                                      date_pattern='dd.mm.yyyy',
                                                      year=datetime.now().year,
                                                      month=datetime.now().month,
                                                      day=datetime.now().day,
                                                      state="readonly")
        self.manufacturing_date_entry.place(x=10,
                                            y=60 + (7 * font_size * 1.5))

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=font_size * 5 + font_size * 6 + 40 + font_size * 5)
        self.button_frame.place(x=0,
                                y=4 * (15 + font_size * 3) + 20 + font_size * 2 + font_size * 3 + 30)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", font_size),
                                           state="normal",
                                           command=lambda: self.change_entry_data_item(),
                                           height=font_size * 1.5,
                                           width=font_size * 5)
        self.change_button.place(x=10,
                                 y=10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_item(),
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
        self.master.switch_window("1.4")
        self.write_personal_json()

    def change_entry_data_item(self):
        last_chosen_item = json_reader("item_var", "last_chosen_item", main_pi_location + "../JSON/")
        infos = json_reader("item_var", f"infos_item_{last_chosen_item}", main_pi_location + "../JSON/")

        self.title_entry_unchanged_overlay_label.place_forget()
        self.title_entry_unchanged_overlay_label_frame.place_forget()
        self.info1_entry_unchanged_overlay_label.place_forget()
        self.info1_entry_unchanged_overlay_label_frame.place_forget()
        self.info2_entry_unchanged_overlay_label.place_forget()
        self.info2_entry_unchanged_overlay_label_frame.place_forget()
        self.info3_entry_unchanged_overlay_label.place_forget()
        self.info3_entry_unchanged_overlay_label_frame.place_forget()
        self.info4_entry_unchanged_overlay_label.place_forget()
        self.info4_entry_unchanged_overlay_label_frame.place_forget()
        self.info5_entry_unchanged_overlay_label.place_forget()
        self.info5_entry_unchanged_overlay_label_frame.place_forget()
        self.info6_entry_unchanged_overlay_label.place_forget()
        self.info6_entry_unchanged_overlay_label_frame.place_forget()

        self.title_entry.configure(state="normal")
        self.title_entry.delete(0, ctk.END)
        self.title_entry.insert(0, f"{infos[0]}")
        self.info1_entry.configure(state="normal")
        self.info1_entry.delete(0, ctk.END)
        self.info1_entry.insert(0, f"{infos[1]}")
        self.info2_entry.configure(state="normal")
        self.info2_entry.delete(0, ctk.END)
        self.info2_entry.insert(0, f"{infos[2]}")
        self.info3_entry.configure(state="normal")
        self.info3_entry.delete(0, ctk.END)
        self.info3_entry.insert(0, f"{infos[3]}")
        self.info4_entry.configure(state="normal")
        self.info4_entry.delete(0, ctk.END)
        self.info4_entry.insert(0, f"{infos[4]}")
        self.info5_entry.configure(state="normal")
        self.info5_entry.delete(0, ctk.END)
        self.info5_entry.insert(0, f"{infos[5]}")
        self.info6_entry.configure(state="normal")
        self.info6_entry.delete(0, ctk.END)
        self.info6_entry.insert(0, f"{infos[6]}")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_item(self):
        infos_item = [self.title_entry.get(),
                      self.info1_entry.get(),
                      self.info2_entry.get(),
                      self.info3_entry.get(),
                      self.info4_entry.get(),
                      self.info5_entry.get(),
                      self.info6_entry.get()]

        allowed_characters = set(string.digits + ".")

        if (len(infos_item[0].strip()) >= 1 and
                len(infos_item[1].strip()) >= 1 and
                len(infos_item[2].strip()) >= 1 and
                len(infos_item[3].strip()) >= 1 and
                len(infos_item[4].strip()) >= 1 and
                len(infos_item[5].strip()) >= 1 and
                len(infos_item[6].strip()) >= 1 and
                set(infos_item[1]) <= allowed_characters and
                set(infos_item[2]) <= allowed_characters and
                set(infos_item[3]) <= allowed_characters and
                set(infos_item[4]) <= allowed_characters and not
                infos_item[2] == infos_item[3]):
            self.continue_button.configure(state="normal")
            last_chosen_item = json_reader("item_var", "last_chosen_item", main_pi_location + "../JSON/")
            json_writer("item_var", f"infos_item_{last_chosen_item}", infos_item, main_pi_location + "../JSON/")

            self.title_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=font_size * 1.5 + 15)
            self.title_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)
            self.info1_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=3 * font_size * 1.5 + 30)
            self.info1_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)
            self.info2_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=5 * font_size * 1.5 + 45)
            self.info2_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)
            self.info3_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=15 + (5 * font_size * 1.5 + 45) + (
                                                                         2 * font_size * 1.5))
            self.info3_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)
            self.info4_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=15 + font_size * 1.5)
            self.info4_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)
            self.info5_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=30 + (3 * font_size * 1.5))
            self.info5_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)
            self.info6_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=45 + (5 * font_size * 1.5))
            self.info6_entry_unchanged_overlay_label.place(x=10,
                                                           rely=0.1)
            self.update_labels(infos_item)

            self.title_entry.configure(state="disabled")
            self.info1_entry.configure(state="disabled")
            self.info2_entry.configure(state="disabled")
            self.info3_entry.configure(state="disabled")
            self.info4_entry.configure(state="disabled")
            self.info5_entry.configure(state="disabled")
            self.info6_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        else:
            self.continue_button.configure(state="disabled")
            if len(infos_item[0].strip()) < 1:
                print("Please provide material")
                messagebox.showinfo("Eingabefehler", "Bitte Werkstoff eigeben!")
            elif len(infos_item[1].strip()) < 1:
                print("Please provide tension")
                messagebox.showinfo("Eingabefehler", "Bitte Umfangsspannung eingeben!")
            elif len(infos_item[2].strip()) < 1:
                print("Please provide SDR")
                messagebox.showinfo("Eingabefehler", "Bitte SDR eingeben!")
            elif len(infos_item[3].strip()) < 1:
                print("Please provide diameter")
                messagebox.showinfo("Eingabefehler", "Bitte Nenn-Außendurchmesser eingeben!")
            elif len(infos_item[4].strip()) < 1:
                print("Please provide regulation period")
                messagebox.showinfo("Eingabefehler", "Bitte Prüfdauer (Regelung) eingeben!")
            elif len(infos_item[5].strip()) < 1:
                print("Please provide form of delivery")
                messagebox.showinfo("Eingabefehler", "Bitte Lieferform eingeben!")
            elif len(infos_item[6].strip()) < 1:
                print("Please provide manufacturing process")
                messagebox.showinfo("Eingabefehler", "Bitte Herstellungsverfahren eingeben!")
            elif not set(infos_item[1]) <= allowed_characters or not set(infos_item[2]) <= allowed_characters or not \
                    set(infos_item[3]) <= allowed_characters or not set(infos_item[4]) <= allowed_characters:
                print("Please only input [1 2 3 4 5 6 7 8 9 0 .]")
                print(infos_item)
                messagebox.showinfo("Eingabefehler", "Bitte nur erlaubte Zeichen eingeben!\n[1 2 3 4 5 6 7 8 9 0 .]")

    def update_labels(self, infos):
        self.title_entry_unchanged_overlay_label.configure(text=infos[0])
        self.info1_entry_unchanged_overlay_label.configure(text=infos[1])
        self.info2_entry_unchanged_overlay_label.configure(text=infos[2])
        self.info3_entry_unchanged_overlay_label.configure(text=infos[3])
        self.info4_entry_unchanged_overlay_label.configure(text=infos[4])
        self.info5_entry_unchanged_overlay_label.configure(text=infos[5])
        self.info6_entry_unchanged_overlay_label.configure(text=infos[6])

    def item_select(self, which):
        json_writer("item_var", "last_chosen_item", which, main_pi_location + "../JSON/")
        last_chosen_item = json_reader("item_var", "last_chosen_item", main_pi_location + "../JSON/")
        infos = json_reader("item_var", f"infos_item_{last_chosen_item}", main_pi_location + "../JSON/")
        self.update_labels(infos)

    def reset_input_new_test(self):
        self.save_button.configure(state="disabled")
        self.continue_button.configure(state="normal")
        self.change_button.configure(state="normal")

    def write_personal_json(self):
        manufacturing_date = self.manufacturing_date_entry.get()
        last_chosen_item = json_reader("item_var", "last_chosen_item", main_pi_location + "../JSON/")
        infos_item = json_reader("item_var", f"infos_item_{last_chosen_item}", main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "infos_item", infos_item, personal_folder_path)
        json_writer(personal_json_name, "manufacturing_date", manufacturing_date, personal_folder_path)
