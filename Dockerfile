# Use the official Python image as the base image
FROM python:3.x

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=roadlink.settings
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Add any required system packages here

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . /app/

# Collect static files (if applicable)
RUN python manage.py collectstatic --noinput

# Migrate the database (if applicable)
RUN python manage.py migrate

# Expose the port the application runs on (optional)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
