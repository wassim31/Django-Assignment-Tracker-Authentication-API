# Django Assignment Tracker & Authentication API

This project is a full-featured Django REST API that implements secure user authentication and a real-time assignment tracking system. It was developed as part of a backend development assignment.

## 🔐 Authentication Features

- Built with Django's built-in authentication system and Django REST Framework's token-based authentication.
- Secure password hashing and storage using Django's default PBKDF2.
- Endpoints:
  - **User Registration** with OTP validation and email verification.
  - **Login** and **Logout** using token-based authentication.
  - **Password Reset** functionality with secure email-based reset flow.
- Full unit test coverage for all authentication-related endpoints.

## 📋 Assignment Tracking

- A dedicated model to track assignments with the following fields:
  - `name`: assignment name
  - `description`: details about the assignment
  - `status`: one of `todo`, `in progress`, `done`, `error`
  - `created_at`, `updated_at`: auto-managed timestamps
  - `assignee`: ForeignKey to the user
- REST API endpoints include:
  - Filtering, sorting, pagination, and search support.
  - Full CRUD operations (Create, Read, Update, Delete).
- All endpoints are protected with appropriate permissions.

## 🗃️ Database

- Powered by **PostgreSQL**, fully integrated with Django.
- Extended with **TimescaleDB** for time-series optimizations and performance tuning on timestamped assignment data.
- Demonstrates optimized queries for time-based operations.

## 🧪 Testing

- Unit tests implemented for:
  - User registration, login, logout, password reset.
  - Assignment creation, update, deletion, and retrieval.

## API Endpoints (must be a SwaggerAPI template, DRF includes built-in postman for testing)

### 1- Accounts endpoints (Using APIView)

1. **User account Information:** `/accounts/`
    - Method: `GET`
    - Requires authentication

2. **User account Change:** `/accounts/change/`
    - Method: `POST`
    - Requires authentication
    - Update user information (first name, last name)

3. **User Login:** `/accounts/login/`
    - Method: `POST`
    - Input: Email and password
    - Returns user information

4. **User Signup:** `/accounts/signup/`
    - Method: `POST`
    - Input: First name, last name, email, and password
    - Returns success message

5. **OTP Email account Activation:** `/accounts/activate-account/`
   
   - please get the activation code from the tty , due to the issue
   [#1](https://github.com/wassim31/attraxia_django_assessment/issues/1)

    - Method: `POST`
    - Input: Activation code
    - Activates user accounts so that users can login

6. **User Logout:** `/accounts/logout/`
    - Method: `POST`
    - Requires authentication
    - Logs out the user

7. **Password Reset Request:** `/accounts/password-reset/`
    - Method: `POST`
    - Input: Email
    - Sends a verification code for password reset to the user's email

8. **Password Reset Verify:** `/accounts/password-reset/verify/`
    - Method: `POST`
    - Input: Verification code and new password
    - Resets the user's password



9. **Password Change:** `/accounts/password-change/`
    - Method: `POST`
    - Requires authentication
    - Input: Old password and new password
    - Changes the user's password

### 2- Assignments endpoints (using ViewSet)

- Just type : `127.0.0.1:8000/assignments` (use DRF postman-like page) or curl and specify the http method
