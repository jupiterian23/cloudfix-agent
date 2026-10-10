"""Basic cloud troubleshooting logic for CloudFix Agent."""

from dataclasses import dataclass


@dataclass
class Diagnosis:
    issue: str
    likely_cause: str
    recommended_action: str
    risk: str = "Low"


def diagnose(problem: str) -> Diagnosis:
    """Identify common cloud-support issues from a problem description."""
    text = problem.lower()

    if "access denied" in text or "unauthorized" in text:
        return Diagnosis(
            issue="Access or permissions failure",
            likely_cause=(
                "The identity may lack required permissions, "
                "or a policy may explicitly deny the request."
            ),
            recommended_action=(
                "Verify the active identity and review IAM policies, "
                "resource policies, and any explicit denies."
            ),
        )

    if "timeout" in text or "connection timed out" in text:
        return Diagnosis(
            issue="Network connectivity failure",
            likely_cause=(
                "Traffic may be blocked by routing, firewall rules, "
                "security groups, or an unavailable destination."
            ),
            recommended_action=(
                "Check DNS resolution, routes, security groups, "
                "network ACLs, and destination health."
            ),
        )

    if "503" in text or "service unavailable" in text:
        return Diagnosis(
            issue="Service availability failure",
            likely_cause=(
                "The service may be unhealthy, overloaded, "
                "or unable to reach its dependencies."
            ),
            recommended_action=(
                "Inspect service health, application logs, resource "
                "utilization, and dependency availability."
            ),
        )

    return Diagnosis(
        issue="Unknown or unclassified issue",
        likely_cause="There is not enough information to identify a cause.",
        recommended_action=(
            "Collect the exact error message, timestamps, relevant logs, "
            "affected resource, and recent changes."
        ),
        risk="Needs investigation",
    )
