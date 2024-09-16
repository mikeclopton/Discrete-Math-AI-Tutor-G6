# THIS WILL NOT WORK WITHOUT THE NECESSARY DEPENDENCIES INSTALLED. DO NOT ATTEMPT TO RUN CODE, IT WILL NOT WORK

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageGrab # type: ignore
import cv2 # type: ignore
import numpy as np # type: ignore
import pytesseract

# Set the Tesseract executable path. Adjust the path if it's different on your machine.
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR'

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognition")
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg='white')
        self.canvas.pack()

        self.button_clear = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.button_clear.pack()

        self.button_recognize = tk.Button(self.root, text="Recognize", command=self.recognize_digit)
        self.button_recognize.pack()

        self.button_copy = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.button_copy.pack()

        self.canvas.bind("<B1-Motion>", self.draw)
        self.last_x, self.last_y = None, None
        self.recognized_digit = ""

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line((self.last_x, self.last_y, event.x, event.y), width=8, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.last_x = event.x
        self.last_y = event.y

    def clear_canvas(self):
        self.canvas.delete("all")
        self.last_x, self.last_y = None, None

    def recognize_digit(self):
        # Capture the canvas area
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        image = ImageGrab.grab().crop((x, y, x1, y1))
        image = image.convert('L')  # Convert to grayscale
        image.save("digit.png")  # Save the image for recognition
        
        # Preprocess the image and recognize the digit
        self.recognized_digit = self.recognize_from_image("digit.png")
        
        # Display the recognized digit
        if self.recognized_digit:
            messagebox.showinfo("Result", f"Recognized Digit: {self.recognized_digit}")
        else:
            messagebox.showerror("Error", "Could not recognize any digit.")

    def recognize_from_image(self, image_path):
        # Preprocess the image
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # Resize the image to 28x28 pixels (like the MNIST dataset)
        img = cv2.resize(img, (28, 28))

        # Apply binary thresholding to convert to black and white
        _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
        
        # Save the preprocessed image for debugging
        cv2.imwrite("preprocessed_digit.png", img)

        # Use Tesseract to recognize the digit
        digit = pytesseract.image_to_string(img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        digit = digit.strip()  # Clean up the recognized text

        return digit if digit else None

    def copy_to_clipboard(self):
        if self.recognized_digit:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.recognized_digit)
            self.root.update()  # Keep it on the clipboard after the window is closed
            messagebox.showinfo("Copied", f"Digit '{self.recognized_digit}' copied to clipboard.")
        else:
            messagebox.showerror("Error", "No digit to copy. Please recognize a digit first.")

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()