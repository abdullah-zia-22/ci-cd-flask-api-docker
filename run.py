"""Modules required for running app"""
from api import app

# RUN API
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)  # add host='----'
