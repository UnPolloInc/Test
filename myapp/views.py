from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from myapp.models import Project, User
from django.views.generic import DetailView, ListView


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class ToolbarContextMixin(object):
  def get_projects(self):
        return Project.objects.filter(user=self.request.user)[:3] if self.request.user.is_authenticated() else None

  def get_context_data(self, **kwargs):
    context = super(ToolbarContextMixin, self).get_context_data(**kwargs)
    context['projects'] = self.get_projects()
    return context

@login_required
def home(request):

    return render(request, 'myapp/home.html', {})

class ProjectDetail(LoginRequiredMixin, ToolbarContextMixin, DetailView):
    model = Project

class ProjectList(LoginRequiredMixin, ToolbarContextMixin, ListView):
    model = Project
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user.id)

@login_required
def user_detail(request, username):
    return render(request, 'myapp/user_detail.html')