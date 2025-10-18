from faker import Faker
from app.models import Entry, db

def generate_fake_entries(n): # n == how_many new entries
    fake = Faker()
    for _ in range(n):
        post = Entry(
            title=fake.sentence(),
            body='\n'.join(fake.paragraphs(15)),
            is_published=True
        )
        db.session.add(post)
    db.session.commit()