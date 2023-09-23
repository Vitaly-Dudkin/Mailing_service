# Generated by Django 4.2.5 on 2023-09-20 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try', models.DateTimeField(auto_now_add=True, verbose_name='Last_try')),
                ('status', models.CharField(choices=[('successful', 'Success'), ('error', 'Error')], max_length=10, verbose_name='Status_of_sending')),
                ('server_response', models.CharField(blank=True, null=True, verbose_name='Server_response')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='Client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='Newsletter')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]