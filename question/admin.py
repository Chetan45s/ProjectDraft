from django.contrib import admin
from question.models import *
from django import forms

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

class TextQuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TextQuestionForm, self).__init__(*args, **kwargs)
        self.fields['Variable'].help_text = "Variable Name Should Start with $"

    class Meta:
        model = TextQuestion
        exclude = ()

    def clean(self):
        Variable = self.cleaned_data.get('Variable')
        Document_id = self.cleaned_data.get('Document').id
        Variable_Occurance = TextQuestion.objects.filter(Document=Document_id,Variable=Variable)

        if Variable[0] != "$":
            raise forms.ValidationError("Variable Name Should Start with $")
        insert = self.instance.pk == None
        if insert:
            if len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        else:
            TextQuestionObj = TextQuestion.objects.get(id=self.instance.pk)
            if TextQuestionObj.Variable == Variable:
                pass
            elif len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        return self.cleaned_data

@admin.register(TextQuestion)
class TextQuestionAdmin(admin.ModelAdmin):
    form = TextQuestionForm
    pass

class ConditionalQuestionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ConditionalQuestionForm, self).__init__(*args, **kwargs)
        self.fields['Variable'].help_text = "Variable Name Should Start with $"

    class Meta:
        model = ConditionalQuestion
        exclude = ()

    def clean(self):
        Variable = self.cleaned_data.get('Variable')
        Document_id = self.cleaned_data.get('Document').id
        Variable_Occurance = ConditionalQuestion.objects.filter(Document=Document_id,Variable=Variable)

        if Variable[0] != "$":
            raise forms.ValidationError("Variable Name Should Start with $")
        insert = self.instance.pk == None
        if insert:
            if len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        else:
            ConditionalQuestionObj = ConditionalQuestion.objects.get(id=self.instance.pk)
            if ConditionalQuestionObj.Variable == Variable:
                pass
            elif len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        return self.cleaned_data

@admin.register(ConditionalQuestion)
class ConditionalQuestionAdmin(admin.ModelAdmin):
    form = ConditionalQuestionForm
    pass

@admin.register(BooleanQuestion)
class BooleanQuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(DateQuestion)
class DateQuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(OptionalQuestion)
class OptionalQuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(AddressQuestion)
class AddressQuestionAdmin(admin.ModelAdmin):
    pass