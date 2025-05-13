# Citation for the following program
# Date: 24 April 2025
# Code adapted from the ZMQ Intro guide provided on the Canvas Assignment page.
# URL: https://canvas.oregonstate.edu/courses/2024370/assignments/9998154?module_item_id=25330208
# Note: In this resource, they provided the following citation:
# This code was largely based on the example found on zguide titled hwserver: https://zguide.zeromq.org/docs/chapter1/ # (c) 2010-2012 Pieter Hintjens

import zmq

# Set up the environment so we can begin creating sockets (should only be declared once at the start of a file)
context = zmq.Context()

# Create a socket of the reply socket type
socket = context.socket(zmq.REP)

# Bind the port to this socket, using the following format: protocol://interface:port
socket.bind("tcp://*:5555")

# Function to convert input date to format


# Function to query by the specified date
def queryByDate(date, records):
    record_count = len(records)
    filtered_records = []

    # Iterate through to find records with matching date
    for i in range(record_count):
        if records[i][0] == date:
            filtered_records.append(records[i])
    
    # Return the matching records
    return filtered_records

# Loop to listen for messages from the client
while True:
    # Receive the client's message
    message = socket.recv()

    if len(message) > 0:
        # If client quits, break out of the loop
        if message.decode() == 'Q':
            break

        # Otherwise, decode and print message and respond to client
        print(f"Received message from the client: {message.decode()}")

        # Parse the date and records data from the message
        received_date = int(message[0:9])
        received_records = message[9:]

        # Perform the query on records with the given date & send results back
        send_records = queryByDate(received_date, received_records)
        socket.send_string(str(send_records))

# Destroy the context to make a clean exit
context.destroy()