from channels.sessions import channel_session
from channels import Group



def ws_connect(message):
    path = message['path']
    if path == b'/index/':
        Group('index').add(message.reply_channel)
        message.reply_channel.send({'accept': True})


def ws_message(message):
    Group('index').send({'text': message.content['text'],})

def ws_disconnect(message):
    Group('index').discard(message.reply_channel)

