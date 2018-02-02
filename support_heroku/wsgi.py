from whitenoise import WhiteNoise

from support-heroku import app

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')
