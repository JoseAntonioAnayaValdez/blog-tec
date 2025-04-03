from app import db
from app.models.post import Post
from app.models.category import Category
from flask import Blueprint, render_template, request, redirect, url_for, flash


post_bp = Blueprint('post', __name__, url_prefix='/posts')

@post_bp.route('/')
def list_posts():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template('post/listpost.html', posts=posts, categories=categories)
