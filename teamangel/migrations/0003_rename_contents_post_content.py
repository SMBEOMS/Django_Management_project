# Generated by Django 4.2.5 on 2023-09-14 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teamangel", "0002_post_updated_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="contents",
            new_name="content",
        ),
    ]
