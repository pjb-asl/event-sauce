from event_sauce import test_classifier


def extract_significant_kvp(dictionary, significant_fields):
    if dictionary is not None:
        return {k: dictionary[k] for k in dictionary.keys() & significant_fields}
    else:
        return None


def has_a_significant_delta(first, second, significant_fields):
    stripped_first = extract_significant_kvp(first, significant_fields)
    stripped_second = extract_significant_kvp(second, significant_fields)
    if stripped_first != stripped_second:
        return True
    return False


def summarize(events):
    previous_event = None
    states = []
    change_classifier = test_classifier.TestClassifier()
    for event in events:
        if has_a_significant_delta(previous_event, event, change_classifier.significant_fields()):
            state_change = change_classifier.classify_state_change(previous_event, event)
            if state_change:
                states.append(state_change)
        previous_event = event
    return states

