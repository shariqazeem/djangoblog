# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for running Django in a production mode
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV DJANGO_SECRET_KEY='django-insecure-v0=%5snki&wa=c*khm0mvr74tzb%zt+u0cq8e4h1-@(tncz5#@' 
ENV DJANGO_DEBUG=False

# Set your working directory
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Expose the port your Django application is running on (e.g., 8000)
EXPOSE 8000

# Start your Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
