# Generated by Django 5.1.2 on 2024-11-28 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_curso_disciplina"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="disciplina",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.disciplina"
            ),
        ),
    ]
