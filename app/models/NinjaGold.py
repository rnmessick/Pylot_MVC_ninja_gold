
from system.core.model import Model
from flask import session, request
from random import randrange
from time import strftime
from datetime import datetime

class NinjaGold(Model):
    def __init__(self):
        super(NinjaGold, self).__init__()

    def process(self):
        if not 'total_gold' in session:
            session['total_gold'] = 0
            session['activity_history'] = []

        search_settings = {
            'farm': {'min': 10 , 'max': 20},
            'cave': {'min': 5, 'max': 10},
            'house': {'min': 2, 'max': 5},
            'casino': {'min': -50, 'max': 50},
        }
        location = request.form['location']
        range_max = search_settings[location]['max']
        range_min = search_settings[location]['min']

        # generate random integer between particular range
        rand_gold = randrange(range_min, range_max + 1)
        session['total_gold'] += rand_gold

        current_time = datetime.now().strftime("%Y-%m-%d %I:%M%p")
        # Generate activity string
        if rand_gold < 0:
            text_color = 'red'
            sentence = "Entered a {} and lost {} golds... Ouch... ({})".format(location, rand_gold * -1, current_time)
            # Lost money!
        else:
            text_color = 'green'
            sentence = "Earned {} golds from the {}! ({})".format(rand_gold, location, current_time)

        outcome = {
            'description': sentence,
            'text_color': text_color
        }

        session['activity_history'].insert(0, outcome)
         