import pyautogui
import time
import random
import anthropic
import os
import keyboard
from datetime import datetime, timedelta
import inputs


project_ideas = [
    "Create a Tic-Tac-Toe game where the player competes against the computer with basic AI.",
    "Develop a 2D platformer game using pygame with moving platforms, collectibles, and enemies.",
    "Build a text-based RPG with dungeon exploration, combat mechanics, and a save/load feature.",
    "Code a Battleships game with a simple AI opponent and a visual grid display in the terminal.",
    "Create a Snake game using pygame with increasing speed as the snake grows.",
    "Design a Minesweeper game with a visual grid interface and clickable cells.",
    "Build a Pong game for two players, with increasing difficulty for solo play.",
    "Create a breakout-style game where the player controls a paddle to destroy bricks.",
    "Develop a turn-based strategy game inspired by chess or checkers with custom rules.",
    "Make a trivia game that pulls random questions from an online API like Open Trivia DB.",

    "Write a basic 2D physics engine simulating gravity, collisions, and bouncing.",
    "Create a maze generator and solver using algorithms like DFS or A*.",
    "Develop a simple neural network library from scratch using numpy.",
    "Build a virtual assistant that responds to voice commands using speech recognition.",
    "Write a chatbot engine with pattern matching and NLP capabilities using nltk.",
    "Code a procedural terrain generator using Perlin noise and visualize it with matplotlib.",
    "Develop a Python library for managing and visualizing financial data with matplotlib.",
    "Create a password manager with encryption for securely storing and retrieving passwords.",
    "Build a web scraper that gathers and analyzes news articles from multiple websites.",
    "Design a calendar and scheduling app with a command-line or tkinter-based interface.",

    "Write a fractal generator to create and visualize Mandelbrot or Julia sets.",
    "Develop a music visualizer that responds to audio input in real-time using pygame.",
    "Create a drawing tool where users can create shapes and patterns using tkinter.",
    "Code an interactive 3D shape viewer using PyOpenGL.",
    "Build a random pattern generator for generating wallpapers or textures.",
    "Develop a fireworks simulation with colorful particle effects using pygame.",
    "Create an interactive data visualization tool using Plotly or matplotlib.",
    "Write a starfield simulation with animated stars moving towards the user.",

    "Develop a handwriting recognition system using scikit-learn or TensorFlow.",
    "Write an AI to solve Sudoku puzzles using backtracking or constraint satisfaction.",
    "Create a bot to play Connect Four with Minimax and alpha-beta pruning.",
    "Develop a recommendation system for movies or books using collaborative filtering.",
    "Build a chatbot that learns new patterns and responses from user interactions.",
    "Write an AI for a simplified card game like War or Go Fish.",
    "Create a sentiment analysis tool that classifies the tone of user input.",
    "Develop a basic autonomous agent to navigate a maze using reinforcement learning.",
    
    # Miscellaneous Fun Ideas
    "Build a virtual pet simulator where the user can care for a pet over time.",
    "Create a text-based stock market simulator with random events and trends.",
    "Develop a tool to convert handwritten chess notation into digital chess.com format.",
    "Write a simple weather app that fetches real-time data from an API.",
    "Create a recipe manager that stores, retrieves, and suggests recipes based on ingredients.",
    "Design a quiz generator that creates and grades quizzes based on input topics.",
    "Build a fitness tracker that logs and analyzes workouts.",
    "Write a CLI tool for organizing and renaming files based on custom rules.",
    "Create a multiplayer online game using WebSockets with a Python backend.",
    "Develop a program to analyze and generate statistical insights from text files.",
    "Write a tool for generating random Dungeons & Dragons character stats and backstories.",
    "Build a journaling app with search, tagging, and sentiment analysis features."
]

def input_with_timeout(prompt, timeout=10):
    print(prompt, end=": ", flush=True)
    try:
        response = inputs.get_key(timeout=timeout)
        return response.ev
    except inputs.TimeoutException:
        return None

def move_mice(index):
    pyautogui.hotkey('ctrl', '`')
    pyautogui.write(f'code {index}.py', interval=0.1)
    keyboard.send('enter')
    pyautogui.hotkey('ctrl', 's')

def code(Query):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key is None:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        system="You are a model that writes python code. You should work in a series of steps. First, create a coding idea. Then, take a minute, and try to refine it, think of all the details. Write it as the first couple lines of your response, but these shall start in a #, as to not trigger a error with the compiler. Divide the problem into managable steps. Next, proceed to coding the idea, this part without any #, as it should be compilable. Try to write it in a way that is easy to understand, and is well documented. Also know that your response will be written in vscode using pyautogui, so refrain from using things like backslash, except to start new lines. Anything that isnt code shall start with a # (in a new line). Last thing, import all needed libraries, even obvious ones like datetime. Good luck!",
        messages=[
            {
                "role": "user", 
                "content": [{"type": "text", "text": Query}]
            }
        ]
    )
    return message.content[0].text



time.sleep(5)
pyautogui.write('###', interval=0.25)


def main():
    file_index = 1

    while True:
        pyautogui.press('enter')
        prompt = input_with_timeout("Enter something", 10)
        if prompt is None:
            idea = random.randit(0, len(project_ideas) - 1)
            prompt = project_ideas[idea]

        message = code(prompt)
        for x in message:
            if x == '\n':
                time.sleep(1)
                keyboard.send('enter')
                for _ in range(3):
                    pyautogui.hotkey('home')
            else:
                pyautogui.write(x, interval=0.1)
        file_index += 1
        move_mice(file_index)



main()
        




