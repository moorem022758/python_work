# Album - Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and 
# an album title, and it should return a dictionary containing this
# information. 
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the 
# album information correctly.

"""Function Created make_clbun()"""
def make_album(artist_name, album_title):
    """Return a dictionary with this information"""
    music = {'artist' : artist_name, 'album' : album_title}
    return music

sounds = make_album("hammer", "hammertime" )
print(sounds)
