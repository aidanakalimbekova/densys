# from safedelete.models import SafeDeleteModel
# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# def random_username():
#     return str(uuid4())

# class User(SafeDeleteModel, AbstractUser):

#     class KIND(models.IntegerChoices):
#         PATIENT = 0
#         DOCTOR = 1

#     username = models.CharField(
#         "username",
#         max_length=150,
#         unique=True,
#         help_text=
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
#         validators=[AbstractUser.username_validator],
#         error_messages={
#             "unique": "A user with that username already exists.",
#         },
#         # Overrided.
#         default=random_username,
#     )

#     email = models.EmailField("email address", blank=True, null=True, unique=True)
#     phone = PhoneNumberField(_("Phone Number"), region="KZ", blank=True)
#     birth_date = models.DateField(_("Birth Date"), null=True, blank=True)
#     kind = models.PositiveSmallIntegerField(
#         _("Type"), choices=KIND.choices, blank=True, null=True
#     )
