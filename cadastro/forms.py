from django.forms import ModelForm
from django import forms
from cadastro.models import Funcionario, Medico, Paciente

class FuncionarioFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FuncionarioFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['rg'].widget.attrs['class'] = 'mask-rg'
        self.fields['nascimento'].widget.attrs['class'] = 'mask-nascimento'
        self.fields['numero'].widget.attrs['class'] = 'mask-numero'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'
        self.fields['telefone_res'].widget.attrs['class'] = 'mask-telefone_res'
        self.fields['celular'].widget.attrs['class'] = 'mask-celular'


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacienteFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['nascimento'].widget.attrs['class'] = 'mask-nascimento'
        self.fields['numero'].widget.attrs['class'] = 'mask-numero'
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'
        self.fields['telefone_res'].widget.attrs['class'] = 'mask-telefone_res'
        self.fields['celular'].widget.attrs['class'] = 'mask-celular'
        self.fields['sus'].widget.attrs['class'] = 'mask-sus'