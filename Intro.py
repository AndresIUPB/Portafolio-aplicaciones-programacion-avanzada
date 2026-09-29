"""Catálogo de aplicaciones de Inteligencia Artificial (Streamlit).

Para añadir una app nueva: agrega un diccionario a la lista APPS. No hace falta tocar la interfaz.
"""
import base64
import html
from collections import Counter
from pathlib import Path

import streamlit as st

# ─────────────────────────── Configuración ───────────────────────────
st.set_page_config(page_title="Catálogo de IA", page_icon="✨", layout="wide")

SITE_URL = "https://sites.google.com/view/aplicacionesdeia/inicio"
# Si escribes tu usuario de GitHub, los repositorios se vuelven enlaces.
# Vacío = se muestra solo el nombre del repositorio (no se inventa ninguna URL).
GITHUB_USER = ""
IMG_DIR = Path(__file__).parent  # carpeta donde están las imágenes de la plantilla

# Cada categoría: (color de acento, emoji de respaldo)
CATEGORIES = {
    "Voz y audio": ("#0a84ff", "🎙️"),
    "Visión": ("#bf5af2", "👁️"),
    "Lenguaje": ("#30b0c7", "💬"),
    "Datos": ("#34c759", "📊"),
    "Modelos predictivos": ("#ff9f0a", "📈"),
    "Sensores e IoT": ("#ff375f", "📡"),
    "Fundamentos": ("#5e5ce6", "🧮"),
}

