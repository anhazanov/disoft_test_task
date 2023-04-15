# Generated by Django 4.2 on 2023-04-15 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0003_alter_tasks_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('comment_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_api.comments')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_api.tasks')),
            ],
        ),
    ]
