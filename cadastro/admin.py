from django.contrib import admin
from cadastro.forms import FuncionarioFormAdmin, PacienteFormAdmin

from cadastro.models import Funcionario, Medico, Paciente

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    form = FuncionarioFormAdmin    
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

    class Media:
        js = (
            "jquery.mask1.min.js",
            "custom.js",
            )
    

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('medico', 'ativo', 'modificado')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    form = PacienteFormAdmin
    list_display = ('paciente', 'medico', 'ativo', 'modificado')

    class Media:
        js = (
            "jquery.mask1.min.js",
            "custom.js",
            )