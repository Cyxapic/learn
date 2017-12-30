# Простой HTTP сервер
# STL python 3.6

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    '''Обработчик'''
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        tpl = """<html>
                    <head>
                        <meta charset='utf-8'>
                    </head>
                    <body>
                        <h1>Привет! <span>\U0001f600</span></h1>
                        <p>\U00002705 - Сервер работает!</p>
                        <form method="POST">
                            <label>Введите имя
                                <input type="text" name="name">
                            </label>
                            <input type="submit">
                        </form>
                    </body>
                </html>
                """
        self.wfile.write(tpl.encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        name = data.decode().split('=')
        self._set_headers()
        tpl = f"""<html>
                    <head>
                        <meta charset='utf-8'>
                    </head>
                    <body>
                        <h1>Привет {name[1]}! <span>\U0001f600</span></h1>
                        <p>\U00002705 - Сервер работает!</p>
                        <p>\U00002705 - POST данные прилетают!</p>
                    </body>
                  </html>
               """
        self.wfile.write(tpl.encode())


class Server:
    server_address = ('localhost', 8080)
    handler = Handler

    def __init__(self):
        self.httpd = HTTPServer(self.server_address, self.handler)

    def run(self):
        print(f'Запущен сервер {self.server_address[0]}:{self.server_address[1]}')
        self.httpd.serve_forever()

    def stop(self):
        print("Останавливаю сервер! Пока!")
        self.httpd.shutdown()
        self.httpd.server_close()


if __name__ == "__main__":
    server = Server()
    try:
        server.run()
    except KeyboardInterrupt:
        server.stop()
