# Description

Code assist is a tool to help you fix buggy code. Using tkinter, you can enter your issue, and the filename, where you encountered the issue. But before sending, mark the relevant code snippet with '#####'.

## Installation

Clone the repository

```bash
git clone https://github.com/Magicninja7/Code_assist.git
```

## Usage

GUI
```python
python copilot.py

#mark the code snippet
#(use "#####")

#in the first input field enter your issue

#in the second, enter the filename, or OCR, to capture the snippet.
```

Or CLI
```bash
python copilot.py --issue "your issue" --file "the file" --ocr "y/n" --github "repo link" --path "file path"
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
