from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from nucleo.models import Colaborador


@require_GET
def home(req):
    colaboradores = Colaborador.objects.all()
    return render(req, 'nucleo/index.html', {
        'colaboradores': colaboradores,
    })


@require_http_methods(["GET", "POST"])
def colaborador(req):
    if req.method == "GET":
        return render(req, 'nucleo/forms/criar.html')

    nome = req.POST.get('nome')
    if not nome:
        return redirect('nucleo-colaborador')

    telefone = req.POST.get('telefone')
    Colaborador.objects.create(
        nome=nome,
        telefone=telefone,
    )
    return redirect('nucleo-inicial')


@require_GET
def tela_editar(req, id):
    colaborador = Colaborador.objects.get(id=id)

    if colaborador is None:
        return redirect('nucleo-colaborador')

    return render(req, 'nucleo/forms/editar.html', {
        "colaborador": colaborador
    })


@require_POST
def atualizar(req, id):
    colaborador = Colaborador.objects.get(id=id)

    if colaborador is None:
        return redirect('nucleo-inicial')

    nome = req.POST.get('nome')

    if nome is None:
        return redirect('nucleo-editar', colaborador)

    telefone = req.POST.get('telefone')

    colaborador.nome = nome
    colaborador.telefone = telefone
    colaborador.save()

    return redirect('nucleo-inicial')