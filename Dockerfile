FROM python:onbuild
#CMD ["gunicorn", "app:app", "-b 0.0.0.0:8000"]
ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENTRYPOINT ["flask", "run"]
CMD ["--host=0.0.0.0"]
