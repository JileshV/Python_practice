def myFunc():
    print("Hello World!")

     #Displays main, if function is run from main file & if ran from main.py, shows module

if __name__ == "__main__":
    print("This code is directly executed through the main file.")
    myFunc()
    print(__name__)