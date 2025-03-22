#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Start Screen ; ID=0

import customtkinter as ctk
import sys
from .JsonFunctions import json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, \
    pruefstueck_image, main_pi_location  # import of shared variables located in the sharedVar-file


class StartScreen(ctk.CTkFrame):  # class for the StartScreen window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         fg_color="transparent",
                         width=window_geometry[0] - 10,
                         height=window_geometry[1] - 10)

        font_size = window_geometry[1] / 40
        pruefstueck_image.configure(size=(window_geometry[0] / 2 - 20,
                                          window_geometry[0] / 2 * (9 / 16) - 20))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text="Start",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w",
                                          width=window_geometry[0] - 20,
                                          height=font_size * 1.5)
        self.indicator_bar.place(x=0,
                                 y=0)

        # button frame------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # a frame for the buttons
                                         corner_radius=20,
                                         width=window_geometry[0] / 3.5,
                                         height=font_size * 9 + 40)
        self.button_frame.place(x=0,
                                y=font_size * 2)

        # new test button------------------------------------------------------------
        self.new_test_button = ctk.CTkButton(master=self.button_frame,
                                             # button to start a new test
                                             corner_radius=10,
                                             text="Neuer Test",
                                             font=("bold", font_size * 2),
                                             width=window_geometry[0] / 3.5 - 20,
                                             height=font_size * 3,
                                             command=lambda: self.new_test_button_function("1.0"))
        # the command calls the App lasses switch_window function and passes "1" as the "which" attribute
        self.new_test_button.place(x=10,
                                   y=10)

        # options button------------------------------------------------------------
        self.options_button = ctk.CTkButton(master=self.button_frame,
                                            # button to open the OptionsScreen
                                            corner_radius=font_size / 2,
                                            text="Optionen",
                                            font=("bold", font_size * 2),
                                            width=window_geometry[0] / 3.5 - 20,
                                            height=font_size * 3,
                                            command=lambda: self.master.switch_window("3"))
        # the command calls the App lasses switch_window function and passes "3" as the "which" attribute
        self.options_button.place(x=10,
                                  y=font_size * 3 + 20)

        # quit button------------------------------------------------------------
        self.quit_button = ctk.CTkButton(master=self.button_frame,
                                         # button to open the OptionsScreen
                                         corner_radius=font_size / 2,
                                         text="Beenden",
                                         font=("bold", font_size * 2),
                                         width=window_geometry[0] / 3.5 - 20,
                                         height=font_size * 3,
                                         command=lambda: sys.exit(0))
        self.quit_button.place(x=10,
                               y=font_size * 6 + 30)

        # image frame------------------------------------------------------------
        self.image_frame = ctk.CTkFrame(master=self,
                                        width=window_geometry[0] / 2,
                                        height=window_geometry[0] / 2 * (9 / 16),
                                        corner_radius=10)  # Frame for the StartScreen image
        self.image_frame.place(x=window_geometry[0] / 2.5,
                               y=font_size * 2)

        # image label----------------------------------------
        self.image_label = ctk.CTkLabel(master=self.image_frame,  # StartScreen image
                                        text="",
                                        image=pruefstueck_image)  # Here goes a render of the test object (maybe a gif)
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

    def new_test_button_function(self, which):
        json_writer("startup_var", "firstControlStartup", 1, main_pi_location + "../JSON/")
        self.master.switch_window(which)
        self.master.windows.get("1.1").reset_input_new_test()
        self.master.windows.get("1.2").reset_input_new_test()
        self.master.windows.get("1.3").reset_input_new_test()
        self.master.windows.get("1.4").reset_input_new_test()
        self.master.windows.get("1.5").reset_input_new_test()
        self.master.windows.get("4.0").reset_input_new_test()
