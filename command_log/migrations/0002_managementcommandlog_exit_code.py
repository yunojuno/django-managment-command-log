# Generated by Django 2.2.5 on 2019-09-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("command_log", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="managementcommandlog",
            name="exit_code",
            field=models.IntegerField(
                default=0, help_text="0 if the command ran without error.", max_length=3
            ),
        )
    ]