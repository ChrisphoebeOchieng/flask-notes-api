from app import app, db
from models import User, Note

with app.app_context():
    # reset the database
    db.drop_all()
    db.create_all()
    
    # create a test user
    user = User(username="phoebe")
    user.set_password("1234")

    db.session.add(user)
    db.session.commit()

    # create some test notes
    note1 = Note(title="First Note", content="This is the content of the first note.", user_id=user.id)
    note2 = Note(title="Gym", content="Leg day", user_id=user.id)

    db.session.add_all([note1, note2])
    db.session.commit()

    print("Database seeded successfully!")


