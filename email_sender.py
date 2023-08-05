import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from web_scraping import scrape_rss_feed

def send_email(to_email, subject, body):
    # Email configuration
    from_email = 'nht042003@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'nht042003@gmail.com'
    smtp_password = 'qjfymkqjajjaprya'  # Generate app password in Gmail settings

    # Create a multipart message
    recipients = to_email.split(',')

    for recipient in recipients:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = recipient.strip()
        msg['Subject'] = subject

        # Add HTML body to the message
        msg.attach(MIMEText(body, 'html'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)


def send_daily_news_summary():
    # Replace 'recipient1@example.com,recipient2@example.com' with the intended recipients' Gmail addresses separated
    # by commas
    email_addresses = 'nht042003@gmail.com'
    subject = 'Latest Technology News Summary - ' + str(datetime.date.today())

    email_body = "<h2>Latest Technology News Summary</h2>"

    websites = {
        'TechCrunch': 'https://techcrunch.com/feed/',
        'Artificial Intelligence News': 'https://www.artificialintelligence-news.com/feed/',
        'The Verge': 'https://www.theverge.com/rss/index.xml',
        'TechRadar': 'https://www.techradar.com/rss'
    }

    for website, url in websites.items():
        email_body += f"<h3>{website}</h3>"
        article_data = scrape_rss_feed(url)
        for idx, article in enumerate(article_data, 1):
            email_body += f"<p><strong>{idx}. {article['title']}</strong></p>"
            email_body += f"<p>{article['summary']}</p>"
            email_body += "<hr>"

    # Send the email to the specified recipients
    send_email(email_addresses, subject, email_body)
