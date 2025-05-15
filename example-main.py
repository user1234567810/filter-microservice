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
    socket.send_string("Q")

    # Return decoded message
    return message.decode()

# ------- Example usage ------------------------------------------------ #
dataToSend = [
            {"date": "20250102", "entry": "Record 1 here"},
            {"date": "20250102", "entry": "Record 2 here"},
            {"date": "20250110", "entry": "Record 3 here"},
            {"date": "20250111", "entry": "Record 4 here"},
            {"date": "20250110", "entry": "Record 5 here"},
            {"date": "20250102", "entry": "Record 6 here"},
            {"date": "20250109", "entry": "Record 7 here"},
            {"date": "20250204", "entry": "Record 8 here"},
            {"date": "20250402", "entry": "Record 9 here"},
            {"date": "20250402", "entry": "Record 10 here"},
        ]

filteredRecords = filterByDate(20250102, dataToSend)
print(filteredRecords)