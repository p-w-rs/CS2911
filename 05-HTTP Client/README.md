# Introduction
The goal of this lab is to write a Python program to request and save a web resource, acting as an HTTP client. You will write code from scratch, sending and receiving bytes over a TCP connection rather than using a prebuilt HTTP library.

You will start from the template http_client.py

The program has at least the following functions; you will add others.

```get_http_resource(url,file_name)```
Using HTTP, request a web resource and store the returned data in the specified file.

Arguments:
- url: string containing URL (including the "http://" protocol declaration and the domain name) for desired resource
- file_name: string containing name of file in which to store response data
- Return value: None


```do_http_exchange(host, port, resource, file_name)```
Using HTTP, request a web resource and store the returned payload data in the specified file.

Arguments:
- host: bytes object with the ASCII the domain name or IP address of the server machine (i.e., host) to connect to
- port: port number to connect to on host
- resource: bytes object with the ASCII path/name of resource to get. This is everything in the URL after the domain name, including the first /.
- file_name: string (str) name of file in which to store the retrieved resource
- Return value: Integer status code given by server

## Operation
Send an HTTP request to retrieve the resource at the specified url.
The client should recognize and interpret both Content-Length and chunked responses
While you need to implement chunking, you do not need to implement the chunk extensions described in the RFC (and the videos)
If successful, store the response data in a file with the specified file_name.
Return the status code given by the server
It is not necessary to handle or report errors that the server hypothetically could make by not following the protocol. (You may assume the servers we recommend follow the protocol correctly.)  On the other hand, it's a good idea to handle USER errors -- if you were writing a browser, what errors could the user make?

## Procedure
You may use the next_byte() method from Lab 4. Whether or not you use next_byte(), your program should use recv correctly. It should handle the situation when recv() returns fewer bytes than expected during normal transmission. It is usually best to just use next_byte()

You do not need to implement a persistent connection. The server will send only one response unless you explicitly request a persistent connection. Nevertheless, your code should be extensible to the persistent case. In other words, when you are reading the message, the program should not attempt to read any bytes past the end of the message, to avoid reading bytes from the second response.

Because a student has asked me to state this explicitly: You should not use HTTP libraries when implementing this lab. The purpose of this lab is for your team to write the library from scratch! (International students: This means, like in cooking, to make something from raw ingredients without any pre-made components.)

Have fun! Ask your instructor if you have any questions!

## Just For Fun
Many servers these days are HTTPS-only. In July of 2018, Google started marking sites as "not secure" which use HTTP instead of HTTPs. In our Fall 2019 offering of Network Protocols, the use of HSTS on most sites prevents Chrome from sending any plain HTTP requests at all. If you have never visited a site, you browser will get a 301 Moved Permanently status code redirecting you to the HTTPS version of the site. After this your browser will remember that the site uses HSTS and refuse to talk to the site in HTTP at all. And for many sites, they are on preloaded list in Chrome that Chrome will NEVER use plain HTTP at all. This is important for security reasons to avoid man-in-the-middle attacks, which we will discuss at the end of the quarter. (Indeed, many sites started transitioning to HTTPS-only in 2016.)

This is very good from a security perspective, but it means if you want to connect to sites, you need to be able to handle HTTPS! It turns out this isn't hard to do. Here are some tips on how to do it if you would like to try it:

HTTPS is simply HTTP wrapped in a TLS socket, offered on port 443 instead of port 80. To connect to an HTTPS server, first establish an ordinary TCP connection to port 443 as you would always do. Then, wrap your TCP socket in a TLS socket using the following code:

context = ssl.create_default_context()
ssl_socket = context.wrap_socket(sock, server_hostname=SMTP_SERVER)
where sock is your connected TCP client socket. Once this command succeeds, use the ssl_socket throughout your code for all the calls to recv() and sendall().

That's it! Let us know if you hit any roadblocks while trying this!