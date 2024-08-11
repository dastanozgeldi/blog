import mistune
from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.models import Post

from .forms import PostForm

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    posts = Post.query.order_by(Post.pub_date.desc()).all()
    return render_template("main/index.html", posts=posts)


def get_post(id) -> Post:
    """Get a post and its author by id.

    Checks that the id exists.

    :param id: id of post to get
    :return: the post
    :raise 404: if a post with the given id doesn't exist
    """
    return Post.query.get_or_404(id, f"Post id {id} doesn't exist.")


@bp.route("/<int:id>", methods=("GET",))
def post(id):
    """See a particular post by specifying its ID."""
    post = get_post(id)
    return render_template("main/post.html", post=post)


@bp.route("/create", methods=("GET", "POST"))
def create():
    """Create a new post."""
    form = PostForm(request.form)
    if form.validate_on_submit():
        Post.create(
            title=form.title.data,
            brief=form.brief.data,
            content=form.content.data,
        )
        flash("Your post has been added.", "success")
        return redirect(url_for("main.index"))

    return render_template("main/create.html", form=form)


@bp.route("/<int:id>/update", methods=("GET", "POST"))
def update(id):
    """Update an existing post."""
    post = get_post(id)
    form = PostForm(request.form)
    if form.validate_on_submit():
        post.update(
            title=form.title.data,
            brief=form.brief.data,
            content=form.content.data,
            modified=True,
        )
        flash("Your post has been updated.", "success")
        return redirect(url_for("main.index"))

    return render_template("main/update.html", post=post, form=form)


@bp.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    """Delete an existing post."""
    get_post(id).delete()
    return redirect(url_for("main.index"))


# Static routes
def get_md_content(route_name):
    with open(f"app/static/markdown/{route_name}.md", "r") as f:
        markdown = f.read()
    return mistune.html(markdown)


@bp.route("/projects")
def projects():
    content = get_md_content("projects")
    return render_template("main/projects.html", content=content)


@bp.route("/about")
def about():
    content = get_md_content("about")
    return render_template("main/about.html", content=content)
