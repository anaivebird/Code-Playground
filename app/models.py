from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICE = (
    (-1, 'Pending'),
    (0, 'OK'),
    (1, 'Failed')
)

LANG_CHOICE = (
    ('c', 'C'),
    ('cpp', 'C++'),
    ('java', 'Java'),
    ('python', 'Python')
)


class Submission(models.Model):
    code = models.TextField()
    lang = models.CharField(max_length=12, choices=LANG_CHOICE)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True)
    verdict = models.IntegerField(choices=STATUS_CHOICE, default=-1)
    running_input = models.TextField(blank=True)
    running_result = models.TextField(blank=True)
