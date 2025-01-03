# Library-Management-System
This project is a simple Library Management System built using Flask, providing CRUD operations for books and members. The application includes features such as pagination, search functionality, and a user-friendly home page.
#
## Features

### 1. CRUD Operations for Books and Members:
- Add, update, delete, and retrieve *books* and *members*

### 2. Search and Pagination:
- Filter books by title or author with case-insensitive search functionality.
- Paginate results for both books and members to improve navigation and usability.

### 3. Web Interface:
- A basic home page with a warm welcome message for users.

#
## Technology Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML
- **Database:** In-memory storage (lists for books and members)
- **Language:** Python 3.

#
## Setup and Execution
### Pre-requisites
- Python 3.x installed on your system
### Steps to Run the Project

1. **Download the following files**:
   - `lms.html`
   - `LMS_app.py`

2. **Upload these files to PyCharm**:
   - Open PyCharm and create a new project.
   - Upload both the `lms.html` and `LMS_app.py` files to your project.

3. **Place the `lms.html` file inside the `templates` directory**:
   - In your project folder, create a folder named `templates` if it doesn't already exist.
   - Move the `lms.html` file into the `templates` folder.

4. **Run the Application**:
   - Run the `LMS_app.py` file in PyCharm. 
   - The Flask API will start, and you can access the application in your browser.

## Note:
Ensure that the Flask package is installed in your environment. If it's not already installed, you can install it using:
```
pip install flask
```
4. Access the application: Open a browser and navigate to:
    [http:://127.0.0.1:5000](url)

#
## API Endpoints
### Books
#### 1. Get All Books:
 - **URL:** /books
  - **Method:** GET
  - **Query Parameters:**
      - **title** (optional): Filter books by title
      - **author** (optional): Filter books by author
      - **page** (optional): Page number (default: 1)
      - **limit** (optional): Number of results per page (default:10)
  - **Response:** List of books (filtered and paginated)
#### 2. Add a Book:
  - **URL:** /books
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
  - **URL:** /books/<book_id>
  - **Method:** PUT
  - **payload:** Fields to update
  - **Response:** Confirmation of the updated book
        
#### 4. Delete a Book:
  - **URL:** /books/<book_id>
  - **Method:** DELETE
  - **Response:** Confirmation of the deleted book

### Members
#### 1. Get All Members:
  - **URL:** /members
  - **Method:** /GET
  - **Query Parameters:**
      - **page** (optional): Page number (default: 1)
      - **limit** (optional): Number of results per page (default: 10)
  - **Response:** List of members (paginated)
#### 2. Add a Member:
  - **URL:** /members
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
  - **URL:** /members/<member_id>
  - **Method:** PUT
  - **payload:** Fields to update
  - **Response:** Confirmation of the updated member
        
#### 4. Delete a Member:
  - **URL:** /members/<member_id>
  - **Method:** DELETE
  - **Response:** Confirmation of the deleted member

#


        
        
      
           
   
