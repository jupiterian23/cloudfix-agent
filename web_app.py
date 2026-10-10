
import streamlit as st
import streamlit.components.v1 as components

from app.agent import diagnose

st.set_page_config(
    page_title="CloudFix Agent",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- CUSTOM CSS --------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #080d19;
        --panel: #111a2b;
        --border: #25334a;
        --cyan: #42d9ff;
        --text: #edf5ff;
        --muted: #92a4bd;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: var(--bg);
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(8, 13, 25, 0.92);
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3, p, label {
        font-family: 'Inter', sans-serif !important;
    }

    .hero {
        background: linear-gradient(125deg, #142742, #10172b 65%, #17203b);
        border: 1px solid #2b4261;
        border-radius: 22px;
        padding: 30px;
        margin-bottom: 22px;
        position: relative;
        overflow: hidden;
    }

    .eyebrow {
        color: var(--cyan);
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero h1 {
        color: #ffffff;
        font-size: clamp(30px, 4vw, 46px);
        font-weight: 800;
        letter-spacing: -1.5px;
        margin: 10px 0;
    }

    .hero p {
        color: #b4c6df;
        max-width: 650px;
        font-size: 15px;
        line-height: 1.8;
    }

    .panel {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 17px;
        padding: 22px;
        margin: 12px 0;
    }

    .metric-label {
        color: var(--muted);
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
    }

    .metric-value {
        color: var(--text);
        font-size: 20px;
        font-weight: 800;
        margin-top: 10px;
    }

    .section-title {
        color: #f1f7ff;
        font-size: 21px;
        font-weight: 800;
        margin: 28px 0 8px;
    }

    .muted {
        color: var(--muted);
        font-size: 13px;
        line-height: 1.7;
    }

    .result-label {
        color: var(--cyan);
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.4px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .result-value {
        color: #f0f6ff;
        font-size: 15px;
        line-height: 1.8;
    }

    .stTextInput input, .stSelectbox [data-baseweb="select"] {
        background: #0c1423;
        border-color: #31445f;
        border-radius: 10px;
        color: #ffffff;
    }

    .stTextInput label, .stSelectbox label {
        color: #c7d6e9 !important;
        font-weight: 600;
    }

    .stButton > button {
        background: linear-gradient(90deg, #1bb9e8, #5488ff);
        color: #06101d;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        min-height: 46px;
        font-weight: 800;
        transition: transform 0.2s, filter 0.2s;
    }

    .stButton > button:hover {
        filter: brightness(1.12);
        transform: translateY(-2px);
        border: none;
        color: #06101d;
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    .footer {
        color: #778ba7;
        text-align: center;
        font-size: 12px;
        padding: 28px 0 5px;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem;
        }

        .hero {
            padding: 21px;
        }

        .hero h1 {
            letter-spacing: -0.5px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- HERO SECTION --------------------

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">☁️ Cloud operations intelligence</div>
        <h1>CloudFix Agent</h1>
        <p>
            Less guessing. Clearer diagnostics. Better next steps.
            Investigate common cloud errors with a troubleshooting
            assistant built for cloud learners and support engineers.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# JavaScript runs inside its own HTML component.
# This animation is decorative and does not access AWS or Python.
components.html(
    """
    <div id="status-card" style="
        background:#111a2b;
        border:1px solid #25334a;
        border-radius:14px;
        padding:15px 18px;
        display:flex;
        align-items:center;
        gap:12px;
        color:#edf5ff;
        font-family:Arial,sans-serif;
    ">
      <div id="status-dot" style="
          width:10px;height:10px;border-radius:50%;
          background:#42d9ff;box-shadow:0 0 14px #42d9ff;
      "></div>
      <div>
        <div style="font-size:11px;letter-spacing:1.5px;color:#92a4bd;">
          AGENT STATUS
        </div>
        <div id="status-text" style="font-size:14px;font-weight:bold;margin-top:4px;">
          Ready to investigate
        </div>
      </div>
      <div style="margin-left:auto;color:#42d9ff;font-size:12px;">
        DEMO MODE
      </div>
    </div>
    <script>
      const messages = [
        "Ready to investigate",
        "Diagnostics standing by",
        "Waiting for your next issue"
      ];
      let index = 0;
      const status = document.getElementById("status-text");

      setInterval(() => {
        index = (index + 1) % messages.length;
        if (status) status.textContent = messages[index];
      }, 3500);
    </script>
    """,
    height=75,
)

# -------------------- OVERVIEW CARDS --------------------

st.markdown('<div class="section-title">Your troubleshooting workspace</div>',
            unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="panel">
            <div class="metric-label">01 / Diagnose</div>
            <div class="metric-value">🔍 Investigate</div>
            <div class="muted">Classify common infrastructure errors.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="panel">
            <div class="metric-label">02 / Understand</div>
            <div class="metric-value">🧠 Find clues</div>
            <div class="muted">Explore likely causes in plain language.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="panel">
            <div class="metric-label">03 / Take action</div>
            <div class="metric-value">🛠️ Next steps</div>
            <div class="muted">Get practical checks to investigate.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------- DIAGNOSIS FORM --------------------

st.markdown('<div class="section-title">Start a diagnosis</div>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="muted">Choose an example or enter an error message from your own lab.</p>',
    unsafe_allow_html=True,
)

examples = {
    "EC2 connection timed out": "EC2 connection timed out",
    "AWS Access Denied when accessing S3":
        "AWS Access Denied when accessing S3",
    "HTTP 503 Service Unavailable": "HTTP 503 Service Unavailable",
    "Enter a custom error": "",
}

selected = st.selectbox("Choose a test case", list(examples.keys()))

problem = st.text_input(
    "Error message",
    value=examples[selected],
    placeholder="Example: EC2 connection timed out",
)

if st.button("⚡ Diagnose issue", use_container_width=True):
    if not problem.strip():
        st.warning("Please enter an error message first.")
    else:
        result = diagnose(problem.strip())

        st.markdown(
            '<div class="section-title">Diagnosis report</div>',
            unsafe_allow_html=True,
        )

        left, right = st.columns([2, 1])

        with left:
            st.markdown(
                f"""
                <div class="panel">
                    <div class="result-label">Detected issue</div>
                    <div class="result-value"><b>{result.issue}</b></div>
                    <br>
                    <div class="result-label">Likely cause</div>
                    <div class="result-value">{result.likely_cause}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with right:
            st.markdown(
                f"""
                <div class="panel">
                    <div class="result-label">Risk level</div>
                    <div class="metric-value">{result.risk}</div>
                    <div class="muted">
                        Informational assessment, not a live infrastructure check.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="panel">
                <div class="result-label">Recommended action</div>
                <div class="result-value">{result.recommended_action}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        report = (
            f"CloudFix Agent Diagnosis\\n"
            f"Issue: {result.issue}\\n"
            f"Likely cause: {result.likely_cause}\\n"
            f"Recommended action: {result.recommended_action}\\n"
            f"Risk: {result.risk}\\n"
        )

        st.download_button(
            "📋 Export diagnosis report",
            data=report,
            file_name="cloudfix-diagnosis.txt",
            mime="text/plain",
            use_container_width=True,
        )

        st.caption(
            "CloudFix Agent uses rule-based suggestions. "
            "Verify recommendations against your actual environment."
        )

st.markdown(
    """
    <div class="footer">
        CLOUDFIX AGENT · BUILT FOR CLOUD LEARNING<br>
        Demo mode · No live AWS access · No automatic remediation
    </div>
    """,
    unsafe_allow_html=True,
)
