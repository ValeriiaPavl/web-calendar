from flask_restful import fields


class EventDao(object):
    def __init__(self, event, date, event_id):
        self.event = event
        self.date = date
        self.id = event_id


events_fields = {
    'event': fields.String,
    'date': fields.String,
    'id': fields.Integer
}