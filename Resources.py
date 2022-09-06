from flask_restful import Resource, marshal_with
from flask import abort
import datetime

from parsers import events_period_parser, add_event_parser
from database import db, Event
from data_serialization import EventDao, events_fields


class Events(Resource):
    @marshal_with(events_fields)
    def get(self):
        period = events_period_parser.parse_args()
        start_time = period['start_time']
        end_time = period['end_time']
        if start_time is None and end_time is None:
            all_events = Event.query.all()
        else:
            all_events = Event.query.filter(Event.date.between(start_time, end_time))
        events_to_show = [EventDao(event=x.event, date=x.date, event_id=x.id) for x in all_events]
        return events_to_show

    def post(self):
        event_data = add_event_parser.parse_args()
        event_name = event_data['event']
        date = event_data['date'].date()
        db.session.add(Event(event=event_name, date=date))
        db.session.commit()
        return {
            "message": "The event has been added!",
            "event": event_name,
            "date": str(date)
        }


class EventsToday(Resource):
    @marshal_with(events_fields)
    def get(self):
        today = datetime.date.today()
        events_for_today = Event.query.filter_by(date=today).all()
        list_of_events = [EventDao(event=event.event, date=event.date, event_id=event.id) for event in events_for_today]
        return list_of_events


class EventByID(Resource):
    @marshal_with(events_fields)
    def get(self, event_id):
        event = Event.query.filter(Event.id == int(event_id)).first()
        if event:
            return EventDao(event=event.event, event_id=event.id, date=event.date)
        else:
            abort(404, "The event doesn't exist!")

    def delete(self, event_id):
        event = Event.query.filter(Event.id == int(event_id)).first()
        if event:
            db.session.delete(event)
            db.session.commit()
            return {
                "message": "The event has been deleted!"
            }
        else:
            abort(404, "The event doesn't exist!")
