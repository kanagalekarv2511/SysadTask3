if __name__ == "__main__":
    import socket  # Import socket module
    import zipfile

#    ONE_CONNECTION_ONLY = (
#        True  # Set this to False if you wish to continuously accept connections
#    )

#    filename = "Example"
    port = 12312  # Reserve a port for your service.
    sock = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    sock.bind((host, port))  # Bind to the port
    sock.listen(5)  # Now wait for client connection.

    print("Server listening....")

    while True:
        conn, addr = sock.accept()  # Establish connection with client.
        print(f"Got connection from {addr}")
        filename=conn.recv(1024).decode()
        print(filename)
        with open(filename, "wb") as received_file:
            while True:
                filedata=conn.recv(1024)
                print ("received{filedata}")
                if not filedata:
                     break
                received_file.write(filedata)
    conn.close()

#        with open(filename, "rb") as in_file:
#            data = in_file.read(1024)
#            while data:
#                conn.send(data)
#                print(f"Sent {data!r}")
#                data = in_file.read(1024)
#
#        print("Done sending")
#        conn.close()
##        if (
##            ONE_CONNECTION_ONLY
##        ):  # This is to make sure that the program doesn't hang while testing
##            break
#
    sock.shutdown(1)
    sock.close()
