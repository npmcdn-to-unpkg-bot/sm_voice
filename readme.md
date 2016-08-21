SurveyMonkey Voice
=
###Summary
A little personal project to facilitate taking SurveyMonkey surveys over the phone. Utilizes SM API and Twilio API. I don't expect anyone will find this but if you want to reuse some of the API wrapper, my SurveyMonkey API submodule from this project is available separately at https://github.com/samesla/sm_api

###Releases
`v0.1`: Aug 21 2016. Basic SM API and Twilio Features exposed through app endpoints.

###Usage
`v0.1:`

1. Clone repo
2. Fill in config.ini
3. Run sm_voice.py
4. From terminal, execute either of the following for testing functionality:
  * `curl http://127.0.0.1:5000/smapitest`
  * `curl -X POST -d 'to=YOUR-PHONE-NUMBER-HERE' http://127.0.0.1:5000/tapitest`


###Features
This is a work in progress. So far the following is available:

####General Features
- [x] Read API details from config file
- [ ] Configure on the fly with any API credentials
- [ ] Basic frontend
- [ ] Have oauth built in to webapp so users can authenticate + voice deliver any surveys

####SurveyMonkey Features
- [x] Write requisite SurveyMonkey API submodule
- [x] Testing SM API endpoints in my webapp
- [ ] Translate json SM Survey to useable object on my webapp
- [ ] Extract Survey Questions and Answers for delivery to user via voice
- [ ] Send user response to Questions back to SurveyMonkey

####Twilio Features
- [x] Write requisite TwilioAPI helper 
- [x] Testing Twilio API endpoints in my webapp
- [ ] Deliver extracted Survey question + answer via voice
- [ ] Extract user answers from touch tone

###License
MIT License. Totally free. Totally no warranties. Copyleft &copy; 2016 Sam Eslamdoust.
