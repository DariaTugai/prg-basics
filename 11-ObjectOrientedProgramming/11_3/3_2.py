# class definition
class Song():
   def __init__(self,name,song,album,year):
      self.name = name
      self.song= song
      self.album = album
      self.year = year

   def __str__(self):
      return f'Performer: {self.name}\nTitle: {self.song}\nAlbum: {self.album}\nYear: {self.year}'
      

# object creation
song1 = Song('Ed Sheeran','Hearts Don\'t Break Around Here','Divide',2017)
song2 = Song('Queen','Bohemian Rhapsody','A Night at the Opera',1975)

## object usage
print(song1)
print('')
print(song2)