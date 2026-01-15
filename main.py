from fastapi import FastAPI
import requests
from database import get_connection

app = FastAPI()

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="",
        password="",   
        database="user_management"
    )



@app.get("/")
def home():
    return {"message": "User API is running"}


@app.post("/add-user")
def add_user(
    name: str,
    email: str,
    gender: str,
    phone: str,
    place: str,
    age: int
):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO user_details (name, email, gender, phone, place, age)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, gender, phone, place, age))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User stored successfully"}


@app.get("/get-users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_details")
    rows = cursor.fetchall()

    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "gender": row[3],
            "phone": row[4],
            "place": row[5],
            "age": row[6]
        })

    cursor.close()
    conn.close()

    return users


@app.get("/fetch-external-users")
def fetch_external_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

    conn = get_connection()
    cursor = conn.cursor()

    for u in data:
        query = """
        INSERT INTO user_details (name, email, gender, phone, place, age)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            u["name"],
            u["email"],
            "Not Specified",
            u["phone"],
            u["address"]["city"],
            25
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "External users fetched and stored successfully"}
