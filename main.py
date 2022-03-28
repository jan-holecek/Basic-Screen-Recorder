import pyautogui 
import cv2 
import numpy as np 
from tkinter import *

class screenRecorder:
    def __init__(self, win):
        # Specify resolution 
        self.resolution = tuple(pyautogui.size())

        # Specify video codec 
        self.codec = cv2.VideoWriter_fourcc(*"XVID") 

        # Specify frames rate
        self.fps = 8.0 

        # GUI title text
        self.title = Label(win, text="ScreenRecorder", font=("Helvetica", 16))
        self.title.pack(ipadx = 5)

        # GUI stop info text
        self.text = Label(win, text="Press Q to stop recording", font=("Helvetica", 8))
        self.text.pack(ipadx = 5)

        # GUI label text
        self.lbl = Label(win, text='Video name')
        self.lbl.pack(ipadx = 5)

        # GUI video name 
        self.name = Entry()
        self.name.pack(ipadx = 5)

        # GUI start button
        self.startBtn = Button(win, text='Start', width = 10, height = 1, command = self.start)
        self.startBtn.place(x = 60, y = 110)

    def start(self):
        # Acquired video title
        self.lbl2 = str(self.name.get())

        # The name of the output file
        self.filename = self.lbl2 + ".avi"

        # Creating a VideoWriter object 
        self.out = cv2.VideoWriter(self.filename, self.codec, self.fps, self.resolution)  

        # Create an empty window 
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 

        # Dimensions this window 
        cv2.resizeWindow("Live", 480, 270)  

        while True: 
            # Take screenshot using PyAutoGUI 
            self.img = pyautogui.screenshot() 

            # Convert the screenshot to a numpy array 
            self.frame = np.array(self.img) 

            # Convert it from BGR(Blue, Green, Red) to 
            # RGB(Red, Green, Blue) 
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) 

            # Write it to the output file 
            self.out.write(self.frame) 

            # Optional: Display the recording screen 
            cv2.imshow("Live", self.frame)
            
            # Closes windows when specified keys are pressed
            if cv2.waitKey(1) == ord('q'): 
                # Release the Video writer 
                self.out.release() 

                # Destroy window
                window.destroy()
                break 


window = Tk()
window.iconbitmap("screenRecorder-icon.ico") # GUI window icon
mywin = screenRecorder(window) 
window.geometry("200x150+10+10") # GUI window dimensions
window.mainloop()
