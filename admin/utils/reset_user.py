from django.contrib.auth import get_user_model

def list_super_user():
    list(get_user_model().objects.filter(is_superuser=True).values_list('username', flat=True))

def list_user():
    # user = list(get_user_model().objects.filter(is_superuser=True).values_list('username', flat=True))
    # return user
    #  print(get_user_model().objects.all())
     return (get_user_model().objects.all())

list_user()