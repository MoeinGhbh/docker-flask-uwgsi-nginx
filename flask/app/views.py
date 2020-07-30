from app import app
import os

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    # It's a simple route with the addition of app_name = os.getenv("APP_NAME"),
    #  which will become apparent later when we use docker-compose.yml 
    # to set some enviromment variables.

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"