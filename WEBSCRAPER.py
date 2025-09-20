from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # This message will be sent to the HTTP response
    message = "Hello from Azure Container Apps! The secret password is: " + os.environ.get('SECRET_MESSAGE', 'default_password')
    print(f"Success! Someone visited the site. We printed this: {message}") # This will be seen in the logs
    return message

if __name__ == '__main__':
    # Listen on the port provided by the environment (needed for Container Apps)
    app.run(debug=True, host='0.0.0.0', port=80)