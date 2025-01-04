# Library-Management-System
This project is a simple Library Management System built using Flask, providing CRUD operations for books and members. The application includes features such as pagination, search functionality, and a user-friendly home page with token based authentication.
#
## Features

### 1. CRUD Operations for Books and Members:
- Add, update, delete, and retrieve *books* and *members*

### 2. Search and Pagination:
- Filter books by title or author with case-insensitive search functionality.
- Paginate results for both books and members to improve navigation and usability.

### 3. Web Interface:
- A basic home page with a warm welcome message for users.
- User can add, search, update and delete a book and member.

#
## Technology Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Javascript
- **Database:** In-memory storage (lists for books and members)
- **Language:** Python 3.x

#
## Setup and Execution
### Pre-requisites
- Python 3.x installed on your system
### Steps to Run the Project

1. **Clone the repository**
   ```
       git clone <repository-url>
       cd Library-Management-System-LMS
   ```
2. **Install dependencies**
   ```
   pip install flask
   pip install flask_jwt_extended
   pip install werkzeug.security
   ```
3. **Run the application**
   ```
      python LMS_app.py
   ```

4. **Access the application:** Open a browser and navigate to:
    [http:://127.0.0.1:5000/login](url)

5. **Login Credentials:**
   ```
   username: admin
   password: password123
   ```

#
## API Endpoints
### Books
#### 1. Get All Books:
 - **URL:** /books/get
  - **Method:** GET
  - **Query Parameters:**
      - **title** (optional): Filter books by title
      - **author** (optional): Filter books by author
      - **page** (optional): Page number (default: 1)
      - **limit** (optional): Number of results per page (default:10)
  - **Response:** List of books (filtered and paginated)
#### 2. Add a Book:
  - **URL:** /books/add
  - **Method:** POST
  - **payload:**
     ```
     json
     {
     "title": "Book Title",
     "author": "Author Name",
     "published_year": 2025
     }
       ```
  - **Response:** Confirmation of the added book
#### 3. Update a Book:
  - **URL:** /books/update/<book_id>
  - **Method:** PUT
  - **payload:** Fields to update
  - **Response:** Confirmation of the updated book
        
#### 4. Delete a Book:
  - **URL:** /books/delete/<book_id>
  - **Method:** DELETE
  - **Response:** Confirmation of the deleted book

### Members
#### 1. Get All Members:
  - **URL:** /members/get
  - **Method:** /GET
  - **Query Parameters:**
      - **page** (optional): Page number (default: 1)
      - **limit** (optional): Number of results per page (default: 10)
  - **Response:** List of members (paginated)
#### 2. Add a Member:
  - **URL:** /members/add
  - **Method:** /POST
  - **Payload:**   
  ```
  json
  {
  "name": "Member Name",
  "email": "member@example.com"
  }
```
- **Response:** Confirmation of the added member
#### 3. Update a Member:
  - **URL:** /members/update/<member_id>
  - **Method:** PUT
  - **payload:** Fields to update
  - **Response:** Confirmation of the updated member
        
#### 4. Delete a Member:
  - **URL:** /members/delete/<member_id>
  - **Method:** DELETE
  - **Response:** Confirmation of the deleted member

# 
# Assumptions and Limitations
1. **Single User Login:** The current system supports only a single user login with a predefined set of credentials. It does not allow multiple user logins simultaneously.
2. **No User Account Creation:** The system does not include functionality for creating user accounts. Users are required to use the predefined credentials to log in. There is no registration mechanism in place.
3. **No Role-Based Authentication:** The authentication mechanism is basic and does not implement role-based access control. A logged-in user has unrestricted access to all system features without any differentiation between different roles.
4. **No Database:** The system uses an in-memory database, meaning that the data (books and members) is lost when the application restarts. No persistent storage mechanism (e.g., SQL or NoSQL database) is in place.
5. **Supports Basic Navigation:** The system supports basic navigation between pages after the user logs in. However, there are no advanced features such as sorting, back-navigation or pagination implemented for these sections.
6. **No Session Expiry:** The application does not implement session expiry. Once the user logs in, the access token remains valid indefinitely unless the user manually logs out or the browser session is cleared. There is no automatic expiration or refresh of the session token.


        
        
      
           
   
