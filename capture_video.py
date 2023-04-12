import cv2
import tkinter as tk
from PIL import Image, ImageTk

def show_frame():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    label_video.imgtk = imgtk
    label_video.configure(image=imgtk)
    label_video.after(10, show_frame)

def capture_image():
    _, frame = cap.read()
    filename = "capture.jpg"
    cv2.imwrite(filename, frame)

root = tk.Tk()
root.title("Capture Images from Live Feed")

label_video = tk.Label(root)
label_video.pack()

button_capture = tk.Button(root, text="Capture Image", command=capture_image)
button_capture.pack()

cap = cv2.VideoCapture(0)
show_frame()

root.mainloop()

