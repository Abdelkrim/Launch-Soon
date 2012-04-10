'''
Created on Apr 9, 2012

@author: abdelkrim boujraf

    - Table name 'interested'

'''

class interested(db.Model):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''

    email = db.StringProperty(indexed=False)
    joined = db.DateTimeProperty(auto_now_add=True,verbose_name='first time user login',indexed=False)
            
    #firstname = db.StringProperty()
    #lastname = db.StringProperty()
    #hash = db.StringProperty(indexed=False)
    #invites
    #googleID = db.StringProperty(indexed=False)
    
