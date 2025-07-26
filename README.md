# User Management Application

A simple user management system with a FastAPI backend and HTML frontend.

## Features

- Add new users with name and email
- View all users in a list
- Real-time form validation
- Responsive design
- CORS enabled for frontend-backend communication

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r reqiurements.txt
```

### 2. Start the Backend Server

```bash
python start_server.py
```

Or alternatively:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start on `http://localhost:8000`

### 3. Open the Frontend

Open `index.html` in your web browser. You can:
- Double-click the file
- Drag and drop into your browser
- Use a local server (recommended)

### 4. API Endpoints

- `GET /` - Health check
- `GET /users` - Get all users
- `POST /users` - Create a new user
- `GET /health` - Health check endpoint

## Troubleshooting

### Network Error Issues

If you're getting network errors:

1. **Check if the backend is running**: Make sure you see "User Management API is running" when you visit `http://localhost:8000`

2. **Check the console**: Open browser developer tools (F12) and check the Console tab for detailed error messages

3. **CORS issues**: The backend now includes CORS middleware to allow frontend requests

4. **Port conflicts**: Make sure port 8000 is not being used by another application

### Database Issues

The application uses SQLite by default. If you need to use PostgreSQL:

1. Update the database URL in `database.py`
2. Make sure PostgreSQL is running
3. Create the database if it doesn't exist

## File Structure

- `main.py` - FastAPI application with endpoints
- `models.py` - SQLAlchemy database models
- `schemas.py` - Pydantic schemas for request/response validation
- `database.py` - Database connection configuration
- `index.html` - Frontend interface
- `start_server.py` - Server startup script
- `reqiurements.txt` - Python dependencies

## Development

The backend includes:
- CORS middleware for frontend communication
- Proper error handling
- Input validation
- Database transaction management
- Health check endpoints

The frontend includes:
- Real-time form validation
- Loading states
- Error handling
- User list display
- Responsive design 