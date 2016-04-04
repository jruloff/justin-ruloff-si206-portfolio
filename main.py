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
#import smtplib
from google.appengine.api import mail

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render())

class EducationHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/education.html')
        self.response.write(template.render())

class ProjectsHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        self.response.write(template.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render())

    def post(self):
        userFirstName = self.request.get("firstName")
        userLastName = self.request.get("lastName")
        userEmail = self.request.get("emailAddr")

        if not mail.is_email_valid(userEmail):
            logging.info("Bad email")

        else:
            senderAddr = "Justin Ruloff <justinruloff@gmail.com>"
            subject = "Thanks for Subscribing!"
            body = "Hi, " + userFirstName + "!" + """ Thanks for subscribing to my life. I won't update you."""

            mail.send_mail(senderAddr,userEmail,subject,body)
        
        #message = "Hey, Thanks for subscribing! I probably won't keep you updated. I'm e-mailing you on one of my throwaway accounts, because this probably isn't very safe."
        #mail = smtplib.SMTP('smtp.gmail.com', 587)
        #mail.ehlo()
        #mail.starttls()
        #mail.login('justinruloffalt@gmail.com','hahapwn3d')
        #mail.sendmail('justinruloffalt@gmail.com',userEmail,message)

        #mail.close()

app = webapp2.WSGIApplication([
    ('/', AboutHandler),
    ('/about.html', AboutHandler),
    ('/education.html', EducationHandler),
    ('/work.html', ProjectsHandler),
    ('/contact.html', ContactHandler)
], debug=True)
