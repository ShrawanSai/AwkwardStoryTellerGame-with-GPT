import random

class StoryTeller:

    def __init__(self,user_name):

        self.char_name = user_name
        self.story_start = ''''''
        self.story_end = ''''''
        self.assigned_story = ''''''
        self.current_story = ''''''
        self.no_of_turns_played = 0

    def name_charachter(self,name):
        self.char_name = name

    def assign_story(self):

        story_starts = [
            '''$$Charachter$$ was on his way back to camp after a long day at work. He was a soldier of the army platoon stationed at the Fourth Maria Hill.
            He got on to his mini truck, turned on his engine and headed back. He was posted at peak and coming back down was rather difficult because of the detoriated and 
            poorly maintained roads. It started to rain suddenly and $$Charachter$$ was now driving with atmost caution. What he did not seem to notice was the
            broken branch of the tree that fell on the road in front of him. He rams into the obstacle on the road, which almos launches the mini truck off the road.
            The vehicle gets off road and tips on its side. But to his luck, that was not all. As he struggled to get out, the vehicle started to move. Itlooked
            like there was going to be a landslide. 
            He tries to get out of the car but''',

            '''Sunlight had sneaked in through the window and was creeping toward the chair where $$Charachter$$'s pants dangled. He was lying bare-chested
            in bed, rubbing some gunk from the corner of his right eye. It must have collected while he was sleeping, and to just let it stay there
             seemed inappropriate. Meanwhile, his left eye was idle, so he gave it the job of looking at his pants. He had taken them off the night before,
              and now regretted tossing them so casually over the chair, where they lay wrinkled and crumpled beside his jacket. As his left eye 
              inspected them, he began to wonder whether while sleeping he had shed, snakelike, a layer of skin, for that’s what his jacket and pants looked
               like. At this point, a drop of sunshine reached his pant leg; the little splotch of leaping light made him think of a golden flea.
                And so he felt itchy all over and had his idle left hand make itself useful by scratching. 
                When then, someone was knocking on the door.'''
        ]


        story_ends = [
            '''3 days later, after $$Charachter$$ walked for all those days, through the woods with barely any food and water, he could see a ray of hope.
            He stood upto see what looked like his army camp. With all the will he could muster, he got himself up and started limping to the base. As he was on his way
            out of the woods, he heard that roar again. It had now turned bigger and scarier from what he could remember his time in the woods. 
            He started to run as fast as he could. He could not go through that again. It seemed to him that he was being followed. At the base of the camp,
            he could finally see some movement. He started waving his hands helplessly and shouting for help. What he didn't seem to notice was that the movement
            was actually the same thing he saw in the woods. The same creature. But now he had only attracted its attention and now started chargig towards. He now frightened to his core. He
            thought it was finally the time to do what he should have done a long time ago. He took out something that looked like a pen from his pocket.
            But then he took off the cap and then started to write something on his arm. He wrote the words, "Wake up you sick freak".''',

            '''$$Charachter$$ now thought to himself. I am never ever drinking again'''
            
        ]

        index = random.randint(0, len(story_starts)-1)
    

        start = story_starts[index]
        end = story_ends[index]

        self.story_start = start.replace("$$Charachter$$", self.char_name)
        self.story_end = end.replace("$$Charachter$$", self.char_name)

    def start_story(self):

        self.current_story = self.story_start + '\n\n'
        

    def append(self, new_addition):

        self.current_story += new_addition+ '\n\n'

        self.no_of_turns_played += 1

    def get_story(self):

        return self.current_story
    
    def count(self):

        return self.no_of_turns_played
        


'''teller = StoryTeller('Shrawan')
teller.name_charachter('Jack')
teller.assign_story()

teller.start_story()
print(teller.current_story)

teller.append('hi')

print(teller.get_story())
print(teller.current_story)'''