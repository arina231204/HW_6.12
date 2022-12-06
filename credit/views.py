
from django.views import generic

from.models import Client, Account, Credit

class IndexView(generic.ListView):
    model = Client
    template_name = 'index.html'
    context_object_name = 'client_list'

class ClientDetailView(generic.DetailView):
    model = Client
    context_object_name = 'client'
    pk_url_kwarg = 'id'

