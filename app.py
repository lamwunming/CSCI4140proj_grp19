#! /usr/bin/env python

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# https://docs.python.org/2/library/basehttpserver.html
# https://docs.python.org/2/library/cgihttpserver.html
import os
# import BaseHTTPServer
from http.server import CGIHTTPRequestHandler, HTTPServer
# import CGIHTTPServer
import webbrowser

PORT = 8080
#TODO: check that port is available,
# and look for a different one if it isn't.

# server_class = BaseHTTPServer.HTTPServer
# handler_class = CGIHTTPServer.CGIHTTPRequestHandler
server_class = HTTPServer
handler_class = CGIHTTPRequestHandler
server_address = ("", PORT)

httpd = server_class(server_address, handler_class)

print("start server.......")

httpd.serve_forever()
