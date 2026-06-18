"""
Transformada de Laplace — Exemplo 4.1: Tanque de Armazenamento de Líquido
UNIMONTES | Disciplina de Equações Diferenciais Ordinárias | Prof. Fernando Félix
Alunos: Bruno Gomes, Júlio César, Leonardo, Marcus, Samuel
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import os
import base64

# ─── Configuração da página ───────────────────────────────────────────────────

st.set_page_config(
    page_title="Exemplo 4.1 — Tanque de Líquido | UNIMONTES",
    page_icon="assets/favicon.png" if os.path.exists("assets/favicon.png") else "⚗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CSS ─────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

  /* ── Reset & Base ── */
  * { box-sizing: border-box; }
  .stApp { background-color: #0D1117; }
  .block-container {
    padding-top: 0 !important;
    max-width: 1280px;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
  }

  /* ── Status bar (topo estilo IDE) ── */
  .status-bar {
    background: #161B22;
    border-bottom: 1px solid #21262D;
    padding: 0.4rem 2rem;
    margin: -1px -2rem 0 -2rem;
    display: flex;
    align-items: center;
    gap: 2rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #8B949E;
  }
  .status-bar .status-item { display: flex; align-items: center; gap: 0.4rem; }
  .status-dot { width: 6px; height: 6px; border-radius: 50%; }
  .dot-green { background: #3FB950; }
  .dot-blue  { background: #58A6FF; }
  .dot-gold  { background: #C9A227; }
  .status-bar .status-right { margin-left: auto; }

  /* ── Header principal ── */
  .header-bar {
    background: linear-gradient(135deg, #0F2540 0%, #162A47 60%, #1A3356 100%);
    border-bottom: 2px solid #C9A227;
    padding: 1.5rem 2rem;
    margin: 0 -2rem 0 -2rem;
    display: flex;
    align-items: center;
    gap: 1.75rem;
    position: relative;
    overflow: hidden;
  }
  .header-bar::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 40%;
    height: 100%;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.02'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    pointer-events: none;
  }
  .header-logo-wrap {
    width: 76px; height: 76px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(201,162,39,0.35);
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; overflow: hidden;
    position: relative;
  }
  .header-logo-wrap::after {
    content: '';
    position: absolute;
    inset: 0;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.04);
  }
  .header-text { flex: 1; }
  .header-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #C9A227;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
  }
  .header-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.55rem;
    font-weight: 600;
    color: #F0F6FC;
    margin: 0;
    line-height: 1.2;
    letter-spacing: -0.01em;
  }
  .header-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.78rem;
    font-weight: 400;
    color: #8B949E;
    margin-top: 0.3rem;
    letter-spacing: 0.01em;
  }
  .header-meta {
    text-align: right;
    font-family: 'Inter', sans-serif;
    font-size: 0.73rem;
    color: #6E7681;
    line-height: 1.8;
    flex-shrink: 0;
  }
  .header-meta strong { color: #8B949E; }

  /* ── Divider ── */
  .divider {
    border: none;
    border-top: 1px solid #21262D;
    margin: 2rem 0;
  }

  /* ── Section headers ── */
  .section-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.63rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #C9A227;
    margin-bottom: 0.4rem;
  }
  .section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.35rem;
    font-weight: 600;
    color: #E6EDF3;
    margin: 0 0 1.2rem 0;
    line-height: 1.3;
    letter-spacing: -0.01em;
  }

  /* ── Info cards ── */
  .info-panel {
    background: #161B22;
    border: 1px solid #21262D;
    border-top: 2px solid #1F6FEB;
    padding: 1.1rem 1.25rem;
    margin-bottom: 0.85rem;
  }
  .info-panel-gold {
    background: #161B22;
    border: 1px solid #21262D;
    border-top: 2px solid #C9A227;
    padding: 1.1rem 1.25rem;
    margin-bottom: 0.85rem;
  }
  .info-panel-green {
    background: #161B22;
    border: 1px solid #21262D;
    border-top: 2px solid #3FB950;
    padding: 1.1rem 1.25rem;
    margin-bottom: 0.85rem;
  }
  .panel-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #58A6FF;
    margin-bottom: 0.5rem;
  }
  .panel-label-gold { color: #C9A227; }
  .panel-label-green { color: #3FB950; }
  .panel-body {
    font-family: 'Inter', sans-serif;
    font-size: 0.84rem;
    color: #8B949E;
    line-height: 1.7;
  }
  .panel-body strong { color: #C9D1D9; }

  /* ── Step cards (resolução) ── */
  .step-card {
    background: #161B22;
    border: 1px solid #21262D;
    border-left: 3px solid #30363D;
    padding: 1.1rem 1.4rem;
    margin-bottom: 0.7rem;
  }
  .step-card-active {
    background: #0D2137;
    border: 1px solid #1F6FEB40;
    border-left: 3px solid #1F6FEB;
    padding: 1.1rem 1.4rem;
    margin-bottom: 0.7rem;
  }
  .step-card-result {
    background: #111B0E;
    border: 1px solid #3FB95040;
    border-left: 3px solid #3FB950;
    padding: 1.25rem 1.4rem;
    margin-bottom: 0.7rem;
  }
  .step-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #6E7681;
    margin-bottom: 0.45rem;
  }
  .step-tag-blue  { color: #58A6FF; }
  .step-tag-green { color: #3FB950; }
  .step-body {
    font-family: 'Inter', sans-serif;
    font-size: 0.84rem;
    color: #8B949E;
    line-height: 1.7;
    margin: 0.35rem 0;
  }
  .step-body strong { color: #C9D1D9; }

  /* ── Result cards (métricas) ── */
  .metric-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.75rem;
    margin-bottom: 1.25rem;
  }
  .metric-card {
    background: #161B22;
    border: 1px solid #21262D;
    border-top: 2px solid #30363D;
    padding: 1rem 1.1rem;
    text-align: center;
  }
  .metric-card-blue  { border-top-color: #1F6FEB; }
  .metric-card-gold  { border-top-color: #C9A227; }
  .metric-card-green { border-top-color: #3FB950; }
  .metric-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.61rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #6E7681;
    margin-bottom: 0.3rem;
  }
  .metric-sublabel {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #6E7681;
    margin-bottom: 0.45rem;
  }
  .metric-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.4rem;
    font-weight: 600;
    color: #58A6FF;
  }
  .metric-value-gold  { color: #C9A227; }
  .metric-value-green { color: #3FB950; }
  .metric-value-gray  { color: #6E7681; }

  /* ── Expression box ── */
  .expr-box {
    background: #0D1117;
    border: 1px solid #21262D;
    border-left: 3px solid #58A6FF;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1.25rem;
  }
  .expr-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #58A6FF;
    margin-bottom: 0.75rem;
  }

  /* ── Warning ── */
  .warn-box {
    background: #2D1B00;
    border: 1px solid #C9A22740;
    border-left: 3px solid #C9A227;
    padding: 0.9rem 1.2rem;
    font-family: 'Inter', sans-serif;
    font-size: 0.84rem;
    color: #C9A227;
  }

  /* ── Botão ── */
  div[data-testid="stButton"] > button {
    background: #1F6FEB !important;
    color: #FFFFFF !important;
    border: none !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    padding: 0.6rem 1.8rem !important;
    border-radius: 4px !important;
    transition: background 0.15s !important;
  }
  div[data-testid="stButton"] > button:hover {
    background: #388BFD !important;
  }

  /* ── Inputs ── */
  div[data-testid="stNumberInput"] input {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.9rem !important;
    color: #58A6FF !important;
    background: #0D1117 !important;
    border-color: #30363D !important;
    border-radius: 4px !important;
  }
  div[data-testid="stNumberInput"] label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem !important;
    color: #8B949E !important;
    letter-spacing: 0.04em !important;
  }

  /* ── Radio ── */
  div[data-testid="stRadio"] > div { flex-direction: row !important; gap: 1rem; }
  div[data-testid="stRadio"] label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.8rem !important;
    color: #8B949E !important;
  }

  /* ── Table ── */
  table { width: 100%; border-collapse: collapse; }
  th {
    background: #161B22;
    color: #8B949E;
    padding: 0.6rem 0.9rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    text-align: left;
    border-bottom: 2px solid #1F6FEB;
  }
  td {
    padding: 0.55rem 0.9rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #8B949E;
    border-bottom: 1px solid #21262D;
  }
  tr:hover td { background: #161B22; color: #C9D1D9; }

  /* ── App item (lista de aplicações) ── */
  .app-item {
    border-top: 1px solid #21262D;
    padding: 1rem 0;
    font-family: 'Inter', sans-serif;
    font-size: 0.84rem;
    color: #8B949E;
    line-height: 1.65;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
  }
  .app-item-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    color: #1F6FEB;
    background: #1F6FEB15;
    border: 1px solid #1F6FEB30;
    padding: 0.25rem 0.5rem;
    white-space: nowrap;
    margin-top: 0.1rem;
    flex-shrink: 0;
  }
  .app-item-text strong { color: #C9D1D9; display: block; margin-bottom: 0.2rem; }

  /* ── Footer ── */
  .footer {
    margin-top: 3rem;
    padding: 1.5rem 0;
    border-top: 1px solid #21262D;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: #6E7681;
    text-align: center;
    letter-spacing: 0.04em;
  }
  .footer span { color: #C9A227; }

  /* ── LaTeX inline override ── */
  .stMarkdown .katex { color: #C9D1D9 !important; }

  /* ── Markdown text override ── */
  .stMarkdown p, .stMarkdown li {
    color: #8B949E;
  }
</style>
""", unsafe_allow_html=True)


