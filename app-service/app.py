import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/health_check', methods=['GET'])
def hello():
   message = "service is running"
   return message


if __name__ == '__main__':
   app.run()
