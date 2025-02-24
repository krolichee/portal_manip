import tornado.ioloop

import tornado.web

import tornado.websocket


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):

        print("WebSocket opened")


    def on_message(self, message):

        print(f"Received message: {message}")

        # Эхо-ответ

        self.write_message(f"You said: {message}")


    def on_close(self):

        print("WebSocket closed")


    def check_origin(self, origin):

        # Разрешаем все источники (для разработки)

        return True


def make_app():

    return tornado.web.Application([
        (r"/ws", WebSocketHandler),])


if __name__ == "__main__":

    app = make_app()

    app.listen(8765)

    print("WebSocket server started on ws://localhost:8765/ws")

    tornado.ioloop.IOLoop.current().start()