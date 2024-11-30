from app import create_app
from sqlalchemy import inspect
import os
from flask_migrate import Migrate

from app.models import db  # SQLAlchemy object ko import karein


app = create_app()

# Application context ke andar database operations karte hain
with app.app_context():
    inspector = inspect(db.engine)
    print(inspector.get_table_names())

    print("Template folder path:", os.path.abspath('app/templates'))

@app.before_request
def create_tables():
    db.create_all()  # Sab tables pehle request se pehle create hongi

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
