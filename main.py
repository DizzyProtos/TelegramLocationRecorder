import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web
from misc import bot, db_service
import Handlers
import json
import constants
import tornado.options
from tornado.options import define
define("port", default=5000, help="run on the given port", type=int)


class LocationsHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')

    def get(self):
        all_locations = db_service.get_all_locations()
        dicts_locations = [x.__dict__ for x in all_locations]
        self.write(json.dumps(dicts_locations))

    def options(self):
        self.set_status(204)
        self.finish()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        port = tornado.options.options.port
        self.render('./templates/index.html')


# application settings and handle mapping info
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/locations", LocationsHandler),
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()
    # bot.polling()
