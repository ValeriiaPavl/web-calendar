It's a small project created to save future and past events in the web calendar 
with the help of REST API endpoints.

To start the server use a terminal and command 'python -m flask run' in the folder with the app. 
After that  you can visit the page http://127.0.0.1:5000/event to see all listed events
or '/event/today' to see events for today. Also you can see events for some period, in this case the link 
should look like this: 
http://127.0.0.1:5000/event?start_time=YYY-MM-DD&end_time=YYY-MM-DD.
To add new event use this command: 'curl -d 'date=YYY-MM-DD&event=event_name' POST http://127.0.0.1:5000/event'.
To delete an event use 'curl DELETE http://127.0.0.1:5000/event/<event_id>'.

What I've learned while I was working with it:
- how to create a simple REST service with the Flask framework;
- marshalling and parsing objects;
- work with a SQLite database using the Flask-SQLAlchemy extension;
- work with date objects in Python.