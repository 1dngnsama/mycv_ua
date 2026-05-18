import os
import io
from datetime import datetime

import requests
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily


# ─────────────────────────────────────────────
# ШРИФТИ З ПIДТРИМКОЮ КИРИЛИЦI
# ─────────────────────────────────────────────
FONT_FILES = {
    "DejaVu":        "DejaVuSans.ttf",
    "DejaVu-Bold":   "DejaVuSans-Bold.ttf",
    "DejaVu-Italic": "DejaVuSans-Oblique.ttf",
    "DejaVu-BoldIt": "DejaVuSans-BoldOblique.ttf",
}

def _find_font_dir() -> str:
    """Шукає директорiю з .ttf файлами."""
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
    if os.path.isdir(local) and all(
        os.path.isfile(os.path.join(local, f)) for f in FONT_FILES.values()
    ):
        return local

    try:
        import matplotlib
        mpl = os.path.join(matplotlib.get_data_path(), "fonts", "ttf")
        if os.path.isdir(mpl) and all(
            os.path.isfile(os.path.join(mpl, f)) for f in FONT_FILES.values()
        ):
            return mpl
    except Exception:
        pass

    raise FileNotFoundError(
        "Не вдалося знайти шрифти DejaVuSans. "
        "Створи папку fonts/ поряд з main.py i помiсти туди файли DejaVuSans*.ttf"
    )


@st.cache_resource
def register_fonts():
    font_dir = _find_font_dir()
    for name, filename in FONT_FILES.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(font_dir, filename)))
    registerFontFamily(
        "DejaVu",
        normal="DejaVu",
        bold="DejaVu-Bold",
        italic="DejaVu-Italic",
        boldItalic="DejaVu-BoldIt",
    )

register_fonts()


# ─────────────────────────────────────────────
# НАЛАШТУВАННЯ СТОРIНКИ
# ─────────────────────────────────────────────
st.set_page_config(page_title="Resume - Andrii Nikoliuk", layout="wide")


