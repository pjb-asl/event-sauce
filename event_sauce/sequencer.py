def events_are_different(first, second):
    first_local = first.copy()
    second_local = second.copy()
    del(first_local['event_time'])
    del(second_local['event_time'])
    if second_local == first_local:
        return False
    return True


def no_previous_events(events):
    if len(events) == 0:
        return True
    return False


def get_previous_event(events, new_event):
    sorted_events = sorted(events, key=lambda k: k['event_time'])
    most_recent_previous = None
    for event in sorted_events:
        if new_event['event_time'] >= event['event_time']:
            most_recent_previous = event
    return most_recent_previous


def get_next_event(events, new_event):
    sorted_events = sorted(events, key=lambda k: k['event_time'])
    for event in sorted_events:
        if event['event_time'] > new_event['event_time']:
            return event
    return None


def sequence(new, previous_events):
    deletions = []
    creations = []
    if no_previous_events(previous_events):
        creations = [new]
    else:
        last = get_previous_event(previous_events, new)
        next = get_next_event(previous_events, new)
        print('Last: {}'.format(last))
        print('Next: {}'.format(next))
        if events_are_different(last, new):
            print('We are creating a new one')
            creations = [new]
            print(creations)
        if next:
            if not events_are_different(new, next):
                deletions = [next]
    return deletions, creations
