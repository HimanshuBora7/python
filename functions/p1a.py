#8-8. User Albums: Start with your program from Exercise 8-7. Write a while 
#loop that allows users to enter an album’s artist and title. Once you have that 
#information, call make_album() with the user’s input and print the dictionary 
#that’s created. Be sure to include a quit value in the while loop.

def make_album(name,title,no_of_songs = None):
    album = {'artist name':name,'title':title}
    if no_of_songs:
        album['no of songs']=no_of_songs
    return album

while True :
 artist = input("enter artist's name ")
 print("(enter q anytime to quit)")
 if artist != 'q':
    album = input("enter the album name ")
    print("(enter q anytime to quit)")
    if album != 'q':
       album_1=make_album(artist,album)
       print(album_1)
    else:
       print("would like to see u again fr survey")
       break
 else:
    print("would like to see u again for the survey ")
    break
