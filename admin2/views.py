from os.path import join

from django.conf import settings
from django.views.generic import ListView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .utils import get_admin2s

ADMIN2_THEME_DIRECTORY = getattr(settings, "ADMIN2_THEME_DIRECTORY", "admin2/bootstrap")


class IndexView(ListView):#(LoginRequiredMixin, StaffuserRequiredMixin, ListView):

    def get_template_names(self):
        return [join(ADMIN2_THEME_DIRECTORY, "index.html")]

    def get_queryset(self):
        return get_admin2s()