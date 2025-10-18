from app import app, db
from app.models import Entry
from app import routes, models

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Entry": models.Entry
   }

if __name__ == "__main__":
    app.run()