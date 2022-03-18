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
        Question_Number = self.cleaned_data.get('Question_Number')

        if Question_Number <= 0:
            raise forms.ValidationError("Question Number should be greater than 0")


        Variable_Occurance = TextQuestion.objects.filter(Document=Document_id,Variable=Variable)
        Question_Number_Occurance = TextQuestion.objects.filter(Document=Document_id,Question_Number=Question_Number)

        if Variable[0] != "$":
            raise forms.ValidationError("Variable Name Should Start with $")
        insert = self.instance.pk == None

        # if creating object for the first time
        if insert:
            if len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
            if len(Question_Number_Occurance) == 1:
                raise forms.ValidationError("Enter Question Number that is unqiue for this Document")
        else: # if updating the object
            TextQuestionObj = TextQuestion.objects.get(id=self.instance.pk)
            # if user doesn't changed the question number and variable then nothing just pass
            if TextQuestionObj.Variable == Variable:
                pass
            elif len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
            if TextQuestionObj.Question_Number == Question_Number:
                pass
            elif len(Question_Number_Occurance) == 1:
                raise forms.ValidationError("Enter Question Number that is unqiue for this Document")
            
        return self.cleaned_data

@admin.register(TextQuestion)
class TextQuestionAdmin(admin.ModelAdmin):
    save_as = True
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
        Question_Number = self.cleaned_data.get('Question_Number')

        if Question_Number <= 0:
            raise forms.ValidationError("Question Number should be greater than 0")
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
    save_as = True
    form = ConditionalQuestionForm
    pass

class BooleanQuestionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BooleanQuestionForm, self).__init__(*args, **kwargs)
        self.fields['Variable'].help_text = "Variable Name Should Start with $"

    class Meta:
        model = BooleanQuestion
        exclude = ()

    def clean(self):
        Variable = self.cleaned_data.get('Variable')
        Document_id = self.cleaned_data.get('Document').id
        Question_Number = self.cleaned_data.get('Question_Number')

        if Question_Number <= 0:
            raise forms.ValidationError("Question Number should be greater than 0")
        Variable_Occurance = BooleanQuestion.objects.filter(Document=Document_id,Variable=Variable)

        if Variable[0] != "$":
            raise forms.ValidationError("Variable Name Should Start with $")
        insert = self.instance.pk == None
        if insert:
            if len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        else:
            BooleanQuestionObj = BooleanQuestion.objects.get(id=self.instance.pk)
            if BooleanQuestionObj.Variable == Variable:
                pass
            elif len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        return self.cleaned_data

@admin.register(BooleanQuestion)
class BooleanQuestionAdmin(admin.ModelAdmin):
    save_as = True
    form = BooleanQuestionForm
    pass

class DateQuestionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(DateQuestionForm, self).__init__(*args, **kwargs)
        self.fields['Variable'].help_text = "Variable Name Should Start with $"

    class Meta:
        model = ConditionalQuestion
        exclude = ()

    def clean(self):
        Variable = self.cleaned_data.get('Variable')
        Document_id = self.cleaned_data.get('Document').id
        Question_Number = self.cleaned_data.get('Question_Number')

        if Question_Number <= 0:
            raise forms.ValidationError("Question Number should be greater than 0")
        Variable_Occurance = DateQuestion.objects.filter(Document=Document_id,Variable=Variable)

        if Variable[0] != "$":
            raise forms.ValidationError("Variable Name Should Start with $")
        insert = self.instance.pk == None
        if insert:
            if len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        else:
            DateQuestionObj = DateQuestion.objects.get(id=self.instance.pk)
            if DateQuestionObj.Variable == Variable:
                pass
            elif len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        return self.cleaned_data

@admin.register(DateQuestion)
class DateQuestionAdmin(admin.ModelAdmin):
    save_as = True
    form = DateQuestionForm
    pass


class OptionalQuestionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(OptionalQuestionForm, self).__init__(*args, **kwargs)
        self.fields['Variable'].help_text = "Variable Name Should Start with $"

    class Meta:
        model = OptionalQuestion
        exclude = ()

    def clean(self):
        Variable = self.cleaned_data.get('Variable')
        Document_id = self.cleaned_data.get('Document').id
        Question_Number = self.cleaned_data.get('Question_Number')

        if Question_Number <= 0:
            raise forms.ValidationError("Question Number should be greater than 0")
        Variable_Occurance = OptionalQuestion.objects.filter(Document=Document_id,Variable=Variable)

        if Variable[0] != "$":
            raise forms.ValidationError("Variable Name Should Start with $")
        insert = self.instance.pk == None
        if insert:
            if len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        else:
            OptionalQuestionObj = OptionalQuestion.objects.get(id=self.instance.pk)
            if OptionalQuestionObj.Variable == Variable:
                pass
            elif len(Variable_Occurance) == 1:
                raise forms.ValidationError("Enter Variable Name that is unqiue for this Document")
        return self.cleaned_data

@admin.register(OptionalQuestion)
class OptionalQuestionAdmin(admin.ModelAdmin):
    save_as = True
    form = OptionalQuestionForm
    pass

@admin.register(AddressQuestion)
class AddressQuestionAdmin(admin.ModelAdmin):
    save_as = True
    pass