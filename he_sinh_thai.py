import streamlit as st
import base64

st.set_page_config(
    page_title="Hệ sinh thái 4.0 - TGDV Tuyên Quang",
    page_icon="🌐",
    layout="wide"
)

def read_image_b64(filename, mime="png"):
    try:
        with open(filename, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8"), mime
    except:
        return None, None

logo_b64, _ = read_image_b64("Logo TGDV.png", "png")
codang_b64, _ = read_image_b64("CoDang.jpg", "jpeg")
bg_b64, _ = read_image_b64("HinhNen.jpg", "jpeg")

# ── Background ──────────────────────────────────────────────────────────────
if bg_b64:
    bg_style = f"background-image:url('data:image/jpeg;base64,{bg_b64}');background-size:cover;background-attachment:fixed;background-position:center;"
else:
    bg_style = "background-color:#f0f2f5;"

# ── Global CSS ───────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

.stApp {{
    {bg_style}
    font-family: 'Be Vietnam Pro', sans-serif;
}}

/* ẩn các thành phần mặc định của Streamlit */
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding: 1.5rem 2rem 3rem !important; max-width: 1280px; margin: 0 auto; }}

/* ── BANNER ── */
.banner {{
    background: linear-gradient(135deg, #002147 0%, #003580 55%, #005096 100%);
    border-radius: 14px;
    padding: 28px 36px;
    display: flex;
    align-items: center;
    gap: 24px;
    margin-bottom: 28px;
    border: 1px solid rgba(255,255,255,0.08);
    position: relative;
    overflow: hidden;
}}
.banner::before {{
    content: '';
    position: absolute;
    right: -60px; top: -60px;
    width: 240px; height: 240px;
    border-radius: 50%;
    background: rgba(255,255,255,0.03);
    pointer-events: none;
}}
.banner::after {{
    content: '';
    position: absolute;
    right: 60px; bottom: -80px;
    width: 180px; height: 180px;
    border-radius: 50%;
    background: rgba(255,255,255,0.04);
    pointer-events: none;
}}
.banner-logo img {{
    height: 72px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 2px 6px rgba(0,0,0,0.3));
}}
.banner-logo span {{
    font-size: 48px;
    line-height: 1;
}}
.banner-text h1 {{
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    line-height: 1.3;
    margin-bottom: 5px;
}}
.banner-text p {{
    font-size: 13px;
    color: rgba(255,255,255,0.72);
    font-weight: 400;
    letter-spacing: 0.3px;
}}
.banner-badge {{
    margin-left: auto;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 8px;
    padding: 8px 14px;
    text-align: center;
    white-space: nowrap;
}}
.banner-badge span {{
    display: block;
    font-size: 20px;
    font-weight: 700;
    color: #5de0c4;
    line-height: 1.2;
}}
.banner-badge small {{
    font-size: 11px;
    color: rgba(255,255,255,0.55);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

/* ── SECTION LABEL ── */
.section-label {{
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #5a6a80;
    margin-bottom: 12px;
    padding-left: 2px;
    display: flex;
    align-items: center;
    gap: 8px;
}}
.section-label::after {{
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(0,0,0,0.08);
}}

/* ── GRID ── */
.app-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 14px;
}}

/* ── CARD ── */
a.card {{
    background: rgba(255,255,255,0.96);
    border-radius: 12px;
    padding: 20px 18px 16px;
    text-decoration: none !important;
    color: inherit !important;
    display: flex;
    flex-direction: column;
    gap: 0;
    border: 1px solid rgba(0,0,0,0.07);
    border-top: 3px solid #003580;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-top-color 0.18s ease;
    position: relative;
    overflow: hidden;
}}
a.card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,53,128,0.13);
    border-top-color: #c8102e;
    text-decoration: none !important;
}}

.card-icon {{
    font-size: 30px;
    margin-bottom: 10px;
    line-height: 1;
}}
.card-icon img {{
    height: 32px;
    width: auto;
    object-fit: contain;
}}

.card-title {{
    font-size: 13px;
    font-weight: 700;
    color: #002147;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 7px;
    line-height: 1.3;
}}

.card-desc {{
    font-size: 12px;
    color: #637080;
    line-height: 1.55;
    flex: 1;
    margin-bottom: 14px;
}}

.card-btn {{
    font-size: 11px;
    font-weight: 600;
    color: #003580;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    border: 1.5px solid #003580;
    border-radius: 6px;
    padding: 6px 10px;
    text-align: center;
    transition: background 0.15s, color 0.15s;
}}
a.card:hover .card-btn {{
    background: #003580;
    color: #ffffff;
}}

/* ── DIVIDER ── */
.divider {{
    height: 1px;
    background: rgba(0,0,0,0.08);
    margin: 28px 0;
}}

