from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from cadastro.models import Funcionario, Paciente
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"        
    model = Funcionario
    fields = ['nome', 'cargo', 'cpf', 'rg', 'estado_civil', 'nascimento', 'sexo', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'uf', 'cidade', 'telefone_res', 'celular', 'observacoes']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-funcionarios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro do Funcionário"
        context['botao'] = "Cadastrar"

        return context
    

class PacienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Paciente
    fields = ['paciente', 'profissao', 'cpf', 'estado_civil', 'nascimento', 'sexo', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'uf', 'cidade', 'telefone_res', 'celular', 'sus', 'medico', 'observacoes']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-pacientes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro do Paciente"
        context['botao'] = "Cadastrar"
        return context


class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"       
    model = Funcionario
    fields = ['nome', 'cargo', 'cpf', 'rg', 'estado_civil', 'nascimento', 'sexo', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'uf', 'cidade', 'telefone_res', 'celular', 'observacoes'] 
    template_name = 'cadastro/form.html'  
    success_url = reverse_lazy('listar-funcionarios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro do Funcionário"
        context['botao'] = "Salvar"

        return context


class PacienteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"    
    model = Paciente
    fields = ['paciente', 'profissao', 'cpf', 'estado_civil', 'nascimento', 'sexo', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'uf', 'cidade', 'telefone_res', 'celular', 'sus', 'medico', 'observacoes'] 
    template_name = 'cadastro/form.html'  
    success_url = reverse_lazy('listar-pacientes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro do Paciente"
        context['botao'] = "Salvar"

        return context


class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Funcionario
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('listar-funcionarios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Funcionário"        

        return context


class PacienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Paciente
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('listar-pacientes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Paciente"        

        return context


class FuncionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Visitante", u"Administrador"]
    model = Funcionario
    template_name = 'cadastro/listas/funcionario.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Lista de Funcionarios Cadastrados" 

        return context

    def get_queryset(self):

        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            funcionarios = Funcionario.objects.filter(nome__icontains=txt_nome)
        else:
            funcionarios = Funcionario.objects.all()
        
        return funcionarios


class PacienteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Visitante", u"Administrador"]
    model = Paciente
    template_name = 'cadastro/listas/paciente.html'    
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Lista de Pacientes Cadastrados"    

        return context


    def get_queryset(self):

        txt_paciente = self.request.GET.get('paciente')

        if txt_paciente:
            pacientes = Paciente.objects.filter(paciente__icontains=txt_paciente)
        else:
            pacientes = Paciente.objects.all()

        return pacientes