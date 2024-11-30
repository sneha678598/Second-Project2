from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Initialize SQLAlchemy with the app

    # Import and register blueprints here (after app creation)
    from .routes import main
    app.register_blueprint(main)

    return app

# Register database teardown to close connection after each request
    app.teardown_appcontext(close_db_connection)
    
    with app.app_context():
        from .routes import main
        app.register_blueprint(main)