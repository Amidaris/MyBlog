from flask import render_template, request
from app import app
from app.models import Entry, db
from app.forms import EntryForm


@app.route("/")
def index():
   all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())

   return render_template("homepage.html", all_posts=all_posts)


@app.route("/new-post/", defaults={"entry_id": None}, methods=["GET", "POST"])
@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def create_or_edit_entry(entry_id):
    if entry_id is not None:
        entry = Entry.query.filter_by(id=entry_id).first_or_404()
    else:
        entry = None
  
    form = EntryForm(obj=entry)
    errors = None

    if request.method == 'POST':
        if form.validate_on_submit():
            if entry is None:
                entry = Entry()
                db.session.add(entry)
            form.populate_obj(entry)
            db.session.commit()
        else:
            errors = form.errors

    return render_template("entry_form.html", form=form, errors=errors)