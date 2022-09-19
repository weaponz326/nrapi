# nr-api

## Comands

To create an app in a sub directory, first create the directory, and specify the path to the directory as an option
```bash
py manage.py startapp app_name folder_1/folder_2/app_name
```

The gunicorn command for runnning a project on the deployment server
```bash
gunicorn --worker-tmp-dir /dev/shm --chdir ./projects/proect_name project_name.wsgi
```