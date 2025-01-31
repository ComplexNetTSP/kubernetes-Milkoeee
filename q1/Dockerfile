FROM python:3-alpine

COPY . .

ENV PYTHONUNBUFFERED=1
RUN pip install flask
CMD ["flask", "--app", "test", "run", "--host=0.0.0.0"]