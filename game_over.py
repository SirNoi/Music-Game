from time import sleep
import sqlite3

#I have already made a .db file with the table scores
#The table 'scores' has two columns, name and score.

class GameOver():
    """
    Contains the methods that end the game and record the scores of the users\n
    record_score() -> Records the current players score into an sqlite3 database\n
    end_game() -> Prints the Top 5 in the leaderboard by reading the sqlite 3 database
    """

    def record_score(name,score) -> None:
        """Records the users name and score into a database"""

        connection = sqlite3.connect("leaderboard.db")
        cursor = connection.cursor()
        #Inserts the values
        cursor.execute("INSERT INTO scores VALUES (?,?)",(name,score,))
        connection.commit()

        #closes both connections to avoid errors
        cursor.close()
        connection.close()

    def end_game() -> None:
        """Prints the leaderboard then quits the game"""
        print("\nThe Top 5 are:")

        connection = sqlite3.connect("leaderboard.db")
        cursor = connection.cursor()
            
        #Gets the highest values of each user, allowing users to have more than one entry
        sql = "SELECT name, MAX(score) AS highest_score FROM scores GROUP BY name ORDER BY score DESC;"
        top_five = cursor.execute(sql).fetchall()

        #prints the top 5 users
        for i in range(0,5):
            name = top_five[i][0]
            score = top_five[i][1]

            print(f"{name}:{score}\n")

        #closes both connections to avoid errors
        cursor.close()
        connection.close()

        #Allows the user to read the leaderboard then quits after 3 seconds
        sleep(3)
        quit()
