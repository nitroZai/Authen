from django.db import models
from django.contrib.auth.models import ( 
    AbstractBaseUser,
    BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password = None, is_staff = False, is_admin = False):
        
        if not email:
            raise ValueError("Pass Email")
        if not password:
            raise ValueError("Pass Password")

        user_obj = self.model(
            email = self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password = None):
        user = self.create_user(
            email,
            password = password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password = None):
        user = self.create_user(
            email, 
            password=password,
            is_staff=True,
            is_admin= True
        )
        return user

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=200, unique=True)
    is_active   = models.BooleanField(default=True) 
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False) 
    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    manager = UserManager()


    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_staff
    
    def is_admin(self):
        return self.is_admin