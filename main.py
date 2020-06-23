from misc import bot, db_service
import Handlers
import tornado.ioloop
import tornado.web
import json


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


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('./templates/index.html')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/locations', LocationsHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    bot.polling()
