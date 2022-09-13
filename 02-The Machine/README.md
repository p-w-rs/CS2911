# The Machine

A Java class file contains all the symbols and code to execute a program in the Java interpreter. The class file itself, is represented as a bunch of bytes in a file. The Java interpreter reads this file and parses the bytes to determine what to execute for your program.

Enter “The Machine”: suppose we want to write our own interpreter for a program. We don’t need it to be nearly as complex as the Java interpreter, but we do want it to be able to do some interesting functions as well allow us to practice parsing.

The goal of “The Machine” is for us to learn how to read the context for raw bytes and interpret what they mean. With this exercise we don’t have to worry about the actual receiving or sending of data on a network. The entire program is provided for us right away. In a later lab we’ll write an interpreter for data sent to us over the network.

Just like a Java class file, “The Machine” will execute programs represented by files that contain a bunch of bytes. The program files must be in a format that gives the bytes context or else “The Machine” won’t be able to know what to do.

The goal of this lab is to write a Python program to parse a binary file containing instructions to be executed by "The Machine". The program will execute each instruction in turn and produce output

## Files:
* **interpreter.py**: This is where you will write your code for loading a file, interpreting the contents, and executing the instructions
* **readfile.py**: This will import set_file() and read_byte() functions. To read a file you must first call set_file("name_of_file"), Then you can call read_byte() to get the bytes of the file 1 by 1
* **grader.py**: This will auto grade your interpreter by running `python grader.py`, you may want to create your own main test your code in a more controlled way outside of this file.


## The Protocol
* The first 4 bytes should be (in hex) 31 41 FA CE
* The next 2 bytes say how many operations will be in the file
* The next 1 byte contains the operations to perform

## Operations
### 0000 0001 - Addition
* The first operand is the first 2 bytes after the op code
* The second operand is the second 2 bytes after the op code
### 0000 0010 - Subtraction
* The first operand is the first 2 bytes after the op code
* The second operand is the second 2 bytes after the op code
### 0000 0011 - Multiplication
* The first operand is the first 2 bytes after the op code
* The second operand is the second 2 bytes after the op code
### 0000 0100 - Division 
* The first operand is the first 2 bytes after the op code
* The second operand is the second 2 bytes after the op code
### 0000 0101 - Print
* The string starts immediately after the operation byte
* It ends when the the byte that codes for an ASCII newline is found (e.g. ‘\n’, ‘\x0a’)

### Result
* Create a list with the results from the operations in the order they are run
* For all math ops, push a number into the list
* For the "Print" op, push the ASCII string coded by the bytes into the list
