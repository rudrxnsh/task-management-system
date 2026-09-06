# 🚀 Task Management System

> A practical **FastAPI backend project** built to strengthen real-world backend development skills — from authentication and authorization to database integration, background processing, email notifications, validation, and API architecture.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/JWT-Authentication-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT">
</p>

---

## 📌 Overview

This project is a **RESTful task management backend** developed as a hands-on FastAPI practice project.

The goal was not just to create CRUD endpoints, but to understand how the different pieces of a modern backend fit together:

```text
Client
  │
  ▼
FastAPI Routes
  │
  ├── Validation
  ├── Authentication
  ├── Authorization
  ├── Business Logic
  └── Dependency Injection
  │
  ▼
SQLAlchemy ORM
  │
  ▼
PostgreSQL
```

The project also explores operations that should not unnecessarily block an API response, such as sending emails through background processing.

---

## ✨ What This Project Covers

### 🔐 Authentication & Security

- User registration
- User login
- Password hashing
- JWT-based authentication
- Token validation
- Protected routes
- Authentication dependencies
- Authorization / access control
- Handling invalid or expired authentication data

### 🗄️ Database & ORM

- PostgreSQL integration
- SQLAlchemy ORM
- Database models
- Database sessions
- CRUD operations
- Relationships between application data
- Separating database concerns from API schemas

### ✅ Validation & API Design

- Pydantic schemas
- Request validation
- Response schemas
- Type hints
- HTTP status codes
- `HTTPException`
- Structured API responses
- FastAPI dependency injection
- Automatic API documentation

### ⚡ Background Processing

The project demonstrates how work that does not need to block the API response can be handled in the background.

Example:

```mermaid
sequenceDiagram
    participant C as Client
    participant A as FastAPI
    participant B as Background Task
    participant M as Mail Service

    C->>A: Send request
    A->>A: Validate & process request
    A-->>C: Return API response
    A->>B: Schedule background task
    B->>M: Send email
    M-->>B: Email operation completed
```

### 📧 Email Integration

- Email service integration
- Sending application emails
- Background email processing
- Configuration through environment variables

### ⚙️ Configuration

- Environment-based configuration
- Secret management through `.env`
- Application settings
- Keeping credentials outside source code

---

## 🧠 Learning Map

The project connects several backend concepts into one application:

```mermaid
flowchart TD
    A["FastAPI Fundamentals"] --> B["Routing & Dependencies"]
    B --> C["Pydantic Validation"]
    C --> D["Authentication"]
    D --> E["JWT"]
    E --> F["Authorization"]

    B --> G["SQLAlchemy"]
    G --> H["PostgreSQL"]

    B --> I["Background Tasks"]
    I --> J["Email Service"]

    D --> K["Protected Endpoints"]
    F --> K
    H --> K
    J --> K
```

---

## 🏗️ Application Flow

A typical authenticated operation follows this pattern:

```mermaid
flowchart LR
    U["Client"] --> R["FastAPI Router"]
    R --> V["Validate Request"]
    V --> A["Authenticate"]
    A --> Z{"Authorized?"}

    Z -- "No" --> E["HTTP Error"]
    Z -- "Yes" --> S["Service / Application Logic"]
    S --> DB["SQLAlchemy"]
    DB --> P["PostgreSQL"]
    P --> S
    S --> R
    R --> U
```

This illustrates an important backend principle:

> **Authentication answers "Who are you?" while authorization answers "Are you allowed to do this?"**

---

## 🔐 Authentication Flow

```mermaid
flowchart TD
    A["Register"] --> B["Validate User Data"]
    B --> C["Hash Password"]
    C --> D["Store User in PostgreSQL"]

    D --> E["Login"]
    E --> F["Verify Credentials"]
    F --> G["Create JWT"]
    G --> H["Client Stores Access Token"]

    H --> I["Protected API Request"]
    I --> J["Extract Token"]
    J --> K["Validate JWT"]
    K --> L{"Valid?"}

    L -- "No" --> M["401 Unauthorized"]
    L -- "Yes" --> N["Continue Request"]
```

---

## 🧩 Core Architecture

The backend follows a modular structure so that related functionality can be kept together rather than putting the entire application into a single file.

A typical structure looks like:

```text
task-management-system/
│
├── src/
│   ├── user/
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── dtos.py
│   │   └── ...
│   │
│   ├── task/
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── dtos.py
│   │   └── ...
│   │
│   └── utils/
│       ├── settings.py
│       ├── mail.py
│       └── ...
│
├── .env
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
```

> **Note:** The exact structure may differ depending on the current implementation. The important idea is separation of concerns between routes, schemas/DTOs, models, utilities, and configuration.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **FastAPI** | REST API framework |
| **Pydantic** | Data validation and schemas |
| **SQLAlchemy** | ORM and database interaction |
| **PostgreSQL** | Relational database |
| **JWT** | Authentication tokens |
| **Password Hashing** | Secure credential storage |
| **Uvicorn** | ASGI application server |
| **Background Tasks** | Non-blocking auxiliary operations |
| **Email Service** | Application email notifications |
| **Environment Variables** | Configuration and secrets |

---

## 🚦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rudrxnsh/task-management-system.git
cd task-management-system
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file according to the settings expected by the project.

