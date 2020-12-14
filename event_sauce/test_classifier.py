from event_sauce import classifier_interface


class TestClassifier(classifier_interface.Classifier):

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
            # Delta 01 - State
            if previous['state'] != current['state']:
                return {
                    'type': self._state_map[current['state']],
                    'event_time': current['event_time'],
                    'key': current['key']
                }
            # Delta 02 - Price
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
            # Delta 1 - State but first time seen
            return {
                'type': self._state_map[current['state']],
                'event_time': current['event_time'],
                'key': current['key']
            }
