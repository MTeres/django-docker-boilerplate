#!/bin/bash

python3 manage.py collectstatic -c --noinput

gunicorn base.wsgi -b 0.0.0.0:8000 --reload --log-level=DEBUG --timeout 2200