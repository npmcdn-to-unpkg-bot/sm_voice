import business_logic
from calls_model import Calls
from flask import Flask

app = Flask(__name__)


@app.route('/call_phone', methods=["POST"])
def call_phone():
    business_logic.process_calling_phone()

if __name__ == '__main__':
    calls = Calls()
    app.run()
