import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

donor_key = ndb.Key('Donate', 'default_donors')

class Donor(ndb.Model):
  place = ndb.TextProperty()
  contact = ndb.TextProperty()
  blood = ndb.TextProperty()




class Donate(webapp2.RequestHandler):
  def post(self):
    donor = Donor(parent=donor_key)

    donor.place = self.request.get('place')
    donor.contact = self.request.get('contact')
    donor.blood = self.request.get('blood')

    
    donor.put()
    self.redirect('/')


app = webapp2.WSGIApplication([
								('/', 'views.Home'),
								('/donate', Donate),
								('/new/?', 'views.New'),
								('/logout/?', 'views.Logout'),
								('/signup/?', 'views.Signup'),
							], debug=True)