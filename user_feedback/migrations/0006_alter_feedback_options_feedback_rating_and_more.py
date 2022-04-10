# Generated by Django 4.0.3 on 2022-04-09 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_feedback', '0005_feedback_created_at_feedback_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ('created_at',)},
        ),
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(blank=True, default=5, verbose_name='Rating'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(verbose_name="Зворотній зв'язок"),
        ),
        migrations.AlterField(
            model_name='reply',
            name='feedback',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='user_feedback.feedback', verbose_name='Відповідь на фідбек: '),
        ),
    ]