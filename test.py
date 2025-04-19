import tornado.web
import tornado.ioloop
import json


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world this is a python command from tornado")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class fruitListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")

        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(fruit + "\n")
        fh.close()
        self.write(json.dumps({"status": "success", "fruit": fruit}))q


class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, student_name, courseId):

        self.write(f"Welcome {student_name}, you are viewing courseId{courseId} .")


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
            (r"/fruits", fruitListRequestHandler),
            (r"/isEven", queryParamRequestHandler),
            (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        ]
    )
    port = 8865
    app.listen(port)
    print(f"app is ready and listering on prot {port}")
    tornado.ioloop.IOLoop.current().start()
