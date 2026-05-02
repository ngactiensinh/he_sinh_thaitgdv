import streamlit as st
import base64
import os

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Hệ sinh thái 4.0 - TGDV Tuyên Quang", page_icon="🌐", layout="wide")

# Hàm mã hóa ảnh sang Base64 để hiển thị
def get_image_base64(file_name):
    try:
        with open(file_name, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except:
        return ""

# Lấy dữ liệu các file ảnh
logo_data = get_image_base64("Logo TGDV.png")
codang_data = get_image_base64("CoDang.jpg")

# ==========================================
# 2. CSS GIAO DIỆN SIÊU VIP (VÁ LỖI BANNER & ICON)
# ==========================================
st.markdown(f"""
<style>
    .stApp {{ background-color: #f4f6f9; }}
    
    /* Header Banner - Cố định màu Teal VIP không lo mất nền */
    .hero-banner {{
        background: linear-gradient(135deg, #004B87 0%, #17a2b8 100%) !important;
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        color: white !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin-bottom: 30px;
    }}
    .hero-banner h1 {{ font-size: 32px; font-weight: 900; margin: 15px 0 5px 0; text-transform: uppercase; color: white !important; }}
    .hero-banner p {{ font-size: 16px; opacity: 0.9; color: white !important; }}
    
    /* Grid layout */
    .ecosystem-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        padding: 10px;
    }}
    
    /* Card Style */
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
        height: 100% !important;
    }}
    
    a.app-card:hover {{
        transform: translateY(-8px) !important;
        box-shadow: 0 12px 25px rgba(0,75,135,0.2) !important;
        border-top: 5px solid #C8102E !important;
    }}

    /* Vòng tròn chứa Icon đồng bộ */
    .icon-wrapper {{
        width: 80px;
        height: 80px;
        background: #f8f9fa;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        margin-bottom: 15px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
        overflow: hidden; /* Quan trọng để ảnh không tràn ra ngoài */
    }}

    .app-title {{ font-size: 17px; font-weight: bold; color: #004B87; margin-bottom: 10px; text-transform: uppercase; }}
    .app-desc {{ font-size: 14px; color: #666; line-height: 1.5; margin-bottom: 20px; flex-grow: 1; }}
    
    .access-btn {{
        background-color: #004B87;
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 12px;
        text-transform: uppercase;
    }}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HIỂN THỊ BANNER
# ==========================================
logo_html = f'<img src="data:image/png;base64,{logo_data}" style="height: 85px;">' if logo_data else "🌐"

st.markdown(f"""
<div class="hero-banner">
    {logo_html}
    <h1>HỆ SINH THÁI 4.0</h1>
    <p>BAN TUYÊN GIÁO VÀ DÂN VẬN TỈNH ỦY TUYÊN QUANG</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 4. CHUẨN BỊ NỘI DUNG ỨNG DỤNG
# ==========================================
# Tạo HTML cho Icon Cờ Đảng từ file sếp đã up
if codang_data:
    icon_nghi_quyet = f'<img src="data:image/jpeg;base64,{codang_data}" style="width: 100%; height: 100%; object-fit: cover;">'
else:
    icon_nghi_quyet = "🇻🇳"

apps = [
    {"icon": "🌐", "title": "Điểm tin Báo chí", "link": "https://diemtinhangngaytgdv.streamlit.app/", "desc": "Tổng hợp tin bài tự động 24/7 từ báo chính thống."},
    {"icon": "📑", "title": "Đăng ký Số VB", "link": "https://dangkysovanbantgdv.streamlit.app/", "desc": "Hệ thống cấp số tự động, quản lý sổ văn thư chuẩn."},
    {"icon": "🗂️", "title": "Quản lý Hồ sơ", "link": "https://quan-ly-ho-so-tgdv.streamlit.app/", "desc": "Số hóa hồ sơ nhân sự, xuất Sơ yếu lý lịch chuẩn A4."},
    {"icon": "🏛️", "title": "E-Cabinet", "link": "https://tailieuhopbtgdv.streamlit.app/", "desc": "Phòng họp không giấy, quản lý tài liệu số hóa."},
    {"icon": "📊", "title": "Thu thập Báo cáo", "link": "https://bao-cao-tgdv.streamlit.app/", "desc": "Hệ thống nộp số liệu cơ sở, tổng hợp tự động."},
    {"icon": "🤖", "title": "AI Tra cứu Lương", "link": "https://tracuuluong-tgdvtq.streamlit.app/", "desc": "Trợ lý ảo hỗ trợ tra cứu lương và phụ cấp tự động."},
    {"icon": "📖", "title": "Bản tin Sinh hoạt", "link": "https://bantinchibo.streamlit.app/", "desc": "Bản tin điện tử nội bộ, định dạng lật trang hiện đại."},
    {"icon": icon_nghi_quyet, "title": "Hỏi đáp Nghị quyết", "link": "http://hoidapnghiquyet.tuyenquang.gov.vn", "desc": "Chatbot AI giải đáp Nghị quyết Đại hội Đảng bộ tỉnh."},
    {"icon": "💻", "title": "Hỏi đáp CĐS", "link": "http://hoidapcds.tuyenquang.gov.vn", "desc": "Trợ lý ảo giải đáp về kiến thức Chuyển đổi số."}
]

# Xây dựng Grid
html_grid = '<div class="ecosystem-grid">'
for app in apps:
    html_grid += f"""
    <a href="{app['link']}" target="_blank" class="app-card">
        <div class="icon-wrapper">{app['icon']}</div>
        <div class="app-title">{app['title']}</div>
        <div class="app-desc">{app['desc']}</div>
        <div class="access-btn">Truy cập ngay</div>
    </a>"""
html_grid += '</div>'

st.markdown(html_grid, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'><b>© 2026 - Ban Tuyên giáo và Dân vận Tỉnh ủy Tuyên Quang</b></div>", unsafe_allow_html=True)
