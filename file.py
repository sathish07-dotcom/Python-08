
# **Basic File Handling (Reading & Writing)**  

### **1. Create and Write to a File**  

with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.")


### **2. Read a File (Entire Content)**  

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


### **3. Read a File Line by Line**  

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters


### **4. Append Data to a File**  

with open("example.txt", "a") as file:
    file.write("\nThis line is appended.")


### **5. Read First 10 Characters from a File**  

with open("example.txt", "r") as file:
    content = file.read(10)
    print(content)




# **Intermediate File Operations**  

### **6. Check If a File Exists Before Reading**  

import os
if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print(file.read())
else:
    print("File not found.")


### **7. Read a File and Count Lines**  

with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))


### **8. Write Multiple Lines to a File**  

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)


### **9. Read a File as a List of Lines**  

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)


### **10. Copy Content from One File to Another**  

with open("example.txt", "r") as file1, open("copy.txt", "w") as file2:
    file2.write(file1.read())




# **Advanced File Handling (Modes & Error Handling)**  

### **11. Create a File if It Doesn’t Exist**  

with open("newfile.txt", "x") as file:
    file.write("This file is created if it does not exist.")


### **12. Rename a File**  

import os
os.rename("example.txt", "renamed_file.txt")


### **13. Delete a File**  

import os
if os.path.exists("copy.txt"):
    os.remove("copy.txt")


### **14. Write a Dictionary to a File**  

data = {"name": "Alice", "age": 25}
with open("data.txt", "w") as file:
    file.write(str(data))


### **15. Read a Dictionary from a File**  

with open("data.txt", "r") as file:
    content = file.read()
    dictionary = eval(content)  # Convert string to dictionary
    print(dictionary)




# **Working with CSV and JSON Files**  

### **16. Write Data to a CSV File**  

import csv
data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


### **17. Read Data from a CSV File**  

import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


### **18. Write Data to a JSON File**  

import json
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)


### **19. Read Data from a JSON File**  

import json
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)


### **20. Read a Large File Line by Line (Efficiently)**  

with open("largefile.txt", "r") as file:
    for line in file:
        print(line.strip())  # Process each line one by one

