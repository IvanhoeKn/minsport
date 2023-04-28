from django.db import models


class Status(models.Model):
	status_name = models.CharField(max_length=15, unique=True)

	class Meta:
		verbose_name = "Статус"
		verbose_name_plural = "Статусы"


class VerifyStatus(models.Model):
	name = models.CharField(max_length=20, unique=True)


class Users(models.Model):
	login_email = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20)
	second_name = models.CharField(max_length=20)
	phone = models.CharField(max_length=12, null=True, blank=True)
	status = models.ForeignKey('Status', on_delete=models.PROTECT)


class VerificationUser(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	verification = models.ForeignKey('VerifyStatus', on_delete=models.PROTECT)


class Events(models.Model):
	header = models.CharField(max_length=100, unique=True)
	full_description = models.TextField()
	short_description = models.CharField(max_length=128)
	location = models.CharField(max_length=128)
	data_start = models.DateField()
	data_end = models.DateField()
	organizer = models.ForeignKey('Users', on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='contest_imgs/', null=True, blank=True)


class Organizations(models.Model):
	name = models.CharField(max_length=30, unique=True)
	address = models.CharField(max_length=100)


class ConnectUserToOrg(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	organization_id = models.ForeignKey('Organizations', on_delete=models.CASCADE)


class TableParticipants(models.Model):
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)


class VerificationEvent(models.Model):
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	verification = models.ForeignKey('VerifyStatus', on_delete=models.PROTECT)

# Create your models here.
