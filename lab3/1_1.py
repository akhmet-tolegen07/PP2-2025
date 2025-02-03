class String:
    def __init__(self):
        self.str_value = ""

    def getString(self):
        self.str_value = input("The string: ")

    def printString(self):
        print(self.str_value.upper())

str = String()
str.getString()
str.printString()
