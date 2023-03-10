# Generated by Django 3.2.8 on 2023-03-04 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cargo', models.CharField(choices=[('me', 'Médico(a)'), ('ax', 'Auxiliar de limpeza'), ('re', 'Recepcionista'), ('as', 'Assistente')], max_length=2, verbose_name='Cargo')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=8, unique=True, verbose_name='RG')),
                ('estado_civil', models.CharField(choices=[('s', 'Solteiro(a)'), ('c', 'Casado(a)'), ('d', 'Divorciado(a)'), ('v', 'Viúvo(a)')], max_length=1, verbose_name='Estado civil')),
                ('nascimento', models.DateField(verbose_name='Data de Nasc.')),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('o', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=10, verbose_name='Nº')),
                ('complemento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('uf', models.CharField(choices=[('ac', 'Acre'), ('al', 'Alagoas'), ('ap', 'Amapá'), ('am', 'Amazonas'), ('ba', 'Bahia'), ('ce', 'Ceará'), ('df', 'Distrito Federal'), ('es', 'Espírito Santo'), ('go', 'Goiás'), ('ma', 'Maranhão'), ('mt', 'Mato Grosso'), ('ms', 'Mato Grosso do Sul'), ('mg', 'Minas Gerais'), ('pa', 'Pará'), ('pb', 'Paraíba'), ('pr', 'Paraná'), ('pe', 'Pernambuco'), ('pi', 'Piauí'), ('rj', 'Rio de Janeiro'), ('rn', 'Rio Grande do Norte'), ('rs', 'Rio Grande do Sul'), ('ro', 'Rondônia'), ('rr', 'Roraima'), ('sc', 'Santa Catarina'), ('sp', 'São Paulo'), ('se', 'Sergipe'), ('to', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('telefone_res', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone residencial')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('observacoes', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('medico', models.CharField(max_length=100, verbose_name='Médico')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('paciente', models.CharField(max_length=100, verbose_name='Paciente')),
                ('profissao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Profissão')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('estado_civil', models.CharField(choices=[('s', 'Solteiro(a)'), ('c', 'Casado(a)'), ('d', 'Divorciado(a)'), ('v', 'Viúvo(a)')], max_length=1, verbose_name='Estado civil')),
                ('nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('o', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=10, verbose_name='Nº')),
                ('complemento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('uf', models.CharField(choices=[('ac', 'Acre'), ('al', 'Alagoas'), ('ap', 'Amapá'), ('am', 'Amazonas'), ('ba', 'Bahia'), ('ce', 'Ceará'), ('df', 'Distrito Federal'), ('es', 'Espírito Santo'), ('go', 'Goiás'), ('ma', 'Maranhão'), ('mt', 'Mato Grosso'), ('ms', 'Mato Grosso do Sul'), ('mg', 'Minas Gerais'), ('pa', 'Pará'), ('pb', 'Paraíba'), ('pr', 'Paraná'), ('pe', 'Pernambuco'), ('pi', 'Piauí'), ('rj', 'Rio de Janeiro'), ('rn', 'Rio Grande do Norte'), ('rs', 'Rio Grande do Sul'), ('ro', 'Rondônia'), ('rr', 'Roraima'), ('sc', 'Santa Catarina'), ('sp', 'São Paulo'), ('se', 'Sergipe'), ('to', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('telefone_res', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone residencial')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('sus', models.CharField(max_length=15, unique=True, verbose_name='Número do cartão SUS')),
                ('observacoes', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observações')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.medico', verbose_name='Médico do paciente')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
