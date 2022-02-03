# Generated by Django 4.0.1 on 2022-01-26 17:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('date_contacted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=150)),
                ('date_of_event', models.DateField(default=django.utils.timezone.now)),
                ('event_poster', models.ImageField(blank=True, upload_to='event_pics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg'])])),
                ('description_of_event', models.TextField()),
                ('slug', models.SlugField(default='', max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_caption', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='galleries')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnership', models.CharField(choices=[('personal', 'personal'), ('government', 'government'), ('corporate supply', 'corporate supply'), ('equipment and supply', 'equipment and supply')], max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=40)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField(max_length=400)),
                ('ratings', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profession', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, choices=[('Afghanistan', 'Afghanistan'), ('Akrotiri', 'Akrotiri'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Ashmore and Cartier Islands', 'Ashmore and Cartier Islands'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo, Democratic Republic of the', 'Congo, Democratic Republic of the'), ('Costa Rica', 'Costa Rica'), ("Cote d'Ivoire", "Cote d'Ivoire"), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Korea, North', 'Korea, North'), ('Korea, South', 'Korea, South'), ('Kuwait', 'Kuwait'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Monaco', 'Monaco'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Pakistan', 'Pakistan'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia and Montenegro', 'Serbia and Montenegro'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Taiwan', 'Taiwan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe'), ('Other', 'Other')], default='United States', max_length=50)),
                ('photo', models.ImageField(blank=True, default='volunteer.jpg', upload_to='volunteer_photos')),
                ('phone', models.CharField(blank=True, max_length=40)),
                ('why_join_Orgeon', models.CharField(blank=True, max_length=100)),
                ('date_volunteered', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UsersCheckedIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('has_checked_in', models.BooleanField(default=False)),
                ('date_checked_in', models.DateTimeField(auto_now_add=True)),
                ('checked_in', models.ManyToManyField(related_name='user_checking_in', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('report', models.TextField()),
                ('report_doc', models.FileField(blank=True, upload_to='report_documents', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['docx', 'doc', 'pdf', 'txt', 'odt', 'rtf', 'tex', 'wpd', 'ods ', 'xls', 'xlsm', 'xlsx', 'pptx', 'ppt', 'pps', 'odp'])])),
                ('slug', models.SlugField(default='', max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('has_read', models.ManyToManyField(blank=True, related_name='has_read_report', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('need_replies', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='', max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_user', to=settings.AUTH_USER_MODEL)),
                ('has_read', models.ManyToManyField(blank=True, related_name='has_read_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NotifyMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_title', models.CharField(default='New Notification', max_length=100)),
                ('notify_alert', models.CharField(default='Alert from Orgeonofstars', max_length=200)),
                ('post_slug', models.CharField(blank=True, max_length=100)),
                ('report_slug', models.CharField(blank=True, max_length=100)),
                ('comment_slug', models.CharField(blank=True, max_length=100)),
                ('read', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='', max_length=100)),
                ('date_notified', models.DateTimeField(auto_now_add=True)),
                ('sender_or_receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='...')),
                ('slug', models.SlugField(default='', max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgeon_api.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientInfoProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_plan', models.CharField(choices=[('Eagle', 'Eagle'), ('Kangaroo', 'Kangaroo'), ('Nested', 'Nested')], default='Eagle', max_length=20)),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField(blank=True, default=10)),
                ('email', models.EmailField(blank=True, max_length=255, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('emergency_phone', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='Male', max_length=10)),
                ('client_image', models.ImageField(blank=True, default='client.jpg', upload_to='client_images')),
                ('next_of_kin', models.CharField(blank=True, max_length=50)),
                ('issue', models.TextField()),
                ('progress', models.CharField(choices=[('Assessment', 'Assessment'), ('Development', 'Development'), ('Planning', 'Planning'), ('Implementation', 'Implementation'), ('Evaluation', 'Evaluation'), ('Star', 'Star')], default='Assessment', max_length=30)),
                ('assessment_phase_details', models.TextField(blank=True)),
                ('development_phase_details', models.TextField(blank=True)),
                ('planning_phase_details', models.TextField(blank=True)),
                ('implementation_phase_details', models.TextField(blank=True)),
                ('evaluation_phase_details', models.TextField(blank=True)),
                ('star_phase_details', models.TextField(blank=True)),
                ('slug', models.SlugField(default='', max_length=100)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('assessment_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]