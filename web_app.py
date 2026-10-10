import streamlit as st
from app.agent import diagnose

st.set_page_config(page_title="CloudFix Agent", page_icon="🛠️")

st.title("🛠️ CloudFix Agent")
st.write("Your cloud troubleshooting assistant")
st.info("Demo mode: this app does not connect to or modify live AWS resources.")

examples = {
    "EC2 connection timed out": "EC2 connection timed out",
    "AWS Access Denied when accessing S3":
        "AWS Access Denied when accessing S3",
    "HTTP 503 Service Unavailable": "HTTP 503 Service Unavailable",
}

choice = st.selectbox("Try an example", list(examples.keys()) + ["Enter my own"])
if choice == "Enter my own":
    problem = st.text_area("Describe your error")
else:
    problem = examples[choice]

if st.button("🔍 Diagnose issue", type="primary"):
    if not problem.strip():
        st.warning("Please enter an error description.")
    else:
        result = diagnose(problem)
        st.subheader("Diagnosis results")
        st.write("**Issue:**", result.issue)
        st.write("**Likely cause:**", result.likely_cause)
        st.write("**Recommended action:**", result.recommended_action)
        st.write("**Risk:**", result.risk)
        st.caption("Suggestions are rule-based and are not a verified diagnosis.")
