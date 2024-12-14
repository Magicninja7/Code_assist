from inputimeout import inputimeout, TimeoutOccurred

try:
    user_input = inputimeout(prompt='Please enter something: ', timeout=15)
except TimeoutOccurred:
    user_input = None

print(f'User input: {user_input}')