# CRUD API 
The CRUD API is a RESTful API that allows you to perform CRUD (Create, Read, Update, Delete) operations on person records in a database. This README provides instructions on setting up, running, and using the API.

## Table of Contents
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
* [Installation](#installation)
* [Configuration](#configuration)
* [Running the API](#running-the-api)
* [API Endpoints](#api-endpoints)
    * [Create a Person](#create-a-person)
    * [Retrieve a Person](#retrieve-a-person)
    * [Update a Person](#update-a-person)
    * [Delete a Person](#delete-a-person)
* [Testing the API](#testing-the-api)
### Prerequisites
Before you begin, ensure you have the following:

Python 3.8+
pip (Python package manager)
Flask
Flask-SQLAlchemy
[SQLite] (or an alternative database, based on your choice)
everything in requirements.txt in this repo
## Getting Started
### Installation
Clone this repository to your local machine: git clone https://github.com/yourusername/crud_api.git ------- Navigate to the project directory:
cd task2 ------- Install the required Python packages: pip install -r requirements.txt

### Running the API
Ensure your database is set up and running.

Run the following command to create the database tables:

python app.py -------- The API should now be running locally on your computer

## API Endpoints
### Create a Person
Endpoint: PUT /api

Description: Create a new person with the given name.

Request Body: JSON data containing person details (id, name, age, track).

Example Request: http://localhost:5000/api -H "Content-Type: application/json" -d

```'{
"name": "Peter Ndukwe",
"age": "12",
track: "backend"
}'
```

### Retreive a person
Endpoint: GET /api/<string:user_id>

Description: Retrieve details of a person with the given user id.

Example Request: curl http://localhost:5000/api/string:user_id

### Update a person
Endpoint: PATCH /api/<string:user_id>

Description: Update details of a person with the given ID. Request Body: JSON data containing updated person details (id,age, track).

Example Request: http://localhost:5000/api/<string:user_id> -H "Content-Type: application/json" -d

```'{
    "name": "Lebron James",
    "id": <string:user_id>,
    "age": 40,
 }'
```
### Delete a person
Endpoint: DELETE /api/<string:user_id>

Description: Delete a person with the given user_id.

Example Request: DELETE http://localhost:5000/api/<string:user_id>

## Testing the API
You can use Postman or python scripts (e.g., pytest) to test the API. Detailed instructions for testing the API can be found in the DOCUMENTATION.md.


[![Visits Badge](https://badges.pufler.dev/visits/braydoncoyer/braydoncoyer)](https:braydoncoyer.dev)
[![Twitter Badge](https://img.shields.io/badge/Twitter-Profile-informational?style=flat&logo=twitter&logoColor=white&color=1CA2F1)](https://twitter.com/Ndigitals001)
