import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",

layout=[[sg.Text("SELAMAT DATANG DI KELAS",

font=("Arial",25,"italic","bold","underline"))],

[sg.Text("NPM : 2210010359 ")],
[sg.Text("Nama : Muhammad Alfin Nur Huda ")],
[sg.Text("Kelas : 5M Regular Banjarmasin ")]
],

size=(510,200),
font=("Times", 18))

window()
window.close()