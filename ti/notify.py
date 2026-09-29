"""Optional: email the morning brief.

Only runs when SMTP settings are present as environment variables (set them
as GitHub Actions secrets). Nothing is sent otherwise.

  SMTP_HOST, SMTP_PORT (default 587), SMTP_USER, SMTP_PASSWORD,
  BRIEF_TO (comma separated), BRIEF_FROM (defaults to SMTP_USER)
"""

import os
import smtplib
from email.message import EmailMessage


def email_configured():
    return all(os.environ.get(k) for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD", "BRIEF_TO"))


def send_brief(subject, markdown_body, dashboard_url=""):
    if not email_configured():
        return False
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ.get("BRIEF_FROM") or os.environ["SMTP_USER"]
    msg["To"] = os.environ["BRIEF_TO"]
    body = markdown_body
    if dashboard_url:
        body = f"Full dashboard: {dashboard_url}\n\n{body}"
    msg.set_content(body)
    port = int(os.environ.get("SMTP_PORT", "587"))
    with smtplib.SMTP(os.environ["SMTP_HOST"], port, timeout=30) as smtp:
        smtp.starttls()
        smtp.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
        smtp.send_message(msg)
    return True
