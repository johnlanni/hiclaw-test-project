"""
Flask Hello World Web Application

A simple Flask web application that returns "Hello, World!" at the root endpoint.
"""

from flask import Flask

# Create Flask application instance
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Root endpoint that returns a hello world message.
    
    Returns:
        str: Hello, World! greeting
    """
    return 'Hello, World!'


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)