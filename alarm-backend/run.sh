gunicorn run:app --bind 0.0.0.0:4444 --access-logfile=logs/$(date +%m-%d-%Y)_access.log --error-logfile=logs/$(date +%m-%d-%Y)_error.log
