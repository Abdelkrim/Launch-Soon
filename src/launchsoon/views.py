# coding=UTF-8

'''
Created on Apr 9, 2012

@author: Abdelkrim Boujraf
based on https://github.com/JamesChevalier/Launch-Soon
'''

from google.appengine.dist import use_library
use_library('django', '1.3')

from google.appengine.ext import webapp

import os

from settings import *
from models import Interested
from google.appengine.ext import db
 
from google.appengine.ext.webapp import template

__all__ = ['MainPage',
           'SignUp',
           'InviteFriend',
           ]

# A helper to do the rendering and to add the necessary
# variables for the _base.htm template
def doRender(handler, tname = 'index.htm', values = { }):
    temp = os.path.join(
      os.path.dirname(__file__),
      'templates/' + tname)
    if not os.path.isfile(temp):
        return False

    # Make a copy of the dictionary and add the path and session
    newval = dict(values)
    newval['path'] = handler.request.path
    handler.session = Session()
    if 'username' in handler.session:
        newval['username'] = handler.session['username']

    outstr = template.render(temp, newval)
    handler.response.out.write(outstr)
    return True

#Request handlers
class MainPage(webapp.RequestHandler):
        
    def get(self):   
        url_parser = urlparse(self.request.uri)
        host = 'http://%s' % (url_parser[1])    
        template_values = {
            'OG_TITLE' : OG_TITLE,
            'OG_TYPE' : OG_TYPE,
            'OG_URL' : host,
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
        i = Interested(email=db.Email(self.request.get('email')))
        i.put() 
        
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
        
        
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'thank_you.html')
        self.response.out.write(template.render(path, template_values))
    
    def get(self):
        pass
    
class InviteFriend(webapp.RequestHandler):
    def post(self):
        if self.request.get('guest') is None:
            self.redirect("/")
        
        i = Interested(email=db.Email(self.request.get('email')))
        i.put() 
        
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
        
        
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'thank_you.html')
        self.response.out.write(template.render(path, template_values))
    
    def get(self):
        pass
