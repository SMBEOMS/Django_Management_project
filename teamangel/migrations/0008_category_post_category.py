# Generated by Django 4.2.5 on 2023-09-19 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("teamangel", "0007_remove_post_views"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=200, unique=True),
                ),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="teamangel.category",
            ),
        ),
    ]
