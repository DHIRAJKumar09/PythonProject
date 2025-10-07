from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from .forms import PlayerForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
# TO read the data from the database
def player_list(request):
    players = Player.objects.all();
    return render(request, "player_list.html",{"players":players});


#create -- add new player
def player_create(request):
    if request.method == "POST":
        form = PlayerForm(request.POST);
        if form.is_valid():
            form.save();
            return redirect("player_list");
    else:
        form = PlayerForm();
    return render(request,'player_form.html',{"form":form});

#update -- edit player
def player_update(request,pk):
    player = get_object_or_404(Player,pk=pk);
    if request.method == "POST":
        form = PlayerForm(request.POST,instance =player);
        if form.is_valid():
            form.save();
            return redirect("player_list");
    else:
        form = PlayerForm(instance=player);
    return render(request,'player_form.html',{"form":form});

def player_delete(request,pk):
    player = get_object_or_404(Player,pk=pk);
    if request.method == "POST":
        player.delete();
        return redirect("player_list");
    return render(request,'player_confirm_delete.html',{"player":player});

