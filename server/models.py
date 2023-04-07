from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.Integer)

    @validates('name')
    def name_required(self, key, name):
        names = Author.query.filter(Author.name).all()
        if not name:
            raise ValueError("Failed name validation. Name is required.")
        elif name in names:
            raise ValueError("Failed name validation. Name must be unique.")
        return name
    
    @validates('phone_number')
    def phone_number_validation(self, key, phone_number):
        if len(str(phone_number)) != 10:
            raise ValueError("Failed phone number validation. Number must be 10 digits.")
        return phone_number


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    @validates('title')
    def title_validation(self, key, title):
        if "Won't Believe" and "Secret" and "Top" and "Guess" not in title:
            raise ValueError("Failed title validation. Title required and must be clickbaity.")
        return title


    @validates('content')
    def content_validation(self, key, content):
        if len(content) < 250:
            raise ValueError("Failed content validation. Content must be greater than 250 words.")
        return content
    
    @validates('summary')
    def summary_validation(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Failed summary validation. Summary must be less than 250 words.")
        return summary
        
    @validates('category')
    def category_validation(self, key, category):
        if category != "Fiction" and category != "Non-Fiction":
            raise ValueError("Failed category validation. Category must be Fiction or Non-Fiction.")
        return category