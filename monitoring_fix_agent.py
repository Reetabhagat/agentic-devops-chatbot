def monitoring_fix_agent(user_input: str):
    user_input = user_input.lower()

    if "alertmanager" in user_input:
        return """
🚨 Alertmanager firing too many alerts:

Fix:
1. Group alerts properly
2. Increase alert thresholds
3. Add silence rules
4. Tune alert duration (for:)

Check:
- alertmanager.yaml
"""

    if "metrics missing" in user_input:
        return """
📉 Metrics missing in Prometheus:

Reasons:
1. Exporter not running
2. Wrong scrape config
3. Namespace mismatch

Fix:
- kubectl get pods -n monitoring
- Check scrape_configs
"""

    return "❌ Monitoring Fix Agent could not identify the issue."
