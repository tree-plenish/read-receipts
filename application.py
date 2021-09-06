from flask import Flask, send_file, render_template

application = Flask(__name__)

# API GET request behavior
@application.route('/')
def get_image():
    return send_file('static/blankPixel.png')

# blank page displaying the image
@application.route('/blank')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    application.run()