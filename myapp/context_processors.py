from django.contrib.auth.decorators import login_required
from myapp.models import Project

def toolbar_context_processor(request):
    if request.user.is_authenticated():
        projects = Project.objects.filter(user=request.user)[:3]
    else:
        projects = None
    return {'projects': projects}
