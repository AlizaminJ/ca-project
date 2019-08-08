from flask import render_template, flash, redirect, url_for, url_for
from app import app, db
from .forms import PostForm
from .models import Post
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()

    user = {'nickname': 'Sofus'}
    if form.validate_on_submit():
        post = Post(user_name=form.user_name.data, timestamp=datetime.utcnow(),title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))

    posts = Post.query.all()
    return render_template('index.html',
            title='CoDeAcademy',
            user=user,
            posts=posts,
            form=form)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Post submitted')
        return redirect('/index')
    return render_template('post.html',
                        title='Share your wisdom!',
                        form=form)

