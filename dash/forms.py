from django import forms
from dash.models import AssignmentPupilRelationship, Assignment, Teacher
from django.forms.widgets import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import StrictButton, FormActions, InlineField


class AssignmentForm(forms.ModelForm):
    
    start_date = forms.DateField()
    end_date = forms.DateField()

    class Meta:
        model = Assignment
        fields = ['pupils', 'start_date', 'end_date']
    
    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-assignmentForm'
        self.helper.form_method = 'POST'
        self.helper.form_action = '/homework/'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            InlineField('pupils', id="pupil-field", css_class="form-control", type="select"),
            InlineField('start_date', id="start-date-field", css_class="datepicker form-control"),
            InlineField('end_date', id="end-date-field", css_class="datepicker form-control"),
            StrictButton('Submit', css_class='btn-default', type='input'),
        )
