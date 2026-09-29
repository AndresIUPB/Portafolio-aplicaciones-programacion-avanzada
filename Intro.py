"""
Catálogo de aplicaciones de IA y ciencia de datos (Streamlit).
"""
import html
from collections import Counter

import streamlit as st

st.set_page_config(page_title="Catálogo de IA", page_icon="✨", layout="wide")

SITE_URL = "https://sites.google.com/view/aplicacionesdeia/inicio"
GITHUB_USER = "AndresIUPB"

# categoría: (color de acento, segundo color, trazo del icono SVG 24x24)
CATEGORIES = {
    "Fundamentos": ("#6366f1", "#a78bfa", "M18 5H6l6 7-6 7h12"),
    "Datos": ("#10b981", "#22d3ee", "M4 20V10M10 20V4M16 20v-7M22 20H2"),
    "Modelos predictivos": ("#f59e0b", "#f43f5e", "M3 17l6-6 4 4 8-8M15 7h6v6"),
    "Sensores e IoT": ("#0ea5e9", "#6366f1",
                       "M12 20h.01M8.5 16.5a5 5 0 0 1 7 0M5 13a10 10 0 0 1 14 0M2 9.5a15 15 0 0 1 20 0"),
}

APPS = [
    dict(title="Cálculo aplicado: el gradiente", category="Fundamentos", kind="Sesión 3",
         description="Explora cómo el gradiente indica hacia dónde mejora una función.",
         url="https://calculo-aplicado-gradiente.streamlit.app",
         repository="Calculo-aplicado-gradiente", technologies=["Gradiente"], photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX8GxVZ7UeyLFWxeWiC3-llw7fAUh66-G7zPirIxehqA&s=10"),
    dict(title="Detector de anomalías", category="Fundamentos", kind="Sesión 4",
         description="Practica lógica, eficiencia (Big-O) y vectorización para encontrar datos extraños.",
         url="https://detector-anomalias-pujphzyih8brne8nhox5zv.streamlit.app",
         repository="detector-anomalias", technologies=["Big-O", "Vectorización"], photo="datacenter"),
    dict(title="Preparación de datos", category="Datos", kind="Sesión 5",
         description="Aprende a dejar los datos limpios y listos antes de analizarlos.",
         url="https://preparaci-n-de-datos-yupvhtm8dhjnmfslfsmt3u.streamlit.app",
         repository="Preparaci-n-de-datos", technologies=["Limpieza de datos"], photo="laptop"),
    dict(title="Análisis y preparación con MARCO", category="Datos", kind="Sesión 6",
         description="Una aplicación para revisar y preparar tus datos paso a paso.",
         url="https://preparacion.streamlit.app",
         repository="aplicacion-de-analisis-y-preparacion-de-datos-con-MARCO",
         technologies=["MARCO"], photo="analytics"),
    dict(title="Regresión lineal", category="Modelos predictivos", kind="Sesión 7",
         description="Mira cómo una línea puede describir la relación entre dos variables.",
         url="https://regresion-lineal-py.streamlit.app",
         repository="regresion-lineal", technologies=["Regresión lineal"], photo="architecture"),
    dict(title="Series de tiempo", category="Modelos predictivos", kind="Sesión 8",
         description="Analiza datos que cambian con el tiempo y observa sus patrones.",
         url="https://time-series-intelligence.streamlit.app",
         repository="Time_Series_Intelligence", technologies=["Series de tiempo"], photo="clock"),
    dict(title="Pronóstico de calidad del aire", category="Modelos predictivos", kind="Aplicación",
         description="Consulta una predicción de la calidad del aire a partir de datos.",
         url="https://pronosticador-de-calidad-de-aire.streamlit.app",
         repository="pronosticador-de-calidad-de-aire", technologies=["Predicción"], photo="smog"),
    dict(title="Sensor de humedad IoT", category="Sensores e IoT", kind="Sesión 10",
         description="Sigue cómo un dispositivo captura datos de humedad y cómo se procesan.",
         url="https://dispositivo-iot-humedad.streamlit.app",
         repository="streamlit-dispositivo-iot-humedad", technologies=["IoT", "Captura de datos"],
         photo="greenhouse"),
    dict(title="¿Llueve o no llueve?", category="Modelos predictivos", kind="Sesión 11",
         description="Pasa de predecir un número a tomar una decisión de sí o no.",
         url="https://decisiones-binarias-llueve-o-no-j6ardkm39sqb4dvdqvtqf3.streamlit.app",
         repository="decisiones-binarias-llueve-o-no", technologies=["Regresión logística"], photo="rain"),
    dict(title="De la tierra al algoritmo", category="Modelos predictivos", kind="Sesión 12",
         description="Clasifica la fertilidad de un suelo comparándolo con casos parecidos.",
         url="https://de-la-tierra-al-algoritmo.streamlit.app",
         repository="De-la-Tierra-al-Algoritmo", technologies=["KNN", "Clasificación"], photo="soil"),
]

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&display=swap');
:root{--ink:#0f172a;--mute:#64748b;--line:#e2e8f0;}
html,body,.stApp{font-family:'Inter',-apple-system,'Segoe UI',Roboto,sans-serif;}
.stApp{background:linear-gradient(180deg,#eef2ff 0%,#f8fafc 420px,#f8fafc 100%);}
header[data-testid="stHeader"]{background:transparent;}
.block-container{max-width:1200px;padding-top:1.5rem;padding-bottom:4rem;}
.hero{position:relative;overflow:hidden;border-radius:32px;padding:3.5rem 3rem;margin-bottom:2.5rem;color:#fff;
 background:radial-gradient(600px 300px at 10% 0%,#4f46e5aa,transparent 70%),
 radial-gradient(500px 400px at 100% 100%,#06b6d4aa,transparent 70%),
 radial-gradient(400px 300px at 60% 20%,#c026d355,transparent 70%),#0b1020;
 box-shadow:0 30px 60px -20px #1e1b4b80;}
.hero::before{content:"";position:absolute;inset:0;opacity:.35;pointer-events:none;
 background-image:radial-gradient(#ffffff55 1px,transparent 1px);background-size:26px 26px;
 mask-image:linear-gradient(120deg,#000 0%,transparent 75%);-webkit-mask-image:linear-gradient(120deg,#000 0%,transparent 75%);}
.orb{position:absolute;border-radius:50%;filter:blur(50px);opacity:.55;animation:drift 14s ease-in-out infinite alternate;pointer-events:none;}
.orb.a{width:260px;height:260px;background:#6366f1;top:-80px;right:20%;}
.orb.b{width:220px;height:220px;background:#22d3ee;bottom:-90px;left:35%;animation-delay:-6s;}
@keyframes drift{from{transform:translate(0,0)}to{transform:translate(40px,30px)}}
.hero-in{position:relative;display:flex;gap:2.5rem;align-items:center;justify-content:space-between;flex-wrap:wrap;}
.hero-text{flex:1 1 380px;max-width:640px;}
.hero h1{font-family:'Sora',sans-serif;font-size:clamp(2.1rem,5.5vw,3.7rem);line-height:1.06;font-weight:800;
 letter-spacing:-.03em;margin:0 0 1rem;color:#fff;
 background:linear-gradient(100deg,#fff 30%,#a5b4fc 70%,#67e8f9);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.hero p{font-size:1.1rem;line-height:1.65;color:#cbd5e1;margin:0 0 1.6rem;}
.btn{display:inline-block;padding:.7rem 1.3rem;border-radius:980px;font-weight:600;font-size:.92rem;
 text-decoration:none!important;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;}
.btn:focus-visible{outline:3px solid #67e8f9;outline-offset:2px;}
.btn.light{background:#fff;color:#0f172a!important;}
.btn.light:hover{transform:translateY(-2px);box-shadow:0 10px 24px #00000055;}
.btn.glass{background:#ffffff1f;color:#fff!important;border:1px solid #ffffff40;margin-left:.4rem;}
.btn.glass:hover{background:#ffffff33;}
.topics{flex:0 1 340px;display:grid;grid-template-columns:1fr 1fr;gap:.8rem;}
.topic{background:#ffffff14;border:1px solid #ffffff26;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
 border-radius:20px;padding:1rem;transition:transform .25s ease,background .25s ease;}
.topic:hover{transform:translateY(-3px);background:#ffffff22;}
.topic svg{width:26px;height:26px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
.topic b{display:block;font-family:'Sora',sans-serif;font-size:1.7rem;margin-top:.4rem;color:#fff;}
.topic span{font-size:.82rem;color:#cbd5e1;line-height:1.3;display:block;}
.sec-title{font-family:'Sora',sans-serif;font-size:1.7rem;font-weight:800;letter-spacing:-.02em;color:var(--ink);margin:.5rem 0 .2rem;}
.sec-sub{color:var(--mute);margin:0 0 1rem;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:1.6rem;margin-top:1rem;}
.card{background:#fff;border-radius:24px;overflow:hidden;border:1px solid var(--line);display:flex;flex-direction:column;
 box-shadow:0 2px 4px #0f172a0a,0 12px 28px -8px #0f172a1a;transition:transform .3s ease,box-shadow .3s ease;}
.card:hover{transform:translateY(-6px);box-shadow:0 4px 8px #0f172a0d,0 28px 50px -12px var(--c1);}
.cover{position:relative;height:190px;overflow:hidden;display:flex;align-items:center;justify-content:center;}
.cover>svg{width:64px;height:64px;stroke:#ffffffcc;fill:none;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;}
.cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .6s ease;}
.card:hover .cover img{transform:scale(1.08);}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,#0f172a00 35%,#0f172acc 100%),
 linear-gradient(135deg,var(--c1),transparent 70%);mix-blend-mode:normal;opacity:.75;}
.kind{position:absolute;top:14px;left:14px;background:#ffffffe6;padding:.25rem .75rem;border-radius:980px;
 font-size:.76rem;font-weight:600;color:#0f172a;z-index:2;}
.cat{position:absolute;bottom:12px;left:14px;z-index:2;display:flex;align-items:center;gap:.4rem;color:#fff;font-weight:600;font-size:.85rem;}
.cat svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;}
.body{padding:1.15rem 1.3rem 1.35rem;display:flex;flex-direction:column;gap:.6rem;flex:1;}
.body h3{margin:0;font-family:'Sora',sans-serif;font-size:1.12rem;font-weight:600;line-height:1.3;color:var(--ink);}
.body p{margin:0;color:var(--mute);font-size:.93rem;line-height:1.55;}
.tags{display:flex;flex-wrap:wrap;gap:.4rem;}
.tag{background:#f1f5f9;border-radius:8px;padding:.18rem .6rem;font-size:.76rem;font-weight:500;color:#334155;}
.actions{margin-top:auto;padding-top:.8rem;display:flex;gap:.5rem;flex-wrap:wrap;}
.actions .btn{padding:.55rem 1.05rem;font-size:.84rem;}
.btn.go{color:#fff!important;background:linear-gradient(135deg,var(--c1),var(--c2));}
.btn.go:hover{transform:translateY(-2px);box-shadow:0 8px 18px -4px var(--c1);}
.btn.repo{background:#f1f5f9;color:#0f172a!important;}
.btn.repo:hover{background:#e2e8f0;}
.empty{text-align:center;color:var(--mute);padding:3rem 0;}
div[data-testid="stTextInput"] input{border-radius:14px;padding:.7rem 1rem;}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;}}
@media (max-width:640px){.hero{padding:2rem 1.4rem;border-radius:24px;}.btn.glass{margin:.5rem 0 0;}}
</style>
"""


def esc(text):
    return html.escape(str(text), quote=True)


def icon(category):
    path = CATEGORIES.get(category, ("", "", "M12 5v14M5 12h14"))[2]
    return f'<svg viewBox="0 0 24 24"><path d="{path}"/></svg>'


def photo_url(app, index):
    if app.get("image_url"):
        return app["image_url"]
    if app.get("photo"):
        return f'https://loremflickr.com/640/400/{esc(app["photo"])}?lock={index + 10}'
    return ""


def render_card(app, index):
    c1, c2, _ = CATEGORIES.get(app["category"], ("#6366f1", "#22d3ee", ""))
    src = photo_url(app, index)
    img = (f'<img src="{src}" alt="" loading="lazy" referrerpolicy="no-referrer" '
           f'onerror="this.style.display=\'none\'">' if src else "")
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in app.get("technologies", []))
    repo = app.get("repository")
    repo_btn = (f'<a class="btn repo" href="https://github.com/{esc(GITHUB_USER)}/{esc(repo)}" '
                f'target="_blank" rel="noopener">Repositorio</a>') if repo and GITHUB_USER else ""
    return (
        f'<div class="card" style="--c1:{c1};--c2:{c2}">'
        f'<div class="cover" style="background:linear-gradient(135deg,{c1},{c2})">'
        f'{icon(app["category"])}{img}<div class="shade"></div>'
        f'<span class="kind">{esc(app["kind"])}</span>'
        f'<span class="cat">{icon(app["category"])}{esc(app["category"])}</span></div>'
        '<div class="body">'
        f'<h3>{esc(app["title"])}</h3><p>{esc(app["description"])}</p>'
        f'<div class="tags">{tags}</div>'
        f'<div class="actions"><a class="btn go" href="{esc(app["url"])}" target="_blank" rel="noopener">'
        f'Abrir aplicación</a>{repo_btn}</div></div></div>'
    )


def matches(app, query, category):
    if category != "Todas" and app["category"] != category:
        return False
    text = " ".join([app["title"], app["description"], app["category"], app["kind"],
                     " ".join(app.get("technologies", []))]).lower()
    return all(word in text for word in query.lower().split())


st.markdown(CSS, unsafe_allow_html=True)

counts = Counter(a["category"] for a in APPS)
topic_cards = "".join(
    f'<div class="topic">{icon(cat)}<b>{n}</b><span>{esc(cat)}</span></div>'
    for cat, n in counts.items()
)
st.markdown(
    '<section class="hero"><div class="orb a"></div><div class="orb b"></div><div class="hero-in">'
    '<div class="hero-text"><h1>Aprende datos e inteligencia artificial probándolos.</h1>'
    f'<p>{len(APPS)} aplicaciones interactivas creadas durante el curso: desde el gradiente '
    'hasta la clasificación de suelos. Ábrelas, juega con los datos y mira cómo funcionan.</p>'
    '<a class="btn light" href="#catalogo">Explorar aplicaciones</a>'
    f'<a class="btn glass" href="{esc(SITE_URL)}" target="_blank" rel="noopener">Ejercicios y páginas</a></div>'
    f'<div class="topics">{topic_cards}</div></div></section>'
    '<div id="catalogo"></div>'
    '<div class="sec-title">Catálogo</div>'
    '<p class="sec-sub">Busca por nombre o técnica, o filtra por tema.</p>',
    unsafe_allow_html=True,
)

query = st.text_input("Buscar", placeholder="Busca: series, KNN, regresión, IoT…", label_visibility="collapsed")
options = ["Todas"] + list(counts)
category = st.pills("Tema", options, default="Todas", label_visibility="collapsed",
                    format_func=lambda c: c if c == "Todas" else f"{c} ({counts[c]})") or "Todas"

visible = [(i, a) for i, a in enumerate(APPS) if matches(a, query, category)]
if visible:
    st.caption(f"Mostrando {len(visible)} de {len(APPS)} aplicaciones")
    st.markdown('<div class="grid">' + "".join(render_card(a, i) for i, a in visible) + "</div>",
                unsafe_allow_html=True)
else:
    st.markdown('<div class="empty"><h3>No encontramos resultados</h3>'
                '<p>Prueba con otra palabra o elige "Todas".</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
with st.expander("¿Qué técnicas aparecen en este catálogo?"):
    st.write(", ".join(sorted({t for a in APPS for t in a.get("technologies", [])})))
