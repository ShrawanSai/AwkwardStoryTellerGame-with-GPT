from story_teller_game_logic import StoryTeller
from player_game_logic import Player
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


class Game:
    def __init__(self):

        self.storyteller = ''
        self.players = []
        self.round_count = 0


    def register_storyteller(self,tellerid):

        self.story_teller = StoryTeller(tellerid)
    
    def name_main_charachter(self,name):

        self.story_teller.name_charachter(name)

    def register_user(self,player_name):

        self.players.append(player_name)

    def start_procedure(self):

        self.story_teller.assign_story()

        self.story_teller.start_story()

        return self.story_teller.story_start,self.story_teller.story_end

    def recieve_from_teller(self, bit):

        print(bit)

        self.story_teller.append(bit)

    def player_setup(self):

        self.player_move = Player()
        cards = self.player_move.get_cards()

        return cards
    
    def players_card_choice(self,index):

        self.player_move.choose_card(index)
    
    def invoke_AI(self):

        cur_story = self.story_teller.current_story

        new_addition = self.player_move.pick_AI(cur_story)

        #print(new_addition)

        self.story_teller.current_story = new_addition

        return new_addition

    def end_story(self):

        self.story_teller.append(self.story_teller.story_end)


    



new_game = Game()

new_game.register_storyteller('Shrawan')
new_game.name_main_charachter('Bravick Rhineheart')

new_game.register_user('Aryan')
new_game.register_user('Samarth')


story_start, story_end = new_game.start_procedure()

print(f''' STORY START:
{story_start}''')

print('\n\n')

print(f'''STORY END:
{story_end}''')



print('\n\n\n BOT: Starting Story \n\n\n')
print(new_game.story_teller.current_story)

st_count = 0

while True:
    if new_game.round_count == 10:
        break
    
    message = input()

    message = message.split('$')

    if message[0] == '0':

        #print(message[1])
        new_game.recieve_from_teller(message[1])
        st_count += 1
        print(new_game.story_teller.current_story)

    else:
        my_cards = new_game.player_setup()
        print('BOT: Here are your choices. Select a number\n')
        for i in range(len(my_cards)):
            print(f'{i} : {my_cards[i]}')
        print(f'{i+1} : Call AI')
        print('\n\n')
        
        ch = int(input('BOT : Enter Choice Number'))
        if ch == i+1:
            ai_output = new_game.invoke_AI()
            print(new_game.story_teller.current_story)

        else:
            pcc = my_cards[ch]
            new_game.players_card_choice(ch)
            
            question = input('BOT : Enter the question to ask the story teller')

            print(f'BOT : Storyteller must use this card:  {pcc} ')

    if st_count ==3:
        print('Player\'s turn')
        st_count = 0
    

        

    
    
    