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
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$text')

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

class ConditionalQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$condition')
    If_Yes = models.TextField()
    If_No = models.TextField()

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

class BooleanQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$bool')

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

class DateQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$date')

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

class OptionalQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Question = models.TextField()
    Variable = models.CharField(max_length=50,default='$optional')
    Total_Option = models.IntegerField()
    Option_1 = models.CharField(max_length=500,null=True,blank=True)
    Option_2 = models.CharField(max_length=500,null=True,blank=True)
    Option_3 = models.CharField(max_length=500,null=True,blank=True)
    Option_4 = models.CharField(max_length=500,null=True,blank=True)
    Option_5 = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.Document.id} {self.Question}"

class AddressQuestion(models.Model):
    Document = models.ForeignKey("Document",on_delete=models.CASCADE)
    Address = models.CharField(max_length=500) 
    Locality = models.CharField(max_length=500)
    Pin_Code = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.Document.id} {self.Address}"

    