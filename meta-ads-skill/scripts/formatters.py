def format_campaigns(data):
    if not data:
        return "No campaigns found."

    lines = []
    lines.append("| ID | Name | Status | Objective |")
    lines.append("|---|---|---|---|")

    for item in data:
        lines.append(
            f"| {item.get('id', 'N/A')} | {item.get('name', 'N/A')} | {item.get('status', 'N/A')} | {item.get('objective', 'N/A')} |"
        )

    return "\n".join(lines)


def format_adsets(data):
    if not data:
        return "No ad sets found."

    lines = []
    lines.append("| ID | Name | Status | Campaign ID | Daily Budget |")
    lines.append("|---|---|---|---|---|")

    for item in data:
        lines.append(
            f"| {item.get('id', 'N/A')} | {item.get('name', 'N/A')} | {item.get('status', 'N/A')} | {item.get('campaign_id', 'N/A')} | {item.get('daily_budget', 'N/A')} |"
        )

    return "\n".join(lines)


def format_insights(data):
    if not data:
        return "No insights found."

    lines = []
    lines.append("| Campaign ID | Campaign Name | Spend | Impressions | Clicks |")
    lines.append("|---|---|---|---|---|")

    for item in data:
        lines.append(
            f"| {item.get('campaign_id', 'N/A')} | {item.get('campaign_name', 'N/A')} | {item.get('spend', 'N/A')} | {item.get('impressions', 'N/A')} | {item.get('clicks', 'N/A')} |"
        )

    return "\n".join(lines)
