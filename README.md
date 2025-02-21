# **Entities API**

This is an API for managing entities, where you can register, list, update, and delete entities. The API also has authentication routes for user login and registration.

## **API Endpoints**

### **Auth Routes**

#### **POST** `/auth/login`
Authenticates a user.

**Body:**
```json
{
  "username": "string",
  "password": "string"
}
```
**Response:**
```json
{
    "message": "login realizado com sucesso."
}
```

#### **POST** `/auth/register`
Registers a new user.

**Body:**
```json
{
  "username": "string",
  "password": "string"
}
```
**Response:**
```json
{
  "message": "usuário registrado com sucesso."
}
```

### **Entities Routes**

#### **POST** `/entities`
Creates a new entity.

**Body:**
```json
{
  "name": "string",
  "description": "string",
  "image": "string"
}

```
**Response:**
```json
{
  "message": "entidade criada com sucesso."
}
```

#### **GET** `/entities`
Lists entities. You can filter by IDs by passing an array in the ids parameter.

**Body:**
```json
{
  "ids": array of integer
}

```
**Response:**
```json
{
  "result": [
    {
      "id": 1,
      "name": "Entity 1",
      "description": "Description of the entity.",
      "image": "images/entity_1.png"
    },
    {
      "id": 2,
      "name": "Entity 2",
      "description": "Description of the entity.",
      "image": "images/entity_2.png"
    }
  ]
}
```

#### **PUT** `/entities/{id}`
Updates an existing entity.

**Body:**
```json
{
  "name": "string",
  "description": "string",
  "image": "string"
}

```
**Response:**
```json
{
  "message": "entidade atualizada com sucesso."
}
```

#### **DELETE** `/entities/{id}`
Deletes an entity.

**Response:**
```json
{
  "message": "entidade excluída com sucesso."
}
```

# Installation and Configuration

## Clone the repository:
```
git clone https://github.com/pistorello/umbra-foundation-api.git
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Configure database - db_connection.py:
```
CONN = MySQLDatabase(
  host='your_host'
  database='your_database'
  user='your_user'
  password='your_password'
)
```

## Run database migrations:
```
python migrantions.py migrate
```

## Start the server:
```
python app.py
```

## Access the API at http://localhost:5000

# Technologies
* Flask
* Peewee
