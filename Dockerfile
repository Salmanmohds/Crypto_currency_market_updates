FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /apps
COPY requirements.txt /apps
# RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /apps
# CMD ["python", "app.py"]