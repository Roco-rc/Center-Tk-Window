#!/usr/bin/env python3
""" Programa para centrar ventanas de tkinter en la pantalla. """
# *************************************************************************** #
# Company ... Bit Management (BitMan)
# Author .... Johannes Rosenkranz Cordovez (Roco)
# Email ..... jfronz@gmail.com
# *************************************************************************** #
# License
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
