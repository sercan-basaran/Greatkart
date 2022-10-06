from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile

    #kullanıcı oluşturulduğunda console'da gösteriyor.       
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
        print(created)
        if created:
            UserProfile.objects.create(user=instance)
            print("create the user profile")
        else:
            try:
              profile=UserProfile.objects.get(user=instance)
              profile.save()
            except:
              UserProfile.objects.create(user=instance)
              #print("Profile was not exist, but I created one")
              #print("user is updated")
    
@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    print(instance.username,'this user is being saved')

#post_save.connect(post_save_create_profile_receiver, sender=User)        