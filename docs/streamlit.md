# How a Streamlit app works

A Streamlit app is one Python script, `app.py`. You run it with `streamlit run app.py`, and
Streamlit shows its output as a web page (in a Codespace, on port 8501; click the pop-up to open
it).

## The one idea: the script reruns from top to bottom
Every time a user moves a slider, types a number or clicks a button, Streamlit runs **the whole
script again**, from the first line to the last. Each widget returns its current value, so a
widget is just a variable:

```python
import numpy as np
import pandas as pd
import streamlit as st

st.title("Compound growth")
start = st.number_input("Initial investment ($)", value=10_000)   # a number box
rate = st.sidebar.slider("Annual return (%)", 0.0, 15.0, 7.0)     # a slider in the sidebar
years = st.sidebar.slider("Years", 1, 40, 20)

t = np.arange(years + 1)
value = start * (1 + rate / 100) ** t                              # plain Python
st.line_chart(pd.DataFrame({"Portfolio value": value}, index=t))
st.metric("Final value", f"${value[-1]:,.0f}")
```

Move the "Years" slider and the script reruns with `years` set to the new value; the chart and
the metric are redrawn. There are no callbacks to write.

## What follows from the rerun
| You want to | Use | Why |
|---|---|---|
| Load a data file or download prices once, not on every click | `@st.cache_data` on the function that loads it | Without it, the file is read again on every rerun |
| Keep a model or a database connection | `@st.cache_resource` | One shared object for all users |
| Remember something between reruns (a counter, a list of saved scenarios) | `st.session_state` | Ordinary variables start over on every rerun |
| Let users change several inputs, then compute once | `with st.form("inputs"):` and `st.form_submit_button` | The script reruns only when they submit |
| Rerun only one part of the page | `@st.fragment` | The rest of the page stays as it is |

```python
@st.cache_data
def load_quotes(path):
    return pd.read_csv(path)        # runs once per file; later reruns reuse the result
```

## Layout
- `st.sidebar`: inputs on the left (`st.sidebar.slider`, or `with st.sidebar:`).
- `st.columns(2)`: side-by-side boxes; `st.tabs(["Prices", "Greeks"])`: tabs;
  `st.expander("Method")`: a section that opens on click.
- Output: `st.write`, `st.metric`, `st.dataframe`, `st.line_chart`, `st.altair_chart`,
  `st.error`, `st.info`, `st.download_button`.
- Dollar signs: in text Streamlit formats (`st.markdown`, `st.write`, `st.caption`, widget labels),
  anything between two `$` signs becomes math. Write `\$` for a dollar amount (in a Python string,
  `"\\$"`).

## Keep formulas out of `app.py`
Put calculations in modules (`pricing.py`) and test them with `pytest`; `app.py` only reads inputs,
calls those functions and shows results (see `AGENTS.md`). Tests then do not need Streamlit.

## Run and deploy
- Run: `streamlit run app.py`. Save a file and the page offers to rerun with your change.
- Deploy: share.streamlit.io → Create app → pick your repo and `app.py`. Community Cloud installs
  the packages in `requirements.txt`, so every package you import must be listed there.
- Secrets (API keys): in the app's Settings → Secrets on share.streamlit.io, or in
  `.streamlit/secrets.toml` in the Codespace, which `.gitignore` keeps out of the repo. Read them with
  `st.secrets["KEY_NAME"]`.

## Links
- Main concepts: https://docs.streamlit.io/get-started/fundamentals/main-concepts
- Caching: https://docs.streamlit.io/develop/concepts/architecture/caching
- Session state: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
- Forms and fragments: https://docs.streamlit.io/develop/api-reference/execution-flow/st.form ·
  https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment
- Layout: https://docs.streamlit.io/develop/api-reference/layout
- Deploy and secrets: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app ·
  https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management
