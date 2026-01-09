from flask import Flask, jsonify, render_template_string
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

# قاعدة بيانات بسيطة
def init_db():
    conn = sqlite3.connect('quantum.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stats 
                 (users INT, courses INT, books INT, simulations INT)''')
    c.execute("INSERT OR IGNORE INTO stats VALUES (1000, 50, 150, 30)")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🚀 منصة الفيزياء الكمية - مباشر!</title>
        <style>
            body {
                background: linear-gradient(135deg, #0B0B3B, #000428);
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }
            h1 { color: #00D4FF; font-size: 3rem; margin-bottom: 20px; }
            .live-badge {
                background: #FF0066;
                color: white;
                padding: 10px 20px;
                border-radius: 20px;
                display: inline-block;
                margin-bottom: 20px;
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
            .stats {
                display: flex;
                justify-content: center;
                gap: 30px;
                margin: 40px 0;
                flex-wrap: wrap;
            }
            .stat-card {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 15px;
                border: 2px solid #00D4FF;
                min-width: 200px;
            }
            .stat-number {
                font-size: 2.5rem;
                color: #00FFFF;
                font-weight: bold;
            }
            .btn {
                display: inline-block;
                background: linear-gradient(45deg, #00D4FF, #00FFFF);
                color: #0B0B3B;
                padding: 15px 30px;
                border-radius: 30px;
                text-decoration: none;
                font-weight: bold;
                margin: 10px;
                font-size: 1.2rem;
                transition: transform 0.3s;
            }
            .btn:hover {
                transform: translateY(-5px);
            }
        </style>
    </head>
    <body>
        <div class="live-badge">🔴 بث مباشر على الإنترنت!</div>
        <h1>🚀 منصة الفيزياء الكمية</h1>
        <p style="font-size: 1.2rem; color: #B0B0FF;">
            أول منصة عربية متكاملة للفيزياء الكمية على الإنترنت!
        </p>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="users">1,000+</div>
                <div>مستخدم نشط</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="courses">50+</div>
                <div>دورة تعليمية</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="simulations">30+</div>
                <div>محاكاة تفاعلية</div>
            </div>
        </div>
        
        <div style="margin-top: 40px;">
            <a href="/dashboard" class="btn">🎛️ لوحة التحكم</a>
            <a href="/api/stats" class="btn">📊 الإحصائيات الحية</a>
            <a href="/login" class="btn" style="background: linear-gradient(45deg, #8A2BE2, #4A00E0);">
                👤 تسجيل الدخول
            </a>
        </div>
        
        <div style="margin-top: 60px; color: #888; font-size: 0.9rem;">
            <p>© 2024 منصة الفيزياء الكمية. جميع الحقوق محفوظة.</p>
            <p>العلم نور، والمعرفة قوة 🚀</p>
        </div>
        
        <script>
            // تحديث الإحصائيات
            fetch('/api/stats').then(r => r.json()).then(data => {
                document.getElementById('users').textContent = data.users + '+';
                document.getElementById('courses').textContent = data.courses + '+';
                document.getElementById('simulations').textContent = data.simulations + '+';
            });
        </script>
    </body>
    </html>
    '''

@app.route('/dashboard')
def dashboard():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>لوحة التحكم</title>
        <style>
            body { font-family: Arial; background: #f5f5f5; margin: 0; }
            .sidebar { width: 250px; background: #0B0B3B; color: white; height: 100vh; position: fixed; }
            .main { margin-left: 250px; padding: 20px; }
            .card { background: white; padding: 20px; border-radius: 15px; margin: 15px 0; }
        </style>
    </head>
    <body>
        <div class="sidebar">
            <h2 style="padding: 20px; color: #00D4FF;">لوحة التحكم</h2>
            <div style="padding: 10px 20px;">📊 نظرة عامة</div>
            <div style="padding: 10px 20px;">👥 المستخدمون</div>
            <div style="padding: 10px 20px;">📚 المحتوى</div>
            <div style="padding: 10px 20px;">⚙️ الإعدادات</div>
        </div>
        <div class="main">
            <h1>مرحباً بك في لوحة التحكم</h1>
            <div class="card">
                <h3>📈 إحصائيات الموقع الحي</h3>
                <div id="stats"></div>
            </div>
        </div>
        <script>
            fetch('/api/stats').then(r => r.json()).then(data => {
                document.getElementById('stats').innerHTML = `
                    <p>👥 المستخدمون: <strong style="color: #00D4FF;">${data.users}+</strong></p>
                    <p>🎓 الدورات: <strong style="color: #00D4FF;">${data.courses}+</strong></p>
                    <p>📚 الكتب: <strong style="color: #00D4FF;">${data.books}+</strong></p>
                    <p>⚛️ المحاكيات: <strong style="color: #00D4FF;">${data.simulations}+</strong></p>
                `;
            });
        </script>
    </body>
    </html>
    '''

@app.route('/api/stats')
def api_stats():
    conn = sqlite3.connect('quantum.db')
    c = conn.cursor()
    stats = c.execute("SELECT * FROM stats").fetchone()
    conn.close()
    
    return jsonify({
        'users': stats[0],
        'courses': stats[1],
        'books': stats[2],
        'simulations': stats[3],
        'status': 'online',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/login')
def login():
    return '''
    <html>
    <body style="background: #f5f5f5; padding: 50px; text-align: center;">
        <div style="max-width: 400px; margin: 0 auto; background: white; padding: 30px; border-radius: 15px;">
            <h2>تسجيل الدخول</h2>
            <input type="email" placeholder="البريد الإلكتروني" style="width: 100%; padding: 10px; margin: 10px 0;">
            <input type="password" placeholder="كلمة المرور" style="width: 100%; padding: 10px; margin: 10px 0;">
            <button style="background: #00D4FF; color: white; padding: 10px 30px; border: none; border-radius: 5px;">
                دخول
            </button>
            <p style="color: #666; margin-top: 20px;">
                يمكنك استخدام:<br>
                <strong>admin@quantum.com</strong><br>
                <strong>admin123</strong>
            </p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 الموقع يعمل على: http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)