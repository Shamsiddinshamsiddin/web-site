import os
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'static')
)
app.secret_key = 'urtt-2024-super-secret-key-xavfsizlik'

# ─── Ma'lumotlar ──────────────────────────────────────────────────────────────

STATS = {
    'students': 1200,
    'teachers': 85,
    'courses': 18,
    'graduates': 3400,
}

COURSES = [
    {
        'id': 1,
        'title': "Dasturlash va Ilovalar Ishlab Chiqish",
        'short': "Web, mobil va desktop ilovalar yaratish bo'yicha to'liq kurs.",
        'icon': 'bi-code-slash',
        'color': 'blue',
        'duration': '3 yil',
        'level': 'Boshlang\'ich → Professional',
        'topics': ['Python & Django', 'JavaScript & React', 'Flutter & Dart', 'REST API', 'Git & DevOps'],
        'seats': 50,
    },
    {
        'id': 2,
        'title': "Kiberxavfsizlik",
        'short': "Tarmoq, tizim va ma'lumotlarni himoya qilish mutaxassisi.",
        'icon': 'bi-shield-lock',
        'color': 'red',
        'duration': '3 yil',
        'level': 'O\'rta → Expert',
        'topics': ['Penetration Testing', 'Network Security', 'Ethical Hacking', 'Kriptografiya', 'OSINT'],
        'seats': 30,
    },
    {
        'id': 3,
        'title': "Sun\'iy Intellekt va Ma\'lumotlar Fani",
        'short': "Machine Learning, Deep Learning va Data Science asoslari.",
        'icon': 'bi-cpu',
        'color': 'purple',
        'duration': '3 yil',
        'level': 'O\'rta → Professional',
        'topics': ['Python & NumPy', 'Machine Learning', 'Neural Networks', 'Computer Vision', 'NLP'],
        'seats': 40,
    },
    {
        'id': 4,
        'title': "Kompyuter Tarmoqlari va IT Infratuzilmasi",
        'short': "Tarmoqlarni loyihalash, sozlash va boshqarish.",
        'icon': 'bi-hdd-network',
        'color': 'green',
        'duration': '3 yil',
        'level': 'Boshlang\'ich → Professional',
        'topics': ['Cisco CCNA', 'Linux Admin', 'Cloud (AWS/Azure)', 'VPN & Firewall', 'Docker'],
        'seats': 35,
    },
    {
        'id': 5,
        'title': "Multimedia va Grafik Dizayn",
        'short': "UI/UX, 3D modellashtirish va raqamli kontent yaratish.",
        'icon': 'bi-palette',
        'color': 'orange',
        'duration': '2 yil',
        'level': 'Boshlang\'ich → O\'rta',
        'topics': ['Figma & Adobe XD', 'Photoshop & Illustrator', 'Blender 3D', 'Motion Design', 'Branding'],
        'seats': 45,
    },
    {
        'id': 6,
        'title': "1C Dasturlash va Buxgalteriya Avtomatlashtirish",
        'short': "Korxona iqtisodini raqamlashtirish va 1C platformasi.",
        'icon': 'bi-bar-chart-line',
        'color': 'teal',
        'duration': '2 yil',
        'level': 'Boshlang\'ich → O\'rta',
        'topics': ['1C:Enterprise', 'Buxgalteriya asoslari', 'SQL', 'ERP tizimlari', 'Excel VBA'],
        'seats': 40,
    },
]

LABS = [
    {'name': 'Dasturlash laboratoriyasi', 'desc': '60 ta zamonaviy kompyuter, tezkor internet', 'icon': 'bi-laptop'},
    {'name': 'Kiberxavfsizlik markazi', 'desc': 'Izolyatsiya qilingan tarmoq, hujum simulyatsiyasi', 'icon': 'bi-shield-check'},
    {'name': 'AI/ML laboratoriyasi', 'desc': 'GPU serverlar, NVIDIA Tesla klaster', 'icon': 'bi-gpu-card'},
    {'name': 'Tarmoq laboratoriyasi', 'desc': 'Cisco uskunalari, real tarmoq topologiyasi', 'icon': 'bi-router'},
    {'name': 'Multimedia studiyasi', 'desc': 'Professional kamera, yoritgichlar, yozuv xonasi', 'icon': 'bi-camera-video'},
    {'name': 'Kutubxona va coworking', 'desc': '5000+ elektron kitob, tinch ishlash zonasi', 'icon': 'bi-book'},
]

