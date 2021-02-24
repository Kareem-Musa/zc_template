from django import forms
from .models import State, Locality, Unity

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(StateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})

class LocalityForm(forms.ModelForm):
    class Meta:
        model = Locality
        fields = ['name', 'state']

    def __init__(self, *args, **kwargs):
        super(LocalityForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['state'].widget.attrs.update({'class':'form-control'})

class UnityForm(forms.ModelForm):
    class Meta:
        model = Unity
        fields = ['name', 'state', 'locality']

    def __init__(self, *args, **kwargs):
        super(UnityForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['state'].widget.attrs.update({'class':'form-control'})
        self.fields['locality'].widget.attrs.update({'class':'form-control'})
