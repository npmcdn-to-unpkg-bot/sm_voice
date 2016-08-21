import os
from configparser import ConfigParser, ParsingError
from flask import Flask
from sm_api.smapi_client import SMAPIClient
from twilio_api.client import TwilioAPIClient


def parse_configs(section, required_keys=[]):
    """
    Let's get the API access details from the config.ini file at the root of the application (one level above this file)
    :param section: str: which API details? TwilioAPI or SMAPI?
    :param required_keys: which keys are required (sm_voice needs SMAPI:access_token+api_key Twilio:auth_token+account_sid)
    :return: dict: configuration dictionary
    """
    cfg = ConfigParser()
    cfg.read("config.ini")
    try:
        configuration = dict(cfg.items(section))
        if not configuration.keys() >= set(required_keys):  # if the config keys aren't a superset of the required keys
            raise ParsingError("config.ini")
    except ParsingError as e:
        print("Couldn't load %s configs" % section)
        print(e)
        exit()
    return configuration


smapi_cfg = parse_configs("SMAPI", ["api_key", "access_token"])
tapi_cfg = parse_configs("TwilioAPI", ["auth_token", "account_sid", "from_number"])
app_url = parse_configs("SMVoice", ["app_url"]).get("app_url")

try:
    smapi = SMAPIClient(**smapi_cfg)
except Exception as e:
    print("failed to initialize SMAPIClient. check connection or config.ini credentials.")
    exit()
try:
    tapi = TwilioAPIClient(**tapi_cfg, app_base_url=app_url)
except Exception as e:
    print("Failed to initialize TwilioAPIClient. Check connection or config.ini credentials")
    exit()

app = Flask(__name__, static_folder=(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))))
import sm_voice.views  # this is being imported after because app = Flask(...) needs to be initialized first.



