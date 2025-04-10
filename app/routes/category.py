from app import db
from app.models.category import Category
from flask import Blueprint, render_template, request, redirect, url_for, flash


cat_bp = Blueprint('cat', __name__    )

@cat_bp.route('/')
def list_category():
    categories = Category.query.all()
    return render_template('category/list_category.html', categories=categories)

@cat_bp.route('/create', methods=['GET', 'POST'])
def create_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name = name)

        db.session.add(new_category)
        db.session.commit()

        return redirect(url_for('cat.list_category'))
    
    # Aqui sigue si es GET
    categories = Category.query.all()
    return render_template('category/create_category.html', categories=categories)

# @post_bp.route('/posts/delete/<int:id>')
# def delete_post(id):
#     post = Post.query.get(id)
#     if post:
#         db.session.delete(post)
#         db.session.commit()
#     return redirect(url_for('posts.list_posts'))

# #modificar posts
# @post_bp.route('/post/update/<int:id>', methods=['GET','POST'])
# def update_post(id):
#     post = Post.query.get(id)
#     if request.method == 'POST':
#         post.title = request.form['title']
#         post.category_id = request.form['category_id']
#         post.content = request.form['content']
#         db.session.commit()
#         return redirect(url_for('posts.list_posts'))
    
#     categories = Category.query.all()
#     return render_template('post/update_post.html', post=post, categories=categories)
