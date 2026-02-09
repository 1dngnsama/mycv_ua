import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Resume - Andrii Nikoliuk", layout="wide")

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
    st.write("Місто: Київ")
    st.write("Телефон: +380961220400")
    st.write("Email: andrejnikoluk2006@gmail.com")
    st.markdown("---")
    st.write("LinkedIn: [https://www.linkedin.com/in/andrii-nykoliuk-5664b4353/]")

# --- ГОЛОВНИЙ БЛОК ---
st.title("Андрій Николюк")
st.subheader("Junior AI Tools & Data Applications Developer | Data Analyst")
st.write("Студент 2 курсу спеціальності «Системний аналіз» у ДТЕУ.")

st.markdown("---")

# --- ДОСВІД РОБОТИ ---
st.header("Досвід роботи")

# Робота в NGO
st.subheader("Junior AI Tools & Data Applications Developer")
st.write("**NGO CAT-UA** | вер. 2025 – лют. 2026")
st.write("""
- Проєктування та розробка асинхронного Backend для додатків аналізу новин на базі FastAPI.
- Інтеграція та налаштування LLM (OpenAI, Google) для автоматизації класифікації та сумаризації медіа-контенту.
- Створення користувацьких інтерфейсів на Streamlit для візуалізації результатів аналізу та взаємодії з моделями.
- Оптимізація обробки даних, що дозволило підвищити швидкість аналізу текстової інформації.
""")
st.caption("Стек: Python, FastAPI, Streamlit, LLM Integration, REST API, SQL.")
# Робота в Logika
st.subheader("Python Tutor")
st.write("Logika School | вер. 2025 – дотепер")
st.write("- Викладання основ програмування та прикладного Python.")
st.write("- Допомога у розвитку алгоритмічного мислення та розумінні OOP.")
st.caption("Технології: Python, Object-Oriented Programming (OOP).")

st.markdown("---")

# --- ПРОЄКТИ ---
st.header("Проєкти")

col1, col2 = st.columns(2)

with col1:
    st.subheader("NLP Класифікатор текстів")
    st.write("""
    - Реалізував повний Pipeline обробки тексту: очищення, токенізація та векторізація TF-IDF.
    - Протренував та порівняв моделі класифікації за допомогою Scikit-learn для досягнення оптимальних метрик точності.
    - Розгорнув модель як веб-сервіс для класифікації запитів у реальному часі.
    """)
    st.caption("Технології: Scikit-learn, Pandas, Streamlit, Jupyter.")
    st.caption('Лінк: https://1dngnsama-nlp.streamlit.app/ мова введеня - Англійська')
    

with col2:
    st.subheader("Автоматизація розселення (Streamlit, Pandas)")
    st.write("- Веб-додаток для автоматизації розподілу місць розселення у дитячому таборі.")
    st.write("- Оптимізація процесу: скорочення часу з декількох днів до хвилин.")

st.markdown("---")

# --- НАВИЧКИ ТА ОСВІТА ---
col_skills, col_edu = st.columns(2)

with col_skills:
    st.header("Навички")
    st.write("**Data Science & ML:**")
    st.write("- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, BeautifulSoup)")
    st.write("- NLP, статистичний аналіз, EDA, А/В тестування")
    st.write("- SQL (PostgreSQL, MySQL, Window Functions, CTE)")
    st.write("**Engineering & BI:**")
    st.write("- FastAPI, Streamlit, REST API, LLM Integration")
    st.write("- Tableau, Looker Studio, Google Cloud, Azure, Git")
    st.write("**Мови:** Англійська (B2), Українська (C1)")

with col_edu:
    st.header("Освіта та Курси")
    st.write("**ДТЕУ** — Бакалавр 'Системний Аналіз' (2024 – дотепер)")
    st.write("**Курси:**")
    st.write("- SKELAR: IT Analytics Intensive")
    st.write("- DataCamp: Data Analyst in Python")
    st.write("- DataCamp: Associate Data Analyst in SQL")