# 📊 FUTURE_DS_03 (v3) — Marketing Funnel & Conversion Performance Analysis

**Internship:** Future Interns | Data Science & Analytics Track
**Task:** FUTURE_DS_03 — Marketing Funnel & Conversion Performance Analysis
**Dataset:** Olist Brazilian E-Commerce — Marketing Qualified Leads & Closed Deals

---

## 🆕 What's New in v3
- Dashboard rebuilt with **Plotly** (interactive, dark-theme native — no white chart boxes)
- **Green & Cyan** professional theme
- Cleaner KPI cards, styled tables, and insight cards
- PNG charts and CSV datasets organised into separate folders

---

## 🎯 Objective

Analyze the marketing funnel to:
- Identify where leads drop off in the funnel
- Compare conversion rates across marketing channels
- Understand which business segments and lead profiles drive the most conversions
- Provide actionable recommendations to improve lead-to-customer conversion

---

## 📁 Repository Structure

```
FUTURE_DS_03_v3/
│
├── dashboard/
│   └── app.py                       # Interactive Plotly + Streamlit dashboard
│
├── images/
│   ├── funnel_overview.png
│   ├── channel_performance.png
│   ├── monthly_trend.png
│   ├── behaviour_profile.png
│   └── top_segments.png
│
├── notebook/
│   └── Analysis.ipynb               # Full EDA + funnel analysis (Jupyter)
│
├── report/
│   └── Task_Report.pdf              # Full analysis report
│
├── insights/
│   └── key_insights.md              # Detailed insights & recommendations
│
├── dataset/
│   ├── olist_marketing_qualified_leads_dataset.csv
│   └── olist_closed_deals_dataset.csv
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

| File | Description | Rows |
|------|-------------|------|
| `olist_marketing_qualified_leads_dataset.csv` | MQLs with origin channel and contact date | 8,000 |
| `olist_closed_deals_dataset.csv` | Won deals with segment, lead type, revenue | 842 |

---

## 🔑 Key Findings

| Metric | Value |
|--------|-------|
| Total MQLs | 8,000 |
| Won Deals | 842 |
| **Overall Conversion Rate** | **10.5%** |
| Best Channel (CR) | Paid Search — 12.3% |
| Worst Channel (CR) | Email — 3.0% |
| Top Business Segment | Home Decor (105 deals) |
| Dominant Lead Profile | Cat (61.7%) |

---

## 🚀 How to Run

### Option 1 — Streamlit Dashboard (Recommended)
```bash
pip install -r requirements.txt
cd FUTURE_DS_03_v3
streamlit run dashboard/app.py
```

### Option 2 — Jupyter Notebook
```bash
pip install -r requirements.txt
cd notebook
jupyter notebook Analysis.ipynb
```

---

## 💡 Top Recommendations

1. **Increase Paid Search investment** — highest conversion rate (12.3%) among scalable channels
2. **Redesign Email campaigns** — only 3.0% CR, massive improvement potential
3. **Launch a Referral Program** — 8.5% CR with near-zero acquisition cost
4. **Implement Lead Scoring** — prioritise high-intent leads to reduce the 89.5% drop-off
5. **Focus on Home Decor & Health/Beauty** — consistently top-converting segments

---

## 🛠 Tools Used

- Python (pandas, plotly, matplotlib, seaborn)
- Streamlit
- Jupyter Notebook

---

## 👤 Author

Future Interns — Data Science & Analytics Intern
Track Code: **DS** | Task: **FUTURE_DS_03**
