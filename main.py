#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

michiganLink = "Michigan"
basketballLink = "Basketball"
nikeLink = "Nike"
loginLink = "Login"
michiganPath = "/michigan.html"
basketballPath = "/basketball.html"
nikePath = "/nike.html"
loginMessage = "Login...I bet you can't guess the password"
correctLoginMessage = "You logged in"
michiganMessage = "WHADDUP UMICH!!!"
basketballMessage = "WHADDUP LEBRON!!!"
nikeMessage = "SWOOSH!!!"

class MainHandler(webapp2.RequestHandler):
    def get(self):

        currentPath = self.request.path

        try:
            template = JINJA_ENVIRONMENT.get_template('templates' + currentPath)

            if currentPath == michiganPath:
               self.response.write(template.render({'title': michiganMessage, 'michigan': michiganLink.upper(), 'basketball': basketballLink, 'nike': nikeLink, 'login': loginLink} ) )

            if currentPath == basketballPath:
               self.response.write(template.render({'title': basketballMessage, 'michigan': michiganLink, 'basketball': basketballLink.upper(), 'nike': nikeLink, 'login': loginLink} ) )

            if currentPath == nikePath:
               self.response.write(template.render({'title': nikeMessage, 'michigan': michiganLink, 'basketball': basketballLink, 'nike': nikeLink.upper(), 'login': loginLink} ) )

        except:
            logging.info(currentPath)
            template = JINJA_ENVIRONMENT.get_template('templates/michigan.html')
            self.response.write(template.render({'title': michiganMessage, 'michigan': michiganLink.upper(), 'basketball': basketballLink, 'nike': nikeLink, 'login': loginLink} ) )



class LoginPageHandler(webapp2.RequestHandler):
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': loginMessage, 'michigan': michiganLink, 'basketball': basketballLink, 'nike': nikeLink, 'login': loginLink.upper()}))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/loginAfter.html')

        inputUsername = self.request.get('name')
        inputPassword = self.request.get('pw')

        if (inputUsername != "Colleen") or (inputPassword != "pass"):
            logging.info("************* " + inputUsername + " *************")
            logging.info("************* " + inputPassword + " *************")
            self.response.write(template.render({'title': loginMessage, 'michigan': michiganLink, 'basketball': basketballLink, 'nike': nikeLink, 'login': loginLink.upper(), 'checkUsername': inputUsername, 'checkPassword': inputPassword}))

        else:
            self.response.write(template.render({'title': correctLoginMessage, 'michigan': michiganLink, 'basketball': basketballLink, 'nike': nikeLink, 'login': loginLink.upper(), 'checkUsername': inputUsername, 'checkPassword': inputPassword}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login.html', LoginPageHandler),
    ('/login', LoginPageHandler),
    ('/.*', MainHandler)
], debug=True)
