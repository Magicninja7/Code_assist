import pytesseract
from PIL import ImageGrab, Image
import tkinter as tk
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def screen():
    bbox = (467, 142, 1852, 858)
    screenshot = ImageGrab.grab(bbox)
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    processed_image = Image.fromarray(thresh)
    extracted_text = pytesseract.image_to_string(processed_image)
    print(extracted_text)
    return extracted_text

def app():
    root = tk.Tk()
    root.title("Code Assist")
    root.geometry("1500x1000")
    root.configure(bg="black")



    prompt_entry = tk.Entry(root, width=50, font=("Arial", 12))
    prompt_entry.pack(pady=20)

    text_display = tk.Text(root, width=100, height=40, font=("Arial", 12))
    text_display.pack(pady=20)
    extracted_text = screen()
    text_display.insert(tk.END, extracted_text)

    def on_send():
        prompt = prompt_entry.get()
        print(f"User prompt: {prompt}")

    send_button = tk.Button(root, text="Send", command=on_send, bg="gray", fg="white", font=("Arial", 12))
    send_button.pack()

    root.mainloop()


app()    