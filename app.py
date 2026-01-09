from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>🚀 منصة الفيزياء الكمية | Vercel</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                background: linear-gradient(135deg, #0B0B3B, #000428);
                color: white;
                font-family: Arial, sans-serif;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                text-align: center;
            }
            .success-badge {
                background: #00FF88;
                color: #000;
                padding: 10px 30px;
                border-radius: 30px;
                display: inline-block;
                margin-bottom: 30px;
                font-weight: bold;
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
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 40px 0;
            }
            .feature {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 15px;
                border: 2px solid rgba(0,212,255,0.3);
            }
            .login-box {
                background: rgba(255,255,255,0.05);
                padding: 30px;
                border-radius: 20px;
                margin-top: 40px;
                border: 2px solid #00D4FF;
            }
            .login-btn {
                display: inline-block;
                background: linear-gradient(45deg, #00D4FF, #00FFFF);
                color: #0B0B3B;
                padding: 15px 40px;
                border-radius: 30px;
                text-decoration: none;
                font-weight: bold;
                font-size: 1.2rem;
                margin-top: 20px;
                transition: all 0.3s;
            }
            .login-btn:hover {
                transform: scale(1.05);
                box-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="success-badge">✅ تم النشر بنجاح على Vercel!</div>
            <h1>منصة الفيزياء الكمية</h1>
            <p style="font-size: 1.2rem; color: #B0B0FF; margin-bottom: 30px;">
                أول منصة عربية متكاملة للفيزياء الكمية | مجاناً على Vercel
            </p>
            
            <div class="features">
                <div class="feature">
                    <h3>🎓 تعلم مجاني</h3>
                    <p>دروس فيديو عالية الجودة في الفيزياء الكمية</p>
                </div>
                <div class="feature">
                    <h3>⚛️ محاكيات تفاعلية</h3>
                    <p>تجارب فيزيائية ثلاثية الأبعاد مباشرة في المتصفح</p>
                </div>
                <div class="feature">
                    <h3>📚 مكتبة شاملة</h3>
                    <p>آلاف الكتب والأبحاث العلمية المجانية</p>
                </div>
            </div>
            
            <div class="login-box">
                <h3 style="color: #00FFFF; margin-bottom: 20px;">🔑 بيانات الدخول التجريبية</h3>
                <div style="background: rgba(0,0,0,0.3); padding: 20px; border-radius: 10px;">
                    <p><strong>البريد الإلكتروني:</strong> admin@quantum.com</p>
                    <p><strong>كلمة المرور:</strong> admin123</p>
                </div>
                <a href="/dashboard" class="login-btn">🚀 بدء الاستخدام</a>
            </div>
            
            <div style="margin-top: 50px; color: #888;">
                <p>© 2024 منصة الفيزياء الكمية | مستضافة مجاناً على Vercel</p>
                <p>رابط الموقع: <strong id="site-url">https://quantum-physics.vercel.app</strong></p>
            </div>
        </div>
        
        <script>
            // تحديث رابط الموقع تلقائياً
            document.getElementById('site-url').textContent = window.location.origin;
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
        <title>لوحة التحكم - منصة الفيزياء الكمية</title>
        <style>
            body {
                background: #f5f5f5;
                font-family: Arial, sans-serif;
                margin: 0;
            }
            .dashboard {
                display: flex;
                min-height: 100vh;
            }
            .sidebar {
                width: 250px;
                background: #0B0B3B;
                color: white;
                padding: 20px;
            }
            .main {
                flex: 1;
                padding: 40px;
            }
            .stats {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }
            .stat-card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                border-top: 5px solid #00D4FF;
            }
            .stat-number {
                font-size: 2.5rem;
                color: #00D4FF;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="sidebar">
                <h2 style="color: #00D4FF;">🧠 منصة الفيزياء الكمية</h2>
                <div style="margin-top: 40px;">
                    <div style="padding: 15px; background: rgba(0,212,255,0.1); border-radius: 10px; margin: 10px 0;">
                        📊 لوحة التحكم
                    </div>
                    <div style="padding: 15px; margin: 10px 0;">👤 الملف الشخصي</div>
                    <div style="padding: 15px; margin: 10px 0;">🎓 دوراتي</div>
                    <div style="padding: 15px; margin: 10px 0;">📚 المكتبة</div>
                    <div style="padding: 15px; margin: 10px 0;">⚛️ المحاكيات</div>
                </div>
            </div>
            <div class="main">
                <h1 style="color: #0B0B3B;">مرحباً بك في لوحة التحكم</h1>
                <p style="color: #666;">موقعك يعمل بنجاح على Vercel 🎉</p>
                
                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-number">1,254</div>
                        <div>مستخدم نشط</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">56</div>
                        <div>دورة متاحة</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">189</div>
                        <div>كتاب علمي</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">32</div>
                        <div>محاكاة تفاعلية</div>
                    </div>
                </div>
                
                <div style="background: white; padding: 30px; border-radius: 15px; margin-top: 30px;">
                    <h3>🚀 إجراءات سريعة</h3>
                    <button style="background: #00D4FF; color: white; border: none; padding: 12px 25px; border-radius: 8px; margin: 10px; cursor: pointer;">
                        بدء دورة جديدة
                    </button>
                    <button style="background: #8A2BE2; color: white; border: none; padding: 12px 25px; border-radius: 8px; margin: 10px; cursor: pointer;">
                        تصفح المكتبة
                    </button>
                    <button style="background: #4A00E0; color: white; border: none; padding: 12px 25px; border-radius: 8px; margin: 10px; cursor: pointer;">
                        تشغيل محاكاة
                    </button>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/api/stats')
def api_stats():
    return jsonify({
        'status': 'active',
        'users': 1254,
        'courses': 56,
        'books': 189,
        'simulations': 32,
        'hosting': 'Vercel',
        'plan': 'Free',
        'uptime': '100%',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)