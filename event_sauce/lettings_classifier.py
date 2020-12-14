from event_sauce import classifier_interface


class LettingsClassifier(classifier_interface.Classifier):

    def __init__(self):
        self._significant_fields = {
            'status',
            'rent_pcm'
        }
        self._status_map = {
            1: "For Rent",
            2: "Rented"
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
        return None