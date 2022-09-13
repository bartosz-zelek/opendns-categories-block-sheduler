# opendns-categories-block-sheduler
<p>Program pozwala na blokowanie i odblokowywanie konkretnych kategorii stron o określonych godzinach w ciągu dnia. Możliwe jest wstawienie kodu na np. Heroku.com (strefa czasowa 2 godziny do tyłu w PL) skąd będą wykonywane zmiany. Wykorzystano moduł Selenium.</p>
<br>
--- ENG ---

<p>A program let you block und unblock specific pages categories at specific hours everyday. You can insert a code on e.g. Heroku.com (time on Heroku server can be different than yours) where changes will be insert. There is used Selenium module.</p>


<p>Download and install the Heroku CLI and GIT.</p>

<p>
  
  In CLI:

  $ heroku login
  
  $ cd my-project/

  $ git init

  $ heroku git:remote -a your_heroku_app_name

  $ heroku buildpacks:add heroku/python

  $ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome#selenium

  $ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver

  $ git add .

  $ git commit -am "initial commit"

  $ git push heroku master

</p>
<br>
<p>
  Go to Heroku app settings and add Config Vars:

  EMAIL                  your_email_on_login.opendns.com

  PASSWORD               your_password_on_login.opendns.com

  CHROMEDRIVER_PATH      /app/.chromedriver/bin/chromedriver

  GOOGLE_CHROME_BIN      /app/.apt/usr/bin/google-chrome

  ------------- ONLY IF PROBLEM WITH CHROME VERSION -------------
  
  GOOGLE_CHROME_CHANNEL  beta
  
  --------------------- MAYBE IT WILL HELP ----------------------
  
</p>
<br>
<p>
  Make sure in Heroku > your_app > Resources, worker is set to ON.
</p>
<br>
<p>
  In loop at the and you can change block/unblock hours.
  Here categories unlock at 22:00 (0:00 w Polsce) and block at 5:50 (7:50 w Polsce).
  You can personalize it and make it more detail, because object 'now' has attributes like now.year, now.month, now.day,    now.hour, now.minute, now.second.
</p>
