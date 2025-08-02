# 📦 Full Stack User Management System

A full-stack CRUD system using **one shared backend** (Flask + MySQL) with:

- ✅ A **Web App** (Flask + Jinja + HTML/CSS/Bootstrap)

---

### 📂 Location: `/web/` (uses backend directly)

---

## 📁 Project Structure

```
project-root/
├── backend/            # Flask API + MySQL connection
│   ├── app.py
│   ├── auth/
│   ├── templates/
│   ├── static/
│   └── database/
│
├── frontend/                # Web frontend (Jinja templates)
│   ├── templates/
│   └── static/

```

---
## 🔌 Shared Backend API

**Backend**: `Flask` + `MySQL` with RESTful routes

### Example Endpoints

- `POST /api/register` – Register a new user
- `POST /api/login` – Authenticate a user
- `GET /api/users` – Get all users (admin only)
- `PUT /api/edit-user/<id>` – Edit user details
- `DELETE /api/delete-user/<id>` – Delete user

---
## 🌐 Web App (Flask + Jinja)

### Features:

- Admin/User registration
- Login via HTML form
- View/edit/delete users
- Flash messages for feedback
