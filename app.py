from datetime import datetime

import validators
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from service import GenerateTinytUrl

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:password@localhost/tiny_url_db"

db = SQLAlchemy(app)


class Links(db.Model):
    """
    This table is used to store original and tiny URL for users with the
    date they were created
    """

    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(200), unique=False, nullable=False)
    tiny_url = db.Column(db.String(200), unique=True, nullable=False)
    date = db.Column(db.String(200), unique=False, nullable=False)

    def __init__(self, original_url, tiny_url, date):
        self.original_url = original_url
        self.tiny_url = tiny_url
        self.date = date


@app.route("/")
def index():
    tiny_url = request.args.get("tiny_url")

    if len(request.full_path) > 2 and not tiny_url:
        return "Invalid Tiny URL format. Please try again."
    elif tiny_url:
        try:
            # Redirect to its Original link
            row = db.session.query(Links).filter(Links.tiny_url == request.url).one()
            return redirect(row.original_url, code=302)

        except:
            return "Tiny URL was not found"

    else:
        return render_template("index.html")


@app.route("/add_original_url", methods=["POST"])
def add_original_url():
    original_url = request.form["original_url"].strip()
    if not validators.url(original_url):
        return "Invalid URL. Please try again"

    tiny_url = GenerateTinytUrl.create_tiny_url(original_url)
    links = Links(original_url, tiny_url, datetime.now())
    db.session.add(links)
    db.session.commit()

    return render_template(
        "link_added.html", tiny_url=tiny_url, original_url=original_url
    )


@app.route("/get_original_url", methods=["GET"])
def get_original_url():
    tiny_url = request.args["tiny_url"].strip()

    try:
        row = db.session.query(Links).filter(Links.tiny_url == tiny_url).one()
    except:
        return "Tiny URL was not found"

    return render_template(
        "link_added.html", tiny_url=row.tiny_url, original_url=row.original_url
    )


if __name__ == "__main__":
    # debug on for testing, set as False for production
    app.run(debug=True)
