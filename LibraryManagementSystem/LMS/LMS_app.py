
from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
app=Flask(__name__)


#In-Memory storage for books and members
books=[]
members=[]
users_cred = {"admin": generate_password_hash("password123")}
app.config['JWT_SECRET_KEY'] = '123Secret789'  # Ensure this is set
jwt = JWTManager(app)

def paginate(data,page,limit):
    start=(page-1)*limit
    end=start+limit
    return data[start:end]

#Home route
@app.route('/home') #app.route(rule, options)
@jwt_required()
def home():
    return render_template('lms.html', books=books, members=members)

#CRUD operations for books
#Get all the books exists in the memory
@app.route('/books',methods=['GET'])
#@jwt_required()
def manage_books():
    return render_template('books.html')

@app.route('/books/get',methods=['GET'])
@jwt_required()
def get_books():
    title=request.args.get('title')
    author=request.args.get('author')
    page=int(request.args.get('page',1))
    limit=int(request.args.get('limit',10))

    filtered_books=books

    #filter based on the input
    if title:
        filtered_books=[book for book in filtered_books if title.lower() in book['title'].lower()]
    if author:
        filtered_books=[book for book in filtered_books if author.lower() in book['author'].lower()]

    paginated_books=paginate(filtered_books,page,limit)
    if len(filtered_books)==0:
        return jsonify({'message':'No Books are existed with provided search criteria. Please alter the search or contact the Library Admin'}), 200
    return jsonify({'data':paginated_books}), 200
    #return redirect(url_for('lms'))

@app.route('/books/add',methods=['POST'])
@jwt_required()
def add_book():
    data=request.get_json()
    data['id']=len(books)+1
    books.append(data)
    return jsonify({'message':'Book added Successfully'}), 201
    #return redirect(url_for('home'))


@app.route('/books/update/<int:book_id>',methods=['PUT'])
@jwt_required()
def update_book(book_id):
    data=request.get_json()
    for book in books:
        if book['id']==book_id:
            book.update(data)
            return jsonify({'message':'Book updated Successfully','book':book}),200
        return jsonify({'error':'Book not found'}), 404

@app.route('/books/delete/<int:book_id>',methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    global books
    books=[book for book in books if book['id']!=book_id]
    return jsonify({'message':'Book deleted Successfully'}), 200


#CRUD for members
@app.route('/members',methods=['GET'])
#@jwt_required()
def manage_members():
    return render_template('members.html')

@app.route('/members/get',methods=['GET'])
@jwt_required()
def get_members():
    page=int(request.args.get('page',1))
    limit=int(request.args.get('limit',10))
    paginated_members=paginate(members,page,limit)
    return jsonify({'data':paginated_members}), 200

@app.route('/members/add',methods=['POST'])
@jwt_required()
def add_member():
    data=request.get_json()
    data['id']=len(members)+1
    members.append(data)
    return jsonify({'message':'Member added Successfully','member':data}), 201

@app.route('/members/update/<int:member_id>',methods=['PUT'])
@jwt_required()
def update_member(member_id):
    data=request.get_json()
    for member in members:
        if member['id']==member_id:
            member.update(data)
            return jsonify({'message':'Member updated Successfully','member':member}), 200
    return jsonify({'error':'Member not found'}), 404

@app.route('/members/delete/<int:member_id>',methods=['DELETE'])
@jwt_required()
def delete_member(member_id):
    global members
    members=[member for member in members if member['id']!=member_id]
    return jsonify({'message':'Member deleted Successfully'}), 200
@app.route('/login',methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username in users_cred  and check_password_hash(users_cred[username], password):
        # Create JWT token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token, redirect_url='/home'), 200
    else:
        return jsonify(message="Invalid credentials"), 401

if __name__=="__main__":
    app.run(debug=True) #app.run(host, port, debug, options)