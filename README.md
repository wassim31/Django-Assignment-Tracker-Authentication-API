### API Endpoints (i read that the norm is to use SwaggerAPI in prod env) 

1. **User Account Information:** `/account/`
    - Method: `GET`
    - Requires authentication

2. **User Account Change:** `/account/change/`
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

5. **Account Activation:** `/activate-account/`
    please get the activation code from the tty , due to the issue
    ![image](https://github.com/user-attachments/assets/dca74bb1-1682-43c4-a0b8-19729bff2306)

    -Method: `POST`
    - Input: Activation code
    - Activates user account so that users can login

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

9. **Email Change Request:** `/email-change/`
    - Method: `POST`
    - Requires authentication
    - Sends a verification code for email change to the user's email

10. **Email Change Verify:** `/email-change/verify/`
    - Method: `POST`
    - Input: Verification code and new email
    - Changes the user's email

11. **Password Change:** `/password-change/`
    - Method: `POST`
    - Requires authentication
    - Input: Old password and new password
    - Changes the user's password
