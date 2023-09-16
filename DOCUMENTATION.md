# CRUD API DOCUMENTATION
This is the documentation for the CRUD API. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person records on a database.
## Table of Contents
* [Standard Request and Response Formats](#standard-request-and-response-formats)
* [Sample API Usage](#sample-api-usage)
* [Setup and Deployment Instructions](#setup-and-deployment-instructions)

## Standard Request and Response Formats
### Create a Person (PUT /api)
Request Format

HTTP Method: POST

URL: /api

Request Headers:

Content-Type: application/json
Request Body:

{
  "id": string'
  "name": string,
  "age": string,
  "track": string
}
Response Format

HTTP Status Code: 201 (Created) on success

JSON Response Body:

```{
 "id": string,"name":string, "age":string, "track":string
}
```
### Retrieve a Person (GET '/api/<string:user_id>')
Request Format

HTTP Method: GET URL: '/api/<string:user_id>'

Response Format

HTTP Status Code: 200 (OK) on success

JSON Response Body:

  ```{
    "id": string,
    "name": string,
    "age": string,
    "track":string
}
```
### Update a Person (PATCH '/api/<string:user_id>')
Request Format

HTTP Method: PATCH

URL: '/api/<string:user_id'>

Request Headers:

Content-Type: application/json Request Body:

```{
    "name": string,
    "age": string
    "track":string
}```
Response Format

HTTP Status Code: 200 (OK) on success

JSON Response Body:

```{
    "name": string, "age": string", track":string
}
```
### Delete a Person (DELETE /api/<string:user_id>)
Request Format

HTTP Method: DELETE URL: '/api/<string:user_id>'

Response Format


HTTP Status Code: 204 (No Content) on success

## Sample API Usage
### Creating a Person Request

PUT /api HTTP/1.1 Host: localhost:5000

Content-Type: application/json

{
    "id":"1",
    "name": "Fushiguro",
    "age": "19",
    "track":"shikigami"
}
Response

```{
    "id":"1", "name": "Fushiguro","age": "19","track":"shikigami"
}
```
### Retrieving a Person Request

GET /api/<string:user_id> HTTP/1.1 Host: localhost:5000

Response
```{
    "id": <string:user_id>,
    "name": "Satoru Gojo",
    "age": "26",
    "track": "limitless"}
```
### Updating a Person Request

PATCH /api/string:user_id HTTP/1.1 Host: localhost:5000

Content-Type: application/json

{
    "name": "Yuji Itadori",
    "id": <string:user_id>,
    "age": "19",
}
Response

```{
    "name": "Yuji Itadori","id": <string:user_id>,"age": "19"
}
```
### Deleting a Person Request

DELETE /api/<string:user_id> HTTP/1.1 Host: localhost:5000

Response

(HTTP Status Code: 204 No Content)

## Setup and Deployment Instructions
To set up and deploy the API locally or on a server, follow these steps:

### Clone the repository to your local machine:
```git clone https://github.com/yourusername/crud_api.git```
### Navigate to the project directory:
```cd person-api```
### Install the required Python packages:
  pip install -r requirements.txt
### Configure the database settings in crud.py.
```app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///" + os.path.join(Path.cwd(), "database.db")
db = SQLAlchemy(app)
@app.before_first_request
def create_tables():
    db.create_all()
```
### Start the API server:
Run python app.py.
The API will be accessible at http://localhost:5000. You can now use Postman or other tools to interact with the API as described in the Sample API Usage section.

You can also make requests by using the requests model in python.
Thank You
