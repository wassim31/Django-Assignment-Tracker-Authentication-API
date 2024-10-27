## API Endpoints (must be a SwaggerAPI template, DRF includes built-in postman for testing)

### 1- Accounts Module API Documentation

1. **User account Information:** `/accounts/`
    - Method: `GET`
    - Requires authentication

2. **User account Change:** `/accounts/change/`
    - Method: `POST`
    - Requires authentication
    - Update user information (first name, last name)

3. **User Login:** `/login/`
    - Method: `POST`
    - Input: Email and password
    - Returns user information

4. **User Signup:** `/signup/`
    - Method: `POST`
    - Input: First name, last name, email, and password
    - Returns success message

5. **OTP Email account Activation:** `/activate-account/`
   
   - please get the activation code from the tty , due to the issue
   [#1](https://github.com/wassim31/attraxia_django_assessment/issues/1)
    ![image](https://github.com/user-attachments/assets/dca74bb1-1682-43c4-a0b8-19729bff2306)

    - Method: `POST`
    - Input: Activation code
    - Activates user accounts so that users can login

6. **User Logout:** `/logout/`
    - Method: `POST`
    - Requires authentication
    - Logs out the user

7. **Password Reset Request:** `/password-reset/`
    - Method: `POST`
    - Input: Email
    - Sends a verification code for password reset to the user's email

8. **Password Reset Verify:** `/password-reset/verify/`
    - Method: `POST`
    - Input: Verification code and new password
    - Resets the user's password



9. **Password Change:** `/password-change/`
    - Method: `POST`
    - Requires authentication
    - Input: Old password and new password
    - Changes the user's password

### 2- Assignment Module API Documentation

### 1. List Assignments
- **URL**: `/assignments/`
- **Method**: `GET`
- **Requires Authentication**: Yes
- **Description**: Lists all assignments with pagination, filtering, searching, and sorting.

---

### 2. Create Assignment
- **URL**: `/assignments/`
- **Method**: `POST`
- **Requires Authentication**: Yes
- **Description**: Creates a new assignment.
- **Input**:
  - `name`: The name of the assignment
  - `description`: A brief description of the assignment
  - `status`: Assignment status (`todo`, `in_progress`, `done`, `error`)
  - `assignee`: ID of the user assigned to this assignment

---

### 3. Retrieve Assignment Details
- **URL**: `/assignments/<id>/`
- **Method**: `GET`
- **Requires Authentication**: Yes
- **Description**: Retrieves detailed information for a specific assignment by ID.

---

### 4. Update Assignment
- **URL**: `/assignments/<id>/`
- **Method**: `PUT` or `PATCH`
- **Requires Authentication**: Yes
- **Description**: Updates an existing assignment. If the assignment status is changed, a status log is created.
- **Input**:
  - Any of the assignment fields (`name`, `description`, `status`, `assignee`)

---

### 5. Delete Assignment
- **URL**: `/assignments/<id>/`
- **Method**: `DELETE`
- **Requires Authentication**: Yes
- **Description**: Deletes a specific assignment by ID.

---

### 6. List Assignment Status Logs
- **URL**: `/assignment-status-logs/`
- **Method**: `GET`
- **Requires Authentication**: Yes
- **Description**: Lists all status change logs for assignments.

---

### 7. Retrieve Assignment Status Log Details
- **URL**: `/assignment-status-logs/<id>/`
- **Method**: `GET`
- **Requires Authentication**: Yes
- **Description**: Retrieves details of a specific assignment status log by ID.

---

## Notes
- All endpoints require user authentication.
- Assignment status change logs provide a record of every update to an assignment's status, including the old status, new status, and the timestamp of the change.
