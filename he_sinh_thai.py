import streamlit as st
import base64
import os

# ==========================================
# 1. CẤU HÌNH TRANG (FULL MÀN HÌNH VIP)
# ==========================================
st.set_page_config(page_title="Hệ sinh thái 4.0 - TGDV Tuyên Quang", page_icon="🌐", layout="wide")

# Hàm lấy Logo Banner (Vẫn giữ nguyên, sếp nhớ để file Logo TGDV.png ở cùng thư mục nhé)
def get_logo_base64():
    try:
        with open("Logo TGDV.png", "rb") as f: return base64.b64encode(f.read()).decode("utf-8")
    except: return ""

# ==========================================
# 2. CSS GIAO DIỆN SIÊU VIP (VÁ LỖI MẤT NỀN & ICON)
# ==========================================
st.markdown(f"""
<style>
    /* Nền ứng dụng màu xám nhẹ sang trọng */
    .stApp {{ background-color: #f4f6f9; }}
    
    /* Header Banner - Đã vá lỗi màu nền VIP (dùng màu chuẩn Teal) */
    .hero-banner {{
        background-color: #17a2b8 !important; /* Dùng màu này đảm bảo sếp không bao giờ lo mất nền */
        background-image: linear-gradient(135deg, #004B87 0%, #17a2b8 100%) !important;
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        color: white !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin-bottom: 30px;
    }}
    .hero-banner h1 {{ font-size: 36px; font-weight: 900; margin: 15px 0 5px 0; text-transform: uppercase; color: white !important;}}
    .hero-banner p {{ font-size: 18px; opacity: 0.9; color: white !important; font-weight: 500;}}
    
    /* Grid layout tự co bóp smart */
    .ecosystem-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        padding: 10px;
    }}
    
    /* Card Style - Bọc kỹ giao diện */
    a.app-card {{
        background-color: white !important;
        border-radius: 12px !important;
        padding: 25px 20px !important;
        text-decoration: none !important;
        color: #333 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
        transition: all 0.3s ease !important;
        border-top: 5px solid #004B87 !important;
    }}
    
    a.app-card:hover {{
        transform: translateY(-8px) !important;
        box-shadow: 0 12px 25px rgba(0,75,135,0.2) !important;
        border-top: 5px solid #C8102E !important;
    }}

    /* CSS cho Icon đồng bộ (Vòng tròn trắng) */
    .icon-wrapper {{
        width: 70px;
        height: 70px;
        background: #f8f9fa;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 35px;
        margin-bottom: 15px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
        overflow: hidden; /* Bọc kỹ SVG bên trong */
    }}

    .app-title {{ font-size: 18px; font-weight: bold; color: #004B87; margin-bottom: 10px; text-transform: uppercase; }}
    .app-desc {{ font-size: 14px; color: #666; line-height: 1.5; margin-bottom: 20px; flex-grow: 1; }}
    
    .access-btn {{
        background-color: #004B87;
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 13px;
        text-transform: uppercase;
    }}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. BANNER CHÍNH (VÁ LỖI CHỮ MÀU TRẮNG)
# ==========================================
logo_data = get_logo_base64()
logo_html = f'<img src="data:image/png;base64,{logo_data}" style="height: 90px; margin-bottom: 10px;">' if logo_data else "🌐"

st.markdown(f"""
<div class="hero-banner">
    {logo_html}
    <h1>HỆ SINH THÁI 4.0</h1>
    <p>BAN TUYÊN GIÁO VÀ DÂN VẬN TỈNH ỦY TUYÊN QUANG</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 4. ĐỊNH NGHĨA SVG CỜ ĐẢNG CHUẨN (VÁ LỖI MẤT ICON)
# ==========================================
# Em đã vẽ lại mã SVG đơn giản hơn để sếp dán vào là nó lên ngay
svg_co_dang = """
<svg width="45" height="45" viewBox="0 0 540 360" xmlns="http://www.w3.org/2000/svg">
    <rect width="540" height="360" fill="#C8102E"/>
    <path fill="#FFCC00" d="M162 90c-35 0-63 28-63 63s28 63 63 63 63-28 63-63-28-63-63-63zm0 100c-20 0-37-17-37-37s17-37 37-37 37 17 37 37-17 37-37 37zM378 90l-30 30 70 70-30 30-70-70-30 30 100 100 60-60-100-100z"/>
    <circle cx="162" cy="153" r="15" fill="#FFCC00"/>
</svg>
"""

# ==========================================
# 5. HIỂN THỊ GRID ỨNG DỤNG (9 EM VIP)
# ==========================================
apps = [
    {"icon": "🌐", "title": "Điểm tin Báo chí", "link": "https://diemtinhangngaytgdv.streamlit.app/", "desc": "Tổng hợp tin bài tự động 24/7 từ báo chính thống."},
    {"icon": "📑", "title": "Đăng ký Số VB", "link": "https://dangkysovanbantgdv.streamlit.app/", "desc": "Hệ thống cấp số tự động, quản lý sổ văn thư chuẩn."},
    {"icon": "🗂️", "title": "Quản lý Hồ sơ", "link": "https://quan-ly-ho-so-tgdv.streamlit.app/", "desc": "Số hóa hồ sơ nhân sự, xuất Sơ yếu lý lịch chuẩn A4."},
    {"icon": "🏛️", "title": "E-Cabinet", "link": "https://tailieuhopbtgdv.streamlit.app/", "desc": "Phòng họp không giấy, quản lý tài liệu số hóa."},
    {"icon": "📊", "title": "Thu thập Báo cáo", "link": "https://bao-cao-tgdv.streamlit.app/", "desc": "Hệ thống nộp số liệu cơ sở, tổng hợp tự động."},
    {"icon": "🤖", "title": "AI Tra cứu Lương", "link": "https://tracuuluong-tgdvtq.streamlit.app/", "desc": "Trợ lý ảo hỗ trợ tra cứu lương và phụ cấp tự động."},
    {"icon": "📖", "title": "Bản tin Sinh hoạt", "link": "https://bantinchibo.streamlit.app/", "desc": "Bản tin điện tử nội bộ, định dạng lật trang hiện đại."},
    # Em đã vá lỗi cái Card này, sếp dán vào là lên cờ đỏ búa liềm ngay
    {"icon": "svg_co", "title": "Hỏi đáp Nghị quyết", "link": "http://hoidapnghiquyet.tuyenquang.gov.vn", "desc": "Chatbot AI giải đáp Nghị quyết Đại hội Đảng bộ tỉnh."},
    {"icon": "💻", "title": "Hỏi đáp CĐS", "link": "http://hoidapcds.tuyenquang.gov.vn", "desc": "Trợ lý ảo giải đáp về kiến thức Chuyển đổi số."}
]

html_grid = '<div class="ecosystem-grid">'
for app in apps:
    # Đoạn này là "ma thuật" để thay thế svg_co bằng lá cờ thật
    icon_content = svg_co_dang if app['icon'] == "svg_co" else app['icon']
    
    html_grid += f"""
    <a href="{app['link']}" target="_blank" class="app-card">
        <div class="icon-wrapper">{icon_content}</div>
        <div class="app-title">{app['title']}</div>
        <div class="app-desc">{app['desc']}</div>
        <div class="access-btn">Truy cập ngay</div>
    </a>"""
html_grid += '</div>'

# Đẩy giao diện lên màn hình
st.markdown(html_grid, unsafe_allow_html=True)

# ==========================================
# 6. FOOTER CHUẨN VIP
# ==========================================
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #666; padding: 20px; font-size: 14px;'>
    <b>© 2026 - Ban Tuyên giáo và Dân vận Tỉnh ủy Tuyên Quang</b><br>
    Phát triển bởi: Ngạc Văn Tuấn - Chuyên viên Văn phòng
</div>
""", unsafe_allow_html=True)
