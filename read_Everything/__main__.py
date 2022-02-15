#/usr/bin/python3

# __main__.py

from configparser import ConfigParser
from importlib import resources # Python 3.7+
import sys

from reader import feed
from reader import viewer

def main():

  # Read URL of RealPython.com
  cfg = ConfigParser()
  cfg.read_string(resources.read_text("read_Everything", "config.txt"))
  url = cfg.get("feed", "url")

  # If ID is given, show the article!
  if len(sys.argv) > 1:
    article = feed.get_article(url, sys.argv[1])
    viewer.show(article)

  # If no ID is given, show a list of the articles!
  else:
    site = feed.get_site(url)
    titles = feed.get_titles(url)
    viewer.show_list(site, titles)

if __name__=="__main__":
  main()
