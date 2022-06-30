from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import random

application = Flask(__name__)
db = SQLAlchemy()
Bootstrap(application)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

#  cur_otp = generateOTP()


def generateOTP(otp_size = 6):
    final_otp = ''
    for i in range(otp_size):
        final_otp = final_otp + str(random.randint(0,9))
    return final_otp



@application.route("/")
def hello_world():
    return render_template("login.html")





if __name__ == "__main__":
    application.run()