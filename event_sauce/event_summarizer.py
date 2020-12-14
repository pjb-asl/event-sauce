import abc


class EventSummerizer(abc.ABC):
    @abc.abstractmethod
    def significant_fields(self):
        pass

    @abc.abstractmethod
    def classify_state_change(self, previous, current):
        pass

    @staticmethod
    @abc.abstractmethod
    def calculate_difference(value1, value2):
        pass
