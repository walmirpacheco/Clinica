from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

CARGO_CHOICES =(
    ('me', 'Médico(a)'),
    ('ax', 'Auxiliar de limpeza'),
    ('re', 'Recepcionista'),
    ('as', 'Assistente'),
)

ESTADO_CIVIL_CHOICES = (
    ('s', 'Solteiro(a)'),
    ('c', 'Casado(a)'),
    ('d', 'Divorciado(a)'),
    ('v', 'Viúvo(a)'),    
)

SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('o', 'Outro'),
)

ESTADOS_CHOICES = (
    ('ac', 'Acre'),
    ('al', 'Alagoas'),
    ('ap', 'Amapá'),
    ('am', 'Amazonas'),
    ('ba', 'Bahia'),
    ('ce', 'Ceará'),
    ('df', 'Distrito Federal'),
    ('es', 'Espírito Santo'),
    ('go', 'Goiás'),
    ('ma', 'Maranhão'),
    ('mt', 'Mato Grosso'),
    ('ms', 'Mato Grosso do Sul'),
    ('mg', 'Minas Gerais'),
    ('pa', 'Pará'),
    ('pb', 'Paraíba'),
    ('pr', 'Paraná'),
    ('pe', 'Pernambuco'),
    ('pi', 'Piauí'),
    ('rj', 'Rio de Janeiro'),
    ('rn', 'Rio Grande do Norte'),
    ('rs', 'Rio Grande do Sul'),
    ('ro', 'Rondônia'),
    ('rr', 'Roraima'),
    ('sc', 'Santa Catarina'),
    ('sp', 'São Paulo'),
    ('se', 'Sergipe'),
    ('to', 'Tocantins'),
)

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=2, choices=CARGO_CHOICES)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    rg = models.CharField('RG', max_length=8, unique=True)
    estado_civil = models.CharField('Estado civil', max_length=1, choices=ESTADO_CIVIL_CHOICES)
    nascimento = models.DateField(verbose_name= 'Data de Nasc.')
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)    
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.CharField('Nº', max_length=10)
    complemento = models.CharField('Complemento', max_length=150, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=150)
    cep = models.CharField('CEP', max_length=9)
    uf = models.CharField('UF', max_length=2, choices=ESTADOS_CHOICES)
    cidade = models.CharField('Cidade', max_length=150)
    telefone_res = models.CharField('Telefone residencial', max_length=15, null=True, blank=True)
    celular = models.CharField('Celular', max_length=15)
    observacoes = models.TextField('Observações', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome


class Medico(Base):
    medico = models.CharField('Médico', max_length=100)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return self.medico

class Paciente(Base):    
    paciente = models.CharField('Paciente', max_length=100)
    profissao = models.CharField('Profissão', null=True, blank=True, max_length=50)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    estado_civil = models.CharField('Estado civil', max_length=1, choices=ESTADO_CIVIL_CHOICES)
    nascimento = models.DateField(verbose_name= 'Data de Nascimento')
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)    
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.CharField('Nº', max_length=10)
    complemento = models.CharField('Complemento', max_length=150, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=150)
    cep = models.CharField('CEP', max_length=9)
    uf = models.CharField('UF', max_length=2, choices=ESTADOS_CHOICES)
    cidade = models.CharField('Cidade', max_length=150)
    telefone_res = models.CharField('Telefone residencial', max_length=15, null=True, blank=True)
    celular = models.CharField('Celular', max_length=15)
    sus = models.CharField('Número do cartão SUS', max_length=15, unique=True)
    medico = models.ForeignKey('cadastro.Medico', verbose_name='Médico do paciente', on_delete=models.PROTECT)    
    observacoes = models.TextField('Observações', max_length=300, null=True, blank=True)    

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.paciente