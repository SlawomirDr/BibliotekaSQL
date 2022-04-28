from app import db

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), index=True)
   author = db.Column(db.String(100), index=True)
   available_status = db.relationship("Available", backref="shelf", lazy="dynamic")
   author_details = db.relationship("Author", backref="author_name", lazy="dynamic")
 #  author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
   
   def __str__(self):
       return f"<Book {self.title}>"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), db.ForeignKey('book.author'))
#    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Author {self.name}>"

class Available(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    on_shelf = db.Column(db.Boolean)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Available {self.book_id} {self.on_shelf}>"