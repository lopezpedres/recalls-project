from app import create_app
from flask_cors import CORS
import os
settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

CORS(app)