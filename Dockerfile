FROM python:3.12-slim
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3030
CMD gunicorn -b 0.0.0.0:3030 main:app