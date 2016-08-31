import uuid
from enum import Enum


class CallState(Enum):
    INIT = 1
    NEXT = 2
    REDO = 3
    COMPLETE = 4


class Calls(object):
    def __init__(self):
        self._calls = list()

    def add_call(self, call):
        # low-weight app, I don't want to handle more than a handful of calls.
        if len(self._calls() <= 5):
            self._calls.append(call)
            return True
        return False

    def get_call(self, id):
        for call in self._calls:
            if call.id == id:
                return call
        return None

    def remove_call(self, id):
        for call in self._calls:
            if call.id == id:
                i = self._calls.index(call)
                del self._calls[i]
                return True
        return False


class Call(object):
    def __init__(self, twilio_sid, survey_id, collector_id):
        self.id = uuid.uuid()
        self.twilio_sid = twilio_sid
        self.survey_id = survey_id  # the survey we are taking
        self.collector_id = collector_id  # the collector that the answers are tied to
        self.survey = {}  # get the survey and put it here
        self.call_state = CallState.INIT
        self.question_counter = 0  # which question are we on

