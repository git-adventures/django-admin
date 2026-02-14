# Deployment Guide (PythonAnywhere)

## First-Time Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/git-adventures/django-admin.git mysite
   cd mysite
   ```

2. Install dependencies:
   ```bash
   pip install django whitenoise
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Go to the **Web** tab on PythonAnywhere and configure your web app, then hit **Reload**.

## Updating After Code Changes

```bash
cd ~/mysite
git pull
pip install whitenoise
python manage.py migrate
python manage.py collectstatic --noinput
```

Then hit **Reload** on the Web tab.

## Why WhiteNoise?

Django's development server (`runserver`) serves static files (CSS/JS) automatically. In production, it doesn't — so the admin panel loads without styling. **WhiteNoise** makes your Django app serve its own static files in production.
