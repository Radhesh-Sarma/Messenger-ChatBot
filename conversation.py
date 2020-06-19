import time
from quote import getquote,getcoronaupdates,weather

user_dict = {}

intro_msg = """
Hi {},
I am Foodie, The ChatBot, I work for Radhesh
Radhesh is currently busy somewhere eating ( ¯\_(ツ)_/¯).

Either you can wait for him to get back, or talk to me!
    send: Foodie menu to get the dishes i can serve you
(to talk to Foodie start your message with Foodie)

 you can also ask me for Radhesh's phone number ,email 
"""

Foodie_msg = """
Ah, so want to talk to Foodie!\n{}
"""

menu_msg = """ 

Hi {},

Getting Bored?, ask Foodie for a life quote
    send: Foodie quote

To get Weather updates 
    send: Foodie weather <location name>

To get CoronaVirus updates in India ,
    send: Foodie corona  
    """



def get_message(msg, user_id, username):
    print("{}: {}".format(user_id, msg))

    if 'foodie' in msg.lower():
        if ('menu' in msg.lower()):
            return menu_msg.format(username)

        elif ('phone' in msg.lower() or 'number' in msg.lower() or 'contact' in msg.lower()):
            return Foodie_msg.format("77-320-99799")

        elif ('email' in msg.lower()):
            return Foodie_msg.format("radheshsarma29@gmail.com")

        elif ('quote' in msg.lower()):
            return getquote()

        elif ('corona' in msg.lower()):
            return getcoronaupdates()

        elif ('weather' in msg.lower()):
            return weather(msg.split()[2])

        elif ('phone' in msg.lower() or 'number' in msg.lower() or 'contact' in msg.lower()):
            return Foodie_msg.format("77-320-99799")

        elif ('email' in msg.lower()):
            return Foodie_msg.format("radheshsarma29@gmail.com")

        else:
            return ("Hey Foodie here! you want to eat something? send Foodie menu to get the menu")

    if user_id not in user_dict:
        user_dict[user_id] = time.time()
        return intro_msg.format(username)

    else:
        if ((time.time() - user_dict[user_id]) > 600):
            user_dict[user_id] = time.time()
            text = "Hey Foodie here!\n you want to eat something?\n send Foodie menu to get the menu"
            return text
    return None

