from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.messages.api import success
from django.views.generic import CreateView, FormView
from django.http import HttpRequest, HttpResponseNotFound, request
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Like, Ordinateur, Categorie, Message, Admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import OrdiForm, CreerUtilisateur, AdminLoginForm


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('accueil')
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Utilisateur non existant')      
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                messages.success(request, 'bienvenue Administrateur !')
            else:
                messages.success(request, 'login avec success !')
            return redirect('/')
        else:
            messages.error(request, 'Utilisateur ou mot de passe incorrect !')
    
    
    context = {'page':page}
    return render(request, 'projet/connexion.html', context)


def logout_page(request):
    logout(request)
    return redirect('accueil')


def enregistrer(request):
    form = CreerUtilisateur(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        messages.success(request, 'enregistrement reussi Bienvenue!')
        return redirect('/')
    else:
        messages.error(request, "erreur lors de l'enregistrement !")
    context = {'form':form}
    return render(request, 'projet/connexion.html', context)


def accueil(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' 
    ordinateur = Ordinateur.objects.filter(
        Q(categorie__nom__icontains=q) |
        Q(nom__icontains=q) |
        Q(prix__icontains=q)  |
        Q(description__icontains=q)|
        Q(marque__icontains=q)
    )
    categories = Categorie.objects.all()
    context = {'ordinateur':ordinateur, 'categories':categories}
    return render(request, 'projet/accueil.html', context)


@login_required(login_url='login')
def suppri_mess(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("vous n'etes pas autorise")
    if request.method=='POST':
        message.delete()
        return redirect('accueil')
    context = {'obj':message}
    return render(request, 'projet/supprimer.html', context)


def detail_pc(request, pk):
    ordi = Ordinateur.objects.get(id=pk)
    user = request.user
    message_ordi = ordi.message_set.all().order_by('-creation')
    if request.method == 'POST':
        message = Message.objects.create(
            utilisateur = request.user,
            ordi=ordi,
            corps=request.POST.get('corps')
        )
        return redirect('ordi', pk=ordi.id)
    
    
    
    # liketotal = likestotal
    context = {'ordi':ordi, 'message':message_ordi, 'user':user}# , 'liketotal': liketotal}
    return render(request, 'projet/detailspc.html', context)


@login_required(login_url='login')
def like(request):
    user = request.user
    if request.method =='POST':
        id_post = request.POST.get('pc_id')
        post_obj = Ordinateur.objects.get(id=id_post)
        
        if user in post_obj.likesO.all():
            post_obj.likesO.remove(user)
        else:
            post_obj.likesO.add(user)
            
        like, creation = Like.objects.get_or_create(user=user, post_id=id_post)
        
        if not creation:
            if like.valeur== 'Like':
                like.valeur ='Unlike'
            else:
                like.valeur= 'Like'
        like.save()
    return render(request, 'projet/detailspc.html')


# admin

class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/login-admin/')
        return super().dispatch(request, *args, **kwargs)


class AdminLogin(FormView):
    template_name = "loginadmin.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("projet:ajouter_art")
    
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        context = {"form":self.form_class, "error": "Invalid credentials"}
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self, request, usr)
        else:
            return render(self.request, self.template_name, context)
        return super().form_valid(form)
    
    
class CreateView(AdminRequiredMixin, CreateView):
    template_name = "projet/ajouter_art.html"
    form_class = OrdiForm
    success_url = reverse_lazy('/')
  
@login_required(login_url='login')    
def ajouter_art(request):
    if not request.user.is_superuser:
        return HttpResponseNotFound("Vous n'etes pas autorisé ici, seuls les Admin!")
    else:
        form = OrdiForm()
        categories = Categorie.objects.all()
        if request.method=="POST":
            data = request.POST
            form = OrdiForm(request.POST)
            if form.is_valid():
                ordi = form.save(commit=False)
                ordi.createur = request.user
                ordi = Ordinateur.objects.create(
                        marque=data['marque'],
                        nom=data['nom'],
                        prix=data['prix'],
                        categorie=Categorie.objects.get(id=data['categorie']),
                        description=data['description'],
                        photo=request.FILES.get('photo')
                    )
                ordi.save()
                messages.warning(request, "Produit Ajoute avec succes !")
                return redirect('/')
        context = {'form':form, 'categories':categories}
        return render(request, 'projet/ajout_art.html', context)