# ─────────────────────────── Datos ───────────────────────────
APPS = [
    # ---- Aplicaciones de la plantilla original ----
    dict(title="Texto a voz", category="Voz y audio", kind="Aplicación",
         description="Escribe un texto y escucha su contenido en audio.",
         url="https://imultimod.streamlit.app/", repository=None,
         technologies=["Voz"], image="txt_to_audio2.png"),
    dict(title="Detector de objetos", category="Visión", kind="Aplicación",
         description="Sube una imagen y descubre qué objetos aparecen en ella.",
         url="https://yolov5cmc.streamlit.app/", repository=None,
         technologies=["YOLO"], image="txt_to_audio.png"),
    dict(title="Tu modelo entrenado", category="Visión", kind="Aplicación",
         description="Prueba un modelo que fue entrenado por nosotros mismos.",
         url="https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/", repository=None,
         technologies=["YOLO"], image="OIG5.jpg"),
    dict(title="Voz a texto", category="Voz y audio", kind="Aplicación",
         description="Habla y mira cómo tu voz se convierte en texto escrito.",
         url="https://traductorw.streamlit.app/", repository=None,
         technologies=["Voz"], image="OIG8.jpg"),
    dict(title="Análisis de datos con agentes", category="Datos", kind="Aplicación",
         description="Analiza tus datos conversando con un agente de IA.",
         url="https://dataagente.streamlit.app/", repository=None,
         technologies=["Agentes"], image="data_analisis.png"),
    dict(title="Transcriptor de audio y video", category="Voz y audio", kind="Aplicación",
         description="Convierte el audio o el video en una transcripción escrita.",
         url="https://transcript-whisper.streamlit.app/", repository=None,
         technologies=["Whisper"], image="OIG3.jpg"),
    dict(title="Chatea con tu PDF", category="Lenguaje", kind="Aplicación",
         description="Sube un documento PDF y hazle preguntas sobre su contenido.",
         url="https://chatpdf-cc.streamlit.app/", repository=None,
         technologies=["RAG"], image="Chat_pdf.png"),
    dict(title="Análisis de imágenes", category="Visión", kind="Aplicación",
         description="Sube una imagen y pide que te la describa y analice.",
         url="https://vision2-gpt4o.streamlit.app/", repository=None,
         technologies=["GPT-4o", "Visión"], image="OIG4.jpg"),
    dict(title="Sistema ciberfísico", category="Sensores e IoT", kind="Aplicación",
         description="Una muestra de cómo la IA puede interactuar con el mundo físico.",
         url="https://vision2-gpt4o.streamlit.app/", repository=None,
         technologies=["Ciberfísico"], image="OIG6.jpg"),
    # ---- Sesiones del curso (tabla) ----
    dict(title="Cálculo aplicado: el gradiente", category="Fundamentos", kind="Sesión 3",
         description="Explora cómo el gradiente indica hacia dónde mejora una función.",
         url="https://calculo-aplicado-gradiente.streamlit.app",
         repository="Calculo-aplicado-gradiente", technologies=["Gradiente"]),
    dict(title="Detector de anomalías", category="Fundamentos", kind="Sesión 4",
         description="Practica lógica, eficiencia (Big-O) y vectorización para encontrar datos extraños.",
         url="https://detector-anomalias-pujphzyih8brne8nhox5zv.streamlit.app",
         repository="detector-anomalias", technologies=["Big-O", "Vectorización"]),
    dict(title="Preparación de datos", category="Datos", kind="Sesión 5",
         description="Aprende a dejar los datos limpios y listos antes de analizarlos.",
         url="https://preparaci-n-de-datos-yupvhtm8dhjnmfslfsmt3u.streamlit.app",
         repository="Preparaci-n-de-datos", technologies=["Limpieza de datos"]),
    dict(title="Análisis y preparación con MARCO", category="Datos", kind="Sesión 6",
         description="Una aplicación para revisar y preparar tus datos paso a paso.",
         url="https://preparacion.streamlit.app",
         repository="aplicacion-de-analisis-y-preparacion-de-datos-con-MARCO",
         technologies=["MARCO"]),
    dict(title="Regresión lineal", category="Modelos predictivos", kind="Sesión 7",
         description="Mira cómo una línea puede describir la relación entre dos variables.",
         url="https://regresion-lineal-py.streamlit.app",
         repository="regresion-lineal", technologies=["Regresión lineal"]),
    dict(title="Series de tiempo", category="Modelos predictivos", kind="Sesión 8",
         description="Analiza datos que cambian con el tiempo y observa sus patrones.",
         url="https://time-series-intelligence.streamlit.app",
         repository="Time_Series_Intelligence", technologies=["Series de tiempo"]),
    dict(title="Pronóstico de calidad del aire", category="Modelos predictivos", kind="Aplicación",
         description="Consulta una predicción de la calidad del aire a partir de datos.",
         url="https://pronosticador-de-calidad-de-aire.streamlit.app",
         repository="pronosticador-de-calidad-de-aire", technologies=["Predicción"]),
    dict(title="Sensor de humedad IoT", category="Sensores e IoT", kind="Sesión 10",
         description="Sigue cómo un dispositivo captura datos de humedad y cómo se procesan.",
         url="https://dispositivo-iot-humedad.streamlit.app",
         repository="streamlit-dispositivo-iot-humedad", technologies=["IoT", "Captura de datos"]),
    dict(title="¿Llueve o no llueve?", category="Modelos predictivos", kind="Sesión 11",
         description="Pasa de predecir un número a tomar una decisión de sí o no.",
         url="https://decisiones-binarias-llueve-o-no-j6ardkm39sqb4dvdqvtqf3.streamlit.app",
         repository="decisiones-binarias-llueve-o-no", technologies=["Regresión logística"]),
    dict(title="De la tierra al algoritmo", category="Modelos predictivos", kind="Sesión 12",
         description="Clasifica la fertilidad de un suelo comparándolo con casos parecidos.",
         url="https://de-la-tierra-al-algoritmo.streamlit.app",
         repository="De-la-Tierra-al-Algoritmo", technologies=["KNN", "Clasificación"]),
]

