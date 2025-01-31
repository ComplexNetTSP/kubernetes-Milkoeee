FROM python:3-alpine

COPY . .

ENV PYTHONUNBUFFERED=1
RUN pip install flask
CMD ["flask", "--app", "app1", "run", "--host=0.0.0.0"]