# ─────────────────────────────────────────────
# ДАНI РЕЗЮМЕ
# ─────────────────────────────────────────────
RESUME_DATA = {
    "name": "Андрій Николюк",
    "title": "Junior AI Tools & Data Applications Developer | Data Analyst",
    "about": "Студент 2 курсу спеціальності «Системний аналіз» у ДТЕУ.",
    "contacts": {
        "city": "Київ",
        "phone": "+380961220400",
        "email": "andrejnikoluk2006@gmail.com"
    },
    "experience": [
        {
            "role": "Pricing Analyst (Data & Automation)",
            "company": "THRASH!ТРАШ!",
            "period": "кві 2026 р. – дотепер",
            "description": [
                "Сфокусований на моніторингу ринку, відстеженні конкурентів та оптимізації робочих процесів за допомогою автоматизації даних та написання скриптів.",
                "Розробка та підтримка власних веб-скрейперів на Python за допомогою BeautifulSoup4 та Playwright для автоматизації збору даних конкурентів з динамічних веб-сайтів, що рендеряться за допомогою JS.",
                "Проєктування легковагових ETL-конвеєрів з використанням Pandas для очищення, об'єднання та перетворення неструктурованих даних з різних файлових джерел в єдині аналітичні набори даних.",
                "Створення внутрішніх скриптів автоматизації та мікро-утиліт для усунення ручного введення даних та оптимізації процесів рутинної звітності."
            ],
            "stack": "Python, Playwright, BeautifulSoup4, Pandas, Data Automation, SQL, Excel/Google Sheets, ETL, Data Analysis, Web Scraping, Relational Databases, EDA, A/B Testing"
        },
        {
            "role": "Junior AI Tools & Data Applications Developer",
            "company": "NGO CAT-UA",
            "period": "січ. 2025 – січ. 2026",
            "description": [
                "Проєктування та розробка асинхронного Backend для додатків аналізу новин на базі FastAPI.",
                "Інтеграція та налаштування LLM (OpenAI, Google) для автоматизації класифікації та сумаризації медіа-контенту.",
                "Створення користувацьких інтерфейсів на Streamlit для візуалізації результатів аналізу та взаємодії з моделями.",
                "Оптимізація обробки даних, що дозволило підвищити швидкість аналізу текстової інформації.",
            ],
            "stack": "Python, FastAPI, Streamlit, LLM Integration, LangChain, REST API, SQL."
        },
        {
            "role": "Python Tutor",
            "company": "Logika School",
            "period": "вер. 2025 – дотепер",
            "description": [
                "Викладання основ програмування та прикладного Python.",
                "Допомога у розвитку алгоритмічного мислення.",
            ],
            "stack": "Python, Object-Oriented Programming, Data analysis, Machine learning"
        }
    ],
    "projects": [
        {
            "name": "NLP Класифікатор текстів",
            "description": [
                "Реалізував повний Pipeline обробки тексту: очищення, токенізація та векторизація TF-IDF.",
                "Протренував та порівняв моделі класифікації за допомогою Scikit-learn для досягнення оптимальних метрик точності.",
                "Розгорнув модель як веб-сервіс для класифікації запитів у реальному часі.",
            ],
            "tech": "Scikit-learn, Pandas, Streamlit.",
            "link": "https://1dngnsama-nlp.streamlit.app/"
        },
        {
            "name": "Автоматизація розселення (Streamlit, Pandas)",
            "description": [
                "Розробив веб-додаток для автоматизації розподілу місць розселення у дитячому таборі.",
                "Впровадив пайплайн автоматизованої обробки вхідних документів (Word, PDF) з використанням технологій OCR.",
                "Налаштував алгоритми очищення та агрегації розпізнаної інформації з подальшим автоматичним додаванням до зведених таблиць.",
            ],
            "tech": "Python, Streamlit, Pandas, LLM APIs, OCR",
            "link": None
        },
        {
            "name": "Tunescope - аналог Shazam",
            "description": [
                "Розробив вебзастосунок для точного розпізнавання музичних треків із мікрофона або завантажених файлів.",
                "Імплементував пайплайн цифрової обробки сигналів (DSP), спектрограми (STFT), Constellation Map та 30-бітні хеші.",
                "Спроєктував швидку систему пошуку співпадінь за алгоритмом гістограм часових зсувів та модуль поповнення бази з YouTube.",
            ],
            "tech": "Python, Streamlit, NumPy, SciPy, SQLite, SQLAlchemy",
            "link": None
        }
    ],
    "skills": {
        "Data Science & ML & AI": [
            "Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, web scraping libraries)",
            "NLP, статистичний аналіз, EDA, A/B тестування",
            "SQL (PostgreSQL, MySQL, Window Functions, CTE)",
        ],
        "Engineering & BI": [
            "FastAPI, Streamlit, REST API, LLM Integration (LangChain)",
            "Tableau, Looker Studio, Google Cloud, Azure, Git"
        ],
        "Languages": "Англійська (B2), Українська (C1)"
    },
    "education": {
        "university": "ДТЕУ — Бакалавр 'Системний Аналіз' (2024 – дотепер)",
        "courses": [
            "SKELAR: IT Analytics Intensive",
            "DataCamp: Data Analyst in Python",
            "DataCamp: Associate Data Analyst in SQL"
        ]
    }
}


# ─────────────────────────────────────────────
# TELEGRAM NOTIFICATION
# ─────────────────────────────────────────────
def send_telegram_notification(event_type: str):
    try:
        bot_token = st.secrets["telegram"]["bot_token"]
        chat_id   = st.secrets["telegram"]["chat_id"]
    except (KeyError, FileNotFoundError):
        return

    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    text = (
        f"Хтось переглядає твоє резюме!\n{now}"
        if event_type == "view"
        else f"Хтось завантажив твоє резюме (PDF)!\n{now}"
    )
    try:
        requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            json={"chat_id": chat_id, "text": text},
            timeout=5
        )
    except Exception:
        pass


