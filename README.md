## Project Description
This project is a secure Flask RESTful API that supports user authentication and a user-owned resource (notes). It allows users to register, log in, and manage their own notes. Each user can only access and modify their own data.

The API uses JWT (JSON Web Tokens) for authentication and ensures that all protected routes are only accessible to authenticated users.



## Features
- User registration (signup)
- User login with JWT authentication
- Persistent login using token verification (/me)
- Create notes
- View notes with pagination
- Protected routes (users can only access their own data)



## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-JWT-Extended
- SQLite



## Installation Instructions

1. Clone the repository:
git clone <your-repo-link> cd flask-c10-summative-lab-sessions-and-jwt-clients/server

2. Install dependencies:
python3 -m pip install pipenv python3 -m pipenv install

3. Activate virtual environment:
python3 -m pipenv shell



## Database Setup

Run the following commands:

export FLASK_APP=app.py flask db init flask db migrate -m "initial migration" flask db upgrade



## Running the Application

Start the server:

python app.py

The API will run on:
http://127.0.0.1:5555



## API Endpoints

### Authentication

#### POST /signup
Create a new user.

Request body:
{   "username": "testuser",   "password": "1234",   "password_confirmation": "1234" }

Response:
- 201 Created
- Returns user and JWT token



#### POST /login
Login an existing user.

Request body:
{   "username": "testuser",   "password": "1234" }

Response:
- 200 OK
- Returns user and JWT token



#### GET /me
Get current logged-in user.

Headers:
Authorization: Bearer <token>

Response:
- 200 OK
- Returns user data



### Notes Resource

#### POST /notes
Create a new note.

Headers:
Authorization: Bearer <token> Content-Type: application/json

Request body:
{   "title": "My note",   "content": "This is a note" }



#### GET /notes
Get all notes for the logged-in user (paginated).

Headers:
Authorization: Bearer <token>

Optional query:
/notes?page=1

Response:
{   "notes": [...],   "total_pages": 1,   "current_page": 1 }



## Security Features
- Passwords are hashed using Bcrypt
- JWT authentication protects all sensitive routes
- Users can only access their own notes
- Unauthorized access returns proper error responses


## Project Structure
server/  ├── app.py  ├── models.py  ├── config.py  ├── seed.py  ├── migrations/  ├── Pipfile  └── Pipfile.lock



