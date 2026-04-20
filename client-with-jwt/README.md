Flask Notes API

Description

Flask Notes API is a backend application built with Flask that allows users to register, log in, and manage personal notes securely. Authentication is handled using JSON Web Tokens (JWT), ensuring that each user can only access their own data.

⸻

Features

* User registration and login
* JWT-based authentication
* Password hashing with bcrypt
* Create, read, update, and delete notes (CRUD)
* User-specific data protection
* Pagination for notes
* SQLite database

⸻

Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-Bcrypt
* Flask-JWT-Extended
* SQLite