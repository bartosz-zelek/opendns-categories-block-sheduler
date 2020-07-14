# opendns-categories-block-sheduler
Program pozwala na blokowanie i odblokowywanie konkretnych kategorii stron o określonych godzinach w ciągu dnia. Możliwe jest wstawienie kodu na np. Heroku.com (strefa czasowa 2 godziny do tyłu w PL) skąd będą wykonywane zmiany. Wykorzystano moduł Selenium.
--- ENG ---
A program let you block und unblock specific pages categories about specific hours everyday. You can insert a code on e.g. Heroku.com (time on Heroku server can be different than yours) where changes will be insert. There is used Selenium module.


Download and install the Heroku CLI and GIT.

In CLI:
$ heroku login
$ cd my-project/
$ git init
$ heroku git:remote -a thatsatest
$ heroku buildpacks:add heroku/python
$ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome#selenium
$ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver
$ git add .
$ git commit -am "initial commit"
$ git push heroku master

Go to Heroku app settings and add Config Vars:
EMAIL                  your_email_on_login.opendns.com
PASSWORD               your_password_on_login.opendns.com
CHROMEDRIVER_PATH      /app/.chromedriver/bin/chromedriver
GOOGLE_CHROME_BIN      /app/.apt/usr/bin/google-chrome
chromedriver           /app/.chromedriver/bin/chromedriver
