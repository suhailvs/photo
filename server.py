#!/usr/bin/env python

'''
Based on https://gist.github.com/chrisbolin/2e90bc492270802d00a6
'''

from http.server import SimpleHTTPRequestHandler
import socketserver as SocketServer

PORT = 8010
httpd = SocketServer.TCPServer(("", PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()

