# Real Estate Property Management System
A Django-based web application designed for real estate agents to efficiently manage property listings and track availability. This system serves as a web-based MVP with the potential to expand into a full API backend and mobile app.

## Features
- Add, edit, and delete property listings.
- View properties in a structured dashboard.
- Track property details such as location, price, and features.
- Ready for future expansion into a mobile app with a REST API backend.

## How It Works
1. Log in as a real estate agent.
2. Add new property listings or update existing ones.
3. View all properties in a dashboard with organized details.
4. Track the status of each property (available, sold, etc.).
5. Export or manage property data as needed.

## Running the App (Python/Django)
1. Clone the repository: ```git clone <repository_url> cd <repository_folder>```
2. Install dependencies: ```pip install -r requirements.txt```
3. Apply migrations: ```python manage.py migrate```
4. Start the development server: ```python manage.py runserver```
5. Open the app in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Future Mobile Integration
- Backend can be refactored into a Django REST API.
- Connect with a React Native mobile app for real estate agents.

## File Structure
- `manage.py` → Django management script
- `properties/` → App folder containing models, views, templates
- `db.sqlite3` → SQLite database file
- `requirements.txt` → Python dependencies
