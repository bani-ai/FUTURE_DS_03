"""
Marketing Funnel & Conversion Performance Dashboard
FUTURE_DS_03 (v3) | Future Interns — Data Science & Analytics
Built with Plotly for full dark-theme integration.
Run: streamlit run dashboard/app.py   (from FUTURE_DS_03_v3 root folder)
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

st.set_page_config(
    page_title="Marketing Funnel Dashboard | FUTURE_DS_03",
    page_icon="📊",
    layout="wide",
)

BG_DARK    = "#0a1f1f"
BG_CARD    = "#0d2b2b"
ACCENT     = "#00b894"
ACCENT2    = "#00cec9"
TEXT_LIGHT = "#e2e8f0"
TEXT_MUTED = "#a0aec0"
GRID_COLOR = "#1f3a3a"
PALETTE = ["#00b894", "#00cec9", "#55efc4", "#81ecec", "#6c5ce7", "#a29bfe", "#fdcb6e", "#e17055"]

st.markdown(f"""
<style>
    .stApp {{ background-color: {BG_DARK}; color: {TEXT_LIGHT}; }}
    .main-header {{
        background: linear-gradient(135deg, #0a1f1f 0%, #0d2b2b 50%, #00b894 100%);
        padding: 0.8rem 1.2rem;
        border-radius: 16px;
        margin-bottom: 0.5rem;
        border-left: 5px solid {ACCENT};
    }}
    .main-header h1 {{ color: #ffffff; font-size: 2rem; margin: 0; }}
    .main-header p  {{ color: {TEXT_MUTED}; margin: 0.3rem 0 0 0; font-size: 0.95rem; }}
    .kpi-card {{
        background: linear-gradient(135deg, {BG_DARK}, {BG_CARD});
        border: 1px solid {GRID_COLOR};
        border-radius: 12px;
        padding: 0.6rem 0.8rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }}
    .kpi-label {{ color: {TEXT_MUTED}; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.4rem; }}
    .kpi-value {{ color: #ffffff; font-size: 1.3rem; font-weight: 700; }}
    .kpi-sub   {{ color: {ACCENT}; font-size: 0.8rem; margin-top: 0.2rem; }}
    .section-title {{
        font-size: 1rem;
        font-weight: 700;
        color: {TEXT_LIGHT};
        padding: 0.3rem 0;
        border-bottom: 2px solid {ACCENT};
        margin-bottom: 0.5rem;
    }}
    .insight-card {{
        background: {BG_CARD};
        border: 1px solid {GRID_COLOR};
        border-left: 4px solid {ACCENT};
        border-radius: 10px;
        padding: 0.5rem 0.8rem;
        margin-bottom: 0.5rem;
    }}
    .insight-card strong {{ color: #fdcb6e; }}
    .insight-rec {{ color: {ACCENT}; font-size: 0.85rem; margin-top: 0.3rem; }}
    hr {{ border-color: {GRID_COLOR} !important; }}
    .js-plotly-plot {{ border-radius: 12px; }}
</style>
""", unsafe_allow_html=True)

def style_fig(fig, title=None, height=250):
    fig.update_layout(
        plot_bgcolor=BG_CARD,
        paper_bgcolor=BG_DARK,
        font=dict(color=TEXT_LIGHT, size=11),
        title=dict(text=title, font=dict(size=13, color=TEXT_LIGHT)) if title else None,
        margin=dict(l=5, r=5, t=35 if title else 5, b=5),
        height=height,
        legend=dict(bgcolor=BG_CARD, bordercolor=GRID_COLOR, borderwidth=1, font=dict(color=TEXT_LIGHT, size=10)),
        xaxis=dict(gridcolor=GRID_COLOR, zerolinecolor=GRID_COLOR, color=TEXT_LIGHT),
        yaxis=dict(gridcolor=GRID_COLOR, zerolinecolor=GRID_COLOR, color=TEXT_LIGHT),
    )
    return fig

BASE    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = os.path.join(BASE, "dataset")

@st.cache_data
def load_data():
    mqls = pd.read_csv(os.path.join(DATASET, "olist_marketing_qualified_leads_dataset.csv"))
    mqls["first_contact_date"] = pd.to_datetime(mqls["first_contact_date"], dayfirst=True, errors="coerce")
    mqls["origin"] = mqls["origin"].fillna("unknown").str.strip().replace("", "unknown")
    deals = pd.read_csv(os.path.join(DATASET, "olist_closed_deals_dataset.csv"))
    deals["won_date"] = pd.to_datetime(deals["won_date"], dayfirst=True, errors="coerce")
    merged = mqls.merge(
        deals[["mql_id","won_date","business_segment","lead_type","lead_behaviour_profile","declared_monthly_revenue"]],
        on="mql_id", how="left"
    )
    merged["converted"] = merged["won_date"].notna().astype(int)
    return mqls, deals, merged

mqls, deals, merged = load_data()

total_mqls  = len(mqls)
total_deals = len(deals)
overall_cr  = total_deals / total_mqls * 100
drop_off    = 100 - overall_cr

cs = merged.groupby("origin").agg(tl=("mql_id","count"), cl=("converted","sum")).reset_index()
cs["cr"] = cs["cl"] / cs["tl"] * 100
cs_f = cs[~cs["origin"].isin(["unknown",""])]
best_ch = cs_f.loc[cs_f["cr"].idxmax(), "origin"]
best_cr = cs_f["cr"].max()

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="main-header">
  <h1>📊 Marketing Funnel & Conversion Analysis</h1>
  <p>FUTURE_DS_03 &nbsp;|&nbsp; Future Interns — Data Science & Analytics &nbsp;|&nbsp; Olist Brazilian E-Commerce Dataset</p>
</div>
""", unsafe_allow_html=True)

# ── KPI Cards ──────────────────────────────────────────────────────────────────
c1,c2,c3,c4,c5 = st.columns(5)
kpis = [
    (c1, "Total MQLs",      f"{total_mqls:,}",   "Marketing Qualified Leads"),
    (c2, "Won Deals",       f"{total_deals:,}",   "Closed Deals"),
    (c3, "Conversion Rate", f"{overall_cr:.1f}%", "Lead → Customer"),
    (c4, "Drop-off Rate",   f"{drop_off:.1f}%",   "Did Not Convert"),
    (c5, "Best Channel",    best_ch,               f"CR: {best_cr:.1f}%"),
]
for col, label, value, sub in kpis:
    col.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# ROW 1 — Funnel Overview  |  Monthly Funnel Trend
# ══════════════════════════════════════════════════════════
r1c1, r1c2 = st.columns(2)

with r1c1:
    st.markdown('<div class="section-title">🔻 Funnel Overview</div>', unsafe_allow_html=True)
    fig = go.Figure(go.Funnel(
        y=["MQLs", "Closed Deals"],
        x=[total_mqls, total_deals],
        textinfo="value+percent initial",
        marker=dict(color=[ACCENT2, ACCENT]),
        connector=dict(line=dict(color=GRID_COLOR, width=1)),
        textfont=dict(color="#ffffff", size=13)
    ))
    fig = style_fig(fig, title=f"Overall Conversion Rate: {overall_cr:.1f}%", height=250)
    st.plotly_chart(fig, use_container_width=True)

with r1c2:
    st.markdown('<div class="section-title">📅 Monthly Funnel Trend</div>', unsafe_allow_html=True)
    mqls_temp = mqls.copy()
    deals_temp = deals.copy()
    mqls_temp["month"]      = mqls_temp["first_contact_date"].dt.to_period("M").astype(str)
    deals_temp["won_month"] = deals_temp["won_date"].dt.to_period("M").astype(str)
    mm = mqls_temp.groupby("month").size().reset_index(name="mqls")
    mw = deals_temp.groupby("won_month").size().reset_index(name="won")
    mw.columns = ["month","won"]
    mo = mm.merge(mw, on="month", how="left").fillna(0)
    mo["cr2"] = mo["won"] / mo["mqls"] * 100
    mo = mo.sort_values("month")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=mo["month"], y=mo["mqls"], name="MQLs", marker_color=ACCENT2, opacity=0.75), secondary_y=False)
    fig.add_trace(go.Bar(x=mo["month"], y=mo["won"], name="Won Deals", marker_color=ACCENT, opacity=0.95), secondary_y=False)
    fig.add_trace(go.Scatter(x=mo["month"], y=mo["cr2"], name="Conv. Rate %", mode="lines+markers",
                              line=dict(color="#fdcb6e", width=2), marker=dict(size=5)), secondary_y=True)
    fig.update_layout(barmode="overlay", xaxis_tickangle=-45)
    fig.update_yaxes(title_text="Count", secondary_y=False, gridcolor=GRID_COLOR, color=TEXT_LIGHT)
    fig.update_yaxes(title_text="Conv. Rate %", secondary_y=True, gridcolor=GRID_COLOR, color="#fdcb6e")
    fig = style_fig(fig, height=250)
    st.plotly_chart(fig, use_container_width=True)

# ══════════════════════════════════════════════════════════
# ROW 2 — Lead Volume by Channel  |  Conversion Rate by Channel
# ══════════════════════════════════════════════════════════
r2c1, r2c2 = st.columns(2)

with r2c1:
    st.markdown('<div class="section-title">📡 Lead Volume by Channel</div>', unsafe_allow_html=True)
    cs_vol = cs_f.sort_values("tl", ascending=False)
    fig = go.Figure(go.Bar(
        x=cs_vol["origin"], y=cs_vol["tl"],
        marker_color=PALETTE[:len(cs_vol)],
        text=cs_vol["tl"], textposition="outside",
        texttemplate="%{text:,}"
    ))
    fig.update_xaxes(tickangle=-30)
    fig = style_fig(fig, title="Lead Volume by Channel", height=250)
    fig.update_layout(yaxis_title="Total MQLs")
    st.plotly_chart(fig, use_container_width=True)

with r2c2:
    st.markdown('<div class="section-title">📊 Conversion Rate by Channel</div>', unsafe_allow_html=True)
    cs_cr = cs_f.sort_values("cr", ascending=False)
    bar_colors = ["#55efc4" if v>=10 else "#fdcb6e" if v>=5 else "#e17055" for v in cs_cr["cr"]]
    fig = go.Figure(go.Bar(
        x=cs_cr["origin"], y=cs_cr["cr"],
        marker_color=bar_colors,
        text=cs_cr["cr"], textposition="outside",
        texttemplate="%{text:.1f}%"
    ))
    avg_cr = cs_f["cr"].mean()
    fig.add_hline(y=avg_cr, line_dash="dash", line_color=ACCENT2,
                   annotation_text=f"Avg: {avg_cr:.1f}%", annotation_font_color=ACCENT2)
    fig.update_xaxes(tickangle=-30)
    fig = style_fig(fig, title="Conversion Rate by Channel (%)", height=250)
    fig.update_layout(yaxis_title="Conv. Rate %")
    st.plotly_chart(fig, use_container_width=True)

# ══════════════════════════════════════════════════════════
# ROW 3 — Business Segments  |  Lead Behaviour Profile
# ══════════════════════════════════════════════════════════
r3c1, r3c2 = st.columns(2)

with r3c1:
    st.markdown('<div class="section-title">🏷️ Top 10 Business Segments</div>', unsafe_allow_html=True)
    ts = deals["business_segment"].value_counts().head(10).sort_values()
    fig = go.Figure(go.Bar(
        x=ts.values, y=ts.index, orientation="h",
        marker_color=[PALETTE[i % len(PALETTE)] for i in range(len(ts))],
        text=ts.values, textposition="outside"
    ))
    fig = style_fig(fig, title="Top 10 Business Segments (Won Deals)", height=250)
    fig.update_layout(xaxis_title="Number of Won Deals")
    st.plotly_chart(fig, use_container_width=True)

with r3c2:
    st.markdown('<div class="section-title">🐱 Lead Behaviour Profile</div>', unsafe_allow_html=True)
    pc = deals["lead_behaviour_profile"].value_counts().head(6)
    fig = go.Figure(go.Pie(
        labels=pc.index, values=pc.values,
        marker=dict(colors=PALETTE[:len(pc)], line=dict(color=BG_DARK, width=2)),
        textinfo="percent+label", textfont=dict(size=11, color="#ffffff"),
        hole=0.35,
        pull=[0.03]*len(pc)
    ))
    fig = style_fig(fig, title="Won Deals by Behaviour Profile", height=250)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Insights ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">💡 Key Insights & Recommendations</div>', unsafe_allow_html=True)
insights = [
    ("🔍 Organic Search dominates volume (2,296 leads, 11.8% CR)",   "Invest in SEO — blogs, keywords, landing page optimisation"),
    ("🚀 Paid Search has the best scalable CR (12.3%)",               "Increase budget; run A/B tests on creatives & landing pages"),
    ("⚠️ Email has very low CR (3.0%) despite 493 leads",            "Redesign nurture sequences; personalise & segment email lists"),
    ("📱 Social brings 1,350 leads but only 5.6% CR",                "Improve CTAs, retargeting, and bottom-of-funnel content"),
    ("💎 Referral converts at 8.5% with near-zero cost",             "Launch a formal referral / partner incentive programme"),
    ("🏠 Home Decor & Health/Beauty are top-converting segments",     "Build vertical-specific campaigns and case studies"),
    ("🐱 Cat-profile leads dominate won deals (61.7%)",              "Train SDRs on data-driven, patient buyer techniques"),
    ("📉 Conversions peaked Apr 2018 then dropped sharply",          "Investigate pipeline health; implement seasonal strategy"),
    ("🎯 89.5% overall drop-off is a major revenue leak",            "Implement lead scoring to prioritise high-intent leads"),
]
col_a, col_b = st.columns(2)
for i, (insight, rec) in enumerate(insights):
    target = col_a if i % 2 == 0 else col_b
    target.markdown(f"""
    <div class="insight-card">
        <strong>{insight}</strong>
        <div class="insight-rec">→ {rec}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>")
st.markdown(f'<p style="color:{TEXT_MUTED}; text-align:center; font-size:0.8rem;">FUTURE_DS_03 v3 | Future Interns — Data Science & Analytics | Python · pandas · Plotly · Streamlit</p>', unsafe_allow_html=True)
