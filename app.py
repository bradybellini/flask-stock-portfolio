import logging, os

from flask import Flask

from logging.handlers import RotatingFileHandler

from flask.logging import default_handler

app = Flask(__name__)
config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
app.config.from_object(config_type)


app.logger.removeHandler(default_handler)

file_handler = RotatingFileHandler('instance/flask-stock-portfolio.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

from project.stocks import stocks_blueprint
from project.users import users_blueprint

# Register the blueprints
app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')
