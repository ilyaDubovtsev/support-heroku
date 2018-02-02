from whitenoise import WhiteNoise

from support_heroku import app

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')
