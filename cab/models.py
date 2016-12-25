from django.db import models
from django.contrib.auth.models import User

class ticket(models.Model):
	trip_to = models.CharField(max_length=50)
	trip_from = models.CharField(max_length=50)
	tolerance_time = models.TimeField()
	trip_time = models.TimeField()
	trip_date = models.DateField()
	issued_by = models.ForeignKey(User, related_name = "cab_issue", on_delete = models.CASCADE)
	cab_type = models.IntegerField() #Seating Capacity

class booked_ticket(models.Model):
	ticket = models.ForeignKey(ticket, related_name = "booked_ticket", on_delete = models.CASCADE)
	booker = models.ForeignKey(User, related_name = "booker", on_delete = models.CASCADE)

class interested_ticket(models.Model):
	ticket = models.ForeignKey(ticket, related_name = "interested_ticket", on_delete = models.CASCADE)
	interested = models.ForeignKey(User, related_name = "interested", on_delete = models.CASCADE)

