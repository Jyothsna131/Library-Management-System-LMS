
from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
app=Flask(__name__)

#In-Memory storage for books and members
books=[]
members=[]

def paginate(data,page,limit):
    start=(page-1)*limit
    end=start+limit
    return data[start:end]

#Home route
@app.route('/') #app.route(rule, options)
def home():
    return render_template('lms.html', books=books, members=members)

#CRUD operations for books
#Get all the books exists in the memory
@app.route('/books',methods=['GET'])
def manage_books():
    return render_template('books2.html')

@app.route('/books/get',methods=['GET'])
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
def add_book():
    data=request.get_json()
    data['id']=len(books)+1
    books.append(data)
    return jsonify({'message':'Book added Successfully'}), 201
    #return redirect(url_for('home'))


@app.route('/books/update/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    data=request.get_json()
    for book in books:
        if book['id']==book_id:
            book.update(data)
            return jsonify({'message':'Book updated Successfully','book':book}),200
        return jsonify({'error':'Book not found'}), 404

@app.route('/books/delete/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    global books
    books=[book for book in books if book['id']!=book_id]
    return jsonify({'message':'Book deleted Successfully'}), 200


#CRUD for members
@app.route('/members',methods=['GET'])
def manage_members():
    return render_template('members.html')

@app.route('/members/get',methods=['GET'])
def get_members():
    page=int(request.args.get('page',1))
    limit=int(request.args.get('limit',10))
    paginated_members=paginate(members,page,limit)
    return jsonify({'data':paginated_members}), 200

@app.route('/members/add',methods=['POST'])
def add_member():
    data=request.get_json()
    data['id']=len(members)+1
    members.append(data)
    return jsonify({'message':'Member added Successfully','member':data}), 201

@app.route('/members/update/<int:member_id>',methods=['PUT'])
def update_member(member_id):
    data=request.get_json()
    for member in members:
        if member['id']==member_id:
            member.update(data)
            return jsonify({'message':'Member updated Successfully','member':member}), 200
    return jsonify({'error':'Member not found'}), 404

@app.route('/members/delete/<int:member_id>',methods=['DELETE'])
def delete_member(member_id):
    global members
    members=[member for member in members if member['id']!=member_id]
    return jsonify({'message':'Member deleted Successfully'}), 200
'''
# Token-based authentication
@app.before_request
def authenticate():
    token=request.headers.get('Authorization')
    if request.endpoint in ['home',None]:
        return
    if token!='Bearer my-secret-token':
        return jsonify(nullcontext)
'''

if __name__=="__main__":
    app.run(debug=True) #app.run(host, port, debug, options)