# 📊 FUTURE_DS_03 — Marketing Funnel & Conversion Performance Analysis

**Internship:** Future Interns | Data Science & Analytics Track
**Task:** FUTURE_DS_03 — Marketing Funnel & Conversion Performance Analysis
**Dataset:** Olist Brazilian E-Commerce — Marketing Qualified Leads & Closed Deals

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
│   └── dashboard_preview.png            # Dashboard screenshot
├── images/
│   ├── funnel_overview.png
│   ├── channel conversion map.png
│   ├── Lead_volume_by_channel.png
│   ├── conversion_by_channel.png
│   ├── monthly_conversion_trend.png
│   ├── business_segments__won_deals_.png
│   └── lead_behaviour_profile_analysis.png
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

## 🖼️ Dashboard Preview

<img width="1920" height="2579" alt="dashboard" src="https://github.com/user-attachments/assets/bebfe7da-ab05-466c-b47a-16b05fa0f26b" />


> **Note:** Run the Streamlit app to explore the fully interactive version with live filters and hover tooltips.

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
| Dominant Lead Profile | Cat (61.2%) |

### Channel Performance

| Channel | MQLs | Won | CR % |
|---------|------|-----|------|
| Paid Search | 1,586 | 195 | 12.3% |
| Organic Search | 2,296 | 271 | 11.8% |
| Direct Traffic | 499 | 56 | 11.2% |
| Referral | 284 | 24 | 8.5% |
| Social | 1,350 | 75 | 5.6% |
| Display | 118 | 6 | 5.1% |
| Other Publicities | 65 | 3 | 4.6% |
| Email | 493 | 15 | 3.0% |
| Other | 150 | 4 | 2.7% |

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
6. **Reallocate Display & Other Publicities budget** — CR below 5.1%, low ROI channels

---

## 🛠 Tools Used

- Python (pandas, plotly, matplotlib, seaborn)
- Streamlit
- Jupyter Notebook

---

## 👤 Author

Bani Priya

🎓 B.Tech in Artificial Intelligence

🏫 Delhi Skill and Entrepreneurship University (DSEU)

---
## ⭐ Acknowledgement

I would like to thank Future Interns for this internship opportunity and for designing such a practical, real-world task. Special thanks to Olist for making the dataset publicly available on Kaggle. This project helped me grow as a data analyst and think beyond the numbers toward real business solutions.
