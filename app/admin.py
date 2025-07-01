from django.contrib import admin
from .models import *

class MembroEquipeInline(admin.TabularInline):
    model = MembroEquipe
    extra = 1

class JogoPlataformaInline(admin.TabularInline):
    model = Jogo_Plataforma
    extra = 1

class CenarioAssetInline(admin.TabularInline):
    model = Cenario_Asset
    extra = 1

class AlocacaoInline(admin.TabularInline):
    model = Alocacao
    extra = 1

class EtapaDesenvolvimentoInline(admin.TabularInline):
    model = EtapaDesenvolvimento
    extra = 1

class TarefaInline(admin.TabularInline):
    model = Tarefa
    extra = 1

class AssetDigitalInline(admin.TabularInline):
    model = AssetDigital
    extra = 1

class EstudioDesenvolvimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'telefone', 'cidade', 'email')
    search_fields = ('nome',)
    inlines = [MembroEquipeInline]

class JogoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'data_lancamento', 'estudio')
    search_fields = ('titulo',)
    inlines = [JogoPlataformaInline, EtapaDesenvolvimentoInline, AssetDigitalInline, AlocacaoInline]

class CenarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'jogo')
    search_fields = ('nome',)
    inlines = [CenarioAssetInline]

class MembroEquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'funcao', 'cidade', 'telefone', 'data_admissao')
    search_fields = ('nome', 'email')

admin.site.register(Funcao)
admin.site.register(TurnoTrabalho)
admin.site.register(TipoAnalise)
admin.site.register(Cidade)
admin.site.register(PlataformaJogo)
admin.site.register(EstudioDesenvolvimento, EstudioDesenvolvimentoAdmin)
admin.site.register(MembroEquipe, MembroEquipeAdmin)
admin.site.register(Jogo, JogoAdmin)
admin.site.register(EtapaDesenvolvimento)
admin.site.register(Tarefa)
admin.site.register(TarefaDetalhe)
admin.site.register(ComponenteProjetoJogo)
admin.site.register(AssetDigital)
admin.site.register(Cenario, CenarioAdmin)
admin.site.register(Ocorrencia)
admin.site.register(AnaliseProcesso)
admin.site.register(UsuarioSistema)
admin.site.register(ConfiguracaoSistema)
