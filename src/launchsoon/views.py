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
from google.appengine.ext.webapp import template

__all__ = ['MainPage', 
           ]
#Request handlers
class MainPage(webapp.RequestHandler):
        
    def get(self):       
        title = 'MainPage'
        signin_signout_text = 'Sign in'
        login_logout_url = users.create_login_url("/")
        
        user = users.get_current_user()
        if user: 
            owner_email = users.get_current_user().email()
            signin_signout_text = 'Sign out'
            login_logout_url = users.create_logout_url("/")
        else:
            owner_email = "guest user"
            
        template_values = {
            'title': title,
            'owner_email': urllib.urlencode(''),
            'login_logout_url': login_logout_url,
            'signin_signout_text' : signin_signout_text ,
            'nickname': owner_email,
        }
        
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'interested_launchrock.html')
        self.response.out.write(template.render(path, template_values))
            