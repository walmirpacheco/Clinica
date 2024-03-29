from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from usuarios.forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from usuarios.models import Perfil


class UsuarioCreate(CreateView):
    template_name = "cadastro/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='Visitante')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context

class PerfilUpdate(UpdateView):
    template_name = "cadastro/form.html"
    model = Perfil
    fields = ['nome_completo', 'cpf', 'celular']
    success_url = reverse_lazy('index')
    

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Meus dados pessoais"
        context['botao'] = "Atualizar"

        return context

def alterarSenha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'paginas/index.html')
        else:
            return redirect('index')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form,
        }
        return render(request, 'usuarios/alterarSenha.html', context)