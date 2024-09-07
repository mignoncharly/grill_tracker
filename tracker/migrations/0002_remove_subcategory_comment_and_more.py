# Generated by Django 4.2.4 on 2024-09-06 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='max_volunteers',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('volunteer', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='tracker.subcategory')),
            ],
        ),
    ]