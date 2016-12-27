from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import TemplateView

from marks.forms import WeightCreateForm, ProfessionalismMarkCreateForm, ControlMarkCreateForm, \
    ClientOrientationMarkCreateForm, CommunicationMarkCreateForm, EfficiencyMarkCreateForm, EvolutionMarkCreateForm, \
    TeamworkMarkCreateForm, LeadershipMarkCreateForm
from marks.models import Weight, ClientOrientationMark, ControlMark, CommunicationMark, ProfessionalismMark, \
    EfficiencyMark, EvolutionMark, LeadershipMark, TeamworkMark


class SuccessMixin(CreateView):
    success_url = reverse_lazy("core:test")
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        user_id = self.request.POST.get('user_id', None)
        if user_id:
            form.instance.who_rated = self.request.user
            form.instance.rated_user = User.objects.filter(id=user_id).first()
            return super(SuccessMixin, self).form_valid(form)
        else:
            return ValueError


class WeightCreateView(SuccessMixin):
    model = Weight
    form_class = WeightCreateForm


class ProfessionalismMarkCreateView(SuccessMixin):
    model = ProfessionalismMark
    form_class = ProfessionalismMarkCreateForm


class ControlMarkCreateView(SuccessMixin):
    model = ControlMark
    form_class = ControlMarkCreateForm


class CommunicationMarkCreateView(SuccessMixin):
    model = CommunicationMark
    form_class = CommunicationMarkCreateForm


class ClientOrientationMarkCreateView(SuccessMixin):
    model = ClientOrientationMark
    form_class = ClientOrientationMarkCreateForm


class EfficiencyMarkCreateView(SuccessMixin):
    model = EfficiencyMark
    form_class = EfficiencyMarkCreateForm


class EvolutionMarkCreateView(SuccessMixin):
    model = EvolutionMark
    form_class = EvolutionMarkCreateForm


class LeadershipMarkCreateView(SuccessMixin):
    model = LeadershipMark
    form_class = LeadershipMarkCreateForm


class TeamworkMarkCreateView(SuccessMixin):
    model = TeamworkMark
    form_class = TeamworkMarkCreateForm


class ResultView(TemplateView):
    template_name = 'marks/result_view.html'
    def get_context_data(self, **kwargs):
        res = super(ResultView, self).get_context_data(**kwargs)

        pk = kwargs.get("pk")
        if pk:
            weights = Weight.objects.filter(rated_user=pk)
            professionalism_mark = ProfessionalismMark.objects.filter(rated_user=pk)
            control_mark = ControlMark.objects.filter(rated_user=pk)
            communication_mark = CommunicationMark.objects.filter(rated_user=pk)
            client_orientation_mark = ClientOrientationMark.objects.filter(rated_user=pk)
            efficiency_mark = EfficiencyMark.objects.filter(rated_user=pk)
            evolution_mark = EvolutionMark.objects.filter(rated_user=pk)
            leadership_mark = LeadershipMark.objects.filter(rated_user=pk)
            teamwork_mark = TeamworkMark.objects.filter(rated_user=pk)
            self.prof_kpi = self.calculate_mark(weights.values()[0].get('professionalism'),professionalism_mark.values()[0])
            self.control_kpi = self.calculate_mark(weights.values()[0].get('control'),control_mark.values()[0])
            self.communication_kpi = self.calculate_mark(weights.values()[0].get('communication'),communication_mark.values()[0])
            self.client_orientation_kpi = self.calculate_mark(weights.values()[0].get('client_orientation'),client_orientation_mark.values()[0])
            self.efficeincy_kpi = self.calculate_mark(weights.values()[0].get('efficiency'),efficiency_mark.values()[0])
            self.evolution_kpi = self.calculate_mark(weights.values()[0].get('evolution'),evolution_mark.values()[0])
            self.leadership_kpi = self.calculate_mark(weights.values()[0].get('leader'),leadership_mark.values()[0])
            self.teamwork_kpi = self.calculate_mark(weights.values()[0].get('teamwork'),teamwork_mark.values()[0])

        res.update({
            "prof_kpi": self.prof_kpi,
            "control_kpi": self.control_kpi,
            "communication_kpi": self.communication_kpi,
            "client_orientation_kpi": self.client_orientation_kpi,
            "efficeincy_kpi": self.efficeincy_kpi,
            "evolution_kpi": self.evolution_kpi,
            "leadership_kpi": self.leadership_kpi,
            "teamwork_kpi": self.teamwork_kpi
        })

        return res

    def calculate_mark(self,weight,mark):
        marks_and_weights = weight*((sum(mark.itervalues())-mark.get('rated_user_id')
                       -mark.get('userinheritance_ptr_id')-
                                        mark.get('who_rated_id')-
                                        mark.get('id')))
        max_mark = weight*(len(mark)-4)*10
        kpi = marks_and_weights/float(max_mark)
        return kpi

