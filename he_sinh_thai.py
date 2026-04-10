import streamlit as st
import base64
import os

# Cấu hình trang cực rộng
st.set_page_config(page_title="Hệ sinh thái 4.0 - TGDV Tuyên Quang", page_icon="🌐", layout="wide")

# Hàm lấy Logo
def get_logo_base64():
    try:
        with open("Logo TGDV.png", "rb") as f: return base64.b64encode(f.read()).decode("utf-8")
    except: return ""

# CSS Giao diện siêu VIP
st.markdown("""
<style>
    /* Hình nền vi mạch điện tử mờ 5% */
    .stApp { 
        background-color: #f4f6f9; 
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cpath d='M20 20 L40 20 L50 30 L50 50 M80 20 L60 20 L50 30 L50 50 M50 50 L50 70 L70 90 L90 90 M50 70 L30 90 L10 90' stroke='%23004B87' stroke-width='2' fill='none' opacity='0.05'/%3E%3Ccircle cx='20' cy='20' r='3' fill='%23004B87' opacity='0.05'/%3E%3Ccircle cx='80' cy='20' r='3' fill='%23004B87' opacity='0.05'/%3E%3Ccircle cx='10' cy='90' r='3' fill='%23004B87' opacity='0.05'/%3E%3Ccircle cx='90' cy='90' r='3' fill='%23004B87' opacity='0.05'/%3E%3Ccircle cx='50' cy='50' r='5' fill='%23004B87' opacity='0.08'/%3E%3C/svg%3E");
        background-repeat: repeat;
    }
    
    /* Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, #004B87 0%, #17a2b8 100%);
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-bottom: 40px;
    }
    .hero-banner h1 { font-size: 38px; font-weight: 900; margin: 15px 0 5px 0; text-transform: uppercase; letter-spacing: 1px;}
    .hero-banner p { font-size: 18px; opacity: 0.9; margin: 0; font-weight: 500;}
    
    /* Grid layout cho các Cards */
    .ecosystem-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        padding: 10px;
    }
    
    /* BẢO VỆ GIAO DIỆN KHỎI STREAMLIT OVERRIDE */
    a.app-card, a.app-card:hover, a.app-card:visited, a.app-card:active {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 12px !important;
        padding: 25px !important;
        text-decoration: none !important;
        color: #333 !important;
        border-top: 5px solid #004B87 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important;
        border-bottom: none !important;
        border-left: none !important;
        border-right: none !important;
    }
    a.app-card:hover {
        transform: translateY(-8px) !important;
        box-shadow: 0 15px 30px rgba(0,75,135,0.15) !important;
        border-top: 5px solid #C8102E !important;
    }
    
    /* Nội dung Card */
    .app-icon { font-size: 45px; margin-bottom: 15px; text-align: center;}
    .app-title { font-size: 20px; font-weight: bold; color: #004B87; margin-bottom: 10px; text-align: center; text-transform: uppercase;}
    .app-desc { font-size: 14px; color: #6c757d; line-height: 1.5; text-align: center; flex-grow: 1; margin-bottom: 20px;}
    
    /* Nút truy cập */
    .access-btn {
        background-color: #f8f9fa;
        color: #004B87;
        border: 2px solid #004B87;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        transition: all 0.3s ease;
        text-transform: uppercase;
        font-size: 14px;
    }
    a.app-card:hover .access-btn {
        background-color: #004B87;
        color: white;
        border-color: #004B87;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BANNER CHÍNH
# ==========================================
logo_data = get_logo_base64()
logo_html = f'<img src="data:image/png;base64,{logo_data}" style="height: 100px; object-fit: contain; margin-bottom: 10px;">' if logo_data else "🌐"

st.markdown(f"""
<div class="hero-banner">
    {logo_html}
    <h1>HỆ SINH THÁI CHUYỂN ĐỔI SỐ 4.0</h1>
    <p>BAN TUYÊN GIÁO VÀ DÂN VẬN TỈNH ỦY TUYÊN QUANG</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# KHU VỰC CHỨA 5 ỨNG DỤNG (Đã Nén Chặt Dữ Liệu + 5 Link của Giám đốc Tuấn)
# ==========================================

html_grid = """<div class="ecosystem-grid"><a href="https://tailieuhopbtgdv.streamlit.app/" target="_blank" class="app-card"><div class="app-icon">🏛️</div><div class="app-title">E-Cabinet TGDV</div><div class="app-desc">Phòng họp không giấy. Cung cấp tài liệu số hóa, quản lý thời gian và thu thập ý kiến đại biểu trực tuyến.</div><div class="access-btn">🚀 Truy cập ngay</div></a><a href="https://quan-ly-ho-so-tgdv.streamlit.app/" target="_blank" class="app-card"><div class="app-icon">🗂️</div><div class="app-title">Quản lý Hồ sơ CBCC</div><div class="app-desc">Hệ thống số hóa hồ sơ nhân sự, tự động cập nhật lịch sử công tác, lương, thưởng và xuất Sơ yếu lý lịch chuẩn A4.</div><div class="access-btn">🚀 Truy cập ngay</div></a><a href="https://bao-cao-tgdv.streamlit.app/" target="_blank" class="app-card"><div class="app-icon">📊</div><div class="app-title">Thu thập Báo cáo</div><div class="app-desc">Hệ thống nộp số liệu cơ sở, tổng hợp tự động và hiển thị Dashboard thống kê dành cho Lãnh đạo Ban.</div><div class="access-btn">🚀 Truy cập ngay</div></a><a href="https://tracuuluong-tgdvtq.streamlit.app/" target="_blank" class="app-card"><div class="app-icon">🤖</div><div class="app-title">Trợ lý AI TGDV</div><div class="app-desc">Trợ lý ảo thông minh hỗ trợ tra cứu nhanh chính sách, chế độ, văn bản pháp luật và tư vấn nghiệp vụ.</div><div class="access-btn">🚀 Truy cập ngay</div></a><a href="https://bantinchibo.streamlit.app/" target="_blank" class="app-card"><div class="app-icon">📰</div><div class="app-title">Bản tin Sinh hoạt</div><div class="app-desc">Bản tin điện tử nội bộ, định dạng lật trang hiện đại phục vụ sinh hoạt Chi bộ và thông tin chuyên đề.</div><div class="access-btn">🚀 Truy cập ngay</div></a></div>"""

st.markdown(html_grid, unsafe_allow_html=True)

st.markdown("<br><hr><center><p style='color: #6c757d; font-size: 14px;'>© 2026 - Bản quyền thuộc về Ban Tuyên giáo và Dân vận Tỉnh ủy Tuyên Quang.<br>Phát triển bởi: Đồng chí Ngạc Văn Tuấn</p></center>", unsafe_allow_html=True)
