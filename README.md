# scrape_mediawiki_and_import_to_bookstack
A script using Python Beautiful Soup to scrape a local mediawiki, create list, and insert them into a "BOOK" in Bookstack!


# Todo Ideas...

app.py --- This code will first scrape all of the article titles from your local MediaWiki. It will then create a Bookstack object and connect to Bookstack. Finally, it will import all of the articles into Bookstack.

xml dump --- you can dump the mediawiki database via: 
```
 cd /opt/OURMAINWiki/maintenance/ ; php dumpBackup.php --full > dump_latest.xml
```

Then use pandoc to somehow convert this to a bunch of ".md" files, which we can loop over and add as "pages" to a new book in bookstack... (No idea?)
