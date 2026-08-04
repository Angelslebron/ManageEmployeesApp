from app.database import Base, SessionLocal, engine
from app.models.user import User
from app.services.auth_service import hash_password


Base.metadata.create_all(bind=engine)


db = SessionLocal()


existing_user = (
    db.query(User)
    .filter(User.username == "admin")
    .first()
)


if not existing_user:

    admin = User(
        username="admin",
        password_hash=hash_password("Admin123!")
    )

    db.add(admin)
    db.commit()

    print("Admin user created.")

else:

    print("Admin user already exists.")


db.close()