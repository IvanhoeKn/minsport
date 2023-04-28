# Generated by Django 4.2 on 2023-04-28 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, unique=True)),
                ('full_description', models.TextField()),
                ('short_description', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('data_start', models.DateField()),
                ('data_end', models.DateField()),
                ('photo', models.ImageField(null=True, upload_to='contest_imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fspru.status')),
            ],
        ),
        migrations.CreateModel(
            name='VerifyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerifyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fspru.users')),
                ('verification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fspru.verifystatus')),
            ],
        ),
        migrations.CreateModel(
            name='VerificationEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fspru.events')),
                ('verification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fspru.verifystatus')),
            ],
        ),
        migrations.CreateModel(
            name='TableParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fspru.events')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fspru.users')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fspru.users'),
        ),
        migrations.CreateModel(
            name='ConnectUserToOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fspru.organizations')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fspru.users')),
            ],
        ),
    ]