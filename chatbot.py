import json

from fbchat import Client, log
from fbchat.models import *
from conversation import get_message

EMAIL = "" #Put your email and password here
PASSWORD = ""
SESSION_ID = ""

class Bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo the message back
        if author_id != self.uid and thread_type == ThreadType.USER:

            user = client.fetchUserInfo(author_id)[author_id]
            print("user: " + user.name)
            msg = get_message(message_object.text, author_id, user.name)

            if msg != None:
                print("sending message...")
                self.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.USER)


def login():
    with open("conf.json", 'r') as conf_file:
        data = json.load(conf_file)
        EMAIL = data['EMAIL']
        PASSWORD = data['PASSWORD']
        SESSION_ID = data['SESSION_ID']

    client = Bot(EMAIL, PASSWORD, session_cookies="")
    session_cookies = client.getSession()
    SESSION_ID = session_cookies
    data['SESSION_ID'] = SESSION_ID

    with open('conf.json', 'w') as conf_file:
        json.dump(data, conf_file)
    return client

client = login()

def login_required(function):
    def wrapper(*args, **kwargs):
        if not client.isLoggedIn():
            login()
        return function(*args, **kwargs)
    
    return wrapper


@login_required
def send_self_message(message):
    message_id = client.send(Message(text=message),thread_id=client.uid, thread_type=ThreadType.USER)
    return message_id

send_self_message("hello Radhesh!")
client.listen()
