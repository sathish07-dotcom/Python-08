
## **Basic Module Usage (Built-in Modules)**
### **1. Import a Built-in Module (`math`)**

import math
print(math.sqrt(16))  # Output: 4.0


### **2. Import a Specific Function from a Module**

from math import factorial
print(factorial(5))  # Output: 120


### **3. Import a Module with an Alias**

import random as rnd
print(rnd.randint(1, 10))  # Output: Random number between 1 and 10


### **4. Use the `os` Module to List Files in a Directory**

import os
print(os.listdir("."))  # Lists files in the current directory


### **5. Use the `sys` Module to Get Command-Line Arguments**

import sys
print(sys.argv)  # Prints command-line arguments




## **Creating and Using Custom Modules**
### **6. Create a Custom Module (`mymodule.py`)**
#Create a file named `mymodule.py` with the following content:

def greet(name):
    return f"Hello, {name}!"


#Now, import and use it in another script:

#import mymodule
print(mymodule.greet("Sathish"))


### **7. Import a Function from a Custom Module**

#from mymodule import greet
print(greet("Swaroop"))


### **8. Reload a Module Using `importlib`**

import importlib
#import mymodule
importlib.reload(mymodule)


### **9. Use `dir()` to List Functions in a Module**

import math
print(dir(math))  # Lists all attributes and functions in the `math` module


## **Advanced Module Operations**
### **16. Use `time` Module for Delays**

import time
print("Start")
time.sleep(2)  # Pause execution for 2 seconds
print("End")


### **17. Use `datetime` to Get Current Date and Time**

from datetime import datetime
print(datetime.now())


### **18. Create a Custom Math Module (`math_utils.py`)**


def square(num):
    return num * num


print(math_utils.square(5))  # Output: 25


### **19. Use `csv` Module to Read a CSV File**

import csv
with open("data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


### **20. Get System Information Using `platform` Module**

import platform
print(platform.system())  # Output: Windows, Linux, or macOS


