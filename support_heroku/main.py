import os

from support-heroku import app


if __name__ == '__main__':
    app.debug = True
    app.run()
