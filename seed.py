from app import app, db
from app.models import User  # import your models here

def run_seed():
    with app.app_context():

        # Example: Add users
        user1 = User(username="admin", email="admin@example.com" )
        user2 = User(username="test", email="test@example.com")

        db.session.add_all([user1, user2])

        user1.set_password('admin')
        user2.set_password('test')

        try:
            db.session.commit()
            print("Seed data inserted successfully!")
        except Exception as e:
            db.session.rollback()
            print("Error while seeding:", e)


if __name__ == "__main__":
    run_seed()
