from socket import *

# import the "regular expressions" module
import re


def get_http_resource(url, file_name):
    """
    Get an HTTP resource from a server
           Parse the URL and call function to actually make the request.

    :param url: full URL of the resource to get
    :param file_name: name of file in which to store the retrieved resource

    (do not modify this function)
    """

    # Parse the URL into its component parts using a regular expression.
    url_match = re.search("http://([^/:]*)(:\d*)?(/.*)", url)
    url_match_groups = url_match.groups() if url_match else []
    #    print 'url_match_groups=',url_match_groups
    if len(url_match_groups) == 3:
        host_name = url_match_groups[0]
        host_port = int(url_match_groups[1][1:]) if url_match_groups[1] else 80
        host_resource = url_match_groups[2]
        print(
            "host name = {0}, port = {1}, resource = {2}".format(
                host_name, host_port, host_resource
            )
        )
        status_string = do_http_exchange(
            host_name.encode(), host_port, host_resource.encode(), file_name
        )
        print('get_http_resource: URL="{0}", status="{1}"'.format(url, status_string))
    else:
        print("get_http_resource: URL parse failed, request not sent")


# Write Helper functions here


def do_http_exchange(host, port, resource, file_name):
    """
    Get an HTTP resource from a server

    :param bytes host: the ASCII domain name or IP address of the server machine (i.e., host) to connect to
    :param int port: port number to connect to on server host
    :param bytes resource: the ASCII path/name of resource to get. This is everything in the URL after the domain name,
           including the first /.
    :param file_name: string (str) containing name of file in which to store the retrieved resource
    :return: the status code
    :rtype: int
    """
    # Open a tcp socket
    # Connect the socket to the host on the given port
    # Create a request as a bytes object
    # Send the request to the host
    # Receive the response for the host
    ## Get the first line of the header first
    ## Extract the message code (e.g. 404, 200)
    ## If 200 proceeed to read the rest of the header lines
    # If the header contains the Content-Length, then
    ## Read the number of bytes given by the content length value
    ## save the bytes to a file given by file_name
    # Else if the header contains the Transfer-Encoding with value chunks
    ## Read each chunk in (remember the number that comes in with the length of the chunck is ASCII hexadecimal numbers)
    ## Combine the chunks
    ## Decode the chunks as ASCII
    ## Write the ASCII to a file given by file_name

    return 500  # Replace this "server error" with the actual status code


if __name__ == "__main__":
    """
    Tests the client on a variety of resources
    """

    # These resource request should result in "Content-Length" data transfer
    get_http_resource("http://www.httpvshttps.com/check.png", "check.png")

    # this resource request should result in "chunked" data transfer
    get_http_resource("http://www.httpvshttps.com/", "index.html")

    # If you find fun examples of chunked or Content-Length pages, please share them with us!
