#!/usr/bin/python3
# Date: 28.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 5; ID=1.4
from tkinter import messagebox

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader

font_size = 0.1


class NewTestScreen05(ctk.CTkFrame):  # class for the NewTestScreen05 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        global font_size

        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size * 0.8, font_size * 0.8))

        def visual_grading_widgets(name, text, y):
            # visual grading options
            label = ctk.CTkLabel(master=self.option_frame,
                                 fg_color=GetStartupVariables.color_SET_blue,
                                 corner_radius=10,
                                 text=text,
                                 text_color=GetStartupVariables.text_color_SET,
                                 font=("bold", font_size),
                                 width=font_size * 15,
                                 height=font_size * 1.5)
            label.place(x=10,
                        y=y)

            checkbox_ok = ctk.CTkCheckBox(master=self.option_frame,
                                          width=font_size * 1.5,
                                          height=font_size * 1.5,
                                          corner_radius=5,
                                          text="OK",
                                          font=("bold", font_size),
                                          command=lambda: self.checkbox_ok_function(name))
            checkbox_ok.place(x=10,
                              y=y + 10 + font_size * 1.5)

            checkbox_not_ok = ctk.CTkCheckBox(master=self.option_frame,
                                              width=font_size * 1.5,
                                              height=font_size * 1.5,
                                              corner_radius=5,
                                              text="Fehler",
                                              font=("bold", font_size),
                                              command=lambda: self.checkbox_not_ok_function(
                                                  name,
                                                  20 + font_size * 10,
                                                  y + 10 + font_size * 1.5))
            checkbox_not_ok.place(x=10 + font_size * 5,
                                  y=y + 10 + font_size * 1.5)

            entry = ctk.CTkEntry(master=self.option_frame,
                                 font=("bold", font_size),
                                 state="disabled",
                                 width=font_size * 23,
                                 height=font_size * 1.5
                                 )

            setattr(self, f"{name}_label", label)
            setattr(self, f"{name}_checkbox_ok", checkbox_ok)
            setattr(self, f"{name}_checkbox_not_ok", checkbox_not_ok)
            setattr(self, f"{name}_not_ok_entry", entry)

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 5:" +
                                                " Visuelle Beurteilung des Prüfstücks und der Schweißverbindungen"),
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
                                         command=lambda: self.master.confirm_go_back("1.3"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # option frame ------------------------------------------------------------
        self.option_frame = ctk.CTkFrame(master=self,  # frame for the textbox
                                         corner_radius=20,
                                         width=window_geometry[0] / 1.5,
                                         height=window_geometry[1] / 2)
        self.option_frame.place(x=0,
                                y=font_size * 2)

        visual_grading_widgets("weldingBead", "Schweißwulst", 10)
        visual_grading_widgets("weldingIndicators", "Schweißindikatoren", 30 + 2 * font_size * 1.5)
        visual_grading_widgets("damages", "Beschädigungen", 50 + 4 * font_size * 1.5)
        visual_grading_widgets("holdingClamps", "Halteklemmen", 70 + 6 * font_size * 1.5)
        visual_grading_widgets("offset", "Versatz", 90 + 8 * font_size * 1.5)

        # save and continue button------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=font_size * 6 + 20 + font_size * 5 + 10)
        self.button_frame.place(x=0,
                                y=font_size * 2 + window_geometry[1] / 2 + 10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="normal",
                                         command=lambda: self.save_textbox_data(),
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
                                             command=lambda: self.master.switch_window("1.5"),
                                             height=font_size * 1.5,
                                             width=font_size * 5)
        self.continue_button.place(x=font_size * 6 + 20,
                                   y=10)

    def save_textbox_data(self):
        visual_grade = [self.weldingBead_checkbox_ok.get(),
                        self.weldingBead_checkbox_not_ok.get(),
                        self.weldingIndicators_checkbox_ok.get(),
                        self.weldingIndicators_checkbox_not_ok.get(),
                        self.damages_checkbox_ok.get(),
                        self.damages_checkbox_not_ok.get(),
                        self.holdingClamps_checkbox_ok.get(),
                        self.holdingClamps_checkbox_not_ok.get(),
                        self.offset_checkbox_ok.get(),
                        self.offset_checkbox_not_ok.get(),
                        self.weldingBead_not_ok_entry.get(),
                        self.weldingIndicators_not_ok_entry.get(),
                        self.damages_not_ok_entry.get(),
                        self.holdingClamps_not_ok_entry.get(),
                        self.offset_not_ok_entry.get()]

        visual_grade_int = visual_grade[0:10]

        if sum(visual_grade_int) == 5 and len(visual_grade[10]) <= 35 \
                and len(visual_grade[11]) <= 35 \
                and len(visual_grade[12]) <= 35 \
                and len(visual_grade[13]) <= 35 \
                and len(visual_grade[14]) <= 35:
            personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
            personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
            json_writer(personal_json_name, "visual_grade", visual_grade, personal_folder_path)
            self.continue_button.configure(state="normal")
        else:
            if sum(visual_grade_int) != 5:
                messagebox.showinfo("Eingabefehler", "Bitte überall ein Kreuz setzen!")
                print("Type something! An empty field is not permitted!")
            elif len(visual_grade[10]) > 45:
                messagebox.showinfo("Eingabefehler", "Zu langer Text bei Schweißwulst!")
                print("Too long text at welding bead")
            elif len(visual_grade[11]) > 45:
                messagebox.showinfo("Eingabefehler", "Zu langer Text bei Schweißindikatoren!")
                print("Too long text at welding indicators")
            elif len(visual_grade[12]) > 45:
                messagebox.showinfo("Eingabefehler", "Zu langer Text bei Beschädigungen!")
                print("Too long text at damages")
            elif len(visual_grade[13]) > 45:
                messagebox.showinfo("Eingabefehler", "Zu langer Text bei Halteklemmen!")
                print("Too long text at holding clamps")
            elif len(visual_grade[14]) > 45:
                messagebox.showinfo("Eingabefehler", "Zu langer Text bei Versatz!")
                print("Too long text at offset")
            self.save_button.configure(state="normal")
            self.continue_button.configure(state="disabled")

    def reset_input_new_test(self):
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")
        self.weldingBead_checkbox_ok.deselect()
        self.weldingBead_checkbox_not_ok.deselect()
        self.weldingIndicators_checkbox_ok.deselect()
        self.weldingIndicators_checkbox_not_ok.deselect()
        self.damages_checkbox_ok.deselect()
        self.damages_checkbox_not_ok.deselect()
        self.holdingClamps_checkbox_ok.deselect()
        self.holdingClamps_checkbox_not_ok.deselect()
        self.offset_checkbox_ok.deselect()
        self.offset_checkbox_not_ok.deselect()
        self.weldingBead_not_ok_entry.place_forget()
        self.weldingIndicators_not_ok_entry.place_forget()
        self.damages_not_ok_entry.place_forget()
        self.holdingClamps_not_ok_entry.place_forget()
        self.offset_not_ok_entry.place_forget()

    def checkbox_ok_function(self, name):
        checkbox = getattr(self, f"{name}_checkbox_not_ok")
        entry = getattr(self, f"{name}_not_ok_entry")
        checkbox.deselect()
        entry.delete(0, "end")
        entry.configure(state="disabled")
        entry.place_forget()

    def checkbox_not_ok_function(self, name, x, y):
        global font_size
        checkbox_ok = getattr(self, f"{name}_checkbox_ok")
        checkbox_not_ok = getattr(self, f"{name}_checkbox_not_ok")
        entry = getattr(self, f"{name}_not_ok_entry")

        if checkbox_not_ok.get() == 1:
            checkbox_ok.deselect()
            entry.configure(state="normal",
                            placeholder_text="eventuelle Kurzbeschreibung des Fehlers",
                            font=("bold", font_size))
            entry.place(x=x,
                        y=y)
            self.master.focus_set()
        else:
            entry.delete(0, "end")
            entry.configure(state="disabled")
            entry.place_forget()
