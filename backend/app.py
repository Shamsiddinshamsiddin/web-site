from flask import Flask, render_template
import os

# Papka manzillarini to'g'ri ko'rsatamiz
app = Flask(__name__, 
            template_folder='../frontend/templates', 
            static_folder='../frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
