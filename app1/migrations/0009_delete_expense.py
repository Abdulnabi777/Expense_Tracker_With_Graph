# Generated by Django 5.1.3 on 2024-11-18 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_expense'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
    ]