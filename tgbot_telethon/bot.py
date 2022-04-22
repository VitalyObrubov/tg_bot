from telethon import TelegramClient, sync, events
import os
import logging
import yaml

config_path=os.path.join(os.path.dirname(__file__), 'config.yml')
with open(config_path, "r") as f:
    raw_config = yaml.safe_load(f)
# Вставляем api_id и api_hash
api_id = raw_config["bot"]["api_id"]
api_hash = raw_config["bot"]["api_hash"]

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=('https://t.me/afweret')))
async def normal_handler(event):
#    print(event.message)
    user_mess=event.message.to_dict()['message']

    s_user_id=event.message.to_dict()['from_id']['user_id']
    user_id=int(s_user_id)
    user=users.get(user_id)

    mess_date=event.message.to_dict()['date']

    f.write(mess_date.strftime("%d-%m-%Y %H:%M")+"\n")
    f.write(str(user_id)+"\n")
    f.write(user_mess+"\n\n")

    f.flush()

client.start()

group_link='https://t.me/afweret'
group = client.get_entity(group_link)
participants = client.get_participants(group_link)
users={}

for partic in client.iter_participants(group):
    lastname=""
    if partic.last_name:
       lastname=partic.last_name
    users[partic.id]=partic.first_name+" "+lastname

f=open('messages_from_chat', 'a') 

client.run_until_disconnected()
f.close()