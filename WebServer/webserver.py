# create a simple web server

import SimpleHTTPServer
import SocketServer

# create an event handler
evtHandler = SimpleHTTPServer.SimpleHTTPRequestHandler

# create the server
myhttpserver = SocketServer.TCPServer(("0.0.0.0", 8080), evtHandler)

print "Server Running... (Ctrl-c to stop)"

myhttpserver.serve_forever()