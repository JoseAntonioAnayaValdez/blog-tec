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

@cat_bp.route('/cat/delete/<int:id>')
def delete_category(id):
    categories = Category.query.get(id)
    if categories:
        db.session.delete(categories)
        db.session.commit()
    return redirect(url_for('cat.list_category'))

#modificar posts
@cat_bp.route('/cat/update/<int:id>', methods=['GET','POST'])
def update_category(id):
    categories = Category.query.get(id)
    if request.method == 'POST':
        categories.name = request.form['name']
        db.session.commit()
        # flash('Category created successfully!', 'success')
        return redirect(url_for('cat.list_category'))
    
    return render_template('category/update_category.html', category=categories)


