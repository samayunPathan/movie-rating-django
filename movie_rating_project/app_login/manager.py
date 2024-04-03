
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,email,username,phone,password=None):
        if not email:
            raise ValueError('email is required')
        if not username:
            raise ValueError('username must set')
        user=self.model(email=self.normalize_email(email),
                        username=username,
                        phone=phone,
                        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password,phone=123):
        
        user=self.create_user(email=self.normalize_email(email),
                        username=username,
                        phone=phone,
                        password=password,
                        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.save(using=self._db)
        return user
 
        
