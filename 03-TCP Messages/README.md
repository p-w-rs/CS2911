# TCP Messages
This week, you will submit your solution to the following problem:

You will write a program to receive one or more messages over the network. You will then write the payload (body) of the received message(s) to a file. The message(s) themselves will be sent between machines using TCP.

## Message Format
A message has a four-byte header with a single field. This field contains the number of lines in a text file as a raw binary number. This four-byte field is in the standard network byte order, that is, big-endian.

Then, the lines follow, sent as ASCII text, each terminated by '\n', that is, a new-line character.

For example, to send the text file:
```
Lab 1
Phileas Fogg
```
These bytes would be sent: (showing both the hexadecimal shorthand and the ASCII characters, just as Wireshark does)

00 00 00 04 4c 61 62 20   31 0a 50 68 69 6c 65 61   ....Lab  1.Philea
73 20 46 6f 67 67 0a 0a   54 68 69 73 20 69 73 20   s Fogg.. This is
6d 79 20 6c 61 62 20 31   20 61 73 73 69 67 6e 6d   my lab 1  assignm
65 6e 74 2e 0a                                      ent..
In this example, there are four lines of text (including the blank line). In the data, we see two \n's in a row (0a 0a) because one is the end of the line "Phileas Fogg, and the next is the end of the blank line.

In this example, you would save the text file, but not any of the header bytes.

Implementation and Test
You code will go in tcp_server.ipynb . Here you must implement a function based on the message protocol described. Once the message is received you must save the message as a .txt file.

In the tcp_client.ipynb file you will find the implementation already made for a client that wishes to pass messages to our server.

To run your code you will first start the tcp_server which should hang and wait for a connection, then start the tcp_client and type in commands as desired. Note that you can change the port in both the files but they just must be the same number.

As a bonus, try to have a friend run the tcp_tester code while you have your server running and see if you can connect to one another.