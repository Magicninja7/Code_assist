import pyautogui
import time
import random
import anthropic
import os
import keyboard
from datetime import datetime, timedelta


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




def code(Query, file):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key is None:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000000,
        temperature=0,
        system="You are a model that writes python code. You will be given a prompt and a code snippet (it will be a python list, where list[0] is the first line). Do what the user says. Wether it is to debug, or to add a feature, you must do it. You will be using pyautogui to write the code, therefor avoid using \ for anything other than to start a new line. Your code must be well-documented, and free from any type of bugs. You can assume that any libraries are already imported. Good luck!",
        messages=[
            {
                "role": "user", 
                "content": [{"type": "text", "text": Query, }]
            }
        ]
    )
    return message.content[0].text


time.sleep(5)
pyautogui.write('###', interval=0.25)




def main():
    pyautogui.press('enter')

    file = input("What file do you want to analyse?")
    prompt = input("Enter your prompt: ")
    message = code(prompt)


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