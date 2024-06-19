# 8-7. Album: Write a function called make_album() that builds a dictionary 
#describing a music album. The function should take in an artist name and an 
#album title, and it should return a dictionary containing these two pieces of 
#information. Use the function to make three dictionaries representing different 
#albums. Print each return value to show that the dictionaries are storing the 
#album information correctly.
#Use None to add an optional parameter to make_album() that allows you to 
#the number of songs, add that value to the album’s dictionary. Make at least 
#one new function call that includes the number of songs on an album.

def make_album(name,title,no_of_songs = None):
    album = {'artist name':name,'title':title}
    if no_of_songs:
        album['no of songs']=no_of_songs
    return album

album_1=make_album("arijit",'meharma')
album_2=make_album("kk",'labo ko')
album_3=make_album('local train','yellow diary',5)

print(album_1)
print(album_2)
print(album_3)