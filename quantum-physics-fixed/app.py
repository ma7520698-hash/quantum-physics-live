from flask import Flask, jsonify, render_template_string
import os
import webbrowser
import threading
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>🚀 منصة الفيزياء الكمية - الإصدار الجديد</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                background: linear-gradient(135deg, #0B0B3B, #000428);
                color: white;
                font-family: Arial, sans-serif;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                padding: 20px;
                text-align: center;
            }
            .success-box {
                background: #00FF88;
                color: #000;
                padding: 15px 30px;
                border-radius: 30px;
                font-weight: bold;
                margin-bottom: 30px;
                animation: bounce 2s infinite;
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            h1 {
                font-size: 3.5rem;
                color: #00D4FF;
                margin-bottom: 20px;
                text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
            }
            .btn-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                margin: 40px 0;
                max-width: 800px;
            }
            .btn {
                background: rgba(255,255,255,0.1);
                border: 2px solid #00D4FF;
                color: white;
                padding: 25px;
                border-radius: 15px;
                text-decoration: none;
                transition: all 0.3s;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .btn:hover {
                background: rgba(0,212,255,0.2);
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(0,212,255,0.3);
            }
            .icon {
                font-size: 2.5rem;
                margin-bottom: 15px;
                color: #00FFFF;
            }
            .login-info {
                background: rgba(255,255,255,0.05);
                padding: 25px;
                border-radius: 15px;
                margin-top: 30px;
                border: 2px solid #8A2BE2;
                max-width: 500px;
            }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body>
        <div class="success-box">
            ✅ تم إنشاء الموقع الجديد بنجاح!
        </div>
        
        <h1>منصة الفيزياء الكمية</h1>
        <p style="color: #B0B0FF; font-size: 1.2rem; margin-bottom: 30px;">
            أول منصة عربية متكاملة للفيزياء الكمية | الإصدار المستقر
        </p>
        
        <div class="btn-grid">
            <a href="/dashboard" class="btn">
                <div class="icon"><i class="fas fa-tachometer-alt"></i></div>
                <div style="font-weight: bold;">لوحة التحكم</div>
                <div style="font-size: 0.9rem; color: #B0B0FF;">إدارة الموقع</div>
            </a>
            
            <a href="/courses" class="btn">
                <div class="icon"><i class="fas fa-graduation-cap"></i></div>
                <div style="font-weight: bold;">الدورات التعليمية</div>
                <div style="font-size: 0.9rem; color: #B0B0FF;">تعلم مجاناً</div>
            </a>
            
            <a href="/library" class="btn">
                <div class="icon"><i class="fas fa-book"></i></div>
                <div style="font-weight: bold;">المكتبة العلمية</div>
                <div style="font-size: 0.9rem; color: #B0B0FF;">آلاف الكتب</div>
            </a>
            
            <a href="/simulations" class="btn">
                <div class="icon"><i class="fas fa-atom"></i></div>
                <div style="font-weight: bold;">المحاكيات</div>
                <div style="font-size: 0.9rem; color: #B0B0FF;">تجارب تفاعلية</div>
            </a>
        </div>
        
        <div class="login-info">
            <h3 style="color: #00FFFF; margin-bottom: 15px;">
                <i class="fas fa-key"></i> بيانات الدخول
            </h3>
            <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 10px;">
                <p><strong>📧 البريد:</strong> admin@quantum.com</p>
                <p><strong>🔐 كلمة المرور:</strong> admin123</p>
            </div>
            <a href="/login" style="
                display: inline-block;
                background: linear-gradient(45deg, #8A2BE2, #4A00E0);
                color: white;
                padding: 12px 30px;
                border-radius: 25px;
                text-decoration: none;
                margin-top: 15px;
                font-weight: bold;
            ">
                <i class="fas fa-sign-in-alt"></i> تسجيل الدخول
            </a>
        </div>
        
        <div style="margin-top: 40px; color: #888; font-size: 0.9rem;">
            <p>© 2024 منصة الفيزياء الكمية | مستضافة على Vercel</p>
            <p>رابط الموقع: <strong id="site-url">جاري التحميل...</strong></p>
        </div>
        
        <script>
            document.getElementById('site-url').textContent = window.location.origin;
            console.log('✅ الموقع يعمل بنجاح!');
        </script>
    </body>
    </html>
    '''

@app.route('/dashboard')
def dashboard():
    return '''
    <html dir="rtl">
    <head>
        <title>لوحة التحكم</title>
        <style>
            body { font-family: Arial; padding: 20px; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; }
            .back-btn { background: #00D4FF; color: white; padding: 10px 20px; text-decoration: none; }
            .card { background: white; padding: 20px; margin: 20px 0; border-radius: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-btn">← الرئيسية</a>
            <h1>🎛️ لوحة التحكم</h1>
            <p>مرحباً بك في لوحة تحكم الموقع</p>
            
            <div class="card">
                <h3>📊 إحصائيات الموقع</h3>
                <p>👥 المستخدمون: <strong>1,254</strong></p>
                <p>🎓 الدورات: <strong>56</strong></p>
                <p>📚 الكتب: <strong>189</strong></p>
                <p>⚛️ المحاكيات: <strong>32</strong></p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/courses')
def courses():
    return '''
    <html dir="rtl">
    <body style="padding: 20px;">
        <a href="/" style="background: #00D4FF; color: white; padding: 10px 20px; text-decoration: none;">← الرئيسية</a>
        <h1>🎓 الدورات التعليمية</h1>
        <div style="border: 1px solid #ddd; padding: 20px; margin: 20px 0;">
            <h3>مقدمة في الفيزياء الكمية</h3>
            <p>مدخل شامل للمفاهيم الأساسية</p>
            <button style="background: #00D4FF; color: white; padding: 10px 20px; border: none; border-radius: 5px;">
                انضم مجاناً
            </button>
        </div>
    </body>
    </html>
    '''

@app.route('/library')
def library():
    return '''
    <html dir="rtl">
    <body style="padding: 20px;">
        <a href="/" style="background: #00D4FF; color: white; padding: 10px 20px; text-decoration: none;">← الرئيسية</a>
        <h1>📚 المكتبة العلمية</h1>
        <p>جاري تحميل الكتب...</p>
    </body>
    </html>
    '''

@app.route('/simulations')
def simulations():
    return '''
    <html dir="rtl">
    <body style="padding: 20px;">
        <a href="/" style="background: #00D4FF; color: white; padding: 10px 20px; text-decoration: none;">← الرئيسية</a>
        <h1>⚛️ المحاكيات التفاعلية</h1>
        <p>جاري تطوير المحاكيات...</p>
    </body>
    </html>
    '''

@app.route('/login')
def login():
    return '''
    <html dir="rtl">
    <head>
        <style>
            body { background: #f5f5f5; display: flex; justify-content: center; align-items: center; height: 100vh; }
            .login-box { background: white; padding: 30px; border-radius: 15px; width: 400px; }
            input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
            button { background: #00D4FF; color: white; border: none; padding: 12px; width: 100%; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>🔑 تسجيل الدخول</h2>
            <input type="email" placeholder="البريد الإلكتروني" id="email">
            <input type="password" placeholder="كلمة المرور" id="password">
            <button onclick="loginUser()">دخول</button>
            <p style="color: #666; margin-top: 20px; text-align: center;">
                للحساب التجريبي:<br>
                <strong>admin@quantum.com</strong><br>
                <strong>admin123</strong>
            </p>
            <a href="/" style="display: block; text-align: center; margin-top: 20px;">← العودة للرئيسية</a>
        </div>
        <script>
            function loginUser() {
                alert('تم الدخول بنجاح!');
                window.location.href = '/dashboard';
            }
        </script>
    </body>
    </html>
    '''

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'active',
        'message': 'الموقع يعمل بنجاح على Vercel',
        'version': '2.0.0',
        'timestamp': datetime.now().isoformat(),
        'endpoints': ['/', '/dashboard', '/courses', '/library', '/simulations', '/login']
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 جاري تشغيل الموقع على المنفذ {port}")
    app.run(host='0.0.0.0', port=port, debug=False)