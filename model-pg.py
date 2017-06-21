from flask.ext.sqlalchemy import SQLAlchemy
from backend-ttt import app

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
