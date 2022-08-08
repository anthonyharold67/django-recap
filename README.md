<h1>Django Recap</h1>

<h3>Commands</h3>

```
#for windows
python -m venv env # sanal ortamımızı oluşturuyoruz
env\Scripts\activate # sanal ortamı aktif hale getiriyoruz
pip install django # django yu yüklüyoruz
django-admin startproject main . # projemizi oluşturuyoruz
django-admin startapp blog # app imizi oluşturuyoruz
python manage.py runserver # uygulamayı çalıştırıyoruz
```

<p>main adında oluşturduğumuz projemizin klasörü içinde bulunan installed apps kısmına oluşturduğumuz app imizi ekliyoruz</p>

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #3rd party apps
    'blog',
]
```

