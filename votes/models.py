from django.db import models
# from django.utils import timezone

# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'Comment: {}'.format(self.name)



class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.ForeignKey(Position,
                on_delete=models.CASCADE,
                related_name='position',
                null=True, blank=True)
    birthdate = models.DateField('Birhday')
    platform = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return 'Candidate: {}'.format(self.lastname)




class Vote(models.Model):
    candidate = models.ForeignKey(Candidate,
                on_delete=models.CASCADE,
                related_name='candidate',
                null=True, blank=True)
    vote_datetime = models.DateTimeField()


    def __str__(self):
        return 'Comment: {}'.format(self.candidate)
