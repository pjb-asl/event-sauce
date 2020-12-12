from event_sauce import sequencer


def test_ec01_the_new_and_previous_events_are_different():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606780800, "state": 2}
    previous_event = {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1}
    assert (sequencer.events_are_different(input_event, previous_event)) == True


def test_ec02_the_new_and_previous_events_are_identical():
    input_event = {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"}
    previous_event = {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"}
    assert (sequencer.events_are_different(input_event, previous_event)) == False


def test_ec02a_the_new_and_previous_events_are_identical_despite_dictionary_keys_order_difference():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600, "state": 1}
    previous_event = {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1}
    assert (sequencer.events_are_different(input_event, previous_event)) == False


def test_ec03_the_next_event_is_identical_to_the_new_event():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600, "state": 2}
    next_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606824000, "state": 2}
    assert (sequencer.events_are_different(input_event, next_event)) == False


def test_ec03_the_next_event_is_not_identical_to_the_new_event():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600, "state": 1}
    next_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606824000, "state": 2}
    assert (sequencer.events_are_different(input_event, next_event)) == True


def test_eo01_the_previous_event_is_retrieved_relative_to_the_new_event():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606816800}
    previously_recorded_events = [
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606780800},
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600}
    ]
    returned_event = sequencer.get_previous_event(previously_recorded_events, input_event)
    assert returned_event['event_time'] == 1606809600


def test_eo02_the_previous_event_is_retrieved_relative_to_the_new_event():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606806000}
    previously_recorded_events = [
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606780800},
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600}
    ]
    returned_event = sequencer.get_previous_event(previously_recorded_events, input_event)
    assert returned_event['event_time'] == 1606780800


def test_eo02_no_previous_event_is_retrieved_relative_to_the_new_event():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606719600}
    previously_recorded_events = [
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606780800},
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600}
    ]
    returned_event = sequencer.get_previous_event(previously_recorded_events, input_event)
    print(returned_event)
    assert returned_event is None


def test_eo03_no_next_event_is_retrieved_relative_to_the_new_event():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606824000}
    previously_recorded_events = [
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606780800},
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600}
    ]
    returned_event = sequencer.get_next_event(previously_recorded_events, input_event)
    assert returned_event is None


def test_eo04_the_next_event_is_retrieved_relative_to_the_new_event():
    input_event = {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606802400, "state": 2}
    previously_recorded_events = [
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606780800, "state": 1},
        {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600, "state": 3}
    ]
    returned_event = sequencer.get_next_event(previously_recorded_events, input_event)
    assert returned_event ==  {"key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "event_time": 1606809600, "state": 3}


def test_es01_no_previous_events():
    input_event = {"event_time": 1606780800, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "description": "Something"}
    previously_recorded_events = []
    event_deletions, event_creations = sequencer.sequence(input_event, previously_recorded_events)
    assert event_deletions == []
    assert event_creations == [
        {"event_time": 1606780800, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "description": "Something"}
    ]


def test_es02_there_is_a_previous_event():
    input_event = {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "status": 1}
    previously_recorded_events = [
        {"event_time": 1606780800, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "status": 2}
    ]
    event_deletions, event_creations = sequencer.sequence(input_event, previously_recorded_events)
    assert event_deletions == []
    assert event_creations == [{"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "status": 1}]


def test_es02a_there_is_a_previous_event_but_they_are_identical():
    input_event = {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"}
    previously_recorded_events = [{"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"}]
    event_deletions, event_creations = sequencer.sequence(input_event, previously_recorded_events)
    assert event_deletions == []
    assert event_creations == []


def test_es02b_there_is_a_previous_event_but_they_are_identical_except_event_time():
    input_event = {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"}
    previously_recorded_events = [{"event_time": 1606719600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"}]
    event_deletions, event_creations = sequencer.sequence(input_event, previously_recorded_events)
    assert event_deletions == []
    assert event_creations == []


def test_es06_there_is_a_third_event_arriving_out_of_order_that_renders_the_event_after_it_pointless():
    input_event = {"event_time": 1606798800, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2}
    previously_recorded_events = [
        {"event_time": 1606719600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606802400, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2}
    ]
    event_deletions, event_creations = sequencer.sequence(input_event, previously_recorded_events)
    assert event_deletions == [{"event_time": 1606802400, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2}]
    assert event_creations == [{"event_time": 1606798800, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2}]






