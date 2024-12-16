import pyautogui
import time
import random
import anthropic
import os
import keyboard
from datetime import datetime, timedelta
import tkinter as tk
import pytesseract
from PIL import ImageGrab, Image
import tkinter as tk
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'





snippet = []
prompt_for = []
files = []

def screen():
    bbox = (467, 142, 1852, 858)
    screenshot = ImageGrab.grab(bbox)
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    processed_image = Image.fromarray(thresh)
    extracted_text = pytesseract.image_to_string(processed_image)
    return extracted_text

def app():
    root = tk.Tk()
    root.title("Code Assist")
    root.geometry("1500x1000")
    root.configure(bg="black")

    prompt_entry = tk.Entry(root, width=50, font=("Arial", 12))
    prompt_entry.pack(pady=20)

    prompt1_entry = tk.Entry(root, width=50, font=("Arial", 12))
    prompt1_entry.pack(pady=20)


    def on_send():
        prompt = prompt_entry.get()
        prompt_for.append(prompt)

    def on_file():
        file = prompt1_entry.get()
        snippet.append(read_file(file))

    send_button = tk.Button(root, text="Send", command=on_send, bg="gray", fg="white", font=("Arial", 12))
    send_button.pack()

    send1_button = tk.Button(root, text="Send", command=on_file, bg="gray", fg="white", font=("Arial", 12))
    send1_button.pack()

    root.mainloop()





def read_file(filename):
    snippet = [] 
    extracting = False 

    with open(filename, 'r') as file:
        for line in file:
            if '#####' in line:
                extracting = not extracting 
                if not extracting:
                    break
                continue
            if extracting:
                snippet.append(line)
    return snippet




def code(Query, file, snippets):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key is None:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000000,
        temperature=0,
        system="You are a model that writes python code. You will be given a prompt and a code snippet (it will be a python list, where list[0] is the first line). Do what the user says. Wether it is to debug, or to add a feature, you must do it. You will be using pyautogui to write the code, therefor avoid using \ for anything other than to start a new line. Your code must be well-documented, and free from any type of bugs. Import all libraries needed. If the given code snippet isnt enough to fix it/create more, return; 'nothing'. Also, acknowledge that the code snippet may not be 100 percent accurate, as ti was caputred with PIL. Good luck!",
        messages=[
            {
                "role": "user", 
                "content": [{"type": "text", "text": zip(Query, snippets)}]
            }
        ]
    )
    final = message.content[0].text
    if final != 'nothing':
        return final
    elif final == 'nothing':
        message1 = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000000,
            temperature=0,
            system="You are a model that writes python code. You will be given a prompt and a code snippet (it will be a python list, where list[0] is the first line). Do what the user says. Wether it is to debug, or to add a feature, you must do it. You will be using pyautogui to write the code, therefor avoid using \ for anything other than to start a new line. Your code must be well-documented, and free from any type of bugs. Import all libraries needed. If the given code snippet isnt enough to fix it/create more, return; 'nothing'.Good luck!",
            messages=[
                {
                    "role": "user", 
                    "content": [{"type": "text", "text": zip(Query, file)}]
                }
            ]
        )
    final = message1.content[0].text
    return final


time.sleep(5)
pyautogui.write('###', interval=0.25)




def main():
    app()
    pyautogui.press('enter')

    file = files[-1]
    if not file:
        snippets = snippet[-1]
    else:
        snippets = ''
    prompt = input("Enter your prompt: ")
    message = code(prompt, file, snippets)


    for x in message:
        if x == '\n':
            time.sleep(1)
            keyboard.send('enter')
            pyautogui.hotkey('enter')
            for _ in range(3):
                pyautogui.hotkey('home')
        else:
            pyautogui.write(x)


main()

