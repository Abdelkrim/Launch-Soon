'''
Created on Apr 9, 2012

@author: abdelkrim boujraf

    - Table name 'interested'
    - Field 'id' (bigint(20)?)
    - Field 'email' (varchar(1000)?)
    - Field 'hash' (varchar(8)?)
    - Field 'invites' (int(20)?)
    - The 'id' field must be set to auto-increment
    - The 'hash' field must be set as unique
    
'''

class interested(db.Model):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''
        
    firstname = db.StringProperty()
    lastname = db.StringProperty()
    email = db.StringProperty(indexed=False)
    hash = db.StringProperty(indexed=False)
    invites
    googleID = db.StringProperty(indexed=False)
    joined = db.DateTimeProperty(auto_now_add=True,verbose_name='first time the user logged',indexed=False)
