import asyncio
from elarian import Elarian, Customer

client = Elarian(org_id='el_org_eu_cl6rMc', app_id='el_app_5XNTq4', api_key='el_k_live_c9b97e705e52d12327bc3bc4874b4776058bae5576c7a4fc5760306ccd554442')

async def on_connected():
  print("App is running!")

  alice = Customer(client=client, number="+254716434058", provider="cellular")

  telegram_channel = {
    'number': 'newton_new_bot',
    'channel': 'telegram'
  }

  print(await alice.send_message(telegram_channel, { 'body': { 'text': 'Hello World!' }}))

async def start():
  client.set_on_connection_error(lambda err: print(f"Connnection error: {err}"))
  client.set_on_connected(on_connected)
  await client.connect()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()