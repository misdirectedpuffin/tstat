from datetime import date
from django.db import models
from django.template.defaultfilters import slugify

class Subject(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.name


    def slugify(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(u'%s %s') % (self.name)
        super(Subject, self).save(*args, **kwargs)

class TeacherSubjectRelationship(models.Model):
    """ Class/course taught, which has a level. """

    class Meta:
        verbose_name = 'Course'

    def __str__(self):
        return '%s %s' % (self.level, self.subject)


    LEVELS = (
            ('Credit', 'Credit'),
            ('General', 'General'),
            ('Foundation', 'Foundation'),
        )
    level = models.CharField(max_length=30, choices=LEVELS)
    subject = models.ForeignKey('Subject')
    teacher = models.ForeignKey('Teacher', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.level, self.subject, self.teacher)

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    subjects = models.ManyToManyField(Subject, blank=True, null=True, through='TeacherSubjectRelationship')
    slug = models.SlugField()

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


    def slugify(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(u'%s %s') % (self.first_name, self.last_name)
        super(Teacher, self).save(*args, **kwargs)


class Pupil(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True)
    number = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    def slugify(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(u'%s %s') % self.first_name, self.last_name
        super(Pupil, self).save(*args, **kwargs)


class Assignment(models.Model):
    pupils = models.ManyToManyField(Pupil, through='AssignmentPupilRelationship')
    title = models.CharField(max_length=50)
    date_assigned = models.DateField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    slug = models.SlugField()
    course = models.ForeignKey('TeacherSubjectRelationship')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def slugify(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(u'%s') % self.title
        super(Assignment, self).save(*args, **kwargs)


class AssignmentPupilRelationship(models.Model):

    """ Grade """

    class Meta:
        verbose_name='Grade'

    pupil = models.ForeignKey(Pupil)
    assignment = models.ForeignKey(Assignment)
    grade = models.CharField(max_length=3, blank=True, null=True)
    date_submitted = models.DateField(blank=True, null=True)

    def __str__(self):
        return u'%s' % self.grade

    @property
    def submitted(self):
        return True if self.date_submitted else False

    @property
    def late_submission(self):
        if self.date_submitted:
            return self.date_submitted > self.assignment.date_due

    @property
    def assignment_overdue(self):
        return all([
            not self.submitted, 
            date.today() > self.assignment.date_due
            ])
