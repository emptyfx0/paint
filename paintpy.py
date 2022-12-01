from tkinter import *
from tkinter import messagebox as mb
from tkinter.filedialog import *
from PIL import ImageTk
from PIL import ImageGrab
from PIL import Image


#---------------GLOBAL-VARIABLES-------------
getx_cash = None
gety_cash = None
color = None
size_draw = None
size_line = None
size = None
dote_array = []
name_figure = None
#--------------------------------------------


class WindowEvents:
    def close_window():
        exit(0)

    #def new_window(envet):


#--------SETINGS-FOR-DRAW--------------------
class DrawEvents:
    def line_function(event):
        global name_figure
        name_figure = "line"
    def triangle_function(event):
        global name_figure
        name_figure = "triangle"
    def rectangle_function(event):
        global name_figure
        name_figure = "rectangle"
    def oval_function(event):
        global name_figure
        name_figure = "oval"
    def cancel_function(event):
        global name_figure
        global dote_array
        dote_array.clear()
        name_figure = None
        
    def redcolor_function(event):
        global color
        color = "red"
        label_color["text"] = "RED"
        label_color["fg"] = "red"
        
    def bluecolor_function(event):
        global color
        color = "blue"
        label_color["text"] = "BLUE"
        label_color["fg"] = "blue"
        
    def greencolor_function(event):
        global color
        color = "green"
        label_color["text"] = "GREEN"
        label_color["fg"] = "green"

    def yellowcolor_function(event):
        global color
        color = "yellow"
        label_color["text"] = "YELLOW"
        label_color["fg"] = "yellow"
        
    def blackcolor_function(event):
        global color
        color = "black"
        label_color["text"] = "BLACK"
        label_color["fg"] = "black"
        
    def purplecolor_function(event):
        global color
        color = "purple"
        label_color["text"] = "PURPLE"
        label_color["fg"] = "purple"    

    def eraser_function(event):
        global color
        global name_figure
        name_figure = None
        color = "white"
        label_color["text"] = "ERASER"
        label_color["fg"] = "black"
        
    def stopdraw_function(event):
        label_status["text"] = "STOP"
        MouseEvents.getXY(event)
        
    def startdraw_function(event):
        label_status["text"] = "START"
        MouseEvents.getXY(event)
        
    def bigsize_function(event):
        global size_draw
        global size_line
        global size
        size_draw = 15
        size_line = 17
        size = 7
        label_fontsize["text"] = "BIG"
        
    def averagesize_function(event):
        global size_draw
        global size_line
        global size
        size_draw = 10
        size_line = 13
        size = 4
        label_fontsize["text"] = "AVERAGE"
        
    def smallsize_function(event):
        global size_draw
        global size_line
        global size
        size_draw = 5
        size_line = 9
        size = 4
        label_fontsize["text"] = "SMALL"

    def clearall_function(event):
        canvas.config(width=1076, height=500)
        root.geometry("1080x560")
        width = canvas["width"]
        height = canvas["height"]
        const_size = 5
        canvas.create_rectangle(int(width)+int(const_size),int(height)+int(const_size),0,0, fill="white", outline="white")
#--------------------------------------------
    


#---------------IMAGE------------------------
class ImageEvents:
    def add_image_function():
        path_file = askopenfilename()
        label_path_file["text"] = str(path_file)
        path = str(label_path_file["text"])
        dir_of_file = path.split(".")
        dir_of_file.reverse()
        if str(dir_of_file[0]) == "png" or str(dir_of_file[0]) == "jpg":
            image = Image.open(str(path))
            image = ImageTk.PhotoImage(image)
            canvas.config(width=image.width(), height=image.height())
            root.geometry("{0}x{1}".format(image.width(), image.height()))
            canvas.create_image(0, 0, image = image, anchor = NW)
        else:
            mb.showerror("Error type", "File can't be ."+dir_of_file[0]) 
        root.mainloop()


    def save_image_function():
        x=root.winfo_rootx()+canvas.winfo_x()
        y=root.winfo_rooty()+canvas.winfo_y()
        x1=x+canvas.winfo_width()
        y1=y+canvas.winfo_height()
        root.geometry("{0}x{1}".format(x1, y1))
        try:
            path_file = asksaveasfilename(filetypes=(("PNG files", "*.png"),("JPG files", "*.jpg")))
            ImageGrab.grab().crop((x,y,x1,y1)).save(str(path_file))
        except ValueError:
            mb.showerror("Error type", "Type can't be \'"+path_file+"\'")
        root.mainloop()
#--------------------------------------------



#---------------DRAW-------------------------
class MouseEvents:
    def getXY(event):
        getx=event.x     
        gety=event.y
        global getx_cash
        global gety_cash
        global size_draw
        global size_line
        global size
        global color
        global name_figure
        global dote_array
        if label_status["text"] == "STOP":
            pass
        if label_status["text"] == "START":
            if name_figure == None:   
                canvas.create_oval(getx,gety,(getx+size_draw),(gety+size_draw), fill = color, outline=color)
                if getx_cash != None and gety_cash != None:
                    canvas.create_line(getx+size, gety+size, (getx_cash+size), (gety_cash+size), fill=color, width=size_line)


                    
            if name_figure == "line":
                dote_array.append(getx)
                dote_array.append(gety)
                if len(dote_array) > 2:
                    if size == None and color == None:
                        canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill="black", width=3)
                    elif size == None and color != None:
                        canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill=color, width=3)
                    elif size != None and color == None:
                        canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill="black", width=size)
                    elif size != None and color != None:
                        canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill=color, width=size)
                    dote_array.clear()
            elif name_figure == "rectangle":
                dote_array.append(getx)
                dote_array.append(gety)
                if len(dote_array) > 2:
                    if size == None and color == None:
                        canvas.create_rectangle(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill="black", width=3)
                    elif size == None and color != None:
                        canvas.create_rectangle(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill=color, width=3)
                    elif size != None and color == None:
                        canvas.create_rectangle(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill="black", width=size)
                    elif size != None and color != None:
                        canvas.create_rectangle(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill=color, width=size)
                    dote_array.clear()
            elif name_figure == "oval":
                dote_array.append(getx)
                dote_array.append(gety)
                if len(dote_array) > 2:
                   if size == None and color == None:
                        canvas.create_oval(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill="black", width=3)
                   elif size == None and color != None:
                        canvas.create_oval(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill=color, width=3)
                   elif size != None and color == None:
                        canvas.create_oval(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill="black", width=size)
                   elif size != None and color != None:
                        canvas.create_oval(dote_array[0], dote_array[1], dote_array[2], dote_array[3], fill=color, width=size)
                   dote_array.clear()
            elif name_figure == "triangle":
                dote_array.append(getx)
                dote_array.append(gety)
                if len(dote_array) > 3:
                    if size == None and color == None:
                         canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], dote_array[4], dote_array[5], dote_array[0], dote_array[1], fill="black", width=3)
                    elif size == None and color != None:
                         canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], dote_array[4], dote_array[5], dote_array[0], dote_array[1], fill=color, width=3)
                    elif size != None and color == None:
                         canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], dote_array[4], dote_array[5], dote_array[0], dote_array[1], fill="black", width=size)
                    elif size != None and color != None:
                         canvas.create_line(dote_array[0], dote_array[1], dote_array[2], dote_array[3], dote_array[4], dote_array[5], dote_array[0], dote_array[1], fill=color, width=size)
                    dote_array.clear()

                   
        if label_status["text"] == "STOP":        
            canvas.bind("<Button-1>", DrawEvents.startdraw_function)
        if label_status["text"] == "START":
            canvas.bind("<ButtonRelease-1>", DrawEvents.stopdraw_function)
        getx_cash = getx
        gety_cash = gety
    def paint(event):
        canvas.bind("<Motion>", MouseEvents.getXY)
#--------------------------------------------


#--------------MAIN--------------------------    
class BindEvents:
    def MainWorkFunction():
        button_red.bind("<Button-1>", DrawEvents.redcolor_function)
        button_blue.bind("<Button-1>", DrawEvents.bluecolor_function)
        button_green.bind("<Button-1>", DrawEvents.greencolor_function)
        button_yellow.bind("<Button-1>", DrawEvents.yellowcolor_function)
        button_black.bind("<Button-1>", DrawEvents.blackcolor_function)
        button_purple.bind("<Button-1>", DrawEvents.purplecolor_function)
        button_big.bind("<Button-1>", DrawEvents.bigsize_function)
        button_average.bind("<Button-1>", DrawEvents.averagesize_function)
        button_small.bind("<Button-1>", DrawEvents.smallsize_function)
        button_eraser.bind("<Button-1>", DrawEvents.eraser_function)
        button_clearall.bind("<Button-1>", DrawEvents.clearall_function)
        button_create_line.bind("<Button-1>", DrawEvents.line_function)
        button_create_square.bind("<Button-1>", DrawEvents.rectangle_function)
        button_create_circle.bind("<Button-1>", DrawEvents.oval_function)
        button_create_triangle.bind("<Button-1>", DrawEvents.triangle_function)
        button_cancel_figure.bind("<Button-1>", DrawEvents.cancel_function)
        canvas.bind("<Button-1>", MouseEvents.paint)
#--------------------------------------------




