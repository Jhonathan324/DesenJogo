from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('geral/', GeralView.as_view(), name='geral'),

    # Jogo e Relacionados
    path('jogos/', JogosView.as_view(), name='jogos'),
    path('jogos/delete/<int:id>/', DeleteJogoView.as_view(), name='delete_jogo'),
    path('jogos/editar/<int:id>/', EditarJogoView.as_view(), name='editar_jogo'),

    path('plataformas/', PlataformasView.as_view(), name='plataformas'),
    path('jogo_plataformas/', JogoPlataformaView.as_view(), name='jogo_plataformas'),

    # Estúdio, Cidades e Equipe
    path('estudios/', EstudioView.as_view(), name='estudios'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('membros/', MembrosView.as_view(), name='membros'),
    path('funcoes/', FuncoesView.as_view(), name='funcoes'),

    # Alocação e Desenvolvimento
    path('alocacoes/', AlocacoesView.as_view(), name='alocacoes'),
    path('etapas/', EtapasView.as_view(), name='etapas'),
    path('tarefas/', TarefasView.as_view(), name='tarefas'),
    path('detalhes_tarefas/', TarefaDetalheView.as_view(), name='detalhes_tarefas'),
    path('componentes/', ComponentesView.as_view(), name='componentes'),
    path('turnos/', TurnosView.as_view(), name='turnos'),

    # Cenários e Assets
    path('cenarios/', CenariosView.as_view(), name='cenarios'),
    path('assets/', AssetsView.as_view(), name='assets'),
    path('cenarios_assets/', CenarioAssetView.as_view(), name='relacoes'),

    # Análises e Ocorrências
    path('tipos_analise/', TiposAnaliseView.as_view(), name='tipos_analise'),
    path('analise_processos/', FormulariosView.as_view(), name='analise_processos'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),

    # Sistema
    path('usuarios/', UsuariosSistemaView.as_view(), name='usuarios'),
    path('configuracoes/', ConfiguracoesSistemaView.as_view(), name='configuracoes'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