A typical configuration may look like:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/task_management

SECRET_KEY=your_secret_key
ALGORITHM=HS256

MAIL_USERNAME=your_email
MAIL_PASSWORD=your_email_password
MAIL_FROM=your_email
MAIL_SERVER=your_mail_server
MAIL_PORT=587
```

> ⚠️ **Never commit your real `.env` file, passwords, database credentials, JWT secrets, or email credentials.**

### 5. Start PostgreSQL

Create a PostgreSQL database and make sure the database connection configured in your environment matches the application settings.

### 6. Run the FastAPI application

```bash
uvicorn main:app --reload
```

The API should then be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 Interactive API Documentation

FastAPI automatically generates interactive API documentation.

Once the application is running:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to:

- Explore endpoints
- Send requests
- Test authentication
- Inspect request schemas
- Inspect response schemas
- Understand available API operations

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🔄 Request Lifecycle

One of the main things this project helped demonstrate is what happens between an incoming request and the final response.

```mermaid
flowchart TD
    A["HTTP Request"] --> B["FastAPI Router"]
    B --> C["Dependency Resolution"]
    C --> D["Request Validation"]
    D --> E["Authentication"]
    E --> F["Authorization"]
    F --> G["Application Logic"]
    G --> H["Database Operation"]
    H --> I["Response Schema"]
    I --> J["HTTP Response"]
```

If something fails at any stage, the application can return an appropriate HTTP error instead of continuing with invalid data or unauthorized access.

---

## ⚡ Why Background Tasks?

Some operations do not need to delay the user's API response.

For example:

```text
Without background processing:

Client
  ↓
API
  ↓
Save data
  ↓
Send email
  ↓
Wait for email operation
  ↓
Response
```

With background processing:

```text
Client
  ↓
API
  ↓
Save data
  ├──────────────► Background Task
  │                     ↓
  │                 Send Email
  ↓
Return Response
```

This project uses FastAPI background task capabilities to demonstrate this request/response pattern.

> Background tasks are useful for lightweight operations that can safely happen after the response. For large, long-running, or distributed workloads, a dedicated task queue/worker architecture would be a stronger next step.

---

## 🧪 Practical Backend Concepts Practiced

This project was used to practice the following concepts:

### FastAPI

- Application setup
- APIRouter
- Path and query parameters
- Request bodies
- Response models
- Dependency injection
- HTTP status codes
- HTTP exceptions
- Automatic OpenAPI documentation

### Authentication

- User registration
- Login
- Password hashing
- JWT creation
- JWT decoding
- Token validation
- Protected endpoints

### Authorization

- User permissions
- Role/access checks
- Restricting protected operations
- Separating authentication from authorization

### Database

- PostgreSQL
- SQLAlchemy models
- Sessions
- Queries
- CRUD operations
- Database relationships
- Persisting application state

### Pydantic

- DTOs / schemas
- Input validation
- Response serialization
- Type-safe request handling

### Application Architecture

- Modular project structure
- Separation of concerns
- Reusable dependencies
- Utility modules
- Configuration management

### Background Processing

- FastAPI `BackgroundTasks`
- Deferred operations
- Background email processing

### Email

- Mail configuration
- Sending application emails
- Integrating email operations with API workflows

---

## 🧭 What I Would Improve Next

This project is intentionally a learning-focused backend and can be extended significantly.

Possible next improvements:

```mermaid
flowchart LR
    A["Current API"] --> B["Automated Tests"]
    B --> C["Database Migrations"]
    C --> D["Redis / Caching"]
    D --> E["Dedicated Task Queue"]
    E --> F["Docker"]
    F --> G["CI/CD"]
    G --> H["Production Deployment"]
    H --> I["Monitoring & Logging"]
```

Potential additions include:

- [ ] Automated testing with Pytest
- [ ] Database migrations with Alembic
- [ ] Pagination and advanced filtering
- [ ] Redis caching
- [ ] Rate limiting
- [ ] Dedicated background workers
- [ ] Docker / Docker Compose
- [ ] CI/CD
- [ ] Production deployment
- [ ] Structured logging
- [ ] Monitoring and observability

---

## 💡 Key Takeaways

Building this project helped connect individual FastAPI concepts into a complete backend workflow.

Instead of learning features in isolation, the project demonstrates how:

```text
Authentication
      +
Authorization
      +
Validation
      +
Database
      +
Business Logic
      +
Background Processing
      +
Email
      ↓
Complete Backend API
```

The next goal is to take these fundamentals further through testing, performance optimization, distributed background processing, deployment, and production-oriented architecture.

---

## 📌 Project Status

**Status:** 🟢 Learning / Development

This project is primarily intended as a practical backend development and FastAPI learning project. The codebase will continue to evolve as additional backend concepts are explored.

---

## 🤝 Feedback

Suggestions, improvements, and constructive feedback are welcome.

If you notice a better architectural approach, security improvement, performance optimization, or cleaner implementation, feel free to open an issue or discussion.

---

## 👨‍💻 Author

**Rudransh**

- GitHub: [@rudrxnsh](https://github.com/rudrxnsh)

---

<p align="center">
  <sub>Built with Python 🐍 and FastAPI ⚡</sub>
</p>
