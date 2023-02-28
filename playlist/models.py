from django.db import models

# Create your models here.
#one model for each of the tables
class Use(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)



#model to save the playlist name, uri, and playlist logo
class Playlist(models.Model):
    id=models.AutoField(primary_key=True)
    playName=models.CharField(max_length=120)
    playUri=models.CharField(max_length=240)
    use=models.CharField(max_length=60,default='anon')
    #logo is prob just a link 
    #add logo here

    def __str__(self):
        return f"ID is {self.id} Name is {self.playName}, link is {self.playUri}, username is {self.use}"