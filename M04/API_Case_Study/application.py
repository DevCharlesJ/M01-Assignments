from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120))

    def toDict(self):
        return {
                "name" : self.name,
                "author" : self.author,
                "publisher" : self.publisher
            }

    def __repr__(self):
        return f"{self.name} - {self.author}"

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return "Hello"


@app.route("/books")
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        output.append(book.toDict())
    return {"books": output}

@app.route("/books/<id>")
def get_book(id):
    res = Book.query.get_or_404(id)

    if isinstance(res, Book):
        return res.toDict()
    else:
        return res

@app.route("/books", methods=['POST'])
def add_book():
    book = Book(
        name=request.json['name'],
        author=request.json['author'],
        publisher=request.json['publisher'],
    )

    db.session.add(book)
    db.session.commit()
    return {'id': book.id}


@app.route("/books/<id>", methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}

    db.session.delete(book)
    db.session.commit()
    return {"message": "YEEET!!!"}