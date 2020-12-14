import event_summarizer


class TestSummarizer(event_summarizer.EventSummarizer):

    def __init__(self):
        self._significant_fields = {
            'state',
            'price'
        }
        self._state_map = {
            1: 'new',
            2: 'update',
            3: 'sold',
            4: 'delivered'
        }

    @staticmethod
    def calculate_difference(value_1, value_2):
        if value_1 > value_2:
            return {"direction": "decrease", "difference": value_2 - value_1}
        else:
            return {"direction": "increase", "difference": value_2 - value_1}

    def significant_fields(self):
        return self._significant_fields

    def classify_state_change(self, previous, current):
        if previous is not None:
            # I think this needs to be more obvious from a sequencial POV
            # e.g. State, Price, Decription order of precedence
            # Also this needs cope with multiple states changing in one observation
            if previous['state'] != current['state']:
                # Can I move message templates to a method
                return {
                    'type': self._state_map[current['state']],
                    'event_time': current['event_time'],
                    'key': current['key']
                }
            if 'price' in previous:
                if previous['price'] != current['price']:
                    difference = self.calculate_difference(previous['price'], current['price'])
                    return {
                        'type': 'price_{}'.format(difference['direction']),
                        'event_time': current['event_time'],
                        'key': current['key'],
                        'price': current['price'],
                        'previous_price': previous['price'],
                        'difference': difference['difference']
                    }
            else:
                if 'price' in current:
                    return {
                        'type': 'price_added',
                        'event_time': current['event_time'],
                        'key': current['key'],
                        'price': current['price']
                    }
        else:
            return {
                'type': self._state_map[current['state']],
                'event_time': current['event_time'],
                'key': current['key']
            }
