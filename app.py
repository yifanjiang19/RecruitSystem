import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import models
from tornado.options import define, options

from database import Base,db_session,engine

define("port", default=8000, help="run on the given port", type=int)

#api
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="POST">'
                   '<input type="text" name="name">'
                   '<input type="text" name="phone">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        asd = models.User(name=self.get_argument("name"),
                          phone=self.get_argument("phone"))
        db_session.add(asd)
        db_session.commit()
class Test(tornado.web.RedirectHandler):
    def post(self):
        return 0


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler),
                                            (r"/asd",Test)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()