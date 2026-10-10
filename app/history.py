"""Store and list CloudFix Agent incidents."""

import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

HISTORY_DIR = Path("logs/incidents")


def save_incident(problem, diagnosis):
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    incident = {
        "id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "problem": problem,
        "issue": diagnosis.issue,
        "likely_cause": diagnosis.likely_cause,
        "recommended_action": diagnosis.recommended_action,
        "risk": diagnosis.risk,
    }

    path = HISTORY_DIR / f"{incident['id']}.json"
    path.write_text(json.dumps(incident, indent=2), encoding="utf-8")
    return path


def list_incidents():
    if not HISTORY_DIR.exists():
        return []

    incidents = []

    for path in HISTORY_DIR.glob("*.json"):
        try:
            incidents.append(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue

    return sorted(
        incidents,
        key=lambda item: item.get("timestamp", ""),
        reverse=True,
    )


def normalize_search_text(value):
    """Normalize common wording variations for incident searches."""
    text = " ".join(value.casefold().split())
    return text.replace("timed out", "timeout")
