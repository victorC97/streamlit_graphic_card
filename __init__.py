import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _streamlit_graphic_card = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_graphic_card",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _streamlit_graphic_card = components.declare_component("streamlit_graphic_card", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def streamlit_graphic_card(title, df, x, y, labels, rounding, defaultColor="#0000FF", thresh=None, threshColor="rgb(255, 90, 132)", key=None):
    x_list = df[x].to_numpy()
    y_list = df[y].to_numpy()
    mean_y = round(df[y].mean(), rounding)
    max_y = round(df[y].max(), rounding)
    min_y = round(df[y].min(), rounding)
    streamlit_graphic_card_value = _streamlit_graphic_card(title=title, x=x_list, y=y_list, metrics={"min": min_y, "mean": mean_y, "max": max_y}, labels={"x": labels[x] if x in labels else None, "y": labels[y] if y in labels else None}, defaultColor=defaultColor, thresh=thresh, threshColor=threshColor, key=key)
    return streamlit_graphic_card_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:
    import streamlit as st
    import numpy as np
    import pandas as pd
    from datetime import datetime

    st.set_page_config(layout="wide")

    nb_samples = 31
    m_temp = 20.4
    m_pH = 6.79
    m_nitrate = 100.3
    m_ammonia = 2.9

    t = [d.date() for d in
         pd.date_range(start=datetime(year=2023, month=1, day=1), end=datetime(year=2023, month=1, day=31), freq="D")]
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
        streamlit_graphic_card(title="Température", df=df_temps, x="date", y="measure",
                               labels={"measure": "°C", "date": "Date"}, defaultColor="rgb(255, 180, 15)", thresh=20, threshColor="rgb(255, 90, 132)", rounding=1, key="streamlit_temp_graphic_card")
    with multiple_graphs[1]:
        streamlit_graphic_card(title="Nitrate", df=df_nitrates, x="date", y="measure",
                               labels={"measure": "mg/L", "date": "Date"}, defaultColor="rgb(132, 99, 255)", thresh=95.2, rounding=2, key="streamlit_nitrate_graphic_card")
    with multiple_graphs[2]:
        streamlit_graphic_card(title="pH", df=df_pHs, x="date", y="measure",
                               labels={"measure": "", "date": "Date"}, defaultColor="rgb(99, 255, 132)", thresh=6, rounding=2, key="streamlit_pH_graphic_card")
    with multiple_graphs[3]:
        streamlit_graphic_card(title="Ammoniaque", df=df_ammonias, x="date", y="measure",
                               labels={"measure": "mg/L", "date": "Date"}, defaultColor="rgb(90, 90, 90)", thresh=2.87, rounding=2, key="streamlit_ammonia_graphic_card")