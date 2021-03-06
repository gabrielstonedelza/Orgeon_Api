from django.db import models
from django.utils import timezone
from PIL import Image
from django.core.validators import FileExtensionValidator
from datetime import date, time, datetime, timedelta
from django.conf import settings
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

PARTNERSHIP_TYPE = (
    ("personal", "personal"),
    ('government', 'government'),
    ('corporate supply', 'corporate supply'),
    ('equipment and supply', 'equipment and supply')
)

FEELINGS_CHOICES = (
    ("Happy", "Happy"),
    ("Sad", "Sad"),
    ("Confued", "Confued"),
    ("Smiling", "Smiling"),
    ("Crying", "Crying"),
    ("Winki", "Winki"),
    ("Chilling", "Chilling"),
)

LEVEL_CHOICES = (
    ("Assessment", "Assessment"),
    ("Development", "Development"),
    ("Planning", "Planning"),
    ("Implementation", "Implementation"),
    ("Evaluation", "Evaluation"),
    ("Star", "Star")
)

GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
)

COUNTRY_OF_CHOICE = (
    ("Afghanistan", "Afghanistan"),
    ("Akrotiri", "Akrotiri"),
    ("Albania", "Albania"),
    ("Algeria", "Algeria"),
    ("American Samoa", "American Samoa"),
    ("Andorra", "Andorra"),
    ("Angola", "Angola"),
    ("Anguilla", "Anguilla"),
    ("Antarctica", "Antarctica"),
    ("Antigua and Barbuda", "Antigua and Barbuda"),
    ("Argentina", "Argentina"),
    ("Armenia", "Armenia"),
    ("Aruba", "Aruba"),
    ("Ashmore and Cartier Islands", "Ashmore and Cartier Islands"),
    ("Australia", "Australia"),
    ("Austria", "Austria"),
    ("Azerbaijan", "Azerbaijan"),
    ("Bahrain", "Bahrain"),
    ("Bangladesh", "Bangladesh"),
    ("Barbados", "Barbados"),
    ("Belarus", "Belarus"),
    ("Belgium", "Belgium"),
    ("Belize", "Belize"),
    ("Benin", "Benin"),
    ("Bermuda", "Bermuda"),
    ("Bhutan", "Bhutan"),
    ("Bolivia", "Bolivia"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Botswana", "Botswana"),
    ("Brazil", "Brazil"),
    ("Bulgaria", "Bulgaria"),
    ("Burkina Faso", "Burkina Faso"),
    ("Burundi", "Burundi"),
    ("Cambodia", "Cambodia"),
    ("Cameroon", "Cameroon"),
    ("Canada", "Canada"),
    ("Cape Verde", "Cape Verde"),
    ("Central African Republic", "Central African Republic"),
    ("Chad", "Chad"),
    ("Chile", "Chile"),
    ("China", "China"),
    ("Colombia", "Colombia"),
    ("Comoros", "Comoros"),
    ("Congo, Democratic Republic of the", "Congo, Democratic Republic of the"),
    ("Costa Rica", "Costa Rica"),
    ("Cote d'Ivoire", "Cote d'Ivoire"),
    ("Croatia", "Croatia"),
    ("Cuba", "Cuba"),
    ("Cyprus", "Cyprus"),
    ("Czech Republic", "Czech Republic"),
    ("Denmark", "Denmark"),
    ("Dominican Republic", "Dominican Republic"),
    ("Ecuador", "Ecuador"),
    ("Egypt", "Egypt"),
    ("El Salvador", "El Salvador"),
    ("Equatorial Guinea", "Equatorial Guinea"),
    ("Eritrea", "Eritrea"),
    ("Estonia", "Estonia"),
    ("Ethiopia", "Ethiopia"),
    ("Finland", "Finland"),
    ("France", "France"),
    ("Gabon", "Gabon"),
    ("Gambia", "Gambia"),
    ("Georgia", "Georgia"),
    ("Germany", "Germany"),
    ("Ghana", "Ghana"),
    ("Gibraltar", "Gibraltar"),
    ("Greece", "Greece"),
    ("Greenland", "Greenland"),
    ("Guatemala", "Guatemala"),
    ("Guinea", "Guinea"),
    ("Guinea-Bissau", "Guinea-Bissau"),
    ("Haiti", "Haiti"),
    ("Honduras", "Honduras"),
    ("Hungary", "Hungary"),
    ("Iceland", "Iceland"),
    ("India", "India"),
    ("Indonesia", "Indonesia"),
    ("Iran", "Iran"),
    ("Iraq", "Iraq"),
    ("Ireland", "Ireland"),
    ("Israel", "Israel"),
    ("Italy", "Italy"),
    ("Jamaica", "Jamaica"),
    ("Japan", "Japan"),
    ("Jordan", "Jordan"),
    ("Kazakhstan", "Kazakhstan"),
    ("Kenya", "Kenya"),
    ("Korea, North", "Korea, North"),
    ("Korea, South", "Korea, South"),
    ("Kuwait", "Kuwait"),
    ("Latvia", "Latvia"),
    ("Lebanon", "Lebanon"),
    ("Liberia", "Liberia"),
    ("Libya", "Libya"),
    ("Liechtenstein", "Liechtenstein"),
    ("Lithuania", "Lithuania"),
    ("Madagascar", "Madagascar"),
    ("Malawi", "Malawi"),
    ("Malaysia", "Malaysia"),
    ("Mali", "Mali"),
    ("Malta", "Malta"),
    ("Mauritania", "Mauritania"),
    ("Mauritius", "Mauritius"),
    ("Mexico", "Mexico"),
    ("Monaco", "Monaco"),
    ("Morocco", "Morocco"),
    ("Mozambique", "Mozambique"),
    ("Namibia", "Namibia"),
    ("Netherlands", "Netherlands"),
    ("New Zealand", "New Zealand"),
    ("Niger", "Niger"),
    ("Nigeria", "Nigeria"),
    ("Norway", "Norway"),
    ("Pakistan", "Pakistan"),
    ("Paraguay", "Paraguay"),
    ("Peru", "Peru"),
    ("Philippines", "Philippines"),
    ("Poland", "Poland"),
    ("Portugal", "Portugal"),
    ("Puerto Rico", "Puerto Rico"),
    ("Qatar", "Qatar"),
    ("Romania", "Romania"),
    ("Russia", "Russia"),
    ("Rwanda", "Rwanda"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Senegal", "Senegal"),
    ("Serbia and Montenegro", "Serbia and Montenegro"),
    ("Sierra Leone", "Sierra Leone"),
    ("Singapore", "Singapore"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Somalia", "Somalia"),
    ("South Africa", "South Africa"),
    ("Spain", "Spain"),
    ("Sri Lanka", "Sri Lanka"),
    ("Sudan", "Sudan"),
    ("Swaziland", "Swaziland"),
    ("Sweden", "Sweden"),
    ("Switzerland", "Switzerland"),
    ("Taiwan", "Taiwan"),
    ("Tanzania", "Tanzania"),
    ("Thailand", "Thailand"),
    ("Togo", "Togo"),
    ("Trinidad and Tobago", "Trinidad and Tobago"),
    ("Tunisia", "Tunisia"),
    ("Turkey", "Turkey"),
    ("Uganda", "Uganda"),
    ("Ukraine", "Ukraine"),
    ("United Arab Emirates", "United Arab Emirates"),
    ("United Kingdom", "United Kingdom"),
    ("United States", "United States"),
    ("Uruguay", "Uruguay"),
    ("Uzbekistan", "Uzbekistan"),
    ("Venezuela", "Venezuela"),
    ("Vietnam", "Vietnam"),
    ("Yemen", "Yemen"),
    ("Zambia", "Zambia"),
    ("Zimbabwe", "Zimbabwe"),
    ("Other", "Other")
)

CARE_PLAN = (
    ("Eagle", "Eagle"),
    ("Kangaroo", "Kangaroo"),
    ("Nested", "Nested"),
)
RATING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
supported_files = ["docx", "doc", "pdf", "txt", "odt", "rtf", "tex", "wpd", "ods ", "xls", "xlsm", "xlsx", "pptx",
                   "ppt", "pps", "odp"]
NOTIFICATIONS_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_TRIGGERS = (
    ("Triggered", "Triggered"),
    ("Not Triggered", "Not Triggered"),
)


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profession = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, default="United States", blank=True)
    photo = models.ImageField(upload_to="volunteer_photos", default="volunteer.jpg", blank=True)
    phone = models.CharField(max_length=40, blank=True)
    why_join_Orgeon = models.CharField(max_length=100, blank=True)
    date_volunteered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} has volunteered."

    def get_volunteer_photo(self):
        if self.photo:
            return "https://orgeonofstars.xyz" + self.photo.url
        return ""

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Events(models.Model):
    theme = models.CharField(max_length=200)
    venue = models.CharField(max_length=150)
    date_of_event = models.DateField(default=timezone.now)
    event_poster = models.ImageField(upload_to='event_pics', blank=True,
                                     validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg'])])
    description_of_event = models.TextField()
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.theme}"

    def save(self, *args, **kwargs):
        value = self.theme
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_event_poster(self):
        if self.event_poster:
            return "https://orgeonofstars.xyz" + self.event_poster.url


class Partnership(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    report = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s report = {self.title}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')
    title = models.CharField(max_length=200)
    message = models.TextField()
    views = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_commenting")
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    time_created = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Comment of {self.post.title}"


class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_liking_post")
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    date_liked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"


class ReportComments(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_commenting_on_report")
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment of {self.report.title}"


class Gallery(models.Model):
    image_caption = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="galleries")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image_caption}"

    def get_gallery_item(self):
        if self.image:
            return "https://orgeonofstars.xyz" + self.image.url
        return ""


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date_contacted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class ClientInfoProgress(models.Model):
    care_plan = models.CharField(max_length=20, choices=CARE_PLAN, default="Eagle")
    assessment_officer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    age = models.IntegerField(default=10, blank=True)
    email = models.EmailField(unique=True, max_length=255, blank=True)
    phone = models.CharField(max_length=20)
    emergency_phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    client_image = models.ImageField(upload_to="client_images", blank=True, default="client.jpg")
    next_of_kin = models.CharField(max_length=50, blank=True)
    issue = models.TextField()
    progress = models.CharField(choices=LEVEL_CHOICES, max_length=30, default="Assessment")
    assessment_phase_details = models.TextField(blank=True)
    development_phase_details = models.TextField(blank=True)
    planning_phase_details = models.TextField(blank=True)
    implementation_phase_details = models.TextField(blank=True)
    evaluation_phase_details = models.TextField(blank=True)
    star_phase_details = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, default='')
    date_issued = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.slug}/"


class UsersCheckedIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_in = models.ManyToManyField(User, related_name="user_checking_in")
    check_date = models.DateField(auto_now_add=True)
    date_checked_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} just checked in "


class Notifications(models.Model):
    notification_id = models.CharField(max_length=100, blank=True, default="")
    notification_tag = models.CharField(max_length=100, blank=True, default="")
    notification_title = models.CharField(max_length=200, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=100, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_receiving_notification", null=True)
    volunteer_id = models.CharField(max_length=100, blank=True)
    partner_id = models.CharField(max_length=100, blank=True)
    contact_id = models.CharField(max_length=100, blank=True)
    report_id = models.CharField(max_length=100, blank=True)
    client_id = models.CharField(max_length=100, blank=True)
    posts_id = models.CharField(max_length=100, blank=True)
    checked_in_id = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title
