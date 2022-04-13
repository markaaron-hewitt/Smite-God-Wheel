# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:10:26 2021

@author: MarkyMark
"""

import tkinter as tk
import smite
from PIL import Image, ImageTk

BACKGROUND_COLOUR = 'black'
TEXT_COLOUR = 'goldenrod1'
FONT = 'Penumbra Half Serif'
BUTTON_COLOUR = 'royalblue4'
BUTTON_TEXT_COLOUR = 'white'
ACTIVE_BUTTON_COLOUR = 'royalblue'
ACTIVE_BUTTON_TEXT_COLOUR = 'white'
BUTTON_WIDTH = 18

class GUI():
    
    def __init__(self, master):
        self.frm_mainframe=tk.Frame(master)
        self.configure_grid()
        self.load_icon()
        self.godNumber = tk.IntVar(self.frm_mainframe, 0)
        self.lbl_title = tk.Label(self.frm_mainframe, text = "Marky Mark's SMITE God Wheel")
        self.lbl_title.grid(row=self.ROW_TITLE, column=0, columnspan = 5)
        self.lbl_godNumber = tk.Label(self.frm_mainframe, text = "Number of Gods:")
        self.lbl_godNumber.grid(row = self.ROW_LBLGODNUMBER, column = 0, columnspan = 5)
        self.rbtn_godNumber1 = tk.Radiobutton(self.frm_mainframe,text = '1', variable = self.godNumber, value = 1, indicator = 0)
        self.rbtn_godNumber1.grid(row=self.ROW_GODNUMBER,column=0)
        self.rbtn_godNumber1.bind("<Return>", self.god1_Event)
        self.rbtn_godNumber2 = tk.Radiobutton(self.frm_mainframe,text = '2', variable = self.godNumber, value = 2, indicator = 0)
        self.rbtn_godNumber2.grid(row=self.ROW_GODNUMBER,column=1)
        self.rbtn_godNumber2.bind("<Return>", self.god2_Event)
        self.rbtn_godNumber3 = tk.Radiobutton(self.frm_mainframe,text = '3', variable = self.godNumber, value = 3, indicator = 0)
        self.rbtn_godNumber3.grid(row=self.ROW_GODNUMBER,column=2)
        self.rbtn_godNumber3.bind("<Return>", self.god3_Event)
        self.rbtn_godNumber4 = tk.Radiobutton(self.frm_mainframe,text = '4', variable = self.godNumber, value = 4, indicator = 0)
        self.rbtn_godNumber4.grid(row=self.ROW_GODNUMBER,column=3)
        self.rbtn_godNumber4.bind("<Return>", self.god4_Event)
        self.rbtn_godNumber5 = tk.Radiobutton(self.frm_mainframe,text = '5', variable = self.godNumber, value = 5, indicator = 0)
        self.rbtn_godNumber5.grid(row=self.ROW_GODNUMBER,column=4,)
        self.rbtn_godNumber5.bind("<Return>", self.god5_Event)
        self.btn_spinWheel=tk.Button(self.frm_mainframe)
        self.btn_spinWheel.config(text='Spin the Wheel!', command=self.spin_wheel, relief = 'raised')
        self.btn_spinWheel.grid(row=self.ROW_SPINWHEEL_BUTTON, column=0, columnspan = 5)
        self.btn_spinWheel.bind("<Return>", self.spin_wheel_Event)
        self.lbl_img_god1 = tk.Label(self.frm_mainframe, bg = BACKGROUND_COLOUR, fg = TEXT_COLOUR, image = "")
        self.lbl_img_god1.grid(row=self.ROW_IMAGES,column=0)
        self.lbl_img_god2 = tk.Label(self.frm_mainframe, bg = BACKGROUND_COLOUR, fg = TEXT_COLOUR, image = "")
        self.lbl_img_god2.grid(row=self.ROW_IMAGES,column=1)
        self.lbl_img_god3 = tk.Label(self.frm_mainframe, bg = BACKGROUND_COLOUR, fg = TEXT_COLOUR, image = "")
        try:
            self.lbl_img_god3.config(image = self.img_icon)
        except:
            pass
        self.lbl_img_god3.grid(row=self.ROW_IMAGES,column=2)
        self.lbl_img_god4 = tk.Label(self.frm_mainframe, bg = BACKGROUND_COLOUR, fg = TEXT_COLOUR, image = "")
        self.lbl_img_god4.grid(row=self.ROW_IMAGES,column=3)
        self.lbl_img_god5 = tk.Label(self.frm_mainframe, bg = BACKGROUND_COLOUR, fg = TEXT_COLOUR, image = "")
        self.lbl_img_god5.grid(row=self.ROW_IMAGES,column=4)
        self.lbl_god1 = tk.Label(self.frm_mainframe, text = "")
        self.lbl_god1.grid(row=self.ROW_NAMES,column=0)
        self.lbl_god2 = tk.Label(self.frm_mainframe, text = "")
        self.lbl_god2.grid(row=self.ROW_NAMES,column=1)
        self.lbl_god3 = tk.Label(self.frm_mainframe, text = "")
        self.lbl_god3.grid(row=self.ROW_NAMES,column=2)
        self.lbl_god4 = tk.Label(self.frm_mainframe, text = "")
        self.lbl_god4.grid(row=self.ROW_NAMES,column=3)
        self.lbl_god5 = tk.Label(self.frm_mainframe, text = "")
        self.lbl_god5.grid(row=self.ROW_NAMES,column=4)
        self.frm_mainframe.pack(fill=tk.BOTH,expand=1)
    
    def get_img_icon(self):
        return self.img_icon
    
    def configure_grid(self):
        self.ROW_TITLE = 0
        self.ROW_LBLGODNUMBER = 1
        self.ROW_GODNUMBER = 2
        self.ROW_SPINWHEEL_BUTTON = 4
        self.ROW_IMAGES = 5
        self.ROW_NAMES = 6
        columns = 0
        while columns < 5:
            self.frm_mainframe.columnconfigure(columns,minsize=155)
            columns += 1
        self.frm_mainframe.rowconfigure(3,minsize=10)
        self.frm_mainframe.rowconfigure(self.ROW_IMAGES,minsize=210)
        self.frm_mainframe.rowconfigure(self.ROW_NAMES,minsize=30)
    
    def spin_wheel_Event(self,event):
        self.spin_wheel()
        #root.destroy()
    
    def god1_Event(self,event):
        self.rbtn_godNumber1.select()
        
    def god2_Event(self,event):
        self.rbtn_godNumber2.select()
        
    def god3_Event(self,event):
        self.rbtn_godNumber3.select()
        
    def god4_Event(self,event):
        self.rbtn_godNumber4.select()
        
    def god5_Event(self,event):
        self.rbtn_godNumber5.select()
        
    def load_icon(self):
        self.icon = Image.open("Smite_Lightning.png")
        self.icon = self.icon.resize((150,150),Image.ANTIALIAS)
        self.img_icon = ImageTk.PhotoImage(self.icon)
    
    def spin_wheel(self):     #Function activated when user clicks to spin the wheel for random gods
        '''
        self.lbl_god1.config(text = "5")
        self.frm_mainframe.update()
        self.frm_mainframe.after(500)
        self.lbl_god1.config(text = "4")
        self.frm_mainframe.update()
        self.frm_mainframe.after(500)
        self.lbl_god1.config(text = "3")
        self.frm_mainframe.update()
        self.frm_mainframe.after(500)
        self.lbl_god1.config(text = "2")
        self.frm_mainframe.update()
        self.frm_mainframe.after(500)
        self.lbl_god1.config(text = "1")
        self.frm_mainframe.update()
        self.frm_mainframe.after(500)
        self.lbl_god1.config(text = "0")
        self.frm_mainframe.update()
        self.frm_mainframe.after(500)
        '''
        
        n = self.godNumber.get()
        self.SpinWheel_Flash(n)
        gods = smite.random_gods(n)
        self.display_god_names(gods,n)
        self.display_god_images(gods,n)
        
    def SpinWheel_Flash(self,n):
        self.display_god_names([],0)
        self.display_god_images([],0) 
        self.frm_mainframe.update()
        self.btn_spinWheel.flash()
        
        '''
        for i in range(3):
            gods = smite.random_gods(n)
            #self.display_god_names(gods,n)
            self.display_god_images(gods,n)
            self.frm_mainframe.update()
            self.frm_mainframe.after(25)
        '''

    def display_god_names(self,gods,n):      #Displays (on the GUI) the n randomised gods recieved
        if n == 0:
            display = ['','','','','']
        elif n == 1:
            display = ['','',gods[0],'','']
        elif n == 2:
            display = ['',gods[0],'',gods[1],'']
        elif n == 3:
            display = ['',gods[0],gods[1],gods[2],'']
        elif n == 4: 
            display = [gods[0],gods[1],'',gods[2],gods[3]]
        else:
            display = [gods[0],gods[1],gods[2],gods[3],gods[4]]
        self.lbl_god1.config(text = display[0])
        self.lbl_god2.config(text = display[1])
        self.lbl_god3.config(text = display[2])
        self.lbl_god4.config(text = display[3])
        self.lbl_god5.config(text = display[4])
    
    def display_god_images(self,gods,n):      #Displays (on the GUI( the images of the n randomised gods recieved
        godImages = []
        for i in range(n):
            godImages.append( gods[i].get_Name() )
            godImages[i] = godImages[i].replace(" ","")
            godImages[i] = godImages[i].replace("'","")     
            godImages[i] = "god_images\SkinArt_"+ godImages[i] + "_Default.jpg"
        if n == 0:
            display = ['','','','','']
        elif n == 1:
            display = ['icon','',godImages[0],'','icon']
        elif n == 2:
            display = ['',godImages[0],'icon',godImages[1],'']
        elif n == 3:
            display = ['icon',godImages[0],godImages[1],godImages[2],'icon']
        elif n == 4: 
            display = [godImages[0],godImages[1],'icon',godImages[2],godImages[3]]
        else:
            display = [godImages[0],godImages[1],godImages[2],godImages[3],godImages[4]]
        if display[0] == '':
            self.lbl_img_god1.config(image = '')
        elif display[0] == 'icon':
            self.lbl_img_god1.config(image = self.img_icon)
        else:
            self.img_god1_load = Image.open(display[0])
            self.img_god1_load=self.img_god1_load.resize((150,200),Image.ANTIALIAS)
            self.img_god1 = ImageTk.PhotoImage(self.img_god1_load)
            self.lbl_img_god1.config(image = self.img_god1)
        if display[1] == '':
            self.lbl_img_god2.config(image = '')
        elif display[1] == 'icon':
            self.lbl_img_god2.config(image = self.img_icon)
        else:
            self.img_god2_load = Image.open(display[1])
            self.img_god2_load=self.img_god2_load.resize((150,200),Image.ANTIALIAS)
            self.img_god2 = ImageTk.PhotoImage(self.img_god2_load)
            self.lbl_img_god2.config(image = self.img_god2)
        if display[2] == '':
            self.lbl_img_god3.config(image = '')
        elif display[2] == 'icon':
            self.lbl_img_god3.config(image = self.img_icon)
        else:
            self.img_god3_load = Image.open(display[2])
            self.img_god3_load=self.img_god3_load.resize((150,200),Image.ANTIALIAS)
            self.img_god3 = ImageTk.PhotoImage(self.img_god3_load)
            self.lbl_img_god3.config(image = self.img_god3)
        if display[3] == '':
            self.lbl_img_god4.config(image = '')
        elif display[3] == 'icon':
            self.lbl_img_god4.config(image = self.img_icon)
        else:
            self.img_god4_load = Image.open(display[3])
            self.img_god4_load=self.img_god4_load.resize((150,200),Image.ANTIALIAS)
            self.img_god4 = ImageTk.PhotoImage(self.img_god4_load)
            self.lbl_img_god4.config(image = self.img_god4)
        if display[4] == '':
            self.lbl_img_god5.config(image = '')
        elif display[4] == 'icon':
            self.lbl_img_god5.config(image = self.img_icon)
        else:
            self.img_god5_load = Image.open(display[4])
            self.img_god5_load=self.img_god5_load.resize((150,200),Image.ANTIALIAS)
            self.img_god5 = ImageTk.PhotoImage(self.img_god5_load)
            self.lbl_img_god5.config(image = self.img_god5)

    def Configure_Preferences(self):        #Sets background colour, text colour etc.
        self.frm_mainframe.config(bg=BACKGROUND_COLOUR)
        self.lbl_title.config(bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR,font = (FONT, 20, "bold"))
        self.lbl_godNumber.config(bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR,font = (FONT, 10, "bold"))
        self.rbtn_godNumber1.config(font = (FONT, 10, "bold"),width=BUTTON_WIDTH,bg=BUTTON_COLOUR,fg=BUTTON_TEXT_COLOUR,activebackground=ACTIVE_BUTTON_COLOUR,activeforeground=ACTIVE_BUTTON_TEXT_COLOUR, selectcolor = ACTIVE_BUTTON_COLOUR)
        self.rbtn_godNumber2.config(font = (FONT, 10, "bold"),width=BUTTON_WIDTH,bg=BUTTON_COLOUR,fg=BUTTON_TEXT_COLOUR,activebackground=ACTIVE_BUTTON_COLOUR,activeforeground=ACTIVE_BUTTON_TEXT_COLOUR, selectcolor = ACTIVE_BUTTON_COLOUR)
        self.rbtn_godNumber3.config(font = (FONT, 10, "bold"),width=BUTTON_WIDTH,bg=BUTTON_COLOUR,fg=BUTTON_TEXT_COLOUR,activebackground=ACTIVE_BUTTON_COLOUR,activeforeground=ACTIVE_BUTTON_TEXT_COLOUR, selectcolor = ACTIVE_BUTTON_COLOUR)
        self.rbtn_godNumber4.config(font = (FONT, 10, "bold"),width=BUTTON_WIDTH,bg=BUTTON_COLOUR,fg=BUTTON_TEXT_COLOUR,activebackground=ACTIVE_BUTTON_COLOUR,activeforeground=ACTIVE_BUTTON_TEXT_COLOUR, selectcolor = ACTIVE_BUTTON_COLOUR)
        self.rbtn_godNumber5.config(font = (FONT, 10, "bold"),width=BUTTON_WIDTH,bg=BUTTON_COLOUR,fg=BUTTON_TEXT_COLOUR,activebackground=ACTIVE_BUTTON_COLOUR,activeforeground=ACTIVE_BUTTON_TEXT_COLOUR, selectcolor = ACTIVE_BUTTON_COLOUR)
        self.lbl_god1.config(bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR,font = (FONT, 10, "bold"))
        self.lbl_god2.config(bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR,font = (FONT, 10, "bold"))
        self.lbl_god3.config(bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR,font = (FONT, 10, "bold"))
        self.lbl_god4.config(bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR,font = (FONT, 10, "bold"))
        self.lbl_god5.config(bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR,font = (FONT, 10, "bold"))
        self.btn_spinWheel.config(font = (FONT, 10, "bold"),bg=BUTTON_COLOUR,fg=BUTTON_TEXT_COLOUR,activebackground=ACTIVE_BUTTON_COLOUR,activeforeground=ACTIVE_BUTTON_TEXT_COLOUR)

def load_image_dictionary():
    print('loading start')
    global IMAGE_DICTIONARY
    IMAGE_DICTIONARY = {}
    for god in smite.GOD_LIST:
        name = god.get_Name()
        file_name = name.replace(" ","")
        file_name = file_name.replace("'","")
        file_name = "god_images\SkinArt_"+ file_name + "_Default.jpg"
        image = Image.open(file_name)
        image = image.resize((150,200),Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        IMAGE_DICTIONARY.update({name:image}) 
    print('loading end')

def main():
    smite.main()
    global root,app
    print('There should probably be a user interface somewhere...')
    root = tk.Tk()
    root.configure(background='black')
    root.title("Smite God Wheel")
    #root.overrideredirect(0)
    app = GUI(root)
    app.Configure_Preferences()
    #load_image_dictionary()
    try:
        #p1 = tk.PhotoImage(file = "Smite_Lightning.png")
        #icon = app.get_icon()
        #icon.thumbnail((100,100))
        #img_icon = ImageTk.PhotoImage(icon)
        root.iconphoto(False, app.get_img_icon())
    except:
       pass
    #root.attributes('-fullscreen', True)
    root.mainloop()

if __name__ == "__main__":
    main()