from django.shortcuts import render
from dash.models import Pupil, Assignment
from dash.models import AssignmentPupilRelationship as Grade
from dash.forms import AssignmentForm
from django.forms.models import inlineformset_factory

def homework(request):
    assignment_form = AssignmentForm(request.POST)

    if request.method == 'POST':

        if assignment_form.is_valid():
            pupils = assignment_form.cleaned_data['pupils'] # returns pupil obj.
            start_date = assignment_form.cleaned_data['start_date']
            end_date = assignment_form.cleaned_data['end_date']
            
            assignment_group = []
            for pupil in pupils:
                

                assignments = Assignment.objects.filter(
                    pupils__pk=pupil.id,
                    date_due__gte=start_date,
                    date_due__lte=end_date
                    ).order_by('course__teacher__last_name')
                pupil_name = pupil.first_name + ' ' + pupil.last_name
                assignment_group.append({pupil_name: assignments})
                # import pdb; pdb.set_trace()


            return render(
                request, 'homework.html', {
                    'assignment_form': assignment_form,
                    'assignment_group': assignment_group,
                    
                })

        return render(request, 'homework.html', {
            'assignment_form': assignment_form,
        })
    assignment_form = AssignmentForm()
    return render(request, 'homework.html', {
        'assignment_form': assignment_form,
    })