# ─────────────────────────────────────────────
# PDF GENERATION
# ─────────────────────────────────────────────
def generate_pdf(data: dict) -> bytes:
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=1.8 * cm,
        leftMargin=1.8 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    ACCENT  = colors.HexColor("#1a6fbf")
    DARK    = colors.HexColor("#1a1a1a")
    GRAY    = colors.HexColor("#555555")
    LIGHTBG = colors.HexColor("#f0f4fa")

    def ps(name, **kw):
        kw.setdefault("fontName", "DejaVu")
        return ParagraphStyle(name, **kw)

    # Виправлено: додано leading=26 та збільшено spaceAfter для уникнення накладання
    s_name   = ps("s_name",   fontSize=20, leading=26, textColor=DARK,   spaceAfter=8,   fontName="DejaVu-Bold")
    s_title  = ps("s_title",  fontSize=10, leading=12, textColor=ACCENT,  spaceAfter=4,   fontName="DejaVu-Italic")
    s_about  = ps("s_about",  fontSize=9,  textColor=GRAY,   spaceAfter=6)
    s_h2     = ps("s_h2",     fontSize=12, textColor=ACCENT,  spaceBefore=10, spaceAfter=4, fontName="DejaVu-Bold")
    s_h2_col = ps("s_h2_col", fontSize=12, textColor=ACCENT,  spaceAfter=6,   fontName="DejaVu-Bold")
    s_job    = ps("s_job",    fontSize=10, textColor=DARK,   spaceAfter=1,   fontName="DejaVu-Bold")
    s_meta   = ps("s_meta",   fontSize=9,  textColor=GRAY,   spaceAfter=3,   fontName="DejaVu-Italic")
    s_body   = ps("s_body",   fontSize=9,  textColor=DARK,   spaceAfter=2,   leftIndent=10)
    s_cap    = ps("s_cap",    fontSize=8,  textColor=GRAY,   spaceAfter=6,   fontName="DejaVu-Italic", leftIndent=10)
    s_cont   = ps("s_cont",   fontSize=9,  textColor=DARK,   spaceAfter=2,   alignment=TA_CENTER)
    s_col    = ps("s_col",    fontSize=9,  textColor=DARK,   leading=14,     fontName="DejaVu")

    story = []

    # Шапка
    story.append(Paragraph(data["name"],  s_name))
    story.append(Paragraph(data["title"], s_title))
    story.append(Paragraph(data["about"], s_about))

    # Контакти (без LinkedIn, 3 колонки розтягнуті на всю ширину)
    c = data["contacts"]
    ct = Table(
        [[
            Paragraph(c["city"],  s_cont),
            Paragraph(c["phone"], s_cont),
            Paragraph(c["email"], s_cont),
        ]],
        colWidths=[5.0*cm, 5.0*cm, 7.4*cm] 
    )
    ct.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LIGHTBG),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(ct)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT))

    # Досвід
    story.append(Paragraph("Досвід роботи", s_h2))
    for job in data["experience"]:
        story.append(Paragraph(job["role"], s_job))
        story.append(Paragraph(f"{job['company']}  |  {job['period']}", s_meta))
        for item in job["description"]:
            story.append(Paragraph(f"- {item}", s_body))
        story.append(Paragraph(f"Стек: {job['stack']}", s_cap))

    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))

    # Проєкти
    story.append(Paragraph("Проєкти", s_h2))
    for proj in data["projects"]:
        story.append(Paragraph(proj["name"], s_job))
        for item in proj["description"]:
            story.append(Paragraph(f"- {item}", s_body))
        story.append(Paragraph(f"Технології: {proj['tech']}", s_cap))
        if proj.get("link"):
            story.append(Paragraph(f"Посилання: {proj['link']}", s_cap))

    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))

    # Навички + Освіта
    sk  = data["skills"]
    edu = data["education"]

    s_section = ps("s_section", fontSize=9, textColor=DARK, fontName="DejaVu-Bold", spaceAfter=2)
    s_item    = ps("s_item",    fontSize=9, textColor=DARK, fontName="DejaVu",      spaceAfter=1, leftIndent=6)

    def skills_paragraphs():
        items = []
        items.append(Paragraph("Data Science & ML & AI:", s_section))
        for s in sk["Data Science & ML & AI"]:
            items.append(Paragraph(f"- {s}", s_item))
        items.append(Spacer(1, 4))
        items.append(Paragraph("Engineering & BI:", s_section))
        for s in sk["Engineering & BI"]:
            items.append(Paragraph(f"- {s}", s_item))
        items.append(Spacer(1, 4))
        items.append(Paragraph(f"Мови: {sk['Languages']}", s_item))
        return items

    def edu_paragraphs():
        items = []
        items.append(Paragraph(edu["university"], s_section))
        items.append(Spacer(1, 4))
        items.append(Paragraph("Курси:", s_section))
        for course in edu["courses"]:
            items.append(Paragraph(f"- {course}", s_item))
        return items

    skills_col = [Paragraph("Навички", s_h2_col)] + skills_paragraphs()
    edu_col    = [Paragraph("Освіта та Курси", s_h2_col)] + edu_paragraphs()

    two_col = Table(
        [[skills_col, edu_col]],
        colWidths=[9*cm, 9*cm]
    )
    two_col.setStyle(TableStyle([
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(two_col)

    doc.build(story)
    buffer.seek(0)
    return buffer.read()


# ─────────────────────────────────────────────
# СПОВІЩЕННЯ ПРИ ПЕРЕГЛЯДІ
# ─────────────────────────────────────────────
if "page_view_sent" not in st.session_state:
    st.session_state["page_view_sent"] = True
    send_telegram_notification("view")


# ─────────────────────────────────────────────
# СТИЛІЗАЦІЯ
# ─────────────────────────────────────────────
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1, h2, h3 { color: #1a1a1a; }
    </style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# БОКОВА ПАНЕЛЬ
# ─────────────────────────────────────────────
with st.sidebar:
    st.title("Контакти")
    st.write(f"Місто: {RESUME_DATA['contacts']['city']}")
    st.write(f"Телефон: {RESUME_DATA['contacts']['phone']}")
    st.write(f"Email: {RESUME_DATA['contacts']['email']}")
    # Посилання на LinkedIn видалено звідси
    st.markdown("---")

    st.subheader("Завантажити резюме")
    if st.button("Згенерувати PDF", use_container_width=True):
        with st.spinner("Генерую PDF..."):
            pdf_bytes = generate_pdf(RESUME_DATA)
            send_telegram_notification("download")
            st.download_button(
                label="Завантажити resume.pdf",
                data=pdf_bytes,
                file_name="Andrii_Nykoliuk_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )


# ─────────────────────────────────────────────
# ГОЛОВНИЙ БЛОК
# ─────────────────────────────────────────────
st.title(RESUME_DATA['name'])
st.subheader(RESUME_DATA['title'])
st.write(RESUME_DATA['about'])

st.markdown("---")

# Досвід роботи
st.header("Досвід роботи")
for job in RESUME_DATA['experience']:
    st.subheader(job['role'])
    st.write(f"**{job['company']}** | {job['period']}")
    for item in job['description']:
        st.write(f"- {item}")
    st.caption(f"Стек/Технології: {job['stack']}")

st.markdown("---")

# Проєкти
st.header("Проєкти")
col1, col2, col3 = st.columns(3)
p1, p2, p3 = RESUME_DATA['projects']

with col1:
    st.subheader(p1['name'])
    for item in p1['description']:
        st.write(f"- {item}")
    st.caption(f"Технології: {p1['tech']}")
    if p1.get('link'):
        st.caption(f"Посилання: {p1['link']}")

with col2:
    st.subheader(p2['name'])
    for item in p2['description']:
        st.write(f"- {item}")
    st.caption(f"Технології: {p2['tech']}")

with col3:
    st.subheader(p3['name'])
    for item in p3['description']:
        st.write(f"- {item}")
    st.caption(f"Технології: {p3['tech']}")

st.markdown("---")

# Навички та Освіта
col_skills, col_edu = st.columns(2)

with col_skills:
    st.header("Навички")
    st.write("**Data & ML:**")
    for s in RESUME_DATA['skills']['Data Science & ML & AI']:
        st.write(f"- {s}")
    st.write("**Engineering & BI:**")
    for s in RESUME_DATA['skills']['Engineering & BI']:
        st.write(f"- {s}")
    st.write(f"**Мови:** {RESUME_DATA['skills']['Languages']}")

with col_edu:
    st.header("Освіта та Курси")
    st.write(f"**{RESUME_DATA['education']['university']}**")
    st.write("**Курси:**")
    for course in RESUME_DATA['education']['courses']:
        st.write(f"- {course}")