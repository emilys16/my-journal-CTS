AUTHOR = 'Emily Scott'
SITENAME = 'Portfolio'
SITEURL = "https://emilys16.github.io/my-journal-CTS"
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

PATH = "content"

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# COPY AND PASTED STUFF
THEME = 'themes/pelican-hyde-master'
PROFILE_IMAGE = "DrawnProfile.png" 
BIO = "A journal about Capybara Life."

# Save pages at the top level instead of /pages/
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

TAG_URL = '/tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ("Home", SITEURL + "/"),
    ("About", SITEURL + "/about.html"),
    ("Issue 1", SITEURL + "/category/issue-1.html"),
    ("Issue 2", SITEURL + "/category/issue-2.html"),
    ("CTS1000", SITEURL + "/category/CTS1000.html"),
    ("CTS2000", SITEURL + "/category/CTS2000.html"),
    ("ENGL3010", SITEURL + "/category/ENGL3010.html"),
    ("Tags", SITEURL + "/tags.html"),
]

# Social widget 

SOCIAL = ( 
("email", "capybarajourno@gmail.com"), 
("github", "https://github.com/cmiya"), 
("bluesky", "https://bsky.app/"), 
("linkedin", "https://www.linkedin.com/"),
)




# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
