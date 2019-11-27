from pyg.web import plugin



web = None

def init(app):
    global web
    web = plugin.SQLAlchemy(app, "postgresql://coffee:wildseven@localhost:5432/coffee")
