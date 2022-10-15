# nrapi

## Comands

To create an app in a sub directory, first create the directory, and specify the path to the directory as an option
```bash
py manage.py startapp app_name folder_1/folder_2/app_name
```

## Production deployment checklist

Uncomment localhost from ALLOWED_HOSTS

set djoser DOMAIN from `localhost` to `netrink.com`