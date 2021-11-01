from django.views.generic import FormView # Importando recursos form.
from django.urls import reverse_lazy # Para redirecionar para outra página.
from django.contrib import messages # Para mensagens de erros ou sucesso.

from .models import Servico, Funcionario
from .forms import ContatoForm # Importando o form.

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm # Informa qual é o form para essa view.
    success_url = reverse_lazy('index') # Redireciona pra o index em caso de sucesso.

    # Função que armazena dados no contexto pra o template.
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs) # Recupera todo o contexto passado em algum momento.
        context['servicos'] = Servico.objects.order_by('?').all() # Retorna todos, ordenando aleatoriamente.
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

    # Valida o formulário. Executa depois de submeter.
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # Caso o formulário seja inválido.
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
