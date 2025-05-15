# cs361-counter-microservice

## Overview
This microservice runs locally and takes two json parameters, a query date and a list of records to query for that date. It returns a list of the records that match the query date.

### How to programmatically request data
1. Connect to the ZMQ socket for the microservice.
2. Format the data to send to match the following:
    dataToSend = {
        "queryDate": "YYYYMMDD",
        "records": [
            {"date": "YYYYMMDD", "entry": "Record data here"},
            {"date": "YYYYMMDD", "entry": "Record data here"},
            {"date": "YYYYMMDD", "entry": "Record data here"},
            {"date": "YYYYMMDD", "entry": "Record data here"},
            {"date": "YYYYMMDD", "entry": "Record data here"},
        ]
    }
3. Use the json.dumps() function to stringify your data.
4. Send your stringified data to the microservice through the socket.

### How to programmatically receive data
1. Remain connected to the ZMQ socket for the microservice.
2. After sending your data to be filtered, the microservice will process the data within 3 seconds.
3. Create a variable to hold the response message from the microservice. The response will be a stringified json object with records in the same format as was sent, but omitting the query date. An example follows:
    [{"date": "YYYYMMDD", "entry": "Record data here"}, {"date": "YYYYMMDD", "entry": "Record data here"},{"date": "YYYYMMDD", "entry": "Record data here"}]
4. You can convert the string back to using the json.loads() function.
5. Send "Q" to close the connection if you are done using the microservice.

![CS 361 UML Sequence Diagram](https://github.com/user-attachments/assets/5d25b8b5-18cd-48dc-b068-a626f68f13ab)
