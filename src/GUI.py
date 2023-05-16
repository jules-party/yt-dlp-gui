import tkinter
import customtkinter as ct
import ytdg_lib as ytlib

formats = [ "mp3", "mp4" ]

ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

app = ct.CTk()
app.title('yt-dlp GUI')
app.geometry("240x400")
app.iconbitmap('icon.ico')

def set_format(fmt: str):
    global _format
    _format = fmt

def submit(url, fmt):
    status_text.configure(text="Downloading...")
    ytlib.download(url, fmt)
    status_text.configure(text="Done!")

text_input = ct.CTkEntry(master=app,
                         placeholder_text="Insert URL Here")

choice_list = ct.CTkComboBox(master=app,
                             state="readonly",
                             values=formats,
                             command=set_format)

submit_button = ct.CTkButton(master=app,
                             text="Submit",
                             command=lambda: submit(text_input.get(), _format))

status_text = ct.CTkLabel(master=app,
                          text="Download Status")

text_input.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
choice_list.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
submit_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
status_text.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

choice_list.set(formats[0])
set_format(formats[0])


app.mainloop()
