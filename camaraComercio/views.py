from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def inicioCurso(request):
    url_angular = 'http://localhost:4200/inicioCurso'
    return redirect(url_angular)
