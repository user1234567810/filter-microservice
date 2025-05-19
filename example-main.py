# Citation for the following program
# Date: 14 May 2025
# Code adapted from the ZMQ Intro guide provided on the Canvas Assignment 4 page.
# URL to Canvas page: https://canvas.oregonstate.edu/courses/2024370/assignments/9998154?module_item_id=25330208
# URL to download the guide pdf: https://canvas.oregonstate.edu/courses/2024370/files/110412067?wrap=1
# Note: In this resource, they provided the following citation:
# This code was heavily based on the example found on # zguide titled hwclient: https://zguide.zeromq.org/docs/chapter1/

import zmq
import json

def filterByDate(queryDate, data):
    # Set up the environment so that we can begin creating sockets
    context = zmq.Context()

    # Create a socket of the request socket type
    socket = context.socket(zmq.REQ)

    # Connect to a remote socket with the address formatted as: protocol://interface:port
    socket.connect("tcp://localhost:5555")

    # Print a statement so the user knows we are about to send a message to the server
    print(f"Sending records to the server...")

    # Send the query date and records data to the server
    dataToSend = {
        "queryDate": queryDate,
        "records": data
    }
    # socket.send_string(str(dataToSend))
    socket.send_string(json.dumps(dataToSend))

    # Get the server's response
    message = socket.recv()

    #End server (send Q to stop)
    # socket.send_string("Q")

    # Return decoded message
    return message.decode()

# ------- Example usage ------------------------------------------------ #
# Specify the file with the mood data records
filename = "mood_data.json"

# Open and load the data from the specified file
with open(filename, 'r') as file:
    records = json.load(file)

# Send the query date and records to the microservice, print the results
filteredRecords = filterByDate('05/07/2025', records)
print(filteredRecords)