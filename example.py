import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
from streamlit_lchart_card import streamlit_lchart_card

st.set_page_config(layout="wide")

t = [datetime.fromtimestamp(d.timestamp()) for d in
     pd.date_range(start=datetime(year=2023, month=1, day=31, hour=0, minute=0),
                   end=datetime(year=2023, month=2, day=1, hour=0, minute=0), freq="3h")]

nb_samples = len(t)
m_temp = 20.4
m_pH = 6.79
m_nitrate = 100.3
m_ammonia = 2.9

temps = [round(m, 1) for m in np.random.normal(m_temp, 2, nb_samples)]
pHs = [round(m, 2) for m in np.random.normal(m_pH, 1, nb_samples)]
nitrates = [round(m, 2) for m in np.random.normal(m_nitrate, 20, nb_samples)]
ammonias = [round(m, 2) for m in np.random.normal(m_ammonia, 0.1, nb_samples)]
water_levels = [float(m) for m in np.random.binomial(1, 0.1, nb_samples)]

df_temps = pd.DataFrame({"date": t, "measure": temps})
df_pHs = pd.DataFrame({"date": t, "measure": pHs})
df_nitrates = pd.DataFrame({"date": t, "measure": nitrates})
df_ammonias = pd.DataFrame({"date": t, "measure": ammonias})
df_water_levels = pd.DataFrame({"date": t, "measure": water_levels})

multiple_graphs = st.columns(4)
with multiple_graphs[0]:
    streamlit_lchart_card(title="Température", df=df_temps, x="date", y="measure",
                          labels={"measure": "°C", "date": "Date"}, defaultColor="rgb(255, 180, 15)", thresh=20,
                          threshColor="rgb(255, 90, 132)", rounding=1, format="%d/%m %Hh",
                          key="streamlit_temp_lchart_card")
with multiple_graphs[1]:
    streamlit_lchart_card(title="Nitrate", df=df_nitrates, x="date", y="measure",
                          labels={"measure": "mg/L", "date": "Date"}, defaultColor="rgb(132, 99, 255)", thresh=95.2,
                          rounding=2, key="streamlit_nitrate_lchart_card")
with multiple_graphs[2]:
    streamlit_lchart_card(title="pH", df=df_pHs, x="date", y="measure",
                          labels={"measure": "", "date": "Date"}, defaultColor="rgb(99, 255, 132)", thresh=6,
                          rounding=2, key="streamlit_pH_lchart_card")
with multiple_graphs[3]:
    streamlit_lchart_card(title="Ammoniaque", df=df_ammonias, x="date", y="measure",
                          labels={"measure": "mg/L", "date": "Date"}, defaultColor="rgb(90, 90, 90)", thresh=2.87,
                          rounding=2, key="streamlit_ammonia_lchart_card")
