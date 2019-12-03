#! /usr/bin/env python3

from flask import Flask, send_file, request
import os
import asyncio
import 锟斤拷生成器
os.chdir(os.path.abspath(os.path.dirname(__file__)))
app = Flask(__name__)

@app.route('/')
def index():
    return send_file('web/index.html')

@app.route('/gen', methods=['POST'])
def shorten():
    try:
        length = int(request.json['length'])
        if length > 4096 or length < 0: raise ValueError()
        with_symbol = request.json['with_symbol'] in [ True, 'True', 'true' ]
        锟斤拷 = 锟斤拷生成器.生成锟斤拷(length, with_symbol, True)
        return 锟斤拷
    except Exception:
        return "", 500

def start_app(app):
    asyncio.set_event_loop(asyncio.new_event_loop())
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8233, address='0.0.0.0')
    IOLoop.instance().start()

if __name__ == "__main__":
    debug = '--debug' in os.sys.argv
    if debug:
        app.run(host='127.0.0.1', port=8233, debug=debug)
    else:
        start_app(app)
