# Django-DDD-Template

A **Django project template** following **Domain-Driven Design (DDD)** principles, inspired by real-world financial systems.  
This template provides a clean architecture for building maintainable, scalable, and reusable Django applications.

---

## 🚀 Features

- **Clean architecture** aligned with DDD
- **Business logic inside models** (no direct manipulation in views)
- **Dependency inversion** for services (decoupled business logic and external services)
- **Strict rules enforced by pre-commit**:  
  - Type hints required for parameters and return values  
  - Linting (`black`, `isort`, `mypy`)  
  - YAML linting  
- **Environment-based settings** (`development.py`, `production.py`)
- **Centralized logging** (ready to integrate with external systems)
- **Serializer-only request/response handling** (all API views must use DRF serializers)
- **No inheritance > 1 layer, no Django signals** (simplicity & readability)

---

## 📂 Project Structure

```
config/ # Django config & environment settings
orders/ # Example domain app
services/ # External services (with interfaces + implementations)
utils/ # Shared helpers
manage.py # Django entrypoint
```

---

## ⚙️ Setup

```bash
# Clone the repo
git clone https://github.com/hamze/django_ddd_template.git
cd django_ddd_template

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Start development server
python manage.py runserver
```

## 🧪 Test Dependency Inversion

Visit the following URL to test the dependency inversion setup:
```commandline
http://127.0.0.1:8000/order/pay
```

## 🧑‍💻 Development Rules

- All business logic lives in models (methods).
- Views must only:
  - Validate input/output with serializers
  - Call model methods for business actions
  - Return responses using DRF serializers
- Always use logger instead of print().
- Follow pre-commit rules before committing.

## 📜 License
MIT