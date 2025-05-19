# filter-microservice

## Overview
This microservice runs locally and takes two parameters, a query date and a list of records to query for that date. It returns a list of the records that match the query date.

### How to programmatically request data
1. Connect to the ZMQ socket for the microservice.
2. Format the data to send to match the following:
    dataToSend = {
        "queryDate": "MM/DD/YYYY",
        "records": [
            {"date": "MM/DD/YYYY", "entry": "Record data here"},
            {"date": "MM/DD/YYYY", "entry": "Record data here"},
            {"date": "MM/DD/YYYY", "entry": "Record data here"},
            {"date": "MM/DD/YYYY", "entry": "Record data here"},
            {"date": "MM/DD/YYYY", "entry": "Record data here"},
        ]
    }
   Note that the query date should be formatted to match the date format in your records, i.e., records with dates 05/06/2025 should have "05/06/2025" for their query date, or records with 20250102 should use "20250102", etc.
4. Use the json.dumps() function to stringify your data.
5. Send your stringified data to the microservice through the socket.

##### Example call (after initiating the socket connection)
Example 1
```
dataToSend = {
    "queryDate": "20250102",
    "records": [
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
}
socket.send_string(json.dumps(dataToSend))
```

Example 2
```
# The following records dictionary can be loaded from an open JSON file using records = json.load(file).
records = [
    {
        "date": "05/06/2025",
        "rating": 8,
        "note": "Feeling good"
    },
    {
        "date": "05/06/2025",
        "rating": 6,
        "note": "blah"
    },
    {
        "date": "05/06/2025",
        "rating": 8,
        "note": "great"
    },
    {
        "date": "05/06/2025",
        "rating": 7,
        "note": "ok"
    },
    {
        "date": "05/06/2025",
        "rating": 9,
        "note": "awesome"
    },
    {
        "date": "05/07/2025",
        "rating": 4,
        "note": "jiffy"
    },
    {
        "date": "05/07/2025",
        "rating": 1,
        "note": "bad"
    }
]
dataToSend = {
    "queryDate": "05/06/2025",
    "records": records
}
socket.send_string(json.dumps(dataToSend))
```

### How to programmatically receive data
1. Remain connected to the ZMQ socket for the microservice.
2. After sending your data to be filtered, the microservice will process the data within 3 seconds.
3. Create a variable to hold the response message from the microservice. The response will be a stringified Python dictionary with records in the same format as was sent from the json file, but omitting the query date. An example follows:
    [{"date": "MM/DD/YYYY", "entry": "Record data here"}, {"date": "MM/DD/YYYY", "entry": "Record data here"},{"date": "MM/DD/YYYY", "entry": "Record data here"}]
If no records match the query date, an empty dictionary will be returned ("[]").
5. You can convert the string back to using the json.loads() function.

##### Example call
Example 1: Receive filtered data directly from the socket (no function defined)
```
message = socket.recv()
filteredRecords = message.decode()
```

Example 2: Return filtered data from a defined function
```
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

    # Return decoded message
    return message.decode()

# ------- Example usage ------------------------------------------------ #
records = [
    {"date": "05/06/2025", "rating": 8, "note": "Feeling good"},
    {"date": "05/06/2025", "rating": 6, "note": "blah"},
    {"date": "05/06/2025", "rating": 8, "note": "great"},
    {"date": "05/06/2025", "rating": 7, "note": "ok"},
    {"date": "05/06/2025", "rating": 9, "note": "awesome"},
    {"date": "05/07/2025", "rating": 4, "note": "jiffy"},
    {"date": "05/07/2025", "rating": 1, "note": "bad"}
]

# Send the query date and records to the microservice, print the results
filteredRecords = filterByDate('05/07/2025', records)
```

### UML Diagram
![UML](https://github.com/user-attachments/assets/ebefad26-58be-4d39-bd1f-363bcfe4454b)

