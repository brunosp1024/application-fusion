from stdimage.models import StdImageField
from django.db import models
import uuid # Usado para gerar nomes aleatórios para arquivos de upload.


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1] # retorna a extensão do arquivo (png, jpg...)
    filename = f'{uuid.uuid4()}.{ext}' # gera um nome aleatório para o arquivo.
    return filename


class Base(models.Model): # Classe base para todos os models.
    criados = models.DateField('Criação', auto_now_add=True) # Define a data automaticamente.
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True # Define a classe como abstrata.


class Servico(Base):
    # Choices para preencher um campo select.
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'), # Chave e valor.
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100) # string com até 100 caracteres.
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES) # É preenchido com a choices.

    class Meta:
        verbose_name = 'Serviço' # Define o nome do modelo no singular.
        verbose_name_plural = 'Serviços' # Define o nome do modelo no plural.

    def __str__(self):
        return self.servico # Cada registro será exibido com o nome definido no serviço.


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE) # Campo associado a classe cargo.
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}) # tamanho padrão definido pra imagem.
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome
