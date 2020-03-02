from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, number, name, gender, phone, college, department, grade,rand,user_is_active, password=None):

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            number = number,
            name = name,
            gender = gender,
            phone = phone,
            college = college,
            department = department,
            grade = grade,
            rand = rand,
            user_is_active = user_is_active,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, number, name, gender, phone, college, department, grade, rand,user_is_active,password):

        user = self.create_user(
            email=email,
            password=password,
            number = number,
            name = name,
            gender = gender,
            phone = phone,
            college = college,
            department = department,
            grade = grade,
            rand = rand,
            user_is_active = user_is_active,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    number = models.CharField(
        verbose_name = '학번',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        verbose_name = '이름',
        max_length=15,
        null=True
    )
    gender = models.CharField(
        verbose_name = '성별',
        max_length=15,
        null=True
    )
    email = models.EmailField(
        verbose_name = '이메일',
        max_length=255,
        unique=True,
        null=True
    )
    phone = models.CharField(
        verbose_name = '전화번호',
        max_length=15,
        null=True
    )
    college = models.CharField(
        verbose_name = '단과대',
        max_length=15,
        null=True
    )
    department = models.CharField(
        verbose_name = '전공',
        max_length=15,
        null=True
    )
    grade = models.IntegerField(
        verbose_name = '학년',
        null=True
    )
    rand = models.IntegerField(
        verbose_name = 'code',
        null = True,
    )
    
    user_is_active= models.IntegerField(
        verbose_name = 'user_is_active',
        null = True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = [
        'name', 
        'gender', 
        'phone',
        'email',
        'college', 
        'department',
        'grade',
        'rand',
        'user_is_active',
    ]

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser