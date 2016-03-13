from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=50)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(blank=True, null=True)
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(User, related_name="likes", blank=True, null=True)

  def __unicode__(self):
      return self.title

  def get_absolute_url(self):
      return reverse('question', args=(self.pk,))
  
  class Meta:
      ordering = ['-added_at']


class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)

  def __unicode__(self):
      return "Answer_{id} to {question}".format(id=self.pk, question=self.question)
