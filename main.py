from customtkinter import *
from tkinter import filedialog
from tkinter import *
import json
import shutil
import os
from PIL import Image
import webbrowser

# Important Functions
def get_settings():
    if not os.path.exists("settings.json"):
        settings = open("settings.json", "w")
        settings.write('{\n    "info": "You can add more extensions in others(sections) or you can add more folders also FORMAT SHOULD BE SAME",\n    "c1": "#00ffff",\n    "c2": "#00dacd",\n    "c3": "#00b690",\n    "c4": "#009184",\n    "ext_types": {\n        "Images": [\n            ".png",\n            ".jpg",\n            ".jpeg",\n            ".gif",\n            ".tiff",\n            ".bmp",\n            ".svg",\n            ".webp"\n        ],\n        "Videos": [\n            ".mp4",\n            ".mkv",\n            ".webm",\n            ".flv",\n            ".vob",\n            ".ogv",\n            ".ogg",\n            ".drc",\n            ".gifv",\n            ".mng",\n            ".avi",\n            ".mov",\n            ".qt",\n            ".wmv",\n            ".yuv",\n            ".rm",\n            ".rmvb",\n            ".asf",\n            ".amv",\n            ".mpg",\n            ".mp2",\n            ".mpeg",\n            ".mpe",\n            ".mpv",\n            ".m2v",\n            ".m4p",\n            ".m4v",\n            ".svi",\n            ".3gp",\n            ".3g2",\n            ".mxf",\n            ".roq",\n            ".nsv",\n            ".f4v",\n            ".f4p",\n            ".f4a",\n            ".f4b"\n        ],\n        "Documents": [\n            ".pdf",\n            ".doc",\n            ".docx",\n            ".xls",\n            ".xlsx",\n            ".ppt",\n            ".pptx",\n            ".txt",\n            ".rtf",\n            ".tex",\n            ".wks",\n            ".wps",\n            ".wpd",\n            ".odt",\n            ".ods",\n            ".odp",\n            ".pages",\n            ".numbers",\n            ".key"\n        ],\n        "Audios": [\n            ".mp3",\n            ".wav",\n            ".ogg",\n            ".m4a",\n            ".flac",\n            ".aiff",\n            ".wma",\n            ".aac",\n            ".alac",\n            ".dsd",\n            ".pcm",\n            ".mp2",\n            ".ac3",\n            ".dts",\n            ".amr",\n            ".ape",\n            ".au",\n            ".caf",\n            ".dss",\n            ".gsm",\n            ".m4p",\n            ".mmf",\n            ".mpc",\n            ".oga",\n            ".opus",\n            ".ra",\n            ".shn",\n            ".tta",\n            ".vox",\n            ".wv"\n        ],\n        "Programs": [\n            ".exe",\n            ".msi",\n            ".apk",\n            ".app",\n            ".bat",\n            ".bin",\n            ".cgi",\n            ".pl",\n            ".com",\n            ".gadget",\n            ".jar",\n            ".wsf",\n            ".fnt",\n            ".cpl",\n            ".cur",\n            ".deskthemepack",\n            ".dll",\n            ".dmp",\n            ".drv",\n            ".icns",\n            ".ico",\n            ".lnk",\n            ".sys",\n            ".cfg",\n            ".ini",\n            ".tmp",\n            ".xpi",\n            ".crdownload",\n            ".part",\n            ".torrent"\n        ],\n        "Compressed": [\n            ".zip",\n            ".rar",\n            ".7z",\n            ".arj",\n            ".deb",\n            ".pkg",\n            ".rpm",\n            ".tar.gz",\n            ".z",\n            ".zipx",\n            ".bin",\n            ".cue",\n            ".dmg",\n            ".iso",\n            ".mdf",\n            ".toast",\n            ".vcd",\n            ".s7z",\n            ".tar",\n            ".gz",\n            ".xz",\n            ".bz2",\n            ".tbz2",\n            ".lzma",\n            ".txz"\n        ],\n        "Others": []\n    }\n}')
        settings.close()
    # Getting Settings
    settings = open("settings.json", "r")
    settings = settings.read()
    settings = json.loads(settings)
    return settings


