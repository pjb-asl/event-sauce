from event_sauce import lettings_classifier


def test_listing_first_seen():
    classifier = lettings_classifier.LettingsClassifier()
    previous_event = None
    current_event = {
        "event_time": 1606809600,
        "key": "a3c78825-d99f-4901-aa4f-395fcefe9751",
        "state": 1
    }
    expected = {
            "type": "new",
            "event_time": 1606809600,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        }
    state_change_classification = classifier.classify_state_change(previous_event, current_event)
    assert state_change_classification == expected
