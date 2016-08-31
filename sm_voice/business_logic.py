from sm_voice import smapi
from sm_api.survey_model import consume_raw_api

def process_incoming_call(request_data):
    # when a user calls in to
    # answer a survey
    pass


def process_calling_phone(name, number):
    # when web UI triggers calling
    # a user's phne
    pass


def ask_question():
    # ask the question of the user
    pass


def get_user_input():
    # get touch tone input and resp
    pass


def send_user_response_to_sm():
    # send user response to SM once all
    # answers are submitted?
    # can also send partial answers.
    pass


def check_survey_compatibility(survey_id):
    # let's keep this simple:
    # up to five questions,
    # all single-choice (multiple option),
    # up to five options per question.
    raw_survey = smapi.get_survey_details(survey_id)
    if raw_survey.get("id") is not None:
        survey = consume_raw_api(raw_survey)
        if survey is not None:
            # we managed to parse! so it's mostly compatible.
            # TODO: implement further checks.
            if survey.pages == 1 and len(survey.questions) <= 10:
                for q in survey.questions:
                    if len(q.options) > 5:
                        return False
                return True
    return False


def create_phone_collector(survey_id):
    # create a collector (SurveyMonkey
    # terminology) specifically
    # for gathering phone input.
    # Call it something unique aka:
    # MonkeyCallerCollector
    # Again, limit to 5 max
    if check_survey_compatibility(survey_id) is True:
        collector = smapi.create_collector(survey_id)
        if collector.get("status") == "open":
            return survey_id, collector.get("id")
            # we should attach this to the call object here.


def choose_survey_and_collector(survey_id, collector_id):
    # which SM collector to survey the user with
    if check_survey_compatibility(survey_id) is True:
        collector = smapi.get_collector(collector_id)
        if collector.get("status") == "open":
            return survey_id, collector_id
            # we should attach this to the call object here.

