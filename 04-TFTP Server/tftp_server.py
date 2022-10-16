from socket import *
import os
import math

TFTP_PORT = 69
TFTP_HOST = "localhost"
TFTP_BLOCK_SIZE = 512
MAX_UDP_PACKET_SIZE = 65536

# Helper functions
def get_file_block_count(filename):
    """
    Determines the number of TFTP blocks for the given file
    :param filename: THe name of the file
    :return: The number of TFTP blocks for the file or -1 if the file does not exist
    """
    try:
        # Use the OS call to get the file size
        #   This function throws an exception if the file doesn't exist
        file_size = os.stat(filename).st_size
        return math.ceil(file_size / TFTP_BLOCK_SIZE)
    except:
        return -1


def get_file_block(filename, block_number):
    """
    Get the file block data for the given file and block number
    :param filename: The name of the file to read
    :param block_number: The block number (1 based)
    :return: The data contents (as a bytes object) of the file block
    """
    file = open(filename, "rb")
    block_byte_offset = (block_number - 1) * TFTP_BLOCK_SIZE
    file.seek(block_byte_offset)
    block_data = file.read(TFTP_BLOCK_SIZE)
    file.close()
    return block_data


def put_file_block(filename, block_data, block_number):
    """
    Writes a block of data to the given file
    :param filename: The name of the file to save the block to
    :param block_data: The bytes object containing the block data
    :param block_number: The block number (1 based)
    :return: Nothing
    """
    file = open(filename, "wb")
    block_byte_offset = (block_number - 1) * TFTP_BLOCK_SIZE
    file.seek(block_byte_offset)
    file.write(block_data)
    file.close()


def socket_setup(host, port):
    """
    Sets up a UDP socket to listen on the TFTP port
    :return: The created socket
    """
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((host, port))
    return s


def start_server(host, port):
    rec_socket = socket_setup(host, port)

    # read from udp socket for a client request; use rec_socket.recvfrom(bytesToRecieve) which returns a tuple: (data, (host, port))
    # Determine the request type and preapre to read from a file
    # while not done sending blocks or no errors
    # send block using .sendto(bytesToSend, address)
    # get ACK (if the ack is not for the correct block number you may need to resend a previous block)
    # close your sockets


if __name__ == "__main__":
    start_server(TFTP_HOST, TFTP_PORT)
