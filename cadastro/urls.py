from django.urls import path

from cadastro.views import FuncionarioCreate, FuncionarioUpdate, PacienteCreate, PacienteUpdate, FuncionarioDelete, PacienteDelete, FuncionarioList, PacienteList

urlpatterns = [
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name='cadastro-funcionario'),
    path('cadastrar/paciente/', PacienteCreate.as_view(), name='cadastro-paciente'),

    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
    path('editar/paciente/<int:pk>/', PacienteUpdate.as_view(), name='editar-paciente'),

    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name='excluir-funcionario'),
    path('excluir/paciente/<int:pk>/', PacienteDelete.as_view(), name='excluir-paciente'),

    path('listar/funcionarios/', FuncionarioList.as_view(), name='listar-funcionarios'),
    path('listar/pacientes/', PacienteList.as_view(), name='listar-pacientes'),
]