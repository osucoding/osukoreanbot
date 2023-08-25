import logging as log
import json
import datetime

class Event:
    def __init__(self, event_obj=None):
        if event_obj:
            self.__desc = event_obj['description']
            year = event_obj['year']
            month = event_obj['month']
            date = event_obj['date']
            self.__datetime = datetime.datetime(year, month, date)
        else:
            self.__desc = 'No future events known to this bot. Contact `@Coffee to Code Converter` on this server.'

    def get_readable_datetime(self):
        return self.__datetime.strftime('%x') if self.__datetime is not None else 'N/A'

    def get_description(self):
        return self.__desc


def next_command(body):
    argument_obj = body['data']['options'][0]
    argument = argument_obj['name']

    if argument == 'osu':
        today = datetime.datetime.now()
        next_event = search_next_event(today, 'osu_events.json')
        content = f"Next event: {next_event.get_description()}, scheduled on {next_event.get_readable_datetime()}"
        return {
            'statusCode': 200,
            'body': json.dumps({
                'type': 4,
                'data': {
                    'content': content,
                }
            })
        }
    else:
        msg = f'Invalid argument: {argument}'
        log.error(msg)
        return {
            'statusCode': 400,
            'body': json.dumps(msg)
        }


def search_next_event(target_date: datetime, filename: str):
    events = []
    with open(filename, 'r') as f:
        data = json.load(f)
        for event in data['events']:
            events.append(event)
    # check if target_date is past the last event
    if target_date > datetime.datetime(events[-1]['year'], events[-1]['month'], events[-1]['date']):
        return Event()
    # search for next event
    left, right = 0, len(events) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        current_event = events[mid]
        year = current_event['year']
        month = current_event['month']
        date = current_event['date']
        event = datetime.datetime(year, month, date)

        if event < target_date:
            left = mid + 1
        elif event > target_date:
            right = mid - 1
        else:
            # found exact date
            if mid != len(events) - 1:
                return Event(events[mid + 1])
            else:
                return Event()

    # target_date not found
    # handle special cases
    if mid == 0 or mid == len(events) - 1:
        return Event(events[mid])
    else:
        return Event(events[mid + 1])
