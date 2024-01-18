from PyInquirer import prompt, style_from_dict, Token
import sys


def run_program(choice):
    if choice == "Caesar Cipher":
        path = "Caesar_cipher.py"
    elif choice == "One-Time Pad":
        path = "XOR_cipher.py"
    with open(path, "rb") as f:
        code = f.read()
    exec(code)


custom_style = style_from_dict({
    Token.Separator: '#2d60bf',
    Token.QuestionMark: '#ff591d bold',
    Token.Selected: '#6dff43 bold',  # default
    Token.Pointer: '#ff591d bold',
    Token.Instruction: '#ff591d bold',  # default
    Token.Answer: '#92d84b bold',
    Token.Question: '#fff79a',
})


questions = [
    {
        "type": "list",
        "name": "program",
        "message": "Select a Cipher :",
        "choices": ["Caesar Cipher", "One-Time Pad"],
    }
]

answers = prompt(questions,style=custom_style)
choice = answers["program"]


run_program(choice)
