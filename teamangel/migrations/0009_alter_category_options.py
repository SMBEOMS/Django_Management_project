# Generated by Django 4.2.5 on 2023-09-19 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teamangel", "0008_category_post_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]