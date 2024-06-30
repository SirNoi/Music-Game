from music import _Music_Raw_,artist_title
from time import sleep
import game_over as gm
#^ Importing the classes from the other files

#Lambda function to clear the console
clear = lambda: print("\033c", end="", flush=True)

#constant value of max chances to compare the players chances against
MAXIMUM_CHANCES = 2

class Game():

    #resets the raw song data so there is a new song each time it is called
    def reset_song_info():
        raw = _Music_Raw_.get_raw_choice()
        artist = artist_title.get_artist(raw)

        #unpacks the tuple from the first_letters_title() method 
        titles = artist_title.first_letters_title(raw)
        original_title = titles[0]
        letters = titles[1]

        #returns a tuple
        return artist,original_title,letters

    #main game loop, takes in the name of the user and score
    #name so the final score can be recorded with a name
    #and the score so the score of the user can be tracked
    def main_loop(count,name:str) -> None:
        main = True
        chances = 0
        raw = Game.reset_song_info()

        while main:
            
            #gets the questions details
            artist = raw[0]
            original_title = raw[1]
            letters = raw[2]

            #prints the artist and the letters of the words of the title
            print(f"\nThe artist is : {artist}")
            print("The letters of the title are:")
            for i in letters:
                print(f"{i}")

            #gets the user's input and strips it of trailing and leading whitespace
            attempt = input("Your Guess: ").strip()
            chances += 1

            #checks if the input is correct
            if attempt.upper() == original_title.upper() and chances < MAXIMUM_CHANCES:
                #resets chances to 0 when correct and adds 3 to the score
                #recursion to make the game run again
                chances = 0
                count =count + 3
                clear()
                #passes the new value of count and also repasses the name back in
                Game.main_loop(count,name)

            elif attempt.upper() == original_title.upper() and chances == MAXIMUM_CHANCES:
                #same thing as above but only adds 1 to the score since it is the second
                #try on the same question
                chances = 0
                count = count + 1
                clear()
                Game.main_loop(count,name)

            elif attempt.upper() != original_title.upper() and chances == MAXIMUM_CHANCES:
                #if the user doesn't get it right on the second attempt, the game ends and
                #the final score is passed into the record_score() function
                clear()
                print("Game over")
                sleep(1)
                print(f"\nYour final score is : {count}")
                #records the fianl score
                gm.GameOver.record_score(name,count)
                sleep(2)
                #ends the game, showing the leaderboard
                gm.GameOver.end_game()


