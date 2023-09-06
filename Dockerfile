# Use Alpine Linux as the base image
FROM python:3.x-alpine

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=roadlink.settings
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apk update && \
    apk add --no-cache \
    # Add any required system packages here

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL and initialize the database
RUN apk add --no-cache postgresql postgresql-dev && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install psycopg2-binary && \
    apk --purge del .build-deps && \
    apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/Your/Timezone /etc/localtime && \
    echo "Your/Timezone" > /etc/timezone && \
    mkdir -p /run/postgresql && \
    chown -R postgres /run/postgresql && \
    su postgres -c "initdb -D /var/lib/postgresql/data" && \
    su postgres -c "pg_ctl start -D /var/lib/postgresql/data -o '-c listen_addresses='localhost''" && \
    su postgres -c "createdb roadlink" && \
    su postgres -c "psql -d roadlink -c 'CREATE EXTENSION IF NOT EXISTS hstore;'" && \
    su postgres -c "pg_ctl stop -D /var/lib/postgresql/data"

# Create and set the working directory
WORKDIR /app

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
