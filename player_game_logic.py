import requests
import time
import random

class Player:

    def __init__(self):

        self.total_cards_played = 0
        self.current_set = []
        self.card_chosen = 0
    
    def get_cards(self):

        found = False
        while not found:
            try:
                BASE = 'https://random-word-api.herokuapp.com/'
                words = requests.get(BASE + 'word?number=4').json()
                letters = list('QWERTYUIOPLKJHGFDSAZXCVBNM')
                random.shuffle(letters)
                words += letters[:3]
                self.current_set = words

                return words
                found = True
            except Exception as e:
                print(self.current_set)
                print(e)

                time.sleep(5)
    def choose_card(self,index):
        
        self.card_chosen = self.current_set[index]

    def pick_AI(self,current_story, length = 20):

        BASE = "http://127.0.0.1:5000/"

        lines = current_story.splitlines()
        current_story = lines[-4]+ '\n' + lines[-2]

        current_story = current_story.lstrip().rstrip()

        print(current_story)

        response = requests.post(BASE+ f'storygen/{current_story}/{length}')
        #print(response)
        lines = '\n'.join(lines[:-5])
        answer =  response.json()['gen_text']
        answer = lines+answer
        return answer

'''setup = Player()
print(setup.get_cards())
print(setup.card_chosen)
setup.choose_card(2)
print(setup.card_chosen)

#print(setup.pick_AI('Samarth was',20))

            
'''

