
from system.core.controller import *

class NinjaGolds(Controller):
    def __init__(self, action):
        super(NinjaGolds, self).__init__(action)

        self.load_model('NinjaGold')
      

  
   
    def index(self):

        return self.load_view('index.html')

    def process_money(self):
         # Call model method to do logic work
        self.models['NinjaGold'].process()
        return redirect('/')

