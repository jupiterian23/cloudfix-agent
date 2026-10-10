"""Command-line interface for CloudFix Agent."""

import argparse

from app.agent import diagnose
from app.history import list_incidents, normalize_search_text, save_incident
from app.logging_config import setup_logging


def main():
    parser = argparse.ArgumentParser(
        description="CloudFix Agent - Cloud troubleshooting assistant"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    diagnose_parser = subparsers.add_parser(
        "diagnose", help="Diagnose a cloud issue"
    )
    diagnose_parser.add_argument("problem", nargs="+")

    history_parser = subparsers.add_parser(
        "history", help="List and search saved incidents"
    )
    history_parser.add_argument(
        "--search", help="Search incident text using a keyword"
    )
    history_parser.add_argument(
        "--issue", help="Filter by issue type, e.g. network or access"
    )

    args = parser.parse_args()
    logger = setup_logging()

    if args.command == "diagnose":
        problem = " ".join(args.problem)
        logger.info("Starting diagnosis")

        result = diagnose(problem)
        incident_path = save_incident(problem, result)

        logger.info("Diagnosis completed: %s", result.issue)
        logger.info("Incident saved: %s", incident_path)

        print(f"\nIssue:        {result.issue}")
        print(f"Likely cause: {result.likely_cause}")
        print(f"Recommended:  {result.recommended_action}")
        print(f"Risk:         {result.risk}")
        print(f"Incident ID:  {incident_path.stem}")

    elif args.command == "history":
        incidents = list_incidents()

        if args.search:
            keyword = normalize_search_text(args.search)
            incidents = [
                item for item in incidents
                if keyword in normalize_search_text(" ".join(
                    str(item.get(field, ""))
                    for field in (
                        "id", "problem", "issue",
                        "likely_cause", "recommended_action"
                    )
                ))
            ]

        if args.issue:
            issue_filter = args.issue.casefold()
            incidents = [
                item for item in incidents
                if issue_filter in str(item.get("issue", "")).casefold()
            ]

        if not incidents:
            print("No matching incidents found.")
            return

        print(f"Found {len(incidents)} incident(s).")

        for item in incidents:
            print(
                f"\nID: {item.get('id', 'Unknown')}\n"
                f"Time: {item.get('timestamp', 'Unknown')}\n"
                f"Problem: {item.get('problem', 'Unknown')}\n"
                f"Issue: {item.get('issue', 'Unknown')}"
            )


if __name__ == "__main__":
    main()
