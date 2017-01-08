from django.contrib import admin

from marks.models import Weight, ProfessionalismMark, ControlMark, CommunicationMark, ClientOrientationMark, \
    EfficiencyMark, EvolutionMark, LeadershipMark, TeamworkMark

admin.site.register(Weight)
admin.site.register(ProfessionalismMark)
admin.site.register(ControlMark)
admin.site.register(CommunicationMark)
admin.site.register(ClientOrientationMark)
admin.site.register(EfficiencyMark)
admin.site.register(EvolutionMark)
admin.site.register(LeadershipMark)
admin.site.register(TeamworkMark)

