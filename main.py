import tkinter as tk  # Import the Tkinter library for GUI
from tkinter import filedialog  # Import filedialog module for file selection dialog
import cv2  # Import OpenCV library for image processing
from PIL import Image, ImageTk  # Import Image and ImageTk modules from PIL library for image display
import os

def select_and_show_file():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename()  
    if file_path:  # If a file is selected
        # Read the selected image file
        image = cv2.imread(file_path)
        
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply image inversion
        invert = cv2.bitwise_not(gray_img)
        # Apply Gaussian blur
        blur = cv2.GaussianBlur(invert, (21,21), 0)
        # Apply another inversion
        invertedblur = cv2.bitwise_not(blur)
        # Apply division operation
        sketck = cv2.divide(gray_img, invertedblur, scale=256.0)
        
        # Extract file name and extension from the selected file path
        file_name, file_extension = os.path.splitext(file_path)
        # Generate a new file path for the processed image
        new_file_path = file_name + "_processed" + file_extension
        # Save the processed image to the new file path
        cv2.imwrite(new_file_path, sketck)
        
        # Open a new window to display the processed image
        new_window = tk.Toplevel(root)
        new_window.title("Processed Image")
        
        # Open and resize the processed image
        img = Image.open(new_file_path)
        img = img.resize((300, 300), Image.BICUBIC)
        img = ImageTk.PhotoImage(img)
        
        # Display the processed image in the new window
        label = tk.Label(new_window, image=img)
        label.image = img
        label.pack()

root = tk.Tk()
root.title("Main Window")  # Set the title of the main window
root.geometry("200x200")  # Set the geometry of the main window

# Define function to be executed when button is clicked
def on_click():
    select_and_show_file()

# Create a button for selecting and showing image
button = tk.Button(root, text="Select and Show Image", command=on_click)
button.place(relx=0.5, rely=0.5, anchor="center")  # Place the button in the center of the window

root.mainloop()  # Start the GUI event loop
