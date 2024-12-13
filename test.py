filename = 'mouse_position.py'  # Replace with the path to your file
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

print(read_file(filename))