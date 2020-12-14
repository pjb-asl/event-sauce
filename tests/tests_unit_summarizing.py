from event_sauce import summarizer


def test_initial_event_with_significant_delta_creates_new_entity_state_01():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1}
    ]
    expected = [
        {
            "type": "new",
            "event_time": 1606809600,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_initial_event_with_significant_delta_creates_new_entity_state_02():
    events = [
        {"event_time": 1606809600, "key": "7574d5cc-5e7e-42fc-a17a-179119981697", "state": 1}
    ]
    expected = [
        {
            "type": "new",
            "event_time": 1606809600,
            "key": "7574d5cc-5e7e-42fc-a17a-179119981697"
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_initial_event_with_significant_delta_creates_an_update_entity_state_03():
    events = [
        {"event_time": 1606809600, "key": "7574d5cc-5e7e-42fc-a17a-179119981697", "state": 2}
    ]
    expected = [
        {
            "type": "update",
            "event_time": 1606809600,
            "key": "7574d5cc-5e7e-42fc-a17a-179119981697"
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_second_event__with_significant_delta_creates_two_entity_states():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2}
    ]
    expected = [
        {
            "type": "new",
            "event_time": 1606809600,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "update",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_second_event_with_significant_delta_creates_two_entity_states_but_ignores_insignificant_third():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "TBC"},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "Now Done"}
    ]
    expected = [
        {
            "type": "new",
            "event_time": 1606809600,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "update",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_forth_event_with_significant_delta_creates_three_entity_states_ignoring_third():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "TBC"},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "Now Done"},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "Now Done", "price": 2000}
    ]
    expected = [
        {
            "type": "new",
            "event_time": 1606809600,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "update",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "price_added",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751",
            "price": 2000
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_fifth_event_with_significant_delta_creates_four_entity_states_ignoring_third_price_increase():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "TBC"},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2,
         "description": "Now Done"},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "Now Done",
         "price": 2000},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "Now Done",
         "price": 2300}
    ]
    expected = [
        {
            "type": "new",
            "event_time": 1606809600,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "update",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "price_added",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751",
            "price": 2000
        },
        {
            "type": "price_increase",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751",
            "price": 2300,
            "previous_price": 2000,
            "difference": 300
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_fifth_event_with_significant_delta_creates_four_entity_states_ignoring_third_price_decrease():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "TBC"},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2,
         "description": "Now Done"},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "Now Done",
         "price": 2000},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2, "description": "Now Done",
         "price": 1900}
    ]
    expected = [
        {
            "type": "new",
            "event_time": 1606809600,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "update",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751"
        },
        {
            "type": "price_added",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751",
            "price": 2000
        },
        {
            "type": "price_decrease",
            "event_time": 1606809700,
            "key": "a3c78825-d99f-4901-aa4f-395fcefe9751",
            "price": 1900,
            "previous_price": 2000,
            "difference": -100
        }
    ]
    states = summarizer.summarize(events)
    assert states == expected


def test_has_a_significant_delta_function_01():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 2}
    ]
    expected = True
    result = summarizer.has_a_significant_delta(events[0], events[1])
    assert expected == result


def test_has_a_significant_delta_function_02_no_significance():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1}
    ]
    expected = False
    result = summarizer.has_a_significant_delta(events[0], events[1])
    assert expected == result


def test_has_a_significant_delta_function_03_no_significance_but_has_an_insignificant_change():
    events = [
        {"event_time": 1606809600, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1, "count": 1},
        {"event_time": 1606809700, "key": "a3c78825-d99f-4901-aa4f-395fcefe9751", "state": 1, "count": 2}
    ]
    expected = False
    result = summarizer.has_a_significant_delta(events[0], events[1])
    assert expected == result