# ─── Funções de cálculo ───────────────────────────────────────────────────────

def calcular(A, Rv, M, h_bar, t_max, n_pts=600):
    ARv = A * Rv
    h_dev_inf = Rv * M
    h_inf = h_bar + h_dev_inf
    t = np.linspace(0, t_max, n_pts)
    h_dev = h_dev_inf * (1 - np.exp(-t / ARv))
    h = h_bar + h_dev
    return {
        "ARv": ARv,
        "h_dev_inf": h_dev_inf,
        "h_inf": h_inf,
        "t": t,
        "h_dev": h_dev,
        "h": h,
    }

def fmt(v, d=4):
    if not np.isfinite(v):
        return "—"
    return f"{v:.{d}f}".rstrip("0").rstrip(".") or "0"


# ─── Logo ─────────────────────────────────────────────────────────────────────

logo_path = "assets/logo_unimontes.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as img_file:
        logo_b64 = base64.b64encode(img_file.read()).decode()
    logo_html = (
        f'<div class="header-logo-wrap">'
        f'<img src="data:image/png;base64,{logo_b64}" '
        f'style="width:68px;height:68px;object-fit:contain;" alt="UNIMONTES">'
        f'</div>'
    )
else:
    logo_html = """
    <div class="header-logo-wrap">
      <span style="font-family:'Space Grotesk',sans-serif;font-size:1.5rem;font-weight:700;color:#C9A227;">U</span>
    </div>
    """

