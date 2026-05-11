import os
from flask import Flask, render_template, request, flash

# Fayl joylashgan katalogni aniqlaymiz (backend papkasi)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Frontend papkasiga yo'lni to'g'ri ko'rsatamiz
# backend dan bir pog'ona yuqoriga chiqib, frontend/templates ga kiramiz
template_path = os.path.join(current_dir, '..', 'frontend', 'templates')
static_path = os.path.join(current_dir, '..', 'frontend')

app = Flask(__name__, 
            template_folder=template_path, 
            static_folder=static_path,
            static_url_path='')

app.secret_key = 'urtt_professional_secret_key'

@app.route('/')
def home():
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login mantiqi shu yerda bo'ladi
        pass
    return render_template('login.html')

@app.route('/admission')
def admission():
    return render_template('admission.html')


if __name__ == '__main__':
    # Serverni barcha tarmoq interfeyslarida ishga tushiramiz
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
import os
from flask import Flask, render_template, request, flash

# Fayl joylashgan katalogni aniqlaymiz (backend papkasi)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Frontend papkasiga yo'lni to'g'ri ko'rsatamiz
# backend dan bir pog'ona yuqoriga chiqib, frontend/templates ga kiramiz
template_path = os.path.join(current_dir, '..', 'frontend', 'templates')
static_path = os.path.join(current_dir, '..', 'frontend')

app = Flask(__name__, 
            template_folder=template_path, 
            static_folder=static_path,
            static_url_path='')

app.secret_key = 'urtt_professional_secret_key'

@app.route('/')
def home():
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login mantiqi shu yerda bo'ladi
        pass
    return render_template('login.html')

@app.route('/admission')
def admission():
    return render_template('admission.html')


if __name__ == '__main__':
    # Serverni barcha tarmoq interfeyslarida ishga tushiramiz
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

