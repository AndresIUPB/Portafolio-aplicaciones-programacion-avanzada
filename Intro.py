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
         repository="Calculo-aplicado-gradiente", technologies=["Gradiente"], image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX8GxVZ7UeyLFWxeWiC3-llw7fAUh66-G7zPirIxehqA&s=10"),
    dict(title="Detector de anomalías", category="Fundamentos", kind="Sesión 4",
         description="Practica lógica, eficiencia (Big-O) y vectorización para encontrar datos extraños.",
         url="https://detector-anomalias-pujphzyih8brne8nhox5zv.streamlit.app",
         repository="detector-anomalias", technologies=["Big-O", "Vectorización"], image_url="data:image/jpeg;base64,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"),
    dict(title="Preparación de datos", category="Datos", kind="Sesión 5",
         description="Aprende a dejar los datos limpios y listos antes de analizarlos.",
         url="https://preparaci-n-de-datos-yupvhtm8dhjnmfslfsmt3u.streamlit.app",
         repository="Preparaci-n-de-datos", technologies=["Limpieza de datos"], image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCL0CSI7cDBf2XtTk3t70lN1HY9yn_5ABvZEy2_vhtLw&s"),
    dict(title="Análisis y preparación con MARCO", category="Datos", kind="Sesión 6",
         description="Una aplicación para revisar y preparar tus datos paso a paso.",
         url="https://preparacion.streamlit.app",
         repository="aplicacion-de-analisis-y-preparacion-de-datos-con-MARCO",
         technologies=["MARCO"], image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXbRRrGtGa3oPuUSEiamuR-g05jTfxlDF_5gMBoIucKQ&s=10"),
    dict(title="Regresión lineal", category="Modelos predictivos", kind="Sesión 7",
         description="Mira cómo una línea puede describir la relación entre dos variables.",
         url="https://regresion-lineal-py.streamlit.app",
         repository="regresion-lineal", technologies=["Regresión lineal"], image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3xpk77m5-xhfbxmE4m5Nxh0MhcMdfUWX4Jx-DbHGaOA&s=10"),
    dict(title="Series de tiempo", category="Modelos predictivos", kind="Sesión 8",
         description="Analiza datos que cambian con el tiempo y observa sus patrones.",
         url="https://time-series-intelligence.streamlit.app",
         repository="Time_Series_Intelligence", technologies=["Series de tiempo"], photo="clock"),
    dict(title="Pronóstico de calidad del aire", category="Modelos predictivos", kind="Aplicación",
         description="Consulta una predicción de la calidad del aire a partir de datos.",
         url="https://pronosticador-de-calidad-de-aire.streamlit.app",
         repository="pronosticador-de-calidad-de-aire", technologies=["Predicción"], image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqQs9a6noTLIhKLlokR0qipA0CPwQLMQUnmpR7SvNK_w&s=10"),
    dict(title="Sensor de humedad IoT", category="Sensores e IoT", kind="Sesión 10",
         description="Sigue cómo un dispositivo captura datos de humedad y cómo se procesan.",
         url="https://dispositivo-iot-humedad.streamlit.app",
         repository="streamlit-dispositivo-iot-humedad", technologies=["IoT", "Captura de datos"],
         image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHd8Y1r9KIKAVEDIzxga-s7DDrx3fb-AEUpQ2BMiaFmQ&s=10"),
    dict(title="¿Llueve o no llueve?", category="Modelos predictivos", kind="Sesión 11",
         description="Pasa de predecir un número a tomar una decisión de sí o no.",
         url="https://decisiones-binarias-llueve-o-no-j6ardkm39sqb4dvdqvtqf3.streamlit.app",
         repository="decisiones-binarias-llueve-o-no", technologies=["Regresión logística"], image_url="https://www.google.com/imgres?q=imagen%20ia&imgurl=https%3A%2F%2Fwww.iberdrola.com%2Fdocuments%2F20125%2F3718402%2Fhistoria-ia-746x419.jpg%2F177df891-3f96-d555-0a68-8c80e0d83b62%3Ft%3D1701700838577&imgrefurl=https%3A%2F%2Fwww.iberdrola.com%2Fconocenos%2Fnuestro-modelo-innovacion%2Fhistoria-inteligencia-artificial&docid=GPVJq3SiUZh1ZM&tbnid=MrLAyu8HD88TsM&vet=12ahUKEwiKouGJ3pKXAxURSDABHYxGA7YQnPAOegUIsAEQAA..i&w=746&h=419&hcb=2&ved=2ahUKEwiKouGJ3pKXAxURSDABHYxGA7YQnPAOegUIsAEQAA"),
    dict(title="De la tierra al algoritmo", category="Modelos predictivos", kind="Sesión 12",
         description="Clasifica la fertilidad de un suelo comparándolo con casos parecidos.",
         url="https://de-la-tierra-al-algoritmo.streamlit.app",
         repository="De-la-Tierra-al-Algoritmo", technologies=["KNN", "Clasificación"], image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJHMZnN0NAVMqXOJuxIZh3l3qbGKCx6iMemt8Gxg-D_A&s=10"),
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