# ─── Status bar (estilo IDE) ──────────────────────────────────────────────────

st.markdown("""
<div class="status-bar">
  <div class="status-item">
    <span class="status-dot dot-green"></span>
    <span>app.py</span>
  </div>
  <div class="status-item">
    <span class="status-dot dot-blue"></span>
    <span>EDO · Transformada de Laplace</span>
  </div>
  <div class="status-item">
    <span class="status-dot dot-gold"></span>
    <span>Exemplo 4.1 — Tanque de Armazenamento</span>
  </div>
  <div class="status-right status-item">
    <span>Python · Streamlit · NumPy · Plotly</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Cabeçalho ────────────────────────────────────────────────────────────────

st.markdown(f"""
<div class="header-bar">
  {logo_html}
  <div class="header-text">
    <div class="header-eyebrow">// UNIMONTES · EDO · 2025</div>
    <p class="header-title">Transformada de Laplace — Exemplo 4.1</p>
    <p class="header-sub">Tanque de Armazenamento de Líquido &nbsp;·&nbsp; Função de Transferência &amp; Resposta ao Degrau</p>
  </div>
  <div class="header-meta">
    <strong>Prof. Fernando Félix</strong><br>
    Bruno Gomes · Júlio César<br>
    Leonardo · Marcus · Samuel
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:1.75rem'></div>", unsafe_allow_html=True)

# ─── Seção 1: Modelo físico + Diagrama ───────────────────────────────────────

col_intro, col_diag = st.columns([3, 2], gap="large")

with col_intro:
    st.markdown('<p class="section-eyebrow">// 01 · visão geral</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Sobre o aplicativo</h2>', unsafe_allow_html=True)

    st.markdown("""
<div class="info-panel">
  <div class="panel-label">Stack tecnológico</div>
  <div class="panel-body">
    Desenvolvido em <strong>Python</strong> com <strong>Streamlit</strong> — framework que transforma
    scripts Python em interfaces web interativas sem necessidade de HTML/JS manual.
    O design é controlado inteiramente via <strong>CSS injetado</strong>, definindo tipografia,
    paleta, espaçamento e componentes visuais.
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="info-panel-gold">
  <div class="panel-label panel-label-gold">Lógica de cálculo</div>
  <div class="panel-body">
    Entrada de parâmetros → computação de AR<sub>v</sub>, R<sub>v</sub>M e h(∞) →
    aplicação da solução analítica → plotagem da curva h(t) via Plotly.
    O <strong>NumPy</strong> gera o vetor de tempo e avalia a exponencial;
    o <strong>Plotly</strong> renderiza o gráfico interativo.
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="section-eyebrow" style="margin-top:1.25rem">// equação central</div>', unsafe_allow_html=True)
    st.latex(r"h(t) = \bar{h} + R_vM\!\left(1 - e^{-t/AR_v}\right)")

with col_diag:
    st.markdown('<p class="section-eyebrow">// 02 · modelo físico</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Diagrama do sistema</h2>', unsafe_allow_html=True)

    st.markdown("""
<div style="background:#161B22;border:1px solid #21262D;padding:1.5rem;">
<svg viewBox="0 0 240 195" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
      <path d="M0,0 L7,3.5 L0,7 Z" fill="#58A6FF"/>
    </marker>
    <marker id="arr-gold" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
      <path d="M0,0 L7,3.5 L0,7 Z" fill="#C9A227"/>
    </marker>
    <marker id="arr-both-up" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
      <path d="M0,0 L7,3.5 L0,7 Z" fill="#6E7681"/>
    </marker>
    <marker id="arr-both-dn" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="270">
      <path d="M0,0 L7,3.5 L0,7 Z" fill="#6E7681"/>
    </marker>
    <linearGradient id="liquidGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1F6FEB" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#1F6FEB" stop-opacity="0.18"/>
    </linearGradient>
  </defs>

  <!-- Grid de fundo sutil -->
  <pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse">
    <path d="M 10 0 L 0 0 0 10" fill="none" stroke="#21262D" stroke-width="0.4"/>
  </pattern>
  <rect width="240" height="195" fill="url(#grid)" opacity="0.5"/>

  <!-- Tubo de entrada -->
  <rect x="99" y="0" width="14" height="36" fill="none" stroke="#58A6FF" stroke-width="1.5"/>
  <polygon points="93,30 119,30 106,44" fill="#58A6FF" opacity="0.85"/>
  <text x="118" y="16" font-family="JetBrains Mono,monospace" font-size="10" fill="#58A6FF" font-weight="500">qᵢ(t)</text>

  <!-- Tanque (corpo) -->
  <rect x="42" y="44" width="130" height="108" fill="none" stroke="#30363D" stroke-width="1.5"/>

  <!-- Líquido com gradiente -->
  <rect x="43.5" y="90" width="127" height="61" fill="url(#liquidGrad)"/>
  <!-- Linha d'água -->
  <line x1="43" y1="90" x2="171" y2="90" stroke="#58A6FF" stroke-width="1.2" stroke-dasharray="6 3"/>

  <!-- Label A no tanque (vazio) -->
  <text x="72" y="72" font-family="JetBrains Mono,monospace" font-size="11" fill="#30363D" font-style="italic" font-weight="600">A</text>
  <text x="78" y="84" font-family="JetBrains Mono,monospace" font-size="7.5" fill="#30363D">[m²]</text>

  <!-- Cota h com setas duplas -->
  <line x1="180" y1="90" x2="180" y2="152" stroke="#6E7681" stroke-width="1"
        marker-start="url(#arr-both-up)" marker-end="url(#arr-both-dn)"/>
  <text x="186" y="121" font-family="JetBrains Mono,monospace" font-size="10" fill="#C9D1D9" font-style="italic" font-weight="500">h(t)</text>
  <text x="186" y="133" font-family="JetBrains Mono,monospace" font-size="7.5" fill="#6E7681">[m]</text>

  <!-- h_bar linha referência -->
  <line x1="210" y1="152" x2="210" y2="90" stroke="#6E7681" stroke-width="0.6" stroke-dasharray="3 2"/>
  <text x="218" y="155" font-family="JetBrains Mono,monospace" font-size="8" fill="#6E7681">base</text>

  <!-- Saída com pipe -->
  <rect x="99" y="152" width="14" height="36" fill="none" stroke="#C9A227" stroke-width="1.5"/>
  <polygon points="93,172 119,172 106,186" fill="#C9A227" opacity="0.9"/>
  <text x="118" y="170" font-family="JetBrains Mono,monospace" font-size="9.5" fill="#C9A227">h/Rᵥ</text>

  <!-- Label Rv -->
  <rect x="118" y="174" width="52" height="14" rx="2" fill="#C9A22715" stroke="#C9A22740"/>
  <text x="144" y="184" font-family="JetBrains Mono,monospace" font-size="8" fill="#C9A227" text-anchor="middle">resistência Rᵥ</text>
</svg>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="info-panel-green" style="margin-top:0.75rem">
  <div class="panel-label panel-label-green">Variáveis do sistema</div>
  <div class="panel-body">
    <strong>A</strong> — área da seção transversal [m²]<br>
    <strong>Rᵥ</strong> — resistência hidráulica [m·s/m³]<br>
    <strong>h(t)</strong> — nível do líquido [m]<br>
    <strong>qᵢ(t)</strong> — vazão de entrada [m³/s]
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ─── Seção 2: Desenvolvimento passo a passo ───────────────────────────────────

st.markdown('<p class="section-eyebrow">// 03 · desenvolvimento analítico</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Resolução passo a passo</h2>', unsafe_allow_html=True)

col_passos, col_info = st.columns([3, 1], gap="large")

with col_passos:

    # Passo 1
    st.markdown("""
<div class="step-card">
  <div class="step-tag step-tag-blue">PASSO 01 &nbsp;·&nbsp; Variáveis de desvio</div>
  <div class="step-body">Define-se a variável de desvio subtraindo o ponto de operação em regime permanente:</div>
</div>
""", unsafe_allow_html=True)
    st.latex(r"h' \triangleq h - \bar{h}, \qquad q_i' \triangleq q_i - \bar{q}_i")
    st.markdown("""
<div class="step-card" style="margin-top:0.5rem">
  <div class="step-body">Subtraindo o regime permanente da EDO original e usando <em>dh'/dt = dh/dt</em>, com h'(0) = 0:</div>
</div>
""", unsafe_allow_html=True)
    st.latex(r"A\,\frac{dh'}{dt} = q_i' - \frac{1}{R_v}\,h'")

    # Passo 2
    st.markdown("""
<div class="step-card-active" style="margin-top:1rem">
  <div class="step-tag step-tag-blue">PASSO 02 &nbsp;·&nbsp; Transformada de Laplace</div>
  <div class="step-body">Aplicando a transformada com h'(0) = 0 e usando a propriedade da derivada <strong>ℒ{y'} = sY(s) − y(0)</strong>:</div>
</div>
""", unsafe_allow_html=True)
    st.latex(r"A\bigl[sH'(s) - \underbrace{h'(0)}_{=\,0}\bigr] = Q_i'(s) - \frac{1}{R_v}H'(s)")
    st.latex(r"A\,s\,H'(s) = Q_i'(s) - \frac{1}{R_v}H'(s)")

    # Passo 3
    st.markdown("""
<div class="step-card-active" style="margin-top:1rem">
  <div class="step-tag step-tag-blue">PASSO 03 &nbsp;·&nbsp; Função de transferência G(s)</div>
  <div class="step-body">Reagrupando e isolando a razão <strong>H'(s) / Q'ᵢ(s)</strong>:</div>
</div>
""", unsafe_allow_html=True)
    st.latex(r"G(s) = \frac{H'(s)}{Q_i'(s)} = \frac{R_v}{AR_v s + 1}")

    # Passo 4
    st.markdown("""
<div class="step-card-active" style="margin-top:1rem">
  <div class="step-tag step-tag-blue">PASSO 04 &nbsp;·&nbsp; Resposta ao degrau de magnitude M</div>
  <div class="step-body">Para entrada degrau <em>qᵢ(t) = M</em>, tem-se Q'ᵢ(s) = M/s. Substituindo em G(s):</div>
</div>
""", unsafe_allow_html=True)
    st.latex(r"H'(s) = \frac{R_v}{AR_v s + 1}\cdot\frac{M}{s}")

    # Resultado
    st.markdown("""
<div class="step-card-result" style="margin-top:1rem">
  <div class="step-tag step-tag-green">RESULTADO &nbsp;·&nbsp; Transformada inversa — Eq. 4-13</div>
  <div class="step-body">Pela tabela de transformadas, a transformada inversa fornece o desvio do nível. Retornando à variável original:</div>
</div>
""", unsafe_allow_html=True)
    st.latex(r"h'(t) = R_v M\!\left(1 - e^{-t/AR_v}\right)")
    st.latex(r"\boxed{h(t) = \bar{h} + R_v M\!\left(1 - e^{-t/AR_v}\right)}")

with col_info:
    st.markdown("""
<div class="info-panel" style="margin-top:0">
  <div class="panel-label">Prop. utilizada</div>
  <div class="panel-body" style="font-size:0.78rem">
    Linearidade da transformada: a operação ℒ é linear, permitindo separar termos da EDO.
  </div>
</div>
<div class="info-panel" style="margin-top:0">
  <div class="panel-label">Condição inicial</div>
  <div class="panel-body" style="font-size:0.78rem">
    h'(0) = 0 ⟹ sistema parte do regime permanente. Isso simplifica o numerador.
  </div>
</div>
<div class="info-panel-gold" style="margin-top:0">
  <div class="panel-label panel-label-gold">Polo de G(s)</div>
  <div class="panel-body" style="font-size:0.78rem">
    s = −1 / AR<sub>v</sub><br>
    Parte real negativa ⟹ sistema <strong>estável</strong>.
  </div>
</div>
<div class="info-panel-green" style="margin-top:0">
  <div class="panel-label panel-label-green">Constante de tempo</div>
  <div class="panel-body" style="font-size:0.78rem">
    τ = AR<sub>v</sub><br>
    Em t = τ, o sistema atinge ~63,2% do valor final.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ─── Seção 3: Calculadora ─────────────────────────────────────────────────────

st.markdown('<p class="section-eyebrow">// 04 · calculadora interativa</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Defina os parâmetros do sistema</h2>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    A = st.number_input("A — Área (m²)", min_value=0.01, value=2.0, step=0.1, format="%.2f")
with col2:
    Rv = st.number_input("Rv — Resistência (m·s/m³)", min_value=0.01, value=1.5, step=0.1, format="%.2f")
with col3:
    M = st.number_input("M — Degrau (m³/s)", value=0.5, step=0.1, format="%.2f")
with col4:
    h_bar = st.number_input("h̄ — Nível inicial (m)", min_value=0.0, value=1.0, step=0.1, format="%.2f")
with col5:
    t_max = st.number_input("t máx (s)", min_value=1.0, value=20.0, step=1.0, format="%.1f")

st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
calcular_btn = st.button("▶  Calcular solução")


# ─── Resultados ───────────────────────────────────────────────────────────────

if calcular_btn or "res" in st.session_state:

    if calcular_btn:
        if A <= 0 or Rv <= 0 or t_max <= 0:
            st.markdown('<div class="warn-box">⚠ Os parâmetros A, Rv e t máximo devem ser positivos.</div>',
                        unsafe_allow_html=True)
            st.stop()
        st.session_state["res"] = calcular(A, Rv, M, h_bar, t_max)
        st.session_state["params"] = dict(A=A, Rv=Rv, M=M, h_bar=h_bar, t_max=t_max)

    res = st.session_state["res"]
    p   = st.session_state["params"]

    ARv       = res["ARv"]
    h_dev_inf = res["h_dev_inf"]
    h_inf     = res["h_inf"]
    t_arr     = res["t"]
    h_dev_arr = res["h_dev"]
    h_arr     = res["h"]

    t95 = 3 * ARv  # usado na linha de referência do gráfico

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-eyebrow">// 05 · resultados</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Parâmetros calculados</h2>', unsafe_allow_html=True)

    # ── Cards métricas ───────────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
<div class="metric-card metric-card-blue">
  <div class="metric-label">Const. de tempo τ</div>
  <div class="metric-sublabel">A · Rᵥ</div>
  <div class="metric-value">{fmt(ARv, 3)} s</div>
</div>""", unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
<div class="metric-card metric-card-blue">
  <div class="metric-label">Desvio final h'(∞)</div>
  <div class="metric-sublabel">Rᵥ · M</div>
  <div class="metric-value">{fmt(h_dev_inf, 3)} m</div>
</div>""", unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
<div class="metric-card metric-card-gold">
  <div class="metric-label">Nível final h(∞)</div>
  <div class="metric-sublabel">h̄ + Rᵥ · M</div>
  <div class="metric-value metric-value-gold">{fmt(h_inf, 3)} m</div>
</div>""", unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
<div class="metric-card">
  <div class="metric-label">Nível inicial h̄</div>
  <div class="metric-sublabel">Regime permanente</div>
  <div class="metric-value metric-value-gray">{fmt(p["h_bar"], 3)} m</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)

    # ── Expressão numérica ───────────────────────────────────────────────────
    st.markdown("""
<div class="expr-box">
  <div class="expr-label">// expressões com os valores inseridos</div>
""", unsafe_allow_html=True)

    st.latex(
        rf"G(s) = \frac{{{fmt(p['Rv'], 4)}}}{{{fmt(ARv, 4)}\,s + 1}}"
    )
    st.latex(
        rf"h(t) = {fmt(p['h_bar'], 4)} + {fmt(h_dev_inf, 4)}"
        rf"\!\left(1 - e^{{-t/{fmt(ARv, 4)}}}\right)"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # ── Gráfico ──────────────────────────────────────────────────────────────
    st.markdown('<p class="section-eyebrow">// 06 · visualização</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Resposta temporal h(t)</h2>', unsafe_allow_html=True)

    curva = st.radio(
        "Exibir:",
        ["Nível real h(t)", "Desvio h'(t)", "Ambas as curvas"],
        horizontal=True,
        label_visibility="collapsed",
    )

    BG   = "#0D1117"
    GRID = "#21262D"
    TICK = "#6E7681"
    FONT = "JetBrains Mono, monospace"

    fig = go.Figure()

    # Linhas de referência
    fig.add_hline(
        y=p["h_bar"], line_dash="dash", line_color="#6E7681", line_width=1,
        annotation_text=f"h̄ = {fmt(p['h_bar'], 2)} m",
        annotation_position="top right",
        annotation_font=dict(color="#6E7681", size=10, family=FONT),
    )
    fig.add_hline(
        y=h_inf, line_dash="dash", line_color="#C9A227", line_width=1.2,
        annotation_text=f"h(∞) = {fmt(h_inf, 3)} m",
        annotation_position="bottom right",
        annotation_font=dict(color="#C9A227", size=10, family=FONT),
    )
    fig.add_vline(
        x=ARv, line_dash="dot", line_color="#3FB950", line_width=1,
        annotation_text=f"τ = {fmt(ARv, 2)} s",
        annotation_position="top right",
        annotation_font=dict(color="#3FB950", size=10, family=FONT),
    )
    fig.add_vline(
        x=t95, line_dash="dot", line_color="rgba(63,185,80,0.35)", line_width=0.8,
        annotation_text=f"3τ = {fmt(t95, 2)} s",
        annotation_position="top left",
        annotation_font=dict(color="rgba(63,185,80,0.5)", size=9, family=FONT),
    )

    if curva in ("Nível real h(t)", "Ambas as curvas"):
        fig.add_trace(go.Scatter(
            x=t_arr, y=h_arr, mode="lines",
            name="h(t) — nível real",
            line=dict(color="#1F6FEB", width=2.5),
        ))

    if curva in ("Desvio h'(t)", "Ambas as curvas"):
        fig.add_trace(go.Scatter(
            x=t_arr, y=h_dev_arr, mode="lines",
            name="h'(t) — desvio",
            line=dict(color="#C9A227", width=2, dash="dot"),
        ))

    fig.update_layout(
        plot_bgcolor=BG,
        paper_bgcolor=BG,
        font=dict(family=FONT, size=11, color=TICK),
        margin=dict(l=55, r=55, t=30, b=65),
        xaxis=dict(
            title=dict(text="Tempo (s)", font=dict(color=TICK, size=11)),
            showgrid=True, gridcolor=GRID, gridwidth=1,
            zeroline=True, zerolinecolor="#30363D",
            linecolor="#30363D", linewidth=1,
            tickfont=dict(color=TICK, size=10),
        ),
        yaxis=dict(
            title=dict(text="Nível h(t) [m]", font=dict(color=TICK, size=11)),
            showgrid=True, gridcolor=GRID, gridwidth=1,
            zeroline=True, zerolinecolor="#30363D",
            linecolor="#30363D", linewidth=1,
            tickfont=dict(color=TICK, size=10),
        ),
        legend=dict(
            orientation="h", y=1.08, x=0,
            bgcolor="rgba(0,0,0,0)",
            font=dict(family=FONT, size=11, color="#8B949E"),
        ),
        height=440,
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ─── Seção 4: Aplicações ────────────────────────────────────────────────────

st.markdown('<p class="section-eyebrow">// 07 · aplicações</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">O que a Transformada de Laplace permite fazer</h2>', unsafe_allow_html=True)

col_a1, col_a2 = st.columns(2, gap="large")

APPS_LEFT = [
    ("EDO → Álgebra", "A transformada converte uma equação diferencial em algébrica, facilitando a obtenção da solução no domínio de <em>s</em> e depois no tempo via transformada inversa."),
    ("Função de Transferência", "G(s) = Y(s)/U(s) relaciona entrada e saída de um sistema linear, representando o comportamento dinâmico de forma compacta e manipulável."),
    ("Análise de resposta", "Com G(s) obtido, calcula-se a resposta do sistema a qualquer entrada: degrau, impulso, rampa — como feito no Exemplo 4.1."),
]

APPS_RIGHT = [
    ("Estabilidade pelo plano-s", "Os polos de G(s) determinam o comportamento: partes reais negativas ⟹ estável. O polo s₀ = −1/ARᵥ confirma estabilidade para A, Rᵥ > 0."),
    ("Projeto de controladores", "A função de transferência do processo é ponto de partida para projeto de controladores PID, realimentação de estados e compensadores."),
    ("Sistemas em série / paralelo", "Funções de transferência combinam-se por multiplicação (série) ou soma (paralelo), permitindo análise de processos com múltiplos estágios."),
]

with col_a1:
    for tag, texto in APPS_LEFT:
        st.markdown(f"""
<div class="app-item">
  <span class="app-item-tag">{tag}</span>
  <div class="app-item-text"><span style="font-family:'Inter',sans-serif;font-size:0.84rem;color:#8B949E;">{texto}</span></div>
</div>""", unsafe_allow_html=True)

with col_a2:
    for tag, texto in APPS_RIGHT:
        st.markdown(f"""
<div class="app-item">
  <span class="app-item-tag">{tag}</span>
  <div class="app-item-text"><span style="font-family:'Inter',sans-serif;font-size:0.84rem;color:#8B949E;">{texto}</span></div>
</div>""", unsafe_allow_html=True)


# ─── Rodapé ───────────────────────────────────────────────────────────────────

st.markdown("""
<div class="footer">
  UNIMONTES &nbsp;·&nbsp; Universidade Estadual de Montes Claros &nbsp;·&nbsp;
  Disciplina de Equações Diferenciais Ordinárias &nbsp;·&nbsp; Prof. <span>Fernando Félix</span><br>
  Bruno Gomes &nbsp;·&nbsp; Júlio César &nbsp;·&nbsp; Leonardo &nbsp;·&nbsp; Marcus &nbsp;·&nbsp; Samuel
  &nbsp;&nbsp;—&nbsp;&nbsp;
  built with <span>Streamlit</span> · <span>NumPy</span> · <span>Plotly</span>
</div>
""", unsafe_allow_html=True)
