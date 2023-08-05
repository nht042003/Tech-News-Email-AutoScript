import datetime
import schedule
import time

from web_scraping import scrape_rss_feed
from email_sender import send_email, send_daily_news_summary

if __name__ == "__main__":
    websites = {
        'TechCrunch': 'https://techcrunch.com/feed/',
        'Artificial Intelligence News': 'https://www.artificialintelligence-news.com/feed/',
        'The Verge': 'https://www.theverge.com/rss/index.xml',
        'TechRadar': 'https://www.techradar.com/rss'
    }

    email_addresses = 'nht042003@gmail.com'#,syonlee1@gmail.com'
    subject = 'Latest Technology News Summary - ' + str(datetime.date.today())

    email_body = "<h2>Latest Technology News Summary</h2>"

    for website, url in websites.items():
        email_body += f"<h3>{website}</h3>"
        article_data = scrape_rss_feed(url)
        for idx, article in enumerate(article_data, 1):
            email_body += f"<p><strong>{idx}. {article['title']}</strong></p>"
            email_body += f"<p>{article['summary']}</p>"
            email_body += "<hr>"

    send_email(email_addresses, subject, email_body)

    # Schedule the script to run at 8:00 AM and 8:00 PM Eastern time
    schedule.every().day.at("08:00").do(send_daily_news_summary)
    schedule.every().day.at("20:00").do(send_daily_news_summary)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for 1 minute before checking the schedule again