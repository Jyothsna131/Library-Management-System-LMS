import json
import unittest
from LMS_app import app
import pytest



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True  # Enable testing mode
        self.token = None

        global books
        books = [
            {'id': 1, 'title': 'Book1', 'author': 'Author1'},
            {'id': 2, 'title': 'Book2', 'author': 'Author2'}
        ]

        global members
        members = [
            {'id': 1, 'Name': 'Name1', 'Email': 'Email1'},
            {'id': 2, 'Name': 'Name2', 'Email': 'Email2'}
        ]
        # Perform login to get the token
        login_response = self.app.post('/login', json={
            'username': 'admin',  # Replace with valid username
            'password': 'password123'  # Replace with valid password
        })

        # Assert that login is successful
        self.assertEqual(login_response.status_code, 200, "Login failed during setup")

        # Extract the token from the login response
        self.token = login_response.json.get('access_token', None)

        # Ensure the token is retrieved
        self.assertIsNotNone(self.token, "Token not generated during login")



    # Test login endpoint -- success
    def test_login_success(self):
        response = self.app.post('/login', json={
            'username': 'admin',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.token = data['access_token']  # Save the token for future tests
        self.assertIn('access_token', data)

    # Test login endpoint -- success
    def test_login_Invalid(self):
        response = self.app.post('/login', json={
            'username': 'adminInvalid',
            'password': 'passwordInvalid'
        })
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Invalid credentials')

    #Add book with token
    def test_AddBook_token(self):
        response = self.app.post('/books/add', json={
            'title': 'TestBook',
            'author': 'TestAuthor'
        },
        headers = {'Content-type':'application/json',
            'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Book added Successfully')

    # Add book without token
    def test_AddBook_withoutToken(self):
        response = self.app.post('/books/add', json={
            'title': 'TestBook',
            'author': 'TestAuthor'
        },
        headers={'Content-type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_get_books(self):
        response = self.app.get('/books/get', query_string={'page': 1, 'limit': 10},
                                headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)


    def test_update_book(self):
        response = self.app.put('/books/update/1', json={
            'title': 'UpdateBook',
            'author': 'UpdateAuthor'
        }, headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.app.delete('/books/delete/2',  headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)

    def test_AddMember_token(self):
        response = self.app.post('/members/add', json={
            'Name': 'TestName',
            'Email': 'TestEmail'
        },
        headers={'Content-type': 'application/json',
                                          'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Member added Successfully')

    def test_get_members(self):
        response = self.app.get('/members/get', query_string={'page': 1, 'limit': 10},
                                headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)

    def test_update_member(self):
        response = self.app.put('/members/update/1', json={
            'Name': 'UpdateName',
            'Email': 'UpdateEmail'
        }, headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)

    def test_delete_member(self):
        response = self.app.delete('/members/delete/2',  headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
