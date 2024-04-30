FROM python:3.9.18

# Set the working directory
WORKDIR /app

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Npm install packages in package.json
RUN apt-get update && apt-get install -y npm
COPY package.json /app
RUN npm install

# Copy the current directory contents into the container at /app
COPY . /app

RUN python manage.py collectstatic --noinput

# For now, lets just use runserver to test the app
CMD gunicorn cturner.wsgi:application --bind 0.0.0.0:$PORT


