# start with your program from exercise 8-7.
# Write a while loop that allows users to enter an album's artist and title.
# Once you have that information, call make_album() with the users input.
# print the dicitionary that's created. Be sure to include a quit value in
# the loop.

"""Function Created make_album()"""
def make_album(artist_name, album_title):
    """Return a dictionary with this information"""
    music = {'artist' : artist_name, 'album' : album_title}
    return music

"""While Loop for user input"""
while True:
    print("\nPlease enter the name of an Artist you like:")
    print("(enter 'q' any time to quit)")
    singer = input('artist Name: ')
    if singer == 'q':
        break
    songs = input('artist song: ')
    if songs == 'q':
     break
    
    album = make_album(singer, songs)
    print(f"\nArtist: {album['artist']}, Album: {album['album']}")