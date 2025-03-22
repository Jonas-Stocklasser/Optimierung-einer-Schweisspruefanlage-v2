#!/usr/bin/python3
# Date: 30.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Test Vorbereitung 1; ID=2.0

import customtkinter as ctk
import tkinter as tk
from .JsonFunctions import json_reader, json_writer
import RPi.GPIO as GPIO
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetExamParameterVariables, back_arrow_image

key_held = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, False)


class TestPreparations01(ctk.CTkFrame):  # class for the TestPreparations01 window
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
                                          text=("Testvorbereitung:" +
                                                " Anweisungen befolgen und entlüften"),
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
                                         command=lambda: self.master.confirm_go_back("1.5"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # text_frame------------------------------------------------------------
        self.left_frame = ctk.CTkFrame(master=self,  # frame for the text
                                       corner_radius=20,
                                       width=window_geometry[0] / 2.2,
                                       height=window_geometry[1] / 1.5 + 30 + font_size * 1.5)
        self.left_frame.place(x=0,
                              y=font_size * 2)

        self.text_frame = ctk.CTkFrame(master=self.left_frame,  # frame for the text
                                       corner_radius=10,
                                       width=window_geometry[0] / 2.2 - 20,
                                       height=window_geometry[1] / 1.5)
        self.text_frame.place(x=10,
                              y=10)

        # image_frame------------------------------------------------------------
        """self.right_frame = ctk.CTkFrame(master=self,  # frame for the image
                                        corner_radius=20,
                                        width=window_geometry[0] / 2.2,
                                        height=window_geometry[1] / 1.35)
        self.right_frame.place(x=window_geometry[0] / 2.1,
                               y=font_size * 2)"""

        # continue_button------------------------------------------------------------
        self.continue_button = ctk.CTkButton(master=self.left_frame,
                                             # continue button
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="normal",
                                             command=self.continue_button_function,
                                             height=font_size * 1.5,
                                             width=font_size * 5)
        self.continue_button.place(x=10,
                                   y=window_geometry[1] / 1.5 + 20)

        self.instruction_label = ctk.CTkLabel(master=self.text_frame,
                                              anchor="nw",
                                              text="Anweisungen befolgen!\n"
                                                   "\n"
                                                   "    1. Flansch auf Prüfstück aufsetzen\n"
                                                   "\n"
                                                   "    2. Prüfstück am Flansch aufhängen\n"
                                                   "\n"
                                                   "    3. Entlüftungsventil öffnen!\n"
                                                   "\n"
                                                   "    4. Pumpe an Flansch anschließen\n"
                                                   "\n"
                                                   "    5. Prüfstück entlüften\n"
                                                   "        -> (anschließend Ventil schließen)\n"
                                                   "\n"
                                                   "    6. Prüfstück in das Becken hinablassen\n"
                                                   "        -> Sensor darf nicht untertauchen"   
                                                   "\n"
                                                   "    7. Prüfvorgang starten (erst nach Entlüftung!)\n"
                                                   "        -> Weiter drücken\n"
                                                   "\n"
                                                   "-----------------------------------------------------------\n"
                                                   "Pumpe einschalten (ENTER)\n"
                                                   "-----------------------------------------------------------\n",
                                              justify="left",
                                              font=("bold", font_size - 2),
                                              width=window_geometry[0] / 2.2 - 40,
                                              height=window_geometry[1] / 1.5 - 20)
        self.instruction_label.place(x=10,
                                     y=10)

    def continue_button_function(self):
        self.master.switch_window("4.0")

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size, corner_radius=font_size / 2)
        self.back_button.configure(width=font_size,
                                   height=font_size, corner_radius=font_size / 2)
        back_arrow_image.configure(size=(font_size, font_size), corner_radius=font_size / 2)
        self.continue_button.configure(font=("bold", font_size), width=font_size * 3, height=font_size * 1.5,
                                       corner_radius=font_size / 2)
        self.instruction_label.configure(font=("bold", font_size * 0.9), corner_radius=font_size / 2)

    @staticmethod
    def unair_on(current_window):
        global key_held
        if not key_held and current_window == "2.0":
            print("Entlüftung start")
            GPIO.output(14, True)
            key_held = True

    @staticmethod
    def unair_off(current_window):
        global key_held
        if key_held and current_window == "2.0":
            print("Entlüftung ende")
            GPIO.output(14, False)
            key_held = False
