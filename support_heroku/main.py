import os

from supportHeroku import app


if __name__ == '__main__':
    app.debug = True
    app.run()
