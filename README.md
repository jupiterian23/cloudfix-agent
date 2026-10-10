# CloudFix Agent

A Python-based cloud troubleshooting CLI that helps diagnose common AWS
and infrastructure errors, suggests corrective actions, and records
incident history locally.

## Features

- Diagnose common access and permission errors
- Identify connection timeouts and service-unavailable errors
- Receive a likely cause, recommended action, and risk assessment
- Save and search previous incident records
- Run automated tests with pytest

## Requirements

- Python 3.10 or newer
- pip
- Git

## Setup

```bash
git clone https://github.com/jupiterian23/cloudfix-agent.git
cd cloudfix-agent

python3 -m venv .venv
source .venv/bin/activate

python -m pip install pytest
```

## Usage

Diagnose an issue:

```bash
python -m app.main diagnose "EC2 connection timed out"
python -m app.main diagnose "AWS Access Denied when accessing S3"
```

View incident history:

```bash
python -m app.main history
python -m app.main history --search timeout
```

Run tests:

```bash
python -m pytest -v
```

## Project Structure

- `app/` — diagnosis, CLI, history, and logging modules
- `tests/` — automated tests
- `config/` — configuration files
- `tools/` — supporting tools
- `logs/` — locally generated logs and incident history

## Safety

CloudFix Agent currently uses rule-based diagnostic logic. Review its
recommendations before making infrastructure changes. Do not commit
credentials, access tokens, private keys, or sensitive incident data.

## Roadmap

- Expand diagnostic rules
- Add structured AWS diagnostic integrations
- Build an interactive web demo
