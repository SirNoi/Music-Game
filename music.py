from random import choice

#private class only accessible within this .py file
class _Music_Raw_():
    """Contains methods to get back the raw music data.\n
    get_raw() -> Returns a list(str) with all the music\n
    get_raw_choice() -> Returns a list(str) with a random song using unweighted random selection
    """

    #returns all songs and artists
    def get_raw() -> list[str]:
        with open("music.txt","r") as f:
            raw_data = f.readlines()
        return raw_data

    #returns a random selection of a song and artist
    def get_raw_choice() -> list[str]:
        raw_data = choice(open("music.txt").readlines()).split(":")
        return raw_data


class artist_title():
    """Methods on the artist and song title data.\n
    get_song_title() -> Returns the title of the song\n
    get_artist() -> Returns the artist of the song\n
    first_letters_title() -> Returns a list with the original title and the first letters of each word combined
    
    """
    #gets the song title from the raw data inputted
    def get_song_title(raw) -> str:
        title = raw[0].strip()
        return title  
        
    #gets the artist of the song from the raw data inputted
    def get_artist(raw) -> str:
        artist = raw[1].strip()
        return artist      

    #returns a tuple with the original title and the first letter of each word of the title
    def first_letters_title(raw) -> list[str]:
        title = artist_title.get_song_title(raw)
        words = title.split(" ")
        first_letters = []

        for i in range(len(words)): 
            first_letters.append(words[i][0])
        
        #uses the map() function to apply str onto all the letters and combine them into one list
        first_letters = ''.join(map(str,first_letters))
        return [title,first_letters]   

