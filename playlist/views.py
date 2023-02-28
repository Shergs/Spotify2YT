from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.http import HttpResponse
import os
import shutil
from django.conf import settings
from .models import Use,Playlist
from django.core import serializers

#playlistname=["default"]
#username=[""]

class newPlaylistForm(forms.Form):
    playlist=forms.CharField(label="Playlist Link", widget=forms.TextInput(attrs={'class':'new__input','placeholder': 'Playlist Link'}))
    
    #label="Playlist Link",
    #label="PlaylistNameENG",
    #remove from here
    #name=forms.CharField(label="Your Name")
    #clientID=forms.CharField(label="Client ID")
    #clientSecret=forms.CharField(label="Client Secret")
    #to here
    playlistENG=forms.CharField(label="Playlist Name", widget=forms.TextInput(attrs={'class':'new__input','placeholder': 'Playlist Name'}))

# Create your views here.
def index(request):
    if "playlistname" not in request.session:
        request.session["playlistname"]=["default"]
    #remove from here
   # if "username" not in request.session:
   #     request.session["username"]=[""]
   # if "clientID" not in request.session:
   #     request.session["clientID"]=[""]
   # if "clientSecret" not in request.session:
   #     request.session["clientSecret"]=[""]
    #to here
    if "playlistENG" not in request.session:
        request.session["playlistENG"]=[""]
    
    last_ten = Playlist.objects.all().order_by('-id')[:10]
    return render(request,"playlist/index.html",{
        "playlistname":request.session["playlistname"],
        "playlistENG":request.session["playlistENG"],
        "playlistListed":last_ten
    })

def add(request):
    if request.method=="POST":
        form=newPlaylistForm(request.POST)
        if form.is_valid():
            newPlaylist=form.cleaned_data["playlist"]
            temp=newPlaylist
            #parse the url here for the uri. then set newPlaylist to that string
            if "playlist" in newPlaylist:
                newPlaylist=newPlaylist.split("playlist/",1)[1]
                newPlaylist=newPlaylist.split("?",1)[0]
            #if "album" in newPlaylist:
                #newPlaylist=newPlaylist.split("album/",1)[1]
                #newPlaylist=newPlaylist.split("?",1)[0]
            request.session["playlistname"]=[newPlaylist]


            #remove from here
          #  newname=form.cleaned_data["name"]
          #  request.session["username"]=[newname]
          #  newCID=form.cleaned_data["clientID"]
          #  request.session["clientID"]=[newCID]
          #  newCS=form.cleaned_data["clientSecret"]
          #  request.session["clientSecret"]=[newCS]
            #to here

            playENG=form.cleaned_data["playlistENG"]
            request.session["playlistENG"]=[playENG]

            #username=1245041861
            #clientID=98bef7ae82bb43c3aed3a6090278b930
            #clientsecret=7fe0a4d0d57c41878f9e119c902a7072
            
            #print(f"webBack/playlist/spotifytomp32/spotify_to_mp3.py {newCID} {newCS} {newname} {newPlaylist}")


            #call with hard coded ClientID ClientSecret and Username
            #os.system(f"python C:/Users/sherg/OneDrive/Documents/TestProject/webBack/playlist/spotifytomp32/spotify_to_mp3.py {newCID} {newCS} {newname} {newPlaylist}")
            os.system(f"python C:/Users/sherg/OneDrive/Documents/TestProject/webBack/playlist/spotifytomp32/spotify_to_mp3.py 98bef7ae82bb43c3aed3a6090278b930 7fe0a4d0d57c41878f9e119c902a7072 1245041861 {newPlaylist}")
            
            #make this work with other playlistENG names DONE
            shutil.make_archive('playlist/zipPlaylist','zip', f'C:/Users/sherg/OneDrive/Documents/TestProject/webBack/{playENG}')



            ###insert or add to existing python script, to grab the playlist picture.
            ###insert database add here, insert into playlist model, the playlist name and the playlist link
            playlistData=Playlist()
            playlistData.playName=playENG
            playlistData.playUri=temp
            if request.user.is_authenticated:
                playlistData.use=request.user.username
            playlistData.save()

            #Clean up txt file and the folder after. os.remove for txt file and os.rmdir for folder
            shutil.rmtree(f'{playENG}', ignore_errors=True)

            #print("COMPLETED ALL OPERATIONS!",request.session["playlistname"],request.session["username"],request.session["clientID"],request.session["clientSecret"])
            #i=Playlist.objects.all().count()
            last_ten = Playlist.objects.all().order_by('-id')[:10]
            #last_ten_in_ascending_order = reversed(last_ten)
            last_ten_in_ascending_order=last_ten
            #return HttpResponseRedirect(reverse("playlist:index"))
            #request.session['recent']=serializers.serialize("xml",last_ten)
            #request.session['recent']=last_ten.values_list('id')
            #x=last_ten
            return redirect('playlist:index')

          #  return render(request,"playlist/index.html",{
           #     #"playlistsListed":Playlist.objects.all()
           #     #"playlistsListed":Playlist.objects.filter(id_gte=(i-10))
           #     "playlistsListed":last_ten_in_ascending_order
           # })
            
        else:
            return render(request, "playlist/add.html",{
                "form":form
            })
    return render(request, "playlist/add.html",{
        "form": newPlaylistForm()
    })



def download(request,filename):
    file_path=os.path.join(settings.MEDIA_ROOT,f"playlist/{filename}")
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/zip")
            response['Content-Disposition']='inline; filename='+os.path.basename(file_path)
            return response
    raise Http404