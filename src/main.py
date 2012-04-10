from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import logging 
import os

from launchsoon.views import *

logging.getLogger().setLevel(logging.DEBUG)
    
# Log a message each time this module get loaded.
logging.info('Loading %s, app version = %s',
             __name__, os.getenv('CURRENT_VERSION_ID'))

application = webapp.WSGIApplication([('/', MainPage),
                                      ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