#------------CREATE-WINDOW-AND-ELEMENTS------
if __name__ == "__main__":
    root = Tk()
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    root.title("Paint")
    root.geometry("1080x560")
    root.tk_setPalette(background="silver", foreground="white", activeBackground="black", activeForeground="white")
    #root.resizable(width=False, height=False)


    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Open...", command=ImageEvents.add_image_function)
    filemenu.add_command(label="Save...", command=ImageEvents.save_image_function)
    filemenu.add_command(label="Exit", command=WindowEvents.close_window)
    #filemenu.add_command(label="New", command=WindowEvents.new_window)

    mainmenu.add_cascade(label="File", menu=filemenu)

    label_color = Label(root, font=("Verdana", 10), text="NONE_COLOR", bg="silver", fg="white", height = 1, width = 18)
    label_fontsize = Label(root, font=("Verdana", 10), text="NONE_SIZE", bg="silver", fg="white", height = 1, width = 18)
    label_status = Label(root, font=("Verdana", 10), text="START", bg="silver", fg="white", height = 1, width = 18)
    label_path_file = Label(root)

    button_blue = Button(root, font=("Verdana", 10), bg="blue", fg="white", activebackground="black", activeforeground="white", height = 1, width = 1)
    button_green = Button(root, font=("Verdana", 10), bg="green", fg="white", activebackground="black", activeforeground="white", height = 1, width = 1)
    button_red = Button(root, font=("Verdana", 10), bg="red", fg="white", activebackground="black", activeforeground="white", height = 1, width = 1)
    button_yellow = Button(root, font=("Verdana", 10), bg="yellow", fg="white", activebackground="black", activeforeground="white", height = 1, width = 1)
    button_black = Button(root, font=("Verdana", 10), bg="black", fg="white", activebackground="black", activeforeground="white", height = 1, width = 1)
    button_purple = Button(root, font=("Verdana", 10), bg="purple", fg="white", activebackground="black", activeforeground="white", height = 1, width = 1)


    button_create_line = Button(root, font=("Verdana", 10), text="LINE", bg="black", fg="white", height = 1, width = 9)
    button_create_square = Button(root, font=("Verdana", 10), text="RECTANGLE", bg="black", fg="white", height = 1, width = 9)
    button_create_circle = Button(root, font=("Verdana", 10), text="OVAL", bg="black", fg="white", height = 1, width = 9)
    button_create_triangle = Button(root, font=("Verdana", 10), text="TRIANGLE", bg="black", fg="white", height = 1, width = 9)
    button_cancel_figure = Button(root, font=("Verdana", 10), text="CANCEL", bg="silver", fg="black", height = 1, width = 9)

    button_big = Button(root, font=("Verdana", 10), text="BIG", bg="silver", fg="black", activebackground="black", activeforeground="silver", height = 1, width = 5)
    button_average = Button(root, font=("Verdana", 10), text="AVER.", bg="silver", fg="black", activebackground="black", activeforeground="silver", height = 1, width = 5)
    button_small = Button(root, font=("Verdana", 10), text="SMALL", bg="silver", fg="black", activebackground="black", activeforeground="silver", height = 1, width = 5)

    image = Image.open("eraser.png")
    image = image.resize((12, 12), Image.Resampling.LANCZOS)
    image_button_eraser = ImageTk.PhotoImage(image)
    button_eraser = Button(root, font=("Verdana", 10), image=image_button_eraser, bg="silver", fg="black", activebackground="black", activeforeground="white", height = 22, width = 14)
    button_clearall = Button(root, font=("Verdana", 10), text="CLEAR ALL", bg="silver", fg="black", activebackground="black", activeforeground="white", height = 1, width = 10)

    canvas = Canvas(root, height=500, width=1076, bg="white", cursor="tcross")

    button_blue.place(x=150, y=0)
    button_red.place(x=168, y=0)
    button_green.place(x=186, y=0)
    button_yellow.place(x=204, y=0)
    button_black.place(x=222, y=0)
    button_purple.place(x=240, y=0)
    button_create_line.place(x=390, y=0)
    button_create_square.place(x=390, y=25)
    button_create_circle.place(x=470, y=0)
    button_create_triangle.place(x=470, y=25)
    button_cancel_figure.place(x=555, y=0)
    button_big.place(x=100, y=0)
    button_average.place(x=50, y=0)
    button_small.place(x=0, y=0)
    button_eraser.place(x=258, y=0)
    button_clearall.place(x=277, y=0)
    label_color.place(x=150, y=30)
    label_fontsize.place(x=0, y=30)
    canvas.place(x=0, y=50)

    BindEvents.MainWorkFunction()

    root.mainloop()
#--------------------------------------------
