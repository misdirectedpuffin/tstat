from django.contrib import admin
from dash.models import Pupil, Assignment, Teacher, Subject
from dash.models import AssignmentPupilRelationship as Grade
from dash.models import TeacherSubjectRelationship as Course

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'slug')
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    filter_horizontal = ('subjects'), # Must be a ManyToManyField

class PupilAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'number', 'slug',)
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_assigned',
                    'date_due',)
    filter_horizontal = ('pupils',)
    prepopulated_fields = {'slug': ('title',)}

class GradeAdmin(admin.ModelAdmin):
    list_display = ('pupil', 'assignment', 'grade', 'date_submitted', 'submitted', 'late_submission', 'assignment_overdue')
    # filter_horizontal = ('assignment',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CourseAdmin(admin.ModelAdmin):
    list_display = ('level', 'subject', 'teacher',)
    # prepopulated_fields = {'slug': ('name',)}

admin.site.register(Pupil, PupilAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