# ─────────────────────────── Estilos ───────────────────────────
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&display=swap');
:root{--ink:#1d1d1f;--mute:#6e6e73;--line:#e8e8ed;--bg:#f5f5f7;}
html,body,.stApp,[class*="css"]{font-family:'Manrope',-apple-system,'SF Pro Text','Segoe UI',Roboto,sans-serif;}
.stApp{background:radial-gradient(1200px 500px at 15% -10%,#e3f0ff 0%,transparent 60%),
 radial-gradient(900px 500px at 95% 0%,#efe6ff 0%,transparent 55%),var(--bg);color:var(--ink);}
header[data-testid="stHeader"]{background:transparent;}
.block-container{max-width:1180px;padding-top:2.5rem;padding-bottom:4rem;}
h1,h2,h3,p,span,label,div{color:var(--ink);}
.hero{padding:3.5rem 0 2rem;max-width:760px;}
.hero h1{font-size:clamp(2.2rem,6vw,4rem);line-height:1.05;font-weight:800;letter-spacing:-.03em;margin:0 0 1rem;}
.hero p{font-size:1.15rem;line-height:1.6;color:var(--mute);margin:0 0 1.5rem;max-width:620px;}
.btn{display:inline-block;padding:.65rem 1.2rem;border-radius:980px;font-weight:700;font-size:.92rem;
 text-decoration:none!important;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;}
.btn:focus-visible{outline:3px solid #0a84ff55;outline-offset:2px;}
.btn.primary{background:#0071e3;color:#fff!important;}
.btn.primary:hover{background:#0077ed;transform:translateY(-1px);box-shadow:0 6px 16px #0071e340;}
.btn.ghost{background:#fff;color:#0071e3!important;border:1px solid var(--line);}
.btn.ghost:hover{background:#f0f6ff;}
.stats{display:flex;gap:2.5rem;flex-wrap:wrap;margin:2rem 0 1rem;}
.stat b{display:block;font-size:2rem;font-weight:800;letter-spacing:-.02em;}
.stat span{color:var(--mute);font-size:.9rem;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(285px,1fr));gap:1.4rem;margin-top:1rem;}
.card{background:#fff;border-radius:22px;overflow:hidden;border:1px solid var(--line);display:flex;flex-direction:column;
 box-shadow:0 1px 2px #0000000a,0 8px 24px #00000008;transition:transform .25s ease,box-shadow .25s ease;}
.card:hover{transform:translateY(-4px);box-shadow:0 2px 4px #0000000a,0 18px 40px #00000018;}
.cover{position:relative;height:150px;display:flex;align-items:center;justify-content:center;font-size:3.2rem;overflow:hidden;}
.cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.kind{position:absolute;top:12px;left:12px;background:#ffffffd9;backdrop-filter:blur(8px);padding:.2rem .65rem;
 border-radius:980px;font-size:.75rem;font-weight:700;z-index:2;}
.body{padding:1.1rem 1.2rem 1.25rem;display:flex;flex-direction:column;gap:.55rem;flex:1;}
.cat{font-size:.82rem;font-weight:700;}
.body h3{margin:0;font-size:1.15rem;font-weight:800;letter-spacing:-.01em;line-height:1.25;}
.body p{margin:0;color:var(--mute);font-size:.94rem;line-height:1.5;}
.tags{display:flex;flex-wrap:wrap;gap:.35rem;}
.tag{background:var(--bg);border-radius:8px;padding:.15rem .55rem;font-size:.76rem;font-weight:500;color:#424245;}
.actions{margin-top:auto;padding-top:.7rem;display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;}
.actions .btn{padding:.5rem 1rem;font-size:.85rem;}
.repo{font-size:.78rem;color:var(--mute);word-break:break-all;}
.repo a{color:var(--mute)!important;}
.empty{text-align:center;color:var(--mute);padding:3rem 0;}
@media (prefers-reduced-motion:reduce){*{transition:none!important;}}
@media (max-width:640px){.hero{padding-top:1.5rem;}.stats{gap:1.5rem;}}
</style>
"""

# ─────────────────────────── Funciones ───────────────────────────
@st.cache_data(show_spinner=False)
def image_data_uri(name):
    """Devuelve la imagen local como data URI, o '' si no existe (se usa el degradado)."""
    if not name:
        return ""
    path = IMG_DIR / name
    if not path.is_file():
        return ""
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def esc(text):
    return html.escape(str(text), quote=True)


def render_card(app):
    color, emoji = CATEGORIES.get(app["category"], ("#0a84ff", "✨"))
    uri = image_data_uri(app.get("image"))
    img = f'<img src="{uri}" alt="" loading="lazy" onerror="this.style.display=\'none\'">' if uri else ""
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in app.get("technologies", []))
    repo = app.get("repository")
    repo_html = ""
    if repo:
        if GITHUB_USER:
            repo_html = (f'<a class="btn ghost" href="https://github.com/{esc(GITHUB_USER)}/{esc(repo)}" '
                         f'target="_blank" rel="noopener">Repositorio</a>')
        else:
            repo_html = f'<span class="repo">Repositorio: {esc(repo)}</span>'
    return (
        '<div class="card">'
        f'<div class="cover" style="background:linear-gradient(135deg,{color}26,{color}66)">'
        f'<span class="kind">{esc(app["kind"])}</span>{esc(emoji)}{img}</div>'
        '<div class="body">'
        f'<span class="cat" style="color:{color}">{esc(app["category"])}</span>'
        f'<h3>{esc(app["title"])}</h3>'
        f'<p>{esc(app["description"])}</p>'
        f'<div class="tags">{tags}</div>'
        f'<div class="actions"><a class="btn primary" href="{esc(app["url"])}" target="_blank" rel="noopener">'
        f'Abrir aplicación</a>{repo_html}</div>'
        '</div></div>'
    )


def matches(app, query, category):
    if category != "Todas" and app["category"] != category:
        return False
    if not query:
        return True
    haystack = " ".join([app["title"], app["description"], app["category"], app["kind"],
                         " ".join(app.get("technologies", []))]).lower()
    return all(word in haystack for word in query.lower().split())


# ─────────────────────────── Interfaz ───────────────────────────
st.markdown(CSS, unsafe_allow_html=True)

n_repos = sum(1 for a in APPS if a.get("repository"))
n_cats = len({a["category"] for a in APPS})
st.markdown(
    '<section class="hero"><h1>Inteligencia artificial que puedes probar.</h1>'
    '<p>Una colección de aplicaciones interactivas: convierten voz en texto, reconocen objetos, '
    'analizan datos y hacen predicciones. Abre cualquiera y experimenta.</p>'
    f'<a class="btn primary" href="#catalogo">Ver aplicaciones</a> '
    f'<a class="btn ghost" href="{esc(SITE_URL)}" target="_blank" rel="noopener">Ejercicios y páginas</a>'
    f'<div class="stats"><div class="stat"><b>{len(APPS)}</b><span>aplicaciones</span></div>'
    f'<div class="stat"><b>{n_cats}</b><span>temas</span></div>'
    f'<div class="stat"><b>{n_repos}</b><span>con repositorio</span></div></div></section>'
    '<div id="catalogo"></div>',
    unsafe_allow_html=True,
)

counts = Counter(a["category"] for a in APPS)
query = st.text_input("Buscar", placeholder="Busca por nombre, tema o técnica (por ejemplo: voz, KNN, datos)",
                      label_visibility="collapsed")
options = ["Todas"] + [c for c in CATEGORIES if counts.get(c)]
category = st.pills("Tema", options, default="Todas", label_visibility="collapsed",
                    format_func=lambda c: c if c == "Todas" else f"{c} ({counts[c]})") or "Todas"

visible = [a for a in APPS if matches(a, query, category)]
if visible:
    st.caption(f"{len(visible)} de {len(APPS)} aplicaciones")
    st.markdown('<div class="grid">' + "".join(render_card(a) for a in visible) + "</div>",
                unsafe_allow_html=True)
else:
    st.markdown('<div class="empty"><h3>No encontramos resultados</h3>'
                '<p>Prueba con otra palabra o elige "Todas" en los temas.</p></div>',
                unsafe_allow_html=True)

# ─────────────────────────── Información adicional ───────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("¿Qué temas y técnicas aparecen en este catálogo?"):
    left, right = st.columns(2)
    with left:
        st.markdown("**Temas**")
        for cat, n in counts.most_common():
            st.markdown(f"- {cat}: {n} {'aplicación' if n == 1 else 'aplicaciones'}")
    with right:
        st.markdown("**Técnicas y conceptos**")
        techs = sorted({t for a in APPS for t in a.get("technologies", [])})
        st.markdown(", ".join(techs))

with st.expander("Notas sobre los enlaces"):
    st.markdown(
        "- **Análisis de imágenes** y **Sistema ciberfísico** comparten el mismo enlace de Streamlit.\n"
        "- **Tu modelo entrenado** usa una dirección generada automáticamente por Streamlit.\n"
        "- Los repositorios se muestran por nombre; define `GITHUB_USER` en el código para convertirlos en enlaces."
    )
