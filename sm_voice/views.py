from flask import request, jsonify
from sm_voice import app, smapi, tapi  # flask app, smapi client, and tapi, as set up in init.


@app.route('/choose', methods=["GET", "POST"])
def choose():
    return tapi.get_input("Welcome to SM Voice. Press 1 for sound clip, 2 for exit.", "/play_sound", 1), 200


@app.route('/play_sound', methods=["GET", "POST"])
def play_sound():
    input = request.form.get("Digits", 2)
    if input == '1':
        return tapi.play_sound("/static/sorrydude.mp3"), 200
    else:
        return tapi.hangup(), 200


@app.route('/status', methods=["GET", "POST"])
def status_callback():
    status = request.form
    print("Call Status Update for call %s" % status.get("CallStatus", "N/A"))
    print("Status: %s" % status.get("CallStatus", "N/A"))
    print("Recording: %s" % status.get("RecordingUrl", "N/A"))
    return '', 204


@app.route('/smapitest', methods=["GET", "POST"])
def smapi_test():
    print("sm api test")
    requestvars = request.args
    surveys = smapi.get_surveys_list(**requestvars)
    return jsonify(surveys), 200


@app.route('/tapitest', methods=["GET", "POST"])
def twilio_test():
    print("twilio test")
    to = request.form.get("to")
    if to is not None and to.isnumeric() and 10 <= len(to) <= 11:
        call = tapi.call_phone(to, "/choose", "/status", True)
        print("Twilio Call SID: %s" % call.sid)
        return "OK!", 200
    else:
        return "Invalid", 400
