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


def check_survey_compatibility():
    # let's keep this simple:
    # up to five questions,
    # all single-choice (multiple option),
    # up to five options per question.
    pass


def create_phone_collector():
    # create a collector (SurveyMonkey
    # terminology) specifically
    # for gathering phone input.
    # Call it something unique aka:
    # MonkeyCallerCollector
    # Again, limit to 5 max
    pass

def choose_survey_and_collector():
    # which SM collector to survey the user with
    pass

