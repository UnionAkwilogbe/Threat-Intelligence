"""Optional: email the morning brief.

Only runs when SMTP settings are present as environment variables (set them
as GitHub Actions secrets). Nothing is sent otherwise.

For Gmail you only need two secrets:
  SMTP_USER      your Gmail address
  SMTP_PASSWORD  a Gmail app password (not your normal password)

Optional: SMTP_HOST (default smtp.gmail.com), SMTP_PORT (default 587),
BRIEF_TO (comma separated, defaults to SMTP_USER), BRIEF_FROM.

The email body is the brief as simple HTML (with a plain text fallback), and
the full dashboard is attached as an .html file you can open on any device.
"""

import html
import os
import re
import smtplib
from email.message import EmailMessage


def email_configured():
    return all(os.environ.get(k) for k in ("SMTP_USER", "SMTP_PASSWORD"))


def _inline(text):
    """Escape, then turn **bold**, _italic_ and [text](url) into HTML."""
    text = html.escape(text, quote=True)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"<i>\1</i>", text)
    return re.sub(r"\[(.+?)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', text)


def markdown_to_html(md):
    """Just enough Markdown for the brief: headings, lists, quotes, rules, paragraphs."""
    out, in_ul, in_ol = [], False, False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
        if in_ol:
            out.append("</ol>")
        in_ul = in_ol = False

    for line in md.splitlines():
        s = line.rstrip()
        m_ol = re.match(r"^\d+\. (.*)", s)
        if s.startswith("- "):
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{_inline(s[2:])}</li>")
            continue
        if m_ol:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{_inline(m_ol.group(1))}</li>")
            continue
        close_lists()
        if not s:
            continue
        if s.startswith("#"):
            level = min(len(s) - len(s.lstrip("#")), 3)
            out.append(f"<h{level}>{_inline(s.lstrip('#').strip())}</h{level}>")
        elif s.startswith("> "):
            out.append(f'<blockquote style="margin:8px 0;padding:8px 12px;background:#eef3fd;'
                       f'border-left:4px solid #1d4ed8">{_inline(s[2:])}</blockquote>')
        elif s == "---":
            out.append("<hr>")
        else:
            out.append(f"<p>{_inline(s)}</p>")
    close_lists()
    return ('<div style="font:15px/1.55 -apple-system,Segoe UI,Roboto,sans-serif;max-width:680px;'
            'color:#14171c">' + "\n".join(out) + "</div>")


def send_brief(subject, markdown_body, dashboard_html="", attachment_name="threat-brief.html",
               dashboard_url=""):
    if not email_configured():
        return False
    user = os.environ["SMTP_USER"]
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ.get("BRIEF_FROM") or user
    msg["To"] = os.environ.get("BRIEF_TO") or user
    intro = "The full interactive dashboard is attached. Open the .html file to view it.\n\n"
    if dashboard_url:
        intro = f"Full dashboard: {dashboard_url}\n\n"
    msg.set_content(intro + markdown_body)
    msg.add_alternative(markdown_to_html(intro + markdown_body), subtype="html")
    if dashboard_html:
        msg.add_attachment(dashboard_html.encode("utf-8"), maintype="text", subtype="html",
                           filename=attachment_name)
    host = os.environ.get("SMTP_HOST") or "smtp.gmail.com"
    port = int(os.environ.get("SMTP_PORT") or "587")
    with smtplib.SMTP(host, port, timeout=30) as smtp:
        smtp.starttls()
        smtp.login(user, os.environ["SMTP_PASSWORD"])
        smtp.send_message(msg)
    return True
