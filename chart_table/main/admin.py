from django.contrib import admin
from main.models import Parkir

class ParkirAdmin(admin.ModelAdmin):
    list_display = ('id_card', 'gate', 'status', 'jam', 'tanggal', 'biaya')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

admin.site.register(Parkir, ParkirAdmin)
