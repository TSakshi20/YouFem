from statistics import mode
from django.db import models

# Create your models here.


class Professional(models.Model):
    peid = models.CharField(max_length=50,primary_key=True)
    pfname = models.CharField(max_length=30)
    plname = models.CharField(max_length=30, null=True, blank=True)
    experience = models.IntegerField()
    contact = models.IntegerField()
    profession = models.CharField(max_length=20)
    profile_pic=models.ImageField(null=True,blank=True);
    password=models.CharField(max_length=30,blank=True)

    def __str__(self):
        return (self.pfname+" " +self.plname)



class LegalRight(models.Model):
    #topicid=models.IntegerField(primary_key=True)
    topicname=models.CharField(max_length=50)


    def __str__(self):
        return (self.topicname)


class LegalSubTopic(models.Model):
    subtopicname=models.CharField(max_length=50)
    legaltopic=models.ForeignKey(LegalRight,on_delete=models.CASCADE)
    subtopicimage=models.ImageField(null=True,blank=True);

    def __str__(self):
        return (self.subtopicname)



class LawFaq(models.Model):
    question=models.TextField(max_length=100)
    answer=models.TextField(max_length=200)
    lawsubtopic=models.ForeignKey(LegalSubTopic,on_delete=models.CASCADE)


    def __str__(self):
        return (self.question[0:50])


    
