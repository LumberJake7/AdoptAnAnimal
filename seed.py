from models import db, Animals
from app import app  

with app.app_context():
    db.drop_all()
    db.create_all()

    pet1 = Animals(name="Bluey", species="Dog", age=4, notes ="Is really blue", photo_url="https://www.bluey.tv/wp-content/uploads/2023/07/Bluey.png", available=True)
    pet2 = Animals(name="Tiamat", species="Dragon", age=1000, notes = "May need more hands for pets", photo_url="https://ih1.redbubble.net/image.2296627310.5945/flat,750x,075,f-pad,750x1000,f8f8f8.jpg", available=False)
    pet3 = Animals(name="Clifford", species="Dog", age=5, notes = "He's rather large for his age", photo_url="https://yt3.googleusercontent.com/ytc/AIf8zZSMZt97Dncq4JaYFLhBQc628vx7OvgwNVWRACzz=s900-c-k-c0x00ffffff-no-rj", available=True)

    db.session.add_all([pet1, pet2, pet3])
    db.session.commit()