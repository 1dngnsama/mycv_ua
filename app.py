import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Resume - Andrii Nikoliuk", layout="wide")

# --- ДАНІ РЕЗЮМЕ ---
RESUME_DATA = {
    "name": "Андрій Николюк",
    "title": "Junior AI Tools & Data Applications Developer | Data Analyst",
    "about": "Студент 2 курсу спеціальності «Системний аналіз» у ДТЕУ.",
    "contacts": {
        "city": "Київ",
        "phone": "+380961220400",
        "email": "andrejnikoluk2006@gmail.com",
        "linkedin": "https://www.linkedin.com/in/andrii-nykoliuk-5664b4353/"
    },
    "experience": [
        {
            "role": "Junior AI Tools & Data Applications Developer",
            "company": "NGO CAT-UA",
            "period": "вер. 2025 – лют. 2026",
            "description": [
                "Проєктування та розробка асинхронного Backend для додатків аналізу новин на базі FastAPI.",
                "Інтеграція та налаштування LLM (OpenAI, Google) для автоматизації класифікації та сумаризації медіа-контенту.",
                "Створення користувацьких інтерфейсів на Streamlit для візуалізації результатів аналізу та взаємодії з моделями.",
                "Оптимізація обробки даних, що дозволило підвищити швидкість аналізу текстової інформації."
            ],
            "stack": "Python, FastAPI, Streamlit, LLM Integration, REST API, SQL."
        },
        {
            "role": "Python Tutor",
            "company": "Logika School",
            "period": "вер. 2025 – дотепер",
            "description": [
                "Викладання основ програмування та прикладного Python.",
                "Допомога у розвитку алгоритмічного мислення."
            ],
            "stack": "Python, Object-Oriented Programming (OOP)."
        }
    ],
    "projects": [
        {
            "name": "NLP Класифікатор текстів",
            "description": [
                "Реалізував повний Pipeline обробки тексту: очищення, токенізація та векторізація TF-IDF.",
                "Протренував та порівняв моделі класифікації за допомогою Scikit-learn для досягнення оптимальних метрик точності.",
                "Розгорнув модель як веб-сервіс для класифікації запитів у реальному часі."
            ],
            "tech": "Scikit-learn, Pandas, Streamlit, Jupyter.",
            "link": "https://1dngnsama-nlp.streamlit.app/ мова введеня - Англійська"
        },
        {
            "name": "Автоматизація розселення (Streamlit, Pandas)",
            "description": [
                "Веб-додаток для автоматизації розподілу місць розселення у дитячому таборі.",
                "Оптимізація процесу: скорочення часу з декількох днів до хвилин."
            ],
            "tech": None,
            "link": None
        }
    ],
    "skills": {
        "Data Science & ML": [
            "Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, BeautifulSoup)",
            "NLP, статистичний аналіз, EDA, А/В тестування",
            "SQL (PostgreSQL, MySQL, Window Functions, CTE)"
        ],
        "Engineering & BI": [
            "FastAPI, Streamlit, REST API, LLM Integration",
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

# Стилізація
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1, h2, h3 { color: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# --- БОКОВА ПАНЕЛЬ ---
with st.sidebar:
    st.title("Контакти")
    st.write(f"Місто: {RESUME_DATA['contacts']['city']}")
    st.write(f"Телефон: {RESUME_DATA['contacts']['phone']}")
    st.write(f"Email: {RESUME_DATA['contacts']['email']}")
    st.markdown("---")
    st.write(f"LinkedIn: [{RESUME_DATA['contacts']['linkedin']}]")

# --- ГОЛОВНИЙ БЛОК ---
st.title(RESUME_DATA['name'])
st.subheader(RESUME_DATA['title'])
st.write(RESUME_DATA['about'])

st.markdown("---")

# --- ДОСВІД РОБОТИ ---
st.header("Досвід роботи")

for job in RESUME_DATA['experience']:
    st.subheader(job['role'])
    st.write(f"**{job['company']}** | {job['period']}")
    for item in job['description']:
        st.write(f"- {item}")
    st.caption(f"Стек/Технології: {job['stack']}")

st.markdown("---")

# --- ПРОЄКТИ ---
st.header("Проєкти")

col1, col2 = st.columns(2)

# Розподіл проєктів по колонках
p1 = RESUME_DATA['projects'][0]
p2 = RESUME_DATA['projects'][1]

with col1:
    st.subheader(p1['name'])
    for item in p1['description']:
        st.write(f"- {item}")
    st.caption(f"Технології: {p1['tech']}")
    st.caption(f"Лінк: {p1['link']}")

with col2:
    st.subheader(p2['name'])
    for item in p2['description']:
        st.write(f"- {item}")
    # Другий проєкт не має tech/link

st.markdown("---")

# --- НАВИЧКИ ТА ОСВІТА ---
col_skills, col_edu = st.columns(2)

with col_skills:
    st.header("Навички")
    st.write("**Data & ML:**")
    for s in RESUME_DATA['skills']['Data Science & ML']:
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