import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world this is a python command from tornado")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            num = int(num)
            if num % 2 == 0:
                self.write(f"{num} is even")
            else:
                self.write(f"{num} is odd")
        else:
            self.write(f"{num} is not a number, Please provide a valid number.")


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", basicRequestHandler),
            (r"/animal", listRequestHandler),
            (r"/isEven", queryParamRequestHandler),
        ]
    )
    port = 8865
    app.listen(port)
    print(f"app is ready and listering on prot {port}")
    tornado.ioloop.IOLoop.current().start()
