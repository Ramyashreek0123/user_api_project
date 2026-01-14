# User API Project

This is a FastAPI project for managing users. It allows adding users, fetching users from the database, and fetching external users from an API.

---

## Project Structure

user_api_project/
│
├─ main.py # FastAPI application
├─ setup.sql # SQL script to create database and table
├─ requirements.txt # Python dependencies
├─ .gitignore # Files/folders to ignore in GitHub
└─ README.md # Project instructions

---

## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/<your-username>/user_api_project.git
cd user_api_project


2. Create and activate virtual environment
python -m venv venv

# Activate
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac


3. Install dependencies
pip install -r requirements.txt


4. Setup MySQL database

Make sure MySQL is installed.

Run the SQL script:

mysql -u root -p < setup.sql

This will create database user_management and table user_details.


5. Run the FastAPI app
uvicorn main:app --reload

App will run at: http://127.0.0.1:8080/

Swagger UI (for testing endpoints): http://127.0.0.1:8080/docs

API Endpoints

GET / → Check if API is running

POST /add-user → Add a user

GET /get-users → Fetch all users from DB

GET /fetch-external-users → Fetch and store users from external API


---
```
