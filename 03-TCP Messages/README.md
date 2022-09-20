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

00 00 00 02
4C 61 62 20 31 0A
50 68 69 6C 65 61 73 20 46 6F 67 67 0A

In this example, there are two lines of text. In this example, you would save the text file, but not any of the header bytes.

## Implementation and Test

Your code will go in tcp_server.py . Here you must implement a function based on the message protocol described. Once the message is received you must save the message as a .txt file.

In the tcp_client.py file you will find the implementation already made for a client that wishes to pass messages to our server.

To run your code you will first start the tcp_server which should hang and wait for a connection, then start the tcp_client and type in commands as desired. Note that you can change the port in both the files but they just must be the same number.

## Grading

To pass off you will run your tcp_server.py and I will send you messages with my client program. You then must read those messages back to me outloud. Thus, You can only pass of this lab during lab time since only in the lab room will the firewall let us send messages over the network locally.