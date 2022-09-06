from flask import Flask
from flask_restful import Api
import sys
from Resources import Events, EventsToday, EventByID
from database import db

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
api = Api(app)
db.create_all(app=app)

api.add_resource(Events, '/event')
api.add_resource(EventsToday, '/event/today')
api.add_resource(EventByID, '/event/<int:event_id>')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run
