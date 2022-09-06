from flask_restful import reqparse, inputs

add_event_parser = reqparse.RequestParser()
events_period_parser = reqparse.RequestParser()

add_event_parser.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)
add_event_parser.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)

events_period_parser.add_argument(
    'start_time',
    type=inputs.date,
    help="You haven't wrote the data or data format is incorrect.",
    required=False
)

events_period_parser.add_argument(
    'end_time',
    type=inputs.date,
    help="You haven't wrote the data or data format is incorrect.",
    required=False
)

add_event_parser.add_argument(
    'event_id',
    type=int,
    help="the event must be only integer!",
    required=False
)
