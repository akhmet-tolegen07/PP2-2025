import re
def x(txt):
    snake = ""
    for char in txt:
        if(char.isupper()):
            snake += '_' + char.lower()
        else:
            snake += char
    if snake.startswith('_'):
        snake = snake[1:]
    return snake

txt = input("Enter a string: ")

print(x(txt))