from django.db import models

questionChoice = (
    ('conditional','conditional'),
    ('boolean','boolean'),
    ('text','text'),
    ('date','date'),
)


class Document(models.Model):
    Document_Name = models.CharField(max_length=500)
    Add_File = models.FileField(upload_to='documents')

    def __str__(self):
        return f"{self.Document_Name}"
     
class TextQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question_Number = models.IntegerField(default=0)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$text')
    Double_Quotes = models.BooleanField(default=False)
    Captialize = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

    def getQuestion(self):
        return {
            "Question Number":self.Question_Number,
            "Question":self.Question,
            "Variable":self.Variable,
            "Type":"text"
        }

class ConditionalQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question_Number = models.IntegerField(default=0)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$condition')
    If_Yes = models.TextField()
    If_No = models.TextField()
    Double_Quotes = models.BooleanField(default=False)
    Captialize = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Document.id} {self.Question}"
    
    def getQuestion(self):
        return {
            "Question Number":self.Question_Number,
            "Question":self.Question,
            "Variable":self.Variable,
            "Type":"Conditional"
        }

class BooleanQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question_Number = models.IntegerField(default=0)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$bool')
    Double_Quotes = models.BooleanField(default=False)
    Captialize = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

    def getQuestion(self):
        return {
            "Question Number":self.Question_Number,
            "Question":self.Question,
            "Variable":self.Variable,
            "Type":"Boolean"
        }


class DateQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question_Number = models.IntegerField(default=0)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$date')
    Double_Quotes = models.BooleanField(default=False)
    Captialize = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

    def getQuestion(self):
        return {
            "Question Number":self.Question_Number,
            "Question":self.Question,
            "Variable":self.Variable,
            "Type":"Date"
        }

class OptionalQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question_Number = models.IntegerField(default=0)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$optional')
    Total_Option = models.IntegerField()
    Option_1 = models.CharField(max_length=500,null=True,blank=True)
    Option_2 = models.CharField(max_length=500,null=True,blank=True)
    Option_3 = models.CharField(max_length=500,null=True,blank=True)
    Option_4 = models.CharField(max_length=500,null=True,blank=True)
    Option_5 = models.CharField(max_length=500,null=True,blank=True)
    Double_Quotes = models.BooleanField(default=False)
    Captialize = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

    def getQuestion(self):
        return {
            "Question Number":self.Question_Number,
            "Question":self.Question,
            "Variable":self.Variable,
            "Total Option":self.Total_Option,
            "Type":"Optional"
        }

class AddressQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question_Number = models.IntegerField(default=0)
    Address = models.CharField(max_length=500) 
    Locality = models.CharField(max_length=500)
    Pin_Code = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50) 
    Double_Quotes = models.BooleanField(default=False)
    Captialize = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Document.id} {self.Address}"

    def getQuestion(self):
        return {
            "Question Number":self.Question_Number,
            "Question":self.Question,
            "Type":"Address"
        }

    