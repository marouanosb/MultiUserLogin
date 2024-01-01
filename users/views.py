from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def homepage(request):
    return render(request, 'users/homepage.html')

@login_required
@permission_required('users.view_cours')    #   Seulement ceux autorisés peuvent voir les cours
def cours(request):
    return render(request, 'users/cours.html')

@login_required
@permission_required('users.view_rapport')  #   Seulement ceux autorisés peuvent voir les rapports
def rapports(request):
    return render(request, 'users/rapports.html')
