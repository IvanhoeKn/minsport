from django.db import models

class Status(models.Model):
	status_name = models.CharField(max_length=15, unique=True)
	def __str__(self):
		return f"{self.status_name}"

	class Meta:
		verbose_name = "Статус"
		verbose_name_plural = "Статусы"


class VerifyStatus(models.Model):
	name = models.CharField(max_length=20, unique=True)
	def __str__(self):
		return f"{self.name}"


class Users(models.Model):
	login_email = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20)
	second_name = models.CharField(max_length=20)
	phone = models.CharField(max_length=12, null=True, blank=True)
	status = models.ForeignKey('Status', on_delete=models.PROTECT)
	def __str__(self):
		return f"{self.login_email}"


class VerificationUser(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	verification = models.ForeignKey('VerifyStatus', on_delete=models.PROTECT)
	def __str__(self):
		return f"id_user:{self.user_id}, id_verify:{self.verification}"


class Events(models.Model):
	header = models.CharField(max_length=100, unique=True)
	full_description = models.TextField()
	short_description = models.CharField(max_length=128)
	location = models.CharField(max_length=128)
	data_start = models.DateField()
	data_end = models.DateField()
	organizer = models.ForeignKey('Users', on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='contest_imgs/', null=True, blank=True)
	def __str__(self):
		return f"{self.header}"


class Organizations(models.Model):
	name = models.CharField(max_length=30, unique=True)
	address = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.name}"


class ConnectUserToOrg(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	organization_id = models.ForeignKey('Organizations', on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.user_id}"


class TableParticipants(models.Model):
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.user_id}"


class VerificationEvent(models.Model):
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	verification = models.ForeignKey('VerifyStatus', on_delete=models.PROTECT)
	def __str__(self):
		return f"{self.event_id}"