ADMISSION_STEPS = [
    {
        'num': '01',
        'title': "Hujjatlarni tayyorlash",
        'desc': "Pasport nusxasi, attestat yoki diplom, 4 ta 3×4 fotosurat, tibbiy ma'lumotnoma (086-shakl) va harbiy xizmatga munosabatni tasdiqlovchi hujjat.",
        'icon': 'bi-file-earmark-text',
    },
    {
        'num': '02',
        'title': "Onlayn ariza topshirish",
        'desc': "Saytimiz yoki my.gov.uz orqali ariza to'ldiring. Tanlagan yo'nalishingizni, kontakt ma'lumotlarini kiriting. Ariza raqamingizni eslab qoling.",
        'icon': 'bi-laptop',
    },
    {
        'num': '03',
        'title': "Kirish imtihonlari",
        'desc': "Matematika (test, 30 ta savol) va ona tili (insho yoki diktant) bo'yicha kirish sinovlari o'tkaziladi. Test Pearson VUE tizimida kompyuterda topshiriladi.",
        'icon': 'bi-pencil-square',
    },
    {
        'num': '04',
        'title': "Natijalar va ro'yxatdan o'tish",
        'desc': "Natijalar 3 kun ichida e'lon qilinadi. Qabul qilinganlar to'lov va shartnoma imzolash uchun texnikumga tashrif buyuradi.",
        'icon': 'bi-check2-circle',
    },
    {
        'num': '05',
        'title': "O'qishni boshlash",
        'desc': "Semestr boshida orientatsiya kuni bo'lib o'tadi. Talaba guvohnomasi, jadval va kutubxona kartochkasi topshiriladi. Xush kelibsiz!",
        'icon': 'bi-mortarboard',
    },
]

CONTACTS = {
    'address': "Urganch shahri, Xorazm viloyati, Al-Xorazmiy ko'chasi, 42-uy",
    'phone': "+998 62 224-55-66",
    'phone2': "+998 62 224-55-77",
    'email': "info@urtt.uz",
    'email2': "abiturient@urtt.uz",
    'hours': "Dushanba–Juma: 08:00–17:00 | Shanba: 09:00–13:00",
}

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    featured = COURSES[:3]
    return render_template('index.html', stats=STATS, featured=featured, page='index')


@app.route('/about')
def about():
    return render_template('about.html', labs=LABS, page='about')


@app.route('/courses')
def courses():
    return render_template('courses.html', courses=COURSES, page='courses')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        errors = []
        if not name or len(name) < 2:
            errors.append("Ism kamida 2 ta harfdan iborat bo'lishi kerak.")
        if not phone:
            errors.append("Telefon raqami majburiy.")
        if not message or len(message) < 10:
            errors.append("Xabar kamida 10 ta belgidan iborat bo'lishi kerak.")

        if errors:
            for e in errors:
                flash(e, 'danger')
        else:
            flash(f"Rahmat, {name}! Xabaringiz qabul qilindi. Tez orada bog'lanamiz.", 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html', contacts=CONTACTS, page='contact')


@app.route('/admission')
def admission():
    return render_template('admission.html', steps=ADMISSION_STEPS, courses=COURSES, page='admission')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Demo: haqiqiy loyihada DB dan tekshiriladi
        if username == 'demo' and password == 'urtt2024':
            session['user'] = username
            flash("Xush kelibsiz, talaba! Shaxsiy kabinetingizga kirdingiz.", 'success')
            return redirect(url_for('index'))
        else:
            flash("Login yoki parol noto'g'ri. Qayta urinib ko'ring.", 'danger')

    return render_template('login.html', page='login')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Kabinetdan muvaffaqiyatli chiqdingiz.", 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)