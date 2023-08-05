import feedparser
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')


def clean_html_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    # Remove any image tags
    for img_tag in soup.find_all('img'):
        img_tag.extract()

    return soup.get_text()


def get_summary_sentences(text, num_sentences=3):
    sentences = sent_tokenize(text)
    return ' '.join(sentences[:num_sentences])


def scrape_rss_feed(url):
    article_data = []

    # Parse the RSS feed
    feed = feedparser.parse(url)

    for entry in feed.entries[:3]:  # Get the three latest articles
        title = clean_html_tags(entry.title).strip()
        summary = clean_html_tags(entry.summary).strip()
        summary = get_summary_sentences(summary, num_sentences=3)

        article_data.append({"title": title, "summary": summary})

    return article_data