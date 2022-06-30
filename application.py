from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import random
import asyncio
from elarian import Elarian, Customer

application = Flask(__name__)
db = SQLAlchemy()
Bootstrap(application)

elarian = Elarian(org_id='el_org_eu_cl6rMc', app_id='el_app_5XNTq4', api_key='el_k_live_c9b97e705e52d12327bc3bc4874b4776058bae5576c7a4fc5760306ccd554442')


# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'




async def on_connected():
    print ("it works")


    alice = Customer(client=elarian, number="+254716434058", provider="cellular")

    telegram_channel = {
    'number': 'newton_new_bot',
    'channel': 'telegram'
    }

    print ("it works again")

    try:

        print(await alice.send_message(telegram_channel, { 'body': { 'text': 'Hello World!' }}))

    except Exception as e:

        print({e})
  

async def on_received_telegram(notification, customer):
    print(notification)
    return "Received telegram notification!"

async def start():
  elarian.set_on_connection_error(lambda err: print(f"Connnection error: {err}"))
  elarian.set_on_connected(on_connected)
  elarian.set_on_received_telegram(on_received_telegram)
  await elarian.connect()





@application.route("/",methods=['GET', 'POST'])
async def hello_world():

    await start()


    return render_template("login.html")


@application.route("/client")
async def home():

    return render_template("home.html")


if __name__ == "__main__":

    # asyncio.run(start())
    application.run()

    # loop = asyncio.new_event_loop()
    # loop.create_task(start())
    # loop.run_forever()


    
    