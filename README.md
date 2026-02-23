---

# 📦 FastAPI Campaign CRUD API

A simple FastAPI-based REST API for managing marketing campaigns.

This project demonstrates:

* Basic CRUD operations
* Path & query parameters
* Request body handling
* HTTP status codes
* In-memory storage using a Python dictionary

> ⚠️ Note: This project uses an in-memory dictionary instead of a real database. Data will reset when the server restarts.
> The goal is to learn API design and FastAPI fundamentals.

---

## 🚀 Tech Stack

* Python 3.10+
* FastAPI
* Uvicorn (ASGI server)

---

## 📂 Project Structure

```
.
├── main.py
└── README.md
```

---

## 🔧 Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the Server

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

Since the app uses:

```python
app = FastAPI(root_path="/api/v1")
```

The base API path is:

```
http://127.0.0.1:8000/api/v1
```

---

## 📖 Interactive API Docs

FastAPI automatically generates documentation.

* Swagger UI:

  ```
  http://127.0.0.1:8000/api/v1/docs
  ```

* ReDoc:

  ```
  http://127.0.0.1:8000/api/v1/redoc
  ```

---

## 🗂 Data Model

Each campaign has:

```json
{
  "campaign_id": int,
  "name": string,
  "due_date": datetime,
  "created_at": datetime
}
```

---

## 🔌 API Endpoints

### ✅ GET `/`

Health check endpoint.

Response:

```json
{
  "message": "Hello There!"
}
```

---

### ✅ GET `/campaigns`

Get all campaigns.

Response:

```json
{
  "campaigns": { ... }
}
```

---

### ✅ GET `/campaigns/{id}`

Get campaign by ID.

Returns:

* `200 OK` if found
* `404 Not Found` if not found

---

### ✅ POST `/campaigns`

Create a new campaign.

Request body:

```json
{
  "name": "New Campaign",
  "due_date": "2025-12-31"
}
```

Returns:

* `201 Created`

---

### ✅ PUT `/campaigns/{id}`

Update an existing campaign.

Request body:

```json
{
  "name": "Updated Campaign",
  "due_date": "2026-01-01"
}
```

---

### ✅ DELETE `/campaigns/{id}`

Delete a campaign.

Returns:

* `204 No Content` if successful
* `404 Not Found` if campaign does not exist

---

## 🧠 What This Project Demonstrates

* RESTful API design
* Path parameters
* Request validation basics
* CRUD operations
* HTTP status handling
* In-memory state management

---

## ⚠️ Limitations

* No persistent storage
* No validation via Pydantic models
* No authentication
* No database integration
* Random campaign_id generation (may collide)

---

## 🔜 Next Steps (Improvements)

* Add Pydantic models for request validation
* Replace dictionary with SQL database
* Add proper error handling
* Add unit tests
* Implement dependency injection
* Add authentication

---

## 📌 Learning Goal

This project focuses purely on:

> Understanding how to build REST APIs using FastAPI.

Database integration will be added in future iterations.

---