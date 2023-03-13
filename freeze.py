from flask_frozen import Freezer
from app import app
import pandas as pd

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
