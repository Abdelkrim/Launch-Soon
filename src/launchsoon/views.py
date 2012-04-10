# coding=UTF-8

'''
Created on Apr 9, 2012

@author: Abdelkrim Boujraf
based on https://github.com/JamesChevalier/Launch-Soon
'''

from google.appengine.dist import use_library
use_library('django', '1.3')

from google.appengine.ext import webapp
from google.appengine.api import users
import urllib
import os
from settings import *
 
from google.appengine.ext.webapp import template

__all__ = ['MainPage',
           'SignUp',
           ]
#Request handlers
class MainPage(webapp.RequestHandler):
        
    def get(self):       
        template_values = {
            'OG_TITLE' : OG_TITLE,
            'OG_TYPE' : OG_TYPE,
            'OG_URL' : OG_URL,
            'OG_IMAGE' : OG_IMAGE,
            'OG_IMAGE_TYPE' : OG_IMAGE_TYPE,
            'OG_IMAGE_WIDTH' : OG_IMAGE_WIDTH,
            'OG_IMAGE_HEIGHT' : OG_IMAGE_HEIGHT,
            'OG_DESCRIPTION' : OG_DESCRIPTION,
            'OG_SITE_NAME': OG_SITE_NAME,
        }
        
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'index.html')
        self.response.out.write(template.render(path, template_values))

class SignUp(webapp.RequestHandler):
    def post(self):
        pass
    def get(self):
        pass  