FROM python:3-alpine

COPY . .

ENV PYTHONUNBUFFERED=1
RUN pip install flask
RUN pip install pymongo
CMD ["flask", "--app", "test", "run", "--host=0.0.0.0"]
