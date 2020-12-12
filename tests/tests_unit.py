from event_sauce import sequencer


def test_es01_no_previous_events():
    input_event = {"event_time": 1606780800, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"}
    previous_events = []
    event_deletions, event_creations = sequencer.sequence(input_event, previous_events)
    assert len(event_deletions) == 0
    assert len(event_creations) == 1
