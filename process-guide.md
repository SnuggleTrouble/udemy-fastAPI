# Process guide

1. Import required libraries: sqlalchemy, passlib, bcrypt. See requirements.txt
2. Create database definition and run it in main.py
3. Create database models (tables). See models.py.
4. Create functionality to write to the database.

## FastAPI Specific:

5. Create the schemas.

- Data from user: UserBase
- Response to user: UserDisplay

6. Create API operation. CRUD Functionality. See user.py

## Relationships

- Retrieve elements from multiple tables in a single request.
- Such as items (articles, posts etc.) linked to the user.

7. Define a new model (article) in the models.py file

## Exceptions

- Notify a client of an error
- Raising an exception anywhere stops code from running.

8. Implement error handlers to prevent server crashes

## Custom Exceptions

- Custom exceptions must inherit from Exception
- Provide exception handler

## Response

- Standard response is a model, list, database model, dict etc.
- We can customise the Response object
- No data conversion

### Why?

- Add parameters: Headers, Cookies
- Different types of response (plain text, xml, html, files, streaming)
- Complex decisional logic
- Better documentation

## Request Headers

- Add headers in request function definition

## Cookies
- Store information on the browser
- Can accept str, list, dict, models etc.

## CORS
- Cross Origin Resource Sharing
localhost:8080 <--> localhold:8000