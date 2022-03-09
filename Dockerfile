# getting reference from DockerHUb
FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
# Define the work directory inside the container
WORKDIR /apps
# Copy requirements.txt into container
COPY requirements.txt /apps
# RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy all file from current directory into container
ADD . /apps
# CMD ["python", "app.py"]