state_map = {
    1: 'new',
    2: 'update',
    3: 'sold',
    4: 'delivered'
}


def build_significant_fields():
    return {
        'state',
        'price'
    }


def extract_significant_kvp(dictionary):
    significant_fields = build_significant_fields()
    if dictionary is not None:
        return {k: dictionary[k] for k in dictionary.keys() & significant_fields}
    else:
        return None


def has_a_significant_delta(first, second):
    stripped_first = extract_significant_kvp(first)
    stripped_second = extract_significant_kvp(second)
    if stripped_first != stripped_second:
        return True
    return False


def calculate_difference(value_1, value_2):
    if value_1 > value_2:
        return {"direction": "decrease", "difference": value_2 - value_1}
    else:
        return {"direction": "increase", "difference": value_2 - value_1}


# ToDo: Figure out how to pull this code out into something easier to manage
def construct_state_change(previous_event, event):
    if previous_event is not None:
        if previous_event['state'] != event['state']:
            return {
                'type': state_map[event['state']],
                'event_time': event['event_time'],
                'key': event['key']
            }
        if 'price' in previous_event:
            if previous_event['price'] != event['price']:
                difference = calculate_difference(previous_event['price'], event['price'])
                return {
                    'type': 'price_{}'.format(difference['direction']),
                    'event_time': event['event_time'],
                    'key': event['key'],
                    'price': event['price'],
                    'previous_price': previous_event['price'],
                    'difference': difference['difference']
                }
        else:
            if 'price' in event:
                return {
                    'type': 'price_added',
                    'event_time': event['event_time'],
                    'key': event['key'],
                    'price': event['price']
                }
    else:
        return {
            'type': state_map[event['state']],
            'event_time': event['event_time'],
            'key': event['key']
        }


def summarize(events):
    previous_event = None
    states = []
    for event in events:
        if has_a_significant_delta(previous_event, event):
            state_change = construct_state_change(previous_event, event)
            if state_change:
                states.append(state_change)
        previous_event = event
    return states

