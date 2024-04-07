# Hotel Reservation API

This Hotel Reservation API is a Django application that provides a REST API that provide two endpoints
1. GET /app/hotels : Get list of hotels available in the database
2. POST /app/hotels : Adds a new hotel into the database
`{ name: <name of hotel> ..... }`

## Get Started
Ensure you have Python and pip installed on your system to manage packages and run the developement server.

## How to access the REST API
To get the list of hotels in the database you use the GET request `http://localhost:8000/app/hotels`, 
you get back a list of the saved hotels. e.g 

![The GET Hotel request!](images/1.png  "San Juan Mountains")

To add a new hotel to the database you use the POST request `http://localhost:8000/app/hotels`,
with the details of the hotel like name, price and availability.

![The POST Hotel request!](images/2.png  "San Juan Mountains")

If you request the list of hotels again you see the newly created hotel added to the list hotels
![The GET Hotel request!](images/3.png  "San Juan Mountains")