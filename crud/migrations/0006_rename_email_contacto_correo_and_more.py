# Generated by Django 4.2.2 on 2023-07-14 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='email',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='fono',
            new_name='telefono',
        ),
    ]
