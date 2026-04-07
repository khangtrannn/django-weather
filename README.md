# Django Weather App

A simple weather and air-quality web app built with Django.  
This project fetches real-time AQI (Air Quality Index) data from the AirNow API and displays:

- AQI category (Good, Moderate, Unhealthy, etc.)
- AQI score for a location
- Health guidance for the current AQI category
- Color-coded AQI status card

## Tech Stack

- Python
- Django
- Requests
- Bootstrap 5
- SQLite (default Django database)

## Project Structure

- Main Django project: [weather/weather](weather/weather)
- App: [weather/lookup](weather/lookup)
- Templates: [weather/lookup/templates](weather/lookup/templates)
- Main view logic: [weather/lookup/views.py](weather/lookup/views.py)
- URL routing:
	- [weather/weather/urls.py](weather/weather/urls.py)
	- [weather/lookup/urls.py](weather/lookup/urls.py)

## Features

- Default AQI lookup using a fallback ZIP code
- Manual ZIP code search from the navbar
- AQI category descriptions mapped in the backend
- AQI color classes mapped by category

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd djangoweather
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

From the [weather](weather) directory:

```bash
cd weather
python manage.py migrate
```

### 5. Start development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

## How It Works

1. Home route loads AQI data from AirNow.
2. User can submit a ZIP code from the navbar form.
3. The backend fetches AQI data and maps category to:
	 - health description text
	 - CSS color class
4. Template renders the AQI card and details.

## Important Notes

- The current API key is hardcoded in [weather/lookup/views.py](weather/lookup/views.py). For production, move it to an environment variable.
- This app is intended for learning and local development.

## Dependency Management

This project includes a committed [requirements.txt](requirements.txt) file.

To refresh it after adding/removing packages:

```bash
pip freeze > requirements.txt
```

## Course Reference

Built after completing this course:  
Build a Weather App With Python and Django (Udemy)

