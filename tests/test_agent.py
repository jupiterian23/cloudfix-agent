from app.agent import diagnose


def test_access_denied():
    result = diagnose("AWS Access Denied")
    assert result.issue == "Access or permissions failure"


def test_network_timeout():
    result = diagnose("EC2 connection timed out")
    assert result.issue == "Network connectivity failure"


def test_service_unavailable():
    result = diagnose("Application returned HTTP 503")
    assert result.issue == "Service availability failure"


def test_unknown_issue():
    result = diagnose("Something unusual happened")
    assert result.issue == "Unknown or unclassified issue"


def test_save_incident(tmp_path, monkeypatch):
    from app import history
    from app.agent import diagnose

    monkeypatch.setattr(history, "HISTORY_DIR", tmp_path)

    problem = "EC2 connection timed out"
    result = diagnose(problem)
    path = history.save_incident(problem, result)

    assert path.exists()

    import json
    incident = json.loads(path.read_text(encoding="utf-8"))

    assert incident["problem"] == problem
    assert incident["issue"] == result.issue
    assert incident["id"] == path.stem


def test_list_incidents(tmp_path, monkeypatch):
    from app import history
    from app.agent import diagnose

    monkeypatch.setattr(history, "HISTORY_DIR", tmp_path)

    history.save_incident("EC2 connection timed out",
                          diagnose("EC2 connection timed out"))
    history.save_incident("AWS Access Denied",
                          diagnose("AWS Access Denied"))

    incidents = history.list_incidents()

    assert len(incidents) == 2
    assert all("id" in item for item in incidents)


def test_list_incidents_empty_directory(tmp_path, monkeypatch):
    from app import history

    monkeypatch.setattr(history, "HISTORY_DIR", tmp_path)

    assert history.list_incidents() == []


def test_normalize_timeout_variations():
    from app.history import normalize_search_text

    assert normalize_search_text("TIMED OUT") == "timeout"
    assert normalize_search_text("timeout") == "timeout"
