import webapp2

app = webapp2.WSGIApplication([
								('/', 'views.Home'),
								('/new/?', 'views.New'),
								('/logout/?', 'views.Logout'),
								('/signup/?', 'views.Signup'),
							], debug=True)