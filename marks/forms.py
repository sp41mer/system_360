from django import forms

from marks.models import Weight, ProfessionalismMark, LeadershipMark, TeamworkMark, ControlMark, CommunicationMark, \
    ClientOrientationMark, EfficiencyMark, EvolutionMark

EXCLUDE_FIELDS = ['who_rated', 'rated_user', 'sum_of_all']


class StyleClass(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StyleClass, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'scoring-card__row__input'})


class WeightCreateForm(StyleClass):
    class Meta:
        model = Weight
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class ProfessionalismMarkCreateForm(StyleClass):
    class Meta:
        model = ProfessionalismMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class ControlMarkCreateForm(StyleClass):
    class Meta:
        model = ControlMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class CommunicationMarkCreateForm(StyleClass):
    class Meta:
        model = CommunicationMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class ClientOrientationMarkCreateForm(StyleClass):
    class Meta:
        model = ClientOrientationMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class EfficiencyMarkCreateForm(StyleClass):
    class Meta:
        model = EfficiencyMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class EvolutionMarkCreateForm(StyleClass):
    class Meta:
        model = EvolutionMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class LeadershipMarkCreateForm(StyleClass):
    class Meta:
        model = LeadershipMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


class TeamworkMarkCreateForm(StyleClass):
    class Meta:
        model = TeamworkMark
        exclude = EXCLUDE_FIELDS
        fields = '__all__'


