# ☁️ CloudFix Agent — Cloud Troubleshooting Assistant

A lightweight, Python-based cloud troubleshooting assistant that analyzes common infrastructure errors, identifies likely causes, and recommends practical diagnostic steps.

CloudFix Agent is designed as a learning project for **AWS Cloud Support, Linux troubleshooting, networking, and AI-assisted cloud operations**.

## 🚀 Features

- 🔍 **Automated Error Diagnosis** — Classifies common cloud and infrastructure errors.
- 🌐 **Network Troubleshooting** — Provides diagnostic suggestions for connection timeouts.
- 🔐 **Access Error Analysis** — Helps investigate access-denied and authorization issues.
- ⚠️ **Service Availability Checks** — Suggests troubleshooting steps for HTTP 503 errors.
- 🖥️ **Interactive Web Interface** — Diagnose errors through a Streamlit application.
- 💻 **Command-Line Interface** — Run diagnoses directly from the terminal.
- 📝 **Incident History** — Save and review previous diagnostic incidents.
- 🧪 **Automated Testing** — Includes pytest tests to validate diagnostic behavior.
- 🛡️ **Safe Demo Mode** — Does not connect to or modify live AWS resources.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Diagnostic logic and application development |
| Streamlit | Interactive web interface |
| pytest | Automated testing |
| Linux / Ubuntu | Development and troubleshooting environment |
| Git & GitHub | Version control and source code management |

## 🏗️ Project Structure

```text
cloudfix-agent/
├── app/
│   ├── agent.py
│   ├── history.py
│   ├── logging_config.py
│   └── main.py
├── tests/
│   └── test_agent.py
├── logs/
├── requirements.txt
├── web_app.py
├── .gitignore
├── .env.example
└── README.md
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or later
- Git
- Linux, macOS, or Windows with WSL

### 1. Clone the repository

```bash
git clone https://github.com/jupiterian23/cloudfix-agent.git
cd cloudfix-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the web application

```bash
streamlit run web_app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 💻 Command-Line Usage

Diagnose a network connectivity issue:

```bash
python -m app.main diagnose "EC2 connection timed out"
```

Diagnose an access error:

```bash
python -m app.main diagnose "AWS Access Denied when accessing S3"
```

Review incident history:

```bash
python -m app.main history
```

Search incident history:

```bash
python -m app.main history --search timeout
```

## 🧪 Run Tests

Execute the test suite with:

```bash
python -m pytest -v
```

The current test suite contains **8 tests**, which passed during local validation.

## 🔎 Example Diagnosis

**Input:** `EC2 connection timed out`

**Likely cause:** Network traffic may be blocked by routing, firewall rules, security groups, or an unavailable destination.

**Recommended checks:**
- Verify DNS resolution and destination reachability.
- Inspect route tables and subnet configuration.
- Review security groups and network ACLs.
- Check whether the destination service is running.

**Risk level:** Low — informational recommendation only.

*The output is rule-based and is not a verified diagnosis of a live environment.*

## 🌐 Live Demo

**Status:** Deployment pending.

Once deployed, the live Streamlit application will be linked here.

## 🔐 Security and Limitations

- This project currently uses rule-based diagnostic logic rather than a production AI model.
- It does not automatically access AWS accounts or inspect live infrastructure.
- It does not execute remediation commands or modify cloud resources.
- Diagnostic suggestions should be verified against the actual environment.
- Never commit AWS credentials, access tokens, passwords, or other secrets.

## 🗺️ Future Improvements

- Integrate an LLM-powered diagnostic assistant.
- Add structured log analysis and error-pattern detection.
- Introduce AWS CloudWatch log ingestion with appropriate permissions.
- Expand test coverage and diagnostic scenarios.
- Add multi-cloud troubleshooting support.
- Explore safe, approval-based remediation workflows.

## 👨‍💻 Author

**Shubham Gorule**

BCA Student | Aspiring Cloud Support Engineer

- GitHub: [@jupiterian23](https://github.com/jupiterian23)
- Portfolio: [Cloud Projects Portfolio](https://jupiterian23.github.io/)

---

⭐ If you find this project useful, consider starring the repository.

*Built as a hands-on learning project focused on cloud troubleshooting, infrastructure support, and automation.*
