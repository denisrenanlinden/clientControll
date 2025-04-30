from django.shortcuts import render, get_object_or_404
from .models import Client, AdressInfo

def formatCpf(cpf):
    CPF = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    return CPF

def index(request):
    clients = Client.objects.all().order_by('name')
    adress = AdressInfo.objects.all()

    dados = {
        'clients': clients,
        'adress': adress
    }

    return render(request, "client/index.html", dados)

def client_details(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    formatted_client = {
        'client': client,
        'cpf_formatted': formatCpf(client.cpf)
    }
    return render(request, 'client/client_details.html', formatted_client)
