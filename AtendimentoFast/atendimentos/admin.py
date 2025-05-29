from django.contrib import admin
from .models import Usuario, Cliente, Servico
from .models import HorarioAtendimento
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UsuarioAdmin(BaseUserAdmin):
    list_display = ('email', 'nome', 'tipo_conta', 'is_staff', 'is_active')
    list_filter = ('tipo_conta', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'senha')}),
        ('Informações pessoais', {'fields': ('nome', 'telefone', 'tipo_conta')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'telefone', 'tipo_conta', 'senha1', 'senha2'),
        }),
    )
    search_fields = ('email', 'nome')
    ordering = ('email',)
    filter_horizontal = ()

@admin.register(HorarioAtendimento)
class HorarioAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'hora_inicio', 'hora_fim', 'ativo')
    list_filter = ('dia_semana', 'ativo')
    ordering = ('dia_semana', 'hora_inicio')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cliente)
admin.site.register(Servico)
