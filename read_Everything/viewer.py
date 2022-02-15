# viewer.py

def show(article):
  # Only show one article
  print(article)

def show_list(site, titles):
  # Show the list of articles
  print(f"These are the latest from {site}")
  for article_id, title in enumerate(titles):
    print(f"{article_id: > 3} {title}")
