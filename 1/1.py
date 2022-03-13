class MyClass:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter text: ")

    def printString(self):
        print(self.text.upper())