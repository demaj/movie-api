# Pull official base image
FROM python:3.11.6-slim
LABEL MAINTAINER="Gentian Demaj <gentiani101@gmail.com>"

# Update system dependencies
RUN apt-get update

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv

# Add python to path
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

# Create virtual environment
RUN python -m venv ${VIRTUAL_ENV}

# Set work directory
WORKDIR /code

# Copy project files
COPY requirements.txt requirements.txt
COPY app app

# Install dependencies
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app ${VIRTUAL_ENV} && \
    chown -R app:app /vol && \
    chmod -R 755 /vol

# Switch to non-root user
USER app

# Sanity checks
RUN python --version
