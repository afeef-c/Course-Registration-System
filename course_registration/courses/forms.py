from django import forms
from .models import Student,Course

class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    course_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        course_id = cleaned_data.get('course_id')
        return cleaned_data



class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'maximum_capacity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'title': 'Course Title',
            'description': 'Course Description',
            'maximum_capacity': 'Maximum Capacity',
        }
