#!/usr/bin/env python3
""" Programa para centrar ventanas de tkinter en la pantalla. """
# *************************************************************************** #
# Company ... Bit Management (BitMan)
# Author .... Johannes Rosenkranz Cordovez (Roco)
# Email ..... jfronz@gmail.com
# *************************************************************************** #
# License
# GNU
# *************************************************************************** #


def center_window(window,
                  default=True,
                  margen_vertical=0,
                  margen_horizontal=0):
    ''' ... '''
    window.update_idletasks()

    if default:
        width = window.winfo_width()
        height = window.winfo_height()
    elif default == False:
        width = window.winfo_screenwidth() - vertical_margin
        height = window.winfo_screenheight() - horizontal_margin
    frame_width = window.winfo_rootx() - window.winfo_x()
    window_width = width + 2 * frame_width
    title_bar_height = window.winfo_rooty() - window.winfo_y()
    window_height = height + title_bar_height + frame_width
    posicion_en_x = window.winfo_screenwidth() // 2 - window_width // 2
    posicion_en_y = window.winfo_screenheight() // 2 - window_height // 2
    window.geometry(f'{width}x{height}+{posicion_en_x}+{posicion_en_y-30}')
    window.deiconify()
# *************************************************************************** #
