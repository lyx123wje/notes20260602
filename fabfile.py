from fabric import task

SITENAME = '47.94.179.201'
SITE_FOLDER = f'/home/riyo/sites/{SITENAME}'


@task
def deploy(c):
    _get_latest_source(c)
    _update_virtualenv(c)
    _update_static_files(c)
    _update_database(c)
    _update_nginx_config(c)
    _update_systemd_service(c)
    _restart_services(c)


def _get_latest_source(c):
    c.run(f'cd {SITE_FOLDER} && git pull')


def _update_virtualenv(c):
    c.run(f'cd {SITE_FOLDER} && ./virtualenv/bin/pip install -r requirements.txt')


def _update_static_files(c):
    c.run(f'cd {SITE_FOLDER} && ./virtualenv/bin/python manage.py collectstatic --noinput')


def _update_database(c):
    c.run(f'cd {SITE_FOLDER} && ./virtualenv/bin/python manage.py migrate --noinput')


def _update_nginx_config(c):
    c.run(f'sed -e "s/SITENAME/{SITENAME}/g" {SITE_FOLDER}/deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/{SITENAME}')
    c.run(f'sudo ln -sf /etc/nginx/sites-available/{SITENAME} /etc/nginx/sites-enabled/{SITENAME}')
    c.run('sudo nginx -t && sudo systemctl reload nginx')


def _update_systemd_service(c):
    c.run(f'sed -e "s/SITENAME/{SITENAME}/g" {SITE_FOLDER}/deploy_tools/gunicorn-systemd.template.service | sudo tee /etc/systemd/system/gunicorn-{SITENAME}.service')
    c.run('sudo systemctl daemon-reload')


def _restart_services(c):
    c.run(f'sudo systemctl restart gunicorn-{SITENAME}')
    c.run(f'sudo systemctl enable gunicorn-{SITENAME}')
