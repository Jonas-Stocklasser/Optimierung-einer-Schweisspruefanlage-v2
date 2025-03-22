#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# OptionenFenster; ID = 3

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer


class OptionsScreen(ctk.CTkFrame):  # class for the OptionsScreen window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         fg_color="transparent",
                         width=window_geometry[0] - 10,
                         height=window_geometry[1] - 10)

        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size*0.8, font_size*0.8))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text="Optionen",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w",
                                          width=window_geometry[0] - 30 - font_size*1.5,
                                          height=font_size * 1.5)
        self.indicator_bar.place(x=0,
                                 y=0)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         corner_radius=10,
                                         text="",
                                         anchor="center",
                                         image=back_arrow_image,
                                         command=lambda: self.master.switch_window("0"),
                                         width=font_size*1.5,
                                         height=font_size*1.5)
        # the command doesn't call the switch_window method because there is no unsaved content to loose
        self.back_button.place(x=(window_geometry[0]-font_size*1.5-25),
                               y=0)

        # button frame------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # frame for the buttons and the menu
                                         corner_radius=20,
                                         width=window_geometry[0] / 3.5,
                                         height=font_size * 3 + 30)
        self.button_frame.place(x=0,
                                y=font_size * 2)

        # light mode / dark mode ------------------------------------------------------------
        # label
        self.options_light_dark_label = ctk.CTkLabel(master=self.button_frame,
                                                     # label to describe the menu below
                                                     fg_color=GetStartupVariables.color_SET_blue,
                                                     corner_radius=10,
                                                     text="Anzeigemodus",
                                                     text_color=GetStartupVariables.text_color_SET,
                                                     font=("bold", font_size),
                                                     width=window_geometry[0]/6,
                                                     height=font_size * 1.5,
                                                     )
        self.options_light_dark_label.place(x=10,
                                            y=10)

        # option menu
        self.options_light_dark_menu = ctk.CTkOptionMenu(master=self.button_frame,
                                                         # menu for light / dark
                                                         font=("bold", font_size),
                                                         dropdown_font=("bold", font_size),
                                                         corner_radius=10,
                                                         values=GetStartupVariables.appearance_mode,
                                                         width=window_geometry[0]/3.5-20,
                                                         height=font_size*1.5,
                                                         command=self.appearance_mode_switch)
        # the command automatically passes the current value as an argument to the specified method
        self.options_light_dark_menu.place(x=10,
                                           y=font_size*1.5+20)


    def appearance_mode_switch(self, mode):  # method for switching the appearance mode to dark/light mode
        if mode == "light":
            json_writer("startup_var", "appearance_mode", ["light", "dark"], main_pi_location + "../JSON/")

        elif mode == "dark":
            json_writer("startup_var", "appearance_mode", ["dark", "light"], main_pi_location + "../JSON/")

        ctk.set_appearance_mode(mode)
