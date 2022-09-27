# Introduction

The Trivial File Transfer Protocol (TFTP) was developed to be a simple protocol for serving files to clients. It is like the File Transfer Protocol (FTP) but has fewer and simpler protocol messages. You might see TFTP used today for computers that boot from the network, also known as PXE (Pre-Execution Environment) boot. While not a required test for this lab, with a working TFTP server, you should be able to use it to boot another computer. The goal of this lab is to create a server in Python that will allow clients to download files via the Trivial File Transfer Protocol (TFTP).

You will start from the template: tftps_erver.py

# References
The full details of TFTP as well as TFTP message formats sent between client and server are in RFC-1350: https://tools.ietf.org/html/rfc1350

UDP Examples can be found at https://pythontic.com/modules/socket/udp-client-server-example

# The Exercise
For this lab you will be writing the Python code for a TFTP server. The server will handle requests sent from a TFTP client. The first step is to install the TFTP client on your windows computer. To do this follow the following steps:

1. Click on the “Start” menu or press the Windows key and search for “Control Panel” (You can also open search using Windows Key + S)
2. Click on “Programs” -> “Programs and Features” and then click on “Turn Windows features on or off”
3. Scroll down and check the box labeled “TFTP Client” then click “OK”
4. The installer will run and install the TFTP client software
5. To use the TFTP client, open the Windows command prompt (you can do this by pressing the Windows Key + R, then typing ‘cmd’, and pressing enter).  From the Windows command prompt you can run the TFTP client using the “tftp” command.  If you run the command without any parameters, you will see the help text for the command:

```
C:\>tftp

Transfers files to and from a remote computer running the TFTP service.
TFTP [-i] host [GET | PUT] source [destination]

  -i              Specifies binary image transfer mode (also called
                  octet). In binary image mode the file is moved
                  literally, byte by byte. Use this mode when
                  transferring binary files.
  host            Specifies the local or remote host.
  GET             Transfers the file destination on the remote host to
                  the file source on the local host.
  PUT             Transfers the file source on the local host to
                  the file destination on the remote host.
  source          Specifies the file to transfer.
  destination     Specifies where to transfer the file.
```

```
C:\>tftp mytftp.msoe.edu GET myfile.txt
```

The TFTP client also supports ‘PUT’ which is used to send a file to be stored on the server.  The TFTP server that you will write for this lab only has to support ‘GET’ to retrieve a file.
TFTP uses User Datagram Protocol (UDP) as the transport layer so you will need to use a DGRAM socket in your Python code.  A TFTP server must send and receive data on port 69.
The TFTP RFC defines 5 messages used by TFTP.

Read Request
Write Request
Data Message
Acknowledgement Message
Error Message
The first message that the server receives is a request (either a read or a write).  

Your server will only have to support read requests.  The RFC defines a request as follows:
```
	    2 bytes     string    1 byte     string   1 byte
            ------------------------------------------------
           | Opcode |  Filename  |   0  |    Mode    |   0  |
            ------------------------------------------------
```
The operation code (Opcode) for a request is a 2-byte integer represented in big endian.  The opcode for a read request is 1.  The Filename tells the server which file to read (GET).  It is represented as an ASCII string and ends with a zero byte (null byte).  The Mode represents how the file is to be transferred.  It is represented as an ASCII string and ends with a zero byte (null byte).  Your server will not need to use this value.  Instead all files will be sent in binary.  You will need to parse it from the message, however.

Once the request is parsed, the TFTP server sends a file to a client by sending blocks of data.  The TFTP server breaks a file up into pieces called blocks.  Each block is 512 bytes of data except for the last block which is the rest of the file after the last 512-byte block.  For example, if you have a file that is 1423 bytes long, you would have 3 data blocks: two would be 512 bytes long and the last would be 399 bytes long (512 + 512 + 399 = 1423 bytes).

Data blocks are sent to the client one at a time using a data message which is formatted as follows:
```
                   2 bytes     2 bytes      n bytes
                   ----------------------------------
                  | Opcode |   Block #  |   Data     |
                   ----------------------------------
```
The operation code (Opcode) for a data message is a 2-byte integer represented in big endian.  The opcode for a data message is 3.  All data blocks sent to the client will use the opcode 3.  The block number is a 2-byte integer represented in big endian.  The block number tells the client which block of data is currently being sent (either 1, 2, or 3 in the example above).  Data blocks start at 1 and count until the last block.
Once the server sends the first data block to the client, it must wait for an acknowledgement.  An acknowledgement is sent from the client using the following message format:
```
                         2 bytes     2 bytes
                         ---------------------
                        | Opcode |   Block #  |
                         ---------------------
```
The operation code (Opcode) for an acknowledgement message is a 2-byte integer represented in big endian.  The opcode for a acknowledgement message is 4.  The block number is a 2-byte integer represented in big endian.  In an acknowledgement message, the block number indicates which block is being acknowledged.  For example, if the server sends block 1 to the client, once the client receives the block successfully, it sends an acknowledgement message (with opcode 4) with block number 1.

### What if the file the client requests doesn’t exist? 

You will need to send an error message if the client requests a file that you can’t find.  The TFTP RFC defines an error message format communicating errors to the client.
Here is the format for an error message:
```
               2 bytes     2 bytes      string    1 byte
               -----------------------------------------
              | Opcode |  ErrorCode |   ErrMsg   |   0  |
               -----------------------------------------
```
The operation code (Opcode) for an error message message is a 2-byte integer represented in big endian.  The opcode for an error message always has the value 5.  The error code is a 2-byte integer represented in big endian.  The value of the error code indicates specifically what the error is.  The TFTP RFC defines a set of error codes and what they mean:

   Value     Meaning
   0         Not defined, see error message (if any).
   1         File not found.
   2         Access violation.
   3         Disk full or allocation exceeded.
   4         Illegal TFTP operation.
   5         Unknown transfer ID.
   6         File already exists.
   7         No such user.

The last part of the error message is the error message represented as an ASCII encoded string that ends with a zero (null) byte.  So, if a client sends a read request message for a file that doesn’t exist, your server should send an error message (op code 5) with error code 1 with an error message of b’File not found’.  Don’t forget to add the null byte at the end of the message.

### Can the client send error messages to the server?

Yes, there could be several situations where the client sends an error to the server.  If your script receives an error message from the client, make sure you print out the error code, print the error message, and quit.
