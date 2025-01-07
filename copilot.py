import pyautogui
import time
import random
import anthropic
import os
import keyboard
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog  
import pytesseract
from PIL import ImageGrab, Image
import tkinter as tk
import cv2
import numpy as np
import re
import argparse
import git
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




snippet = []
prompt_for = []
files = []
ocr = ''
if_use_git_gui = []

#screen capture using OCR
def screen():
    global ocr
    bbox = (467, 142, 1852, 858)
    screenshot = ImageGrab.grab(bbox)
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    processed_image = Image.fromarray(thresh)
    extracted_text = pytesseract.image_to_string(processed_image)
    ocr = extracted_text
    return ocr
#end OCR

#tkinter app
def app():

    root = tk.Tk()
    root.title("Code Assist")
    root.geometry("1500x1000")
    root.configure(bg="black")

    prompt_entry = tk.Entry(root, width=50, font=("Arial", 12))
    prompt_entry.pack(pady=20)
    def on_send():
        prompt = prompt_entry.get()
        prompt_for.append(prompt)
    send_button = tk.Button(root, text="Send", command=on_send, bg="gray", fg="white", font=("Arial", 12))
    send_button.pack()



    prompt1_entry = tk.Entry(root, width=50, font=("Arial", 12))
    prompt1_entry.pack(pady=20)
    def on_file():
        file = prompt1_entry.get()
        files.append(file)
    send1_button = tk.Button(root, text="Send", command=on_file, bg="gray", fg="white", font=("Arial", 12))
    send1_button.pack()

    prompt2_entry = tk.Entry(root, width=50, font=("Arial", 12))
    prompt2_entry.pack(pady=20)
    def on_file():
        use = prompt2_entry.get()
        if_use_git_gui.append(use)
    send2_button = tk.Button(root, text="Send", command=on_file, bg="gray", fg="white", font=("Arial", 12))
    send2_button.pack()


    def check_condition():
        if prompt_for and files:
            root.destroy()
        else:
            root.after(100, check_condition)

    check_condition()

    root.mainloop()
#end tkinter

#merge whole code with snippet (using #####)
def merge(message, file):
    n_message = f"\n{message}\n"
    n_file = "".join(file)
    pattern = re.compile(r'(#####)(.*?)(#####)', re.DOTALL)
    merged_content = pattern.sub(r'\1' + n_message + r'\3', n_file)
    return re.sub(r'#####', '', merged_content)
    

#get the whole code from file
def whole_code(filename):
    whole = []
    with open(filename, 'r') as file:
        for line in file:
            whole.append(line)
    return whole
#end getwholecode

#read snippets of code
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
#end read


#prompt to get file fixed
def code(Query, file, snippets):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key is None:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    client = anthropic.Anthropic(api_key=api_key)

    message1 = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=8192,
        temperature=0,
        system="You are a model that writes python code. You will be given a prompt and a code snippet (the relevant code starts and ends, with #####) and the whole code, but it may happen that it will not exist (the prompt will start with Prompt:, and the file, with File:). The snippet was fetched using OCR, so fix the formatting and indentation. Do what the user says. Wether it is to debug, or to add a feature, you must do it. You will be using pyautogui to write the code, therefor avoid using backslash for anything other than to start a new line. Your code must be well-documented, and free from any type of bugs. Dont import necessary libraries, unless theyre not in the whole file. Return only the changed code. Change as little of the code as possible, and fit within the ##### (represents the start and end, of the code snippet the user marker), as the code will later be merged with the whole file. Return only code, if youre not sure, do what you think is right (but whcih involves coding). Remember to document your fixes, and any comments >1 line, fit them within a pair of '''. DO NOT use backsticks, as they arent supported from python 3.x. Good luck!",
        messages=[
            {
                "role": "user", 
                "content": [{"type": "text", "text": f'Prompt: {Query} File: {file}, Snippet: {snippets}'}]
            }
        ]
    )
    final = message1.content[0].text
    return final

#works for CLI
def process_issue(issue, filename, snippets):
    if filename:
        whole = whole_code(filename)
        message = code(issue, whole, snippets)
        final = merge(message, whole)
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(final)

    else:
        message = code(issue, None, snippets)
        print(message)
#end cli

#git functions
def get_folder_path():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def init_local_repo(repo_path):
    return git.Repo.init(repo_path)

def add_remote(repo, remote_name, remote_url):
    try:
        remote = repo.create_remote(remote_name, remote_url)
    except git.exc.GitCommandError:
        remote = repo.remotes[remote_name]
    return remote


def add_changes(repo):
    repo.git.add(A=True)


def commit_changes(repo, message="Initial commit"):
    repo.index.commit(message)


def push_changes(remote, branch="main"):
    remote.push(refspec=branch)

def git_use():
    repo_path = get_folder_path()
    remote_url = input("Enter the repo URL: ")
    repo = init_local_repo(repo_path)
    origin = add_remote(repo, "origin", remote_url)
    add_changes(repo)
    commit_changes(repo, "Initial commit")
    push_changes(origin, "main")

def git_use_cli(repo_path, remote_url):
    repo = init_local_repo(repo_path)
    origin = add_remote(repo, "origin", remote_url)
    add_changes(repo)
    commit_changes(repo, "Initial commit")
    push_changes(origin, "main")
#endgit functions




def run_gui():
    app()
    pyautogui.press('enter')

    file = files[-1] if files else None
    whole = None
    if file == 'OCR':
        snippets = screen()
    else:
        snippets = read_file(file)
        whole = whole_code(file)

    prompt = prompt_for[-1]

    message = code(prompt, whole, snippets)

    final = merge(message, whole)
    with open(file, 'w', encoding="utf-8") as file:
        file.write(final)

    if if_use_git_gui:
        git_use()




def run_cli(args):
    issue = args.issue
    if args.file != "":
        file = args.file
    else:
        file = None
    if args.ocr == 'y':
        snippets = screen()
    else:
        snippets = read_file(file)

    process_issue(issue, file, snippets)

    if args.github:
        git_use_cli(args.path, args.github) 


def main():
    parser = argparse.ArgumentParser(description="Code Assist Tool")
    parser.add_argument("--issue", type=str, help="Describe the issue you're facing")
    parser.add_argument("--file", type=str, help="Path to the file to analyze")
    parser.add_argument("--ocr", type=str, help="y/n")
    parser.add_argument("--github", type=str, help="URl to repo")
    parser.add_argument("--path", type=str, help="Path to repo")
    
    args = parser.parse_args()

    if args.issue or args.file or args.ocr:
        run_cli(args)
    else:
        run_gui()

if __name__ == "__main__":
    main()


