from whitenoise import WhiteNoise

from supportHeroku import app

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')
