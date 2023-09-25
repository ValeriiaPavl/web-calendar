# Web Calendar

It's a small project created to save future and past events in the web calendar 
with the help of REST API endpoints.

### To start Server

1. Clone the project with ```git clone git@github.com:ValeriiaPavl/web-calendar.git```. 
2. To run the server use the terminal and command ```python -m flask run``` in the folder where the app.py file located.

### Available endpoints

* http://127.0.0.1:5000/event
This endpoint is used to see all listed events

* http://127.0.0.1:5000/event/today - to see events for today
 
* http://127.0.0.1:5000/event?start_time=YYY-MM-DD&end_time=YYY-MM-DD  endpoint for events during some period

### Adding and deleting events
* **To add** new event use this command in the terminal: ```curl -d 'date=YYY-MM-DD&event=event_name' POST http://127.0.0.1:5000/event```.
* **To delete** an event use ```curl DELETE http://127.0.0.1:5000/event/<event_id>```.


### What I've learned while I was working with this project:
- how to create a simple REST service with the Flask framework;
- marshalling and parsing objects;
- work with a SQLite database using the Flask-SQLAlchemy extension;
- work with date objects in Python.