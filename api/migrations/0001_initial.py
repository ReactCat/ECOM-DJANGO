from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="shopadmin",
            email = "shopadmin@gmail.com",
            is_staff=True,
            is_superuser=True,
            phone="24224242424",
            gender="female"
            )
        user.set_password("shop2424")
        user.save()


    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),

    ]
