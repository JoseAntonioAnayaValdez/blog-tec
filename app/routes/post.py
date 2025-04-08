from app import db
from app.models.post import Post
from app.models.category import Category
from flask import Blueprint, render_template, request, redirect, url_for, flash


post_bp = Blueprint('posts', __name__    )

@post_bp.route('/')
def list_posts():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template('post/listpost.html', posts=posts, categories=categories)

@post_bp.route('/create', methods=['GET', 'POST'])
def create_posts():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form.get('category_id')
        new_post = Post(title=title, content=content, category_id=category_id)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('posts.list_posts'))
    
    # Aqui sigue si es GET
    categories = Category.query.all()
    return render_template('post/createpost.html', categories=categories)

@post_bp.route('/posts/delete/<int:id>')
def delete_post(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('posts.list_posts'))

@post_bp.route('/post/update/<int:id>', methods=['GET','POST'])
def update_post(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.category_id = request.form['category_id']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('posts.list_posts'))
    
    categories = Category.query.all()
    return render_template('post/update_post.html', post=post, categories=categories)
