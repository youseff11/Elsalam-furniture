from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_productsize_discount_price_productsize_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='show_on_home',
            field=models.BooleanField(
                default=False,
                help_text='فعّل لعرض هذا القسم في الصفحة الرئيسية (حد أقصى 4)',
                verbose_name='عرض في الصفحة الرئيسية',
            ),
        ),
        migrations.AddField(
            model_name='category',
            name='home_display_order',
            field=models.PositiveIntegerField(
                default=0,
                help_text='رقم أصغر = يظهر أولاً',
                verbose_name='ترتيب العرض',
            ),
        ),
        migrations.AddField(
            model_name='category',
            name='home_layout',
            field=models.CharField(
                choices=[('large', 'كبير (يشغل عمودين وصفين)'), ('tall', 'طويل (يشغل عمود وصفين)'), ('wide', 'عادي (يشغل عمود وصف)')],
                default='wide',
                help_text='كبير: يشغل مساحة كبيرة | طويل: عمود كامل | عادي: حجم صغير',
                max_length=10,
                verbose_name='حجم البطاقة',
            ),
        ),
        migrations.AddField(
            model_name='category',
            name='showcase_image',
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format='WEBP',
                help_text='الصورة التي تظهر في الصفحة الرئيسية',
                keep_meta=True,
                null=True,
                quality=80,
                scale=None,
                size=[1200, 800],
                upload_to='categories/',
                verbose_name='صورة العرض',
            ),
        ),
        migrations.AddField(
            model_name='category',
            name='showcase_subtitle',
            field=models.CharField(
                blank=True,
                help_text='مثال: المعيشة الفاخرة',
                max_length=100,
                null=True,
                verbose_name='العنوان الفرعي',
            ),
        ),
        migrations.AddField(
            model_name='category',
            name='showcase_badge',
            field=models.CharField(
                blank=True,
                help_text='مثال: الإصدار المحدود (اتركها فارغة لإخفائها)',
                max_length=50,
                null=True,
                verbose_name='شارة مميزة',
            ),
        ),
    ]
