from socket import *
import struct
import time
import sys

# Port number definitions
# (May have to be adjusted if they collide with ports in use by other programs/services.)
TCP_PORT = 12123

# Address to listen on when acting as server.
# The address '' means accept any connection for our 'receive' port from any network interface
# on this system (including 'localhost' loopback connection).
LISTEN_ON_INTERFACE = "192.168.1.xxx"

# Address of the 'other' ('server') host that should be connected to for 'send' operations.
# When connecting on one system, use 'localhost'
# When 'sending' to another system, use its IP address (or DNS name if it has one)
# OTHER_HOST = '192.168.1.xxx'
OTHER_HOST = "192.168.1.104"


def main():
    """
    Allows user to either send or receive bytes
    """
    # Get chosen operation from the user.
    action = input('Select "(1-TS) tcpsend", or "(2-TR) tcpreceive":')
    # Execute the chosen operation.
    if action in ["1", "TS", "ts", "tcpsend"]:
        tcp_send(OTHER_HOST, TCP_PORT)
    elif action in ["2", "TR", "tr", "tcpreceive"]:
        tcp_receive(TCP_PORT)
    else:
        print('Unknown action: "{0}"'.format(action))


def tcp_send(server_host, server_port):
    """
    - Send multiple messages over a TCP connection to a designated host/port
    - Receive a one-character response from the 'server'
    - Print the received response
    - Close the socket

    :param str server_host: name of the server host machine
    :param int server_port: port number on server to send to
    """
    print('tcp_send: dst_host="{0}", dst_port={1}'.format(server_host, server_port))
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect((server_host, server_port))

    num_lines = int(input("Enter the number of lines you want to send (0 to exit):"))

    while num_lines != 0:
        print("Now enter all the lines of your message")
        # This client code does not completely conform to the specification.
        #
        # In it, I only pack one byte of the range, limiting the number of lines this
        # client can send.
        #
        # While writing tcp_receive, you will need to use a different approach to unpack to meet the specification.
        #
        # Feel free to upgrade this code to handle a higher number of lines, too.
        lines_bytes = num_lines.to_bytes(4, "big")
        for i in range(4):
            tcp_socket.sendall(lines_bytes[i : i + 1])
            time.sleep(0.25)  # Just to mess with your servers. :-)

        # Enter the lines of the message. Each line will be sent as it is entered.
        for line_num in range(0, num_lines):
            line = input("")
            tcp_socket.sendall(line.encode() + b"\n")

        print("Done sending. Awaiting reply.")
        response = tcp_socket.recv(1)
        if response == b"A":  # Note: == in Python is like .equals in Java
            print("File accepted.")
        else:
            print("Unexpected response:", response)

        num_lines = int(
            input("Enter the number of lines you want to send (0 to exit):")
        )

    tcp_socket.sendall(b"\x00\x00")
    time.sleep(
        1
    )  # Just to mess with your servers. :-)  Your code should work with this line here.
    tcp_socket.sendall(b"\x00\x00")
    response = tcp_socket.recv(1)
    if response == b"Q":  # Reminder: == in Python is like .equals in Java
        print("Server closing connection, as expected.")
    else:
        print("Unexpected response:", response)

    tcp_socket.close()


def tcp_receive(listen_port):
    """
    - Listen for a TCP connection on a designated "listening" port
    - Accept the connection, creating a connection socket
    - Print the address and port of the sender
    - Repeat until a zero-length message is received:
      - Receive a message, saving it to a text-file (1.txt for first file, 2.txt for second file, etc.)
      - Send a single-character response 'A' to indicate that the upload was accepted.
    - Send a 'Q' to indicate a zero-length message was received.
    - Close data connection.

    :param int listen_port: Port number on the server to listen on
    """

    print("tcp_receive (server): listen_port={0}".format(listen_port))
    address = ("localhost", listen_port)
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(address)
    tcp_socket.listen()
    (data_socket, sender_address) = tcp_socket.accept()

    done = False
    while not done:
        header = b""
        while len(header) < 4:
            header += data_socket.recv(1)

        n_lines = int.from_bytes(header, byteorder="big")
        if n_lines == 0:
            data_socket.sendall(b"Q")
            done = True
        else:
            lines = []
            for n in range(n_lines):
                cur_byte = b""
                line = ""
                while cur_byte != b"\n":
                    cur_byte = data_socket.recv(1)
                    line += cur_byte.decode("ASCII")
                lines.append(line)
            data_socket.sendall(b"A")
            print("***MESSAGE***\n{}".format("".join(lines)))

    data_socket.close()
    tcp_socket.close()


def next_byte(data_socket):
    """
    Read the next byte from the socket data_socket.

    Read the next byte from the sender, received over the network.
    If the byte has not yet arrived, this method blocks (waits)
      until the byte arrives.
    If the sender is done sending and is waiting for your response, this method blocks indefinitely.

    :param data_socket: The socket to read from. The data_socket argument should be an open tcp
                        data connection (either a client socket or a server data socket), not a tcp
                        server's listening socket.
    :return: the next byte, as a bytes object with a single byte in it
    """
    return data_socket.recv(1)


# Invoke the main method to run the program.
if __name__ == "__main__":
    main()
