from tkinter import *
from tkinter import filedialog

file_path = ""
browser = ""
direct = ""
position = 0
text = ""
mark_text = ""


def image_watermark():
    ####################################################################################################################
    # Creating The Window For The Watermark
    watermark_window = Tk()
    watermark_window.title("Image Watermark")
    watermark_window.config(highlightthickness=0)
    ####################################################################################################################
    # Opening The Specified Image By The User
    canvas = Canvas(highlightthickness=0)
    photo = PhotoImage(file=f"{file_path}")
    canvas.create_image(237, 150, image=photo)  #
    canvas.grid(column=0, row=0, columnspan=3, rowspan=3)
    ####################################################################################################################
    # Applying The WaterMark Position as The User Specified
    if position == 1:  # Top Left
        file = Label(text=f"{mark_text}", font=("Arial", 12, "normal"))
        file.grid(column=0, row=0)

    elif position == 2:  # Top Right
        file = Label(text=f"{mark_text}", font=("Arial", 12, "normal"))
        file.grid(column=2, row=0)

    elif position == 3:  # Center
        file = Label(text=f"{mark_text}", font=("Arial", 12, "normal"))
        file.grid(column=1, row=1)

    elif position == 4:  # Bottom Left
        file = Label(text=f"{mark_text}", font=("Arial", 12, "normal"))
        file.grid(column=0, row=2)

    elif position == 5:  # Bottom Right
        file = Label(text=f"{mark_text}", font=("Arial", 12, "normal"))
        file.grid(column=2, row=2)

    watermark_window.mainloop()


def file_open():
    global direct, browser, text
    ####################################################################################################################
    # Creating The Browser Window
    open_file_window = Tk()
    open_file_window.title("Image Watermark")
    open_file_window.config(padx=100, pady=50)
    ####################################################################################################################
    # Creating The Canvas For The Image Background
    canvas = Canvas(highlightthickness=0)
    photo = PhotoImage(file="C:/Users/abdo_/OneDrive/Desktop/bg.png")
    canvas.create_image(237, 122, image=photo)  #
    canvas.grid(column=0, row=0, columnspan=3, rowspan=3)
    ####################################################################################################################
    # Creating The Inputs For Browsing File Button and The Path Field
    button_explore = Button(open_file_window, text="Browse Files", command=browse_files)
    button_explore.grid(column=3, row=4)
    image_path = Entry(width=40)
    image_path.grid(column=1, row=4, columnspan=2)
    image_path.focus()
    watermark_text = Entry(width=40)
    watermark_text.grid(column=1, row=5, columnspan=2)
    ####################################################################################################################
    # Creating Watermark Positions Option Buttons
    button_top_right = Button(open_file_window, text="Top Right", command=top_right)
    button_top_right.grid(column=5, row=0)
    button_top_left = Button(open_file_window, text="Top Left", command=top_left)
    button_top_left.grid(column=3, row=0)

    button_center = Button(open_file_window, text="Center", command=center)
    button_center.grid(column=4, row=1)

    button_down_right = Button(open_file_window, text="Bottom Right", command=down_right)
    button_down_right.grid(column=5, row=2)
    button_down_left = Button(open_file_window, text="Bottom Left", command=down_left)
    button_down_left.grid(column=3, row=2)

    button_proceed = Button(open_file_window, text="Proceed", command=proceed, bg="blue")
    button_proceed.grid(column=1, row=6)
    ####################################################################################################################
    # Creating Labels For the Program and The Path Input Field
    message = Label(text="Welcome To Image Watermarking Using Tkinter\n"
                         "You can either browse files or enter the path", font=("Arial", 12, "normal"))
    message.grid(column=1, row=3)

    file = Label(text="File Path", font=("Arial", 12, "normal"))
    file.grid(column=0, row=4)

    mark = Label(text="Watermark", font=("Arial", 12, "normal"))
    mark.grid(column=0, row=5)
    ####################################################################################################################
    direct = image_path
    text = watermark_text
    browser = open_file_window
    open_file_window.mainloop()


def top_right():
    global position
    position = 2


def top_left():
    global position
    position = 1


def down_right():
    global position
    position = 5


def down_left():
    global position
    position = 4


def center():
    global position
    position = 3


def proceed():
    global file_path, direct, browser, mark_text
    if (position >= 1) or (position <= 5):
        if len(file_path) != 0:
            mark_text = text.get()
            browser.destroy()
            image_watermark()

        else:
            mark_text = text.get()
            file_path = direct.get()
            browser.destroy()
            image_watermark()


def browse_files():
    global file_path
    filename = filedialog.askopenfilename(initialdir="C:/Users/abdo_/OneDrive/Desktop", title="Select a File",
                                          filetypes=(("all files", "*.jpg*"), ("all files", "*.*")))
    file_path = filename


file_open()

