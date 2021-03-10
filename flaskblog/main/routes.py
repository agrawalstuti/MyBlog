from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')       #helps to redirect from one page to another here / is root page of our website
@main.route('/home') 
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page= page)
    return render_template('home.html',posts=posts)


@main.route('/about')       #helps to redirect on about page
def about():
    return render_template('about.html',title='About')
