import PySimpleGUI as sg 
window = sg.Window(title="Latihan Pertama", layout=[[sg.Text("NPM   : 2210010359")],
                                                    [sg.Text("Nama  : Muhammad Alfin Nur Huda")],
                                                    [sg.Text("Kelas : 5M Reg Pagi BJM")],
                                                    [sg.Text("Matkul : Pemrograman Visual 3")],
                                                    ],size=(400,200))
window()
window.close()