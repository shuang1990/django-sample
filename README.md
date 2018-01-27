##### gunicorn 配置

```
import multiprocessing
import datetime

bind = "127.0.0.1:8000"
workers = 5 # cpu + 1
date = datetime.datetime.now().strftime("%Y-%m-%d")
errorlog = '/var/log/mysite/gunicorn_%s.error.log' % date
accesslog = '/var/log/mysite/gunicorn_%s.access.log' % date
loglevel = 'debug'
proc_name = 'mysite'

## 启动
(venv) work:mysite ys$ gunicorn mysite.wsgi:application -c gunicorn.py

```