/* ── FOOTER ── */
.footer {{
    background: rgba(255,255,255,0.88);
    border-radius: 10px;
    padding: 14px 24px;
    text-align: center;
    font-size: 12.5px;
    color: #4a5568;
    border: 1px solid rgba(0,0,0,0.07);
    line-height: 1.7;
}}
.footer strong {{ color: #002147; font-weight: 600; }}
</style>
""", unsafe_allow_html=True)

# ── BANNER ──────────────────────────────────────────────────────────────────
if logo_b64:
    logo_html = f'<div class="banner-logo"><img src="data:image/png;base64,{logo_b64}" alt="Logo TGDV"></div>'
else:
    logo_html = '<div class="banner-logo"><span>🌐</span></div>'

st.markdown(f"""
<div class="banner">
    {logo_html}
    <div class="banner-text">
        <h1>Hệ sinh thái chuyển đổi số 4.0</h1>
        <p>Ban Tuyên giáo và Dân vận Tỉnh ủy Tuyên Quang</p>
    </div>
    <div class="banner-badge">
        <span>10</span>
        <small>Ứng dụng</small>
    </div>
</div>
""", unsafe_allow_html=True)

# ── APPS DATA ────────────────────────────────────────────────────────────────
if codang_b64:
    icon_nq = f'<img src="data:image/jpeg;base64,{codang_b64}" alt="Cờ Đảng">'
else:
    icon_nq = "🇻🇳"

APPS = [
    {
        "icon": "🌐",
        "title": "Điểm tin Báo chí",
        "desc": "Tổng hợp tin tức tự động 24/7 từ báo chính thống: Thời sự, Quốc tế, Dư luận và Dân vận khéo.",
        "url": "https://diemtinhangngaytgdv.streamlit.app/",
    },
    {
        "icon": "🗂️",
        "title": "Quản lý Hồ sơ CBCC",
        "desc": "Số hóa hồ sơ nhân sự, cập nhật lịch sử công tác, lương và xuất Sơ yếu lý lịch chuẩn A4.",
        "url": "https://quan-ly-ho-so-tgdv.streamlit.app/",
    },
    {
        "icon": "🏛️",
        "title": "E-Cabinet TGDV",
        "desc": "Phòng họp không giấy: tài liệu số hóa, quản lý thời gian và thu thập ý kiến đại biểu trực tuyến.",
        "url": "https://tailieuhopbtgdv.streamlit.app/",
    },
    {
        "icon": "📊",
        "title": "Thu thập Báo cáo",
        "desc": "Nộp số liệu cơ sở, tổng hợp tự động và hiển thị Dashboard thống kê cho Lãnh đạo Ban.",
        "url": "https://bao-cao-tgdv.streamlit.app/",
    },
    {
        "icon": "🤖",
        "title": "AI Tra cứu Lương",
        "desc": "Trợ lý ảo tra cứu tự động thông tin lương, phụ cấp và chế độ của cán bộ, công chức.",
        "url": "https://tracuuluong-tgdvtq.streamlit.app/",
    },
    {
        "icon": "📖",
        "title": "Bản tin Sinh hoạt",
        "desc": "Bản tin điện tử nội bộ định dạng lật trang hiện đại phục vụ sinh hoạt Chi bộ và chuyên đề.",
        "url": "https://bantinchibo.streamlit.app/",
    },
    {
        "icon": icon_nq,
        "title": "Hỏi đáp Nghị quyết",
        "desc": "Chatbot AI tra cứu, giải đáp Nghị quyết Đại hội đại biểu Đảng bộ tỉnh nhiệm kỳ 2025–2030.",
        "url": "http://hoidapnghiquyet.tuyenquang.gov.vn",
        "icon_is_html": True,
    },
    {
        "icon": "💻",
        "title": "Hỏi đáp CĐS",
        "desc": "Trợ lý ảo chuyên biệt cung cấp kiến thức và giải đáp các vấn đề về chuyển đổi số địa phương.",
        "url": "http://hoidapcds.tuyenquang.gov.vn",
    },
    {
        "icon": "📝",
        "title": "Đăng ký Tin bài",
        "desc": "Đăng ký đề tài, gửi bản thảo trực tuyến, duyệt tin và theo dõi tiến độ xuất bản của Ban.",
        "url": "https://dangkytinbaitgdv.streamlit.app/",
    },
    {
        "icon": "📈",
        "title": "Theo dõi Nâng lương",
        "desc": "Quản lý ngạch bậc lương, cảnh báo đến hạn/quá hạn và xuất tờ trình chuẩn thể thức.",
        "url": "https://theodoinangluongbtgdv.streamlit.app/",
    },
]

# ── BUILD GRID HTML ──────────────────────────────────────────────────────────
def make_card(app):
    icon_is_html = app.get("icon_is_html", False)
    if icon_is_html:
        icon_html = f'<div class="card-icon">{app["icon"]}</div>'
    else:
        icon_html = f'<div class="card-icon">{app["icon"]}</div>'

    return f"""
<a href="{app['url']}" target="_blank" class="card">
    {icon_html}
    <div class="card-title">{app['title']}</div>
    <div class="card-desc">{app['desc']}</div>
    <div class="card-btn">Truy cập →</div>
</a>"""

cards_html = "\n".join(make_card(a) for a in APPS)

st.markdown(f"""
<p class="section-label">Danh sách ứng dụng</p>
<div class="app-grid">
{cards_html}
</div>
""", unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <strong>© 2026 Ban Tuyên giáo và Dân vận Tỉnh ủy Tuyên Quang</strong><br>
    Phát triển bởi: Ngạc Văn Tuấn — Chuyên viên Văn phòng Ban Tuyên giáo và Dân vận Tỉnh ủy
</div>
""", unsafe_allow_html=True)
