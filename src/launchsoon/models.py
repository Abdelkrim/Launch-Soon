'''
Created on Apr 9, 2012
@author: abdelkrim boujraf
'''

from google.appengine.ext import db

class Interested(db.Model):
    '''
    People who are interested by the experience.
    We collect their email address and will contact them as soon as the project is ready for a Beta test

USAGE within the Interactive Console: http://localhost:XXXX/_ah/admin/interactive

from google.appengine.ext import db

interested_list = db.GqlQuery("SELECT * FROM Interested")

for interested in interested_list:
    print interested.email
    '''

    email = db.EmailProperty(required=True)
    joined = db.DateTimeProperty(auto_now_add=True,verbose_name='first time user login')
