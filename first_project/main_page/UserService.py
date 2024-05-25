from django.contrib.auth.models import User

class UserService:

    @staticmethod
    def create(username, password):
        try:
            user = User.objects.create_user(username, username, password)
            user.save()
            return user
        except Exception as e:
            return False