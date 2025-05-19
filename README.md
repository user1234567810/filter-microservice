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

### How to programmatically receive data
1. Remain connected to the ZMQ socket for the microservice.
2. After sending your data to be filtered, the microservice will process the data within 3 seconds.
3. Create a variable to hold the response message from the microservice. The response will be a stringified Python dictionary with records in the same format as was sent from the json file, but omitting the query date. An example follows:
    [{"date": "MM/DD/YYYY", "entry": "Record data here"}, {"date": "MM/DD/YYYY", "entry": "Record data here"},{"date": "MM/DD/YYYY", "entry": "Record data here"}]
If no records match the query date, an empty dictionary will be returned ("[]").
5. You can convert the string back to using the json.loads() function.

![UML](https://github.com/user-attachments/assets/ebefad26-58be-4d39-bd1f-363bcfe4454b)

