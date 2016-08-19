"""Copyright (C) Sam Esla, 2016. MIT License. https://opensource.org/licenses/MIT"""
from twilio import twiml
from twilio.rest import TwilioRestClient

class TwilioAPIClient:
    """
    A convenience wrapper around the TwilioRestClient. Makes it simpler to use.
    It handles outgoing calls and already-in-progress calls but DOES NOT handle the entry
    point of incoming calls.

    If you have a Twilio number, your app can receive incoming calls too. Configure the number at
        > https://www.twilio.com/console/phone-numbers/incoming
    with webhook invocation (e.g. app_base_url/<entry_point>). Then set up a route in your app - e.g. /incoming_calls in sm_voice_views.py
    """
    def __init__(self, twilio_account_sid, twilio_auth_token, app_base_url):
        """
        :param twilio_account_sid: str: Twilio account SID (https://www.twilio.com/console/account/settings)
        :param twilio_auth_token: str: Twilio account auth token (https://www.twilio.com/console/account/settings)
        :param app_base_url: str: Your application's URL. https://ExampleTwilioWebServer.com
        :param call_from: str: The caller ID to be displayed on the call. This must be a verified Twilio number.
        """
        self.sid = twilio_account_sid
        self.auth = twilio_auth_token
        self.app_base_url = app_base_url
        self.client = TwilioRestClient(self.sid, self.auth)

    def call_phone(self, call_to, call_from, action_uri, status_callback_uri=None, record=False):

        """
        Create an outgoing call to a phone number.
        :param call_to: str: The number to call
        :param call_from: str: The caller ID to be displayed on the call. This MUST be a verified-by Twilio number.
        :param action_uri: str: Which endpoint in your app should the call invoke after it is picked up?
        :param status_callback_uri: str: Which endpoint in your webapp to send status messages to?
        :param record: bool: Should the call be recorded?
        :return call: Call object from twilio.rest.resources.calls
        """

        status_callback = self.app_base_url + status_callback_uri if status_callback_uri is not None else None
        status_events = ["initiated", "ringing", "answered", "completed"]

        print("Creating outgoing call to: %s" % call_to)
        call = self.client.calls.create(to=call_to,
                                        from_=call_from,
                                        url=self.app_base_url + action_uri,
                                        method="GET",
                                        status_callback=status_callback,
                                        status_callback_method="POST",
                                        status_events=status_events,
                                        record=record,
                                        if_machine="Hangup")
        return call

    def get_input(self, message, action_uri, num_digits):
        r = twiml.Response()
        with r.gather(action=self.app_base_url+action_uri,
                      timeout=5,
                      numDigits=num_digits) as gather:
            gather.say(message)
        return r.toxml(xml_declaration=False)

    @staticmethod
    def play_sound(address_to_file):
        r = twiml.Response()
        r.play(address_to_file)
        return r.toxml(xml_declaration=False)

    @staticmethod
    def say(message):
        r = twiml.Response()
        r.say(message)
        return r.toxml(xml_declaration=False)