def select_dir():
    loading_bar = CTkProgressBar(
        root, width=300, height=10, progress_color='blue')
    loading_bar.pack()
    loading_bar.configure(mode="indeterminate")
    loading_bar.start()
    dir = filedialog.askdirectory()
    if dir:
        list_dir = os.listdir(dir)
    else:
        loading_bar.stop()
        loading_bar.destroy()
        return
    ext_types = settings['ext_types']
    root.title("File Organizer [Abhi Cracker] | Status : Organizing")
    # Mapping The Files According To Their Extensions
    mapping(dir, list_dir, ext_types, loading_bar)


def mapping(dir, list_dir, ext_types, loading_bar):
    # Check if dir is a valid dir
    if not os.path.isdir(dir):
        raise ValueError(f"{dir} is not a valid dir")
    # Create folders for each file type in ext_types
    for folder_name in ext_types:
        folder_path = os.path.join(dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over files in the dir and move them to their respective folders
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[-1].lower()

            # Check which file type the current file belongs to
            for folder_name, extensions in ext_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(dir, folder_name)
                    dest_path = os.path.join(dest_folder, file)

                    # Move the file to the corresponding folder
                    shutil.move(file_path, dest_path)
                    break
            else:
                # If the file extension is not in ext_types, move it to the "Others" folder
                dest_folder = os.path.join(dir, "Others")
                dest_path = os.path.join(dest_folder, file)
                shutil.move(file_path, dest_path)

    for folder_name in ext_types:
        folder_path = os.path.join(dir, folder_name)
        if not os.listdir(folder_path):
            os.rmdir(folder_path)
    loading_bar.stop()
    loading_bar.destroy()
    os.startfile(dir)
    root.title("File Organizer [Abhi Cracker] | Status : Idle")


def github():
    # Opening Github or contact
    url = "https://github.com/AbhiCrackerOfficial"
    webbrowser.register('msedge', None, webbrowser.BackgroundBrowser(
        "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
    webbrowser.get('msedge').open(url)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")  # Fallback on absolute path
    return os.path.join(base_path, relative_path)


def edit_settings():
    # Declaration of Main Components
    # Settings 
    settings = get_settings()
    root.title("File Organizer [Abhi Cracker] | Status : Settings")
    app = CTk()
    app.title("Settings")
    app.geometry("500x700")
    app.resizable(False, False)
    app.iconbitmap(resource_path("icon.ico"))
    # Main Label
    settings_main_label = CTkLabel(app, text="Extension Settings", font=(
        'Agency Fb', 25, 'bold'), text_color=settings['c1'])
    # Message Frame
    message_frame = CTkFrame(app, height=25)
    message_frame_label = CTkLabel(message_frame, text="Logs", font=('Agency Fb', 15, 'bold'),
                                   text_color=settings['c3']).pack(padx=10, pady=10)
    # Settings Importanrt Functions

    def save_file(new_settings):
        root.title("File Organizer [Abhi Cracker] | Status : Save")
        settings = str(json.dumps(new_settings, indent=4))
        settings_file = open("settings.json", "w")
        settings_file.write(settings)
        settings_file.close()
        settings = get_settings()

    def disp_message(mess, color='red'):
        message = CTkLabel(message_frame, text=mess, font=(
            'Agency Fb', 15,'bold'), text_color=color)
        message.pack(pady=5)

    def add_ext():
        # Get Folder Name
        add_dialog1 = CTkInputDialog(text="Name of Folder", title="Add Folder")
        folder_name = (add_dialog1.get_input()).capitalize()
        if (len(folder_name) == 0):
            disp_message("Please Enter a Valid Name")
            return
        elif folder_name in settings['ext_types']:
            disp_message("Folder Already Exists")
            return
        # Get Extensions
        add_dialog2 = CTkInputDialog(
            text="Extensions (seperated by space or commas)", title="Add Extensions")
        input = add_dialog2.get_input()
        if ' ' in input and ',' in input:
            disp_message("Please Enter Extensions in Format")
            return
        elif ',' in input:
            exts = input.split(',')
        elif ' ' in input:
            exts = input.split()
        else:
            disp_message("Please Enter Space even if it's a single Extension")
            return
        if exts == []:
            disp_message("Please Enter Extensions in Format")
            return
        for i in range(len(exts)):
            exts[i] = exts[i].lower()
        # Add Extensions
        settings['ext_types'][folder_name] = exts
        # Save Settings
        save_file(settings)
        disp_message(
            f"Folder '{folder_name}' Added with its extensions", settings['c1'])

    def add_exts():
        # Get Folder Name
        add_dialog1 = CTkInputDialog(text="Name of Folder", title="Get Folder")
        folder_name = (add_dialog1.get_input()).capitalize()
        if (len(folder_name) == 0):
            disp_message("Please Enter a Valid Name")
            return
        elif folder_name not in settings['ext_types']:
            disp_message("Folder Does Not Exists")
            return
        elif folder_name == "Others":
            disp_message("You Can't Edit Others Folder")
            return
        # Get Extensions
        add_dialog2 = CTkInputDialog(
            text="Extensions (seperated by space or commas)", title="Add Extensions")
        input = add_dialog2.get_input()
        if ' ' in input and ',' in input:
            disp_message("Please Enter Extensions in Format")
            return
        elif ',' in input:
            exts = input.split(',')
        elif ' ' in input:
            exts = input.split()
        else:
            disp_message("Please Enter Space even if it's a single Extension")
            return
        if exts == []:
            disp_message("Please Enter Extensions in Format")
            return
        for i in range(len(exts)):
            exts[i] = exts[i].lower()
        # Edit Extensions
        settings['ext_types'][folder_name].extend(exts)
        # Save Settings
        save_file(settings)
        disp_message(
            f"Folder '{folder_name}'s Extensions has been updated", settings['c1'])

    def remove_exts():
        # Get Folder Name
        add_dialog1 = CTkInputDialog(text="Name of Folder", title="Get Folder")
        folder_name = (add_dialog1.get_input()).capitalize()
        if (len(folder_name) == 0):
            disp_message("Please Enter a Valid Name")
            return
        elif folder_name not in settings['ext_types']:
            disp_message("Folder Does Not Exists")
            return
        elif folder_name == "Others":
            disp_message("You Can't Edit Others Folder")
            return
        # Get Extensions
        add_dialog2 = CTkInputDialog(
            text="Extensions (seperated by space or commas)", title="Remove Extensions")
        input = add_dialog2.get_input()
        if ' ' in input and ',' in input:
            disp_message("Please Enter Extensions in Format")
            return
        elif ',' in input:
            exts = input.split(',')
        elif ' ' in input:
            exts = input.split()
        else:
            disp_message("Please Enter Space even if it's a single Extension")
            return
        if exts == []:
            disp_message("Please Enter Extensions in Format")
            return
        # Remove Extensions from folder
        for i in range(len(exts)):
            exts[i] = exts[i].lower()
        for ext in exts:
            if ext in settings['ext_types'][folder_name]:
                settings['ext_types'][folder_name].remove(ext)
        save_file(settings)
        disp_message(
            f"Folder '{folder_name}'s Extensions has been updated", settings['c1'])
    
    def del_folder():
        # Get Folder Name
        add_dialog1 = CTkInputDialog(text="Name of Folder", title="Get Folder")
        folder_name = (add_dialog1.get_input()).capitalize()
        if (len(folder_name) == 0):
            disp_message("Please Enter a Valid Name")
            return
        elif folder_name not in settings['ext_types']:
            disp_message("Folder Does Not Exists")
            return
        elif folder_name == "Others":
            disp_message("You Can't Edit Others Folder")
            return
        # Remove Folder
        settings['ext_types'].pop(folder_name)
        save_file(settings)
        disp_message(f"Folder '{folder_name}' Deleted", settings['c1'])

    def display_ext():
        disp_ext = CTk()
        disp_ext.title("Folders and Extensions")
        disp_ext.geometry("700x600")
        disp_ext.iconbitmap(resource_path("icon.ico"))
        # Main Label
        settings_main_label = CTkLabel(disp_ext, text="Folders and Extensions", font=(
            'Agency Fb', 32, 'bold'), text_color=settings['c1'])
        settings_main_label.pack(pady=20)
        # Back button
        back = CTkButton(disp_ext, text="Back", font=(
            'Sans Serif', 20), text_color=settings['c2'], command=disp_ext.destroy)
        back.pack(side='top', padx=10, pady=10)
        # list Box
        lb = Listbox(disp_ext, width=700, bd=0, highlightthickness=0,
                     selectforeground=settings['c2'], selectbackground='#1a1a1a', bg="#1a1a1a", fg=settings['c1'], font=('Sans Serif', 20))
        # Displaying Extensions
        for folder_name, extensions in settings['ext_types'].items():
            lb.insert(END, f"{folder_name} : {', '.join(extensions)}")
        lb.pack(side=LEFT, fill=BOTH)
        disp_ext.mainloop()

    def clear_logs():
        for label in message_frame.winfo_children():
            label_value = label.cget("text")
            if label_value != "Logs":
                label.destroy()

    def load_default_settings():
        default_settings = '{\n    "info": "You can add more extensions in others(sections) or you can add more folders also FORMAT SHOULD BE SAME",\n    "c1": "#00ffff",\n    "c2": "#00dacd",\n    "c3": "#00b690",\n    "c4": "#009184",\n    "ext_types": {\n        "Images": [\n            ".png",\n            ".jpg",\n            ".jpeg",\n            ".gif",\n            ".tiff",\n            ".bmp",\n            ".svg",\n            ".webp"\n        ],\n        "Videos": [\n            ".mp4",\n            ".mkv",\n            ".webm",\n            ".flv",\n            ".vob",\n            ".ogv",\n            ".ogg",\n            ".drc",\n            ".gifv",\n            ".mng",\n            ".avi",\n            ".mov",\n            ".qt",\n            ".wmv",\n            ".yuv",\n            ".rm",\n            ".rmvb",\n            ".asf",\n            ".amv",\n            ".mpg",\n            ".mp2",\n            ".mpeg",\n            ".mpe",\n            ".mpv",\n            ".m2v",\n            ".m4p",\n            ".m4v",\n            ".svi",\n            ".3gp",\n            ".3g2",\n            ".mxf",\n            ".roq",\n            ".nsv",\n            ".f4v",\n            ".f4p",\n            ".f4a",\n            ".f4b"\n        ],\n        "Documents": [\n            ".pdf",\n            ".doc",\n            ".docx",\n            ".xls",\n            ".xlsx",\n            ".ppt",\n            ".pptx",\n            ".txt",\n            ".rtf",\n            ".tex",\n            ".wks",\n            ".wps",\n            ".wpd",\n            ".odt",\n            ".ods",\n            ".odp",\n            ".pages",\n            ".numbers",\n            ".key"\n        ],\n        "Audios": [\n            ".mp3",\n            ".wav",\n            ".ogg",\n            ".m4a",\n            ".flac",\n            ".aiff",\n            ".wma",\n            ".aac",\n            ".alac",\n            ".dsd",\n            ".pcm",\n            ".mp2",\n            ".ac3",\n            ".dts",\n            ".amr",\n            ".ape",\n            ".au",\n            ".caf",\n            ".dss",\n            ".gsm",\n            ".m4p",\n            ".mmf",\n            ".mpc",\n            ".oga",\n            ".opus",\n            ".ra",\n            ".shn",\n            ".tta",\n            ".vox",\n            ".wv"\n        ],\n        "Programs": [\n            ".exe",\n            ".msi",\n            ".apk",\n            ".app",\n            ".bat",\n            ".bin",\n            ".cgi",\n            ".pl",\n            ".com",\n            ".gadget",\n            ".jar",\n            ".wsf",\n            ".fnt",\n            ".cpl",\n            ".cur",\n            ".deskthemepack",\n            ".dll",\n            ".dmp",\n            ".drv",\n            ".icns",\n            ".ico",\n            ".lnk",\n            ".sys",\n            ".cfg",\n            ".ini",\n            ".tmp",\n            ".xpi",\n            ".crdownload",\n            ".part",\n            ".torrent"\n        ],\n        "Compressed": [\n            ".zip",\n            ".rar",\n            ".7z",\n            ".arj",\n            ".deb",\n            ".pkg",\n            ".rpm",\n            ".tar.gz",\n            ".z",\n            ".zipx",\n            ".bin",\n            ".cue",\n            ".dmg",\n            ".iso",\n            ".mdf",\n            ".toast",\n            ".vcd",\n            ".s7z",\n            ".tar",\n            ".gz",\n            ".xz",\n            ".bz2",\n            ".tbz2",\n            ".lzma",\n            ".txz"\n        ],\n        "Others": []\n    }\n}'
        settings_file = open("settings.json", "w")
        settings_file.write(default_settings)
        settings_file.close()
        disp_message("Default Settings Loaded", settings['c1'])

    # Packing Of Main Components and New Buttons
    settings_main_label.pack(pady=20)
    message_frame.pack(pady=10, fill="x")
    # Extension Add Button
    add_ext = CTkButton(app, text="Add Folder and Extensions", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=add_ext)
    add_ext.pack(pady=12)
    # Extension Delete Button
    del_folder = CTkButton(app, text="Remove Folder", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=del_folder)
    del_folder.pack(pady=12)
    # Extension Edit Button
    edit_ext = CTkButton(app, text="Add Extensions to Folder", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=add_exts)
    edit_ext.pack(pady=12)
    # Extension Edit Button
    edit_ext = CTkButton(app, text="Remove Extensions from Folder", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=remove_exts)
    edit_ext.pack(pady=12)
    edit_ext.pack(pady=12)
    # Extension Display Button
    edit_ext = CTkButton(app, text="Display Folders and Extensions", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=display_ext)
    edit_ext.pack(pady=12)
    # Clear Message Logs
    clear_logs = CTkButton(app, text="Clear Logs", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=clear_logs)
    clear_logs.pack(pady=12)
    # load default settings
    load_default = CTkButton(app, text="Load Default Settings", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=load_default_settings)
    load_default.pack(pady=12)
    # back and save button
    back_save = CTkFrame(app)
    back_save.pack(side="bottom", fill="x")
    # back button
    back = CTkButton(back_save, text="Back", font=(
        'Sans Serif', 15), text_color=settings['c2'], command=lambda: [root.title("File Organizer [Abhi Cracker] | Status : Idle"), app.destroy()])
    back.pack(side="bottom", padx=10, pady=10)
    app.protocol("WM_DELETE_WINDOW", lambda: [root.title(
        "File Organizer [Abhi Cracker] | Status : Idle"), app.destroy()])
    app.mainloop()


# Root
settings = get_settings()
set_appearance_mode("dark")
set_default_color_theme("dark-blue")
root = CTk()
root.iconbitmap(resource_path("icon.ico"))
root.title("File Organizer [Abhi Cracker] | Status : Idle")
root.geometry("500x250")
root.resizable(False, False)

# Main Label
main_label = CTkLabel(root, text="File Organizer", font=(
    "Agency Fb", 42, "bold"), text_color=settings['c1'])
main_label.pack(pady=20)
# Author Label
author_label = CTkLabel(root, text="Developer : Abhi Cracker", font=(
    "Agency Fb", 13, "bold"), text_color=settings['c3'])
author_label.pack(pady=2)
# dir Selector
dir_selector = CTkButton(root, text="Select Directory", font=(
    "Sans Serif", 15), text_color=settings['c2'], command=select_dir)
dir_selector.pack(pady=16)
# Contact
image = CTkImage(dark_image=Image.open(resource_path("contact.png")),
                 size=(30, 30))
image_label = CTkButton(root, image=image, text="", fg_color='transparent',
                        hover_color=settings['c4'], width=10, command=github)
image_label.pack(anchor="se", side="left")
# settings
image = CTkImage(dark_image=Image.open(resource_path("settings.png")),
                 size=(30, 30))
image_label = CTkButton(root, image=image, text="", fg_color='transparent',
                        hover_color=settings['c4'], width=10, command=edit_settings)
image_label.pack(anchor="sw", side="right")
root.mainloop()
