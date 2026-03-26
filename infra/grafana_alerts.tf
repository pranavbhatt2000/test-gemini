provider "grafana" {
  url  = "https://grafana.internal.example.com"
  auth = data.google_secret_manager_secret_version.grafana_service_account_token.secret_data
}

data "google_secret_manager_secret_version" "grafana_service_account_token" {
  secret  = "grafana-service-account-token"
  project = "moloco-eng-resource"
}

data "google_secret_manager_secret_version" "slack_app_token" {
  secret  = "slack-app-token-moloco-airflow-alerts"
  project = "moloco-eng-resource"
}

locals {
  developers = ["daniel.kim", "jane.doe", "john.smith"]
}

# Create Grafana contact points for Slack DMs to each developer
resource "grafana_contact_point" "developer_slack_dm" {
  for_each = toset(local.developers)

  name = "Slack - ${each.value}"

  slack {
    recipient = each.value
    token     = data.google_secret_manager_secret_version.slack_app_token.secret_data
  }
}

resource "grafana_notification_policy" "dev_alerts" {
  group_by      = ["alertname"]
  contact_point = "Slack - daniel.kim"

  policy {
    matcher {
      label = "severity"
      match = "="
      value = "critical"
    }
    contact_point = "Slack - jane.doe"
  }
}
