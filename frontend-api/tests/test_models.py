from app.database import SessionLocal, engine
from app.models import Base, User, Book
import pytest

@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_user_model(setup_db):
    session = SessionLocal()
    new_user = User(email="test@example.com", firstname="Test", lastname="User")
    session.add(new_user)
    session.commit()

    user = session.query(User).filter_by(email="test@example.com").first()
    assert user is not None
    assert user.firstname == "Test"
    assert user.lastname == "User"
    session.close()
