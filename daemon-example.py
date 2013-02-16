#!/usr/bin/env python

import sys, time, symmetricjsonrpc, socket
from daemon import Daemon

class PongRPCServer(symmetricjsonrpc.RPCServer):
  class InboundConnection(symmetricjsonrpc.RPCServer.InboundConnection):
    class Thread(symmetricjsonrpc.RPCServer.InboundConnection.Thread):
      class Request(symmetricjsonrpc.RPCServer.InboundConnection.Thread.Request):
        def dispatch_notification(self, subject):
          assert subject['method'] == "shutdown"
          # Shutdown the server. Note: We must use a
          # notification, not a method for this - when the
          # server's dead, there's no way to inform the
          # client that it is...
          symmetricjsonrpc.ShutDownThread(self.parent.parent.parent)

        def dispatch_request(self, subject):
          assert subject['method'] == "ping"
          # Call the client back
          # self.parent is a symmetricjsonrpc.RPCClient subclass (see the client code for more examples)
          assert self.parent.request("pingping", wait_for_response=True) == "pingpong"
          return "pong"


class MyDaemon(Daemon):
  def run(self):
    # Set up a TCP socket and start listening on it for connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 4712))
    s.listen(1)

    # Create a server thread handling incoming connections
    server = PongRPCServer(s, name="PongServer")

    # Wait for the server to stop serving clients
    server.join()

if __name__ == "__main__":
  daemon = MyDaemon('/tmp/daemon-example.pid')
  if len(sys.argv) == 2:
    if 'start' == sys.argv[1]:
      daemon.start()
    elif 'stop' == sys.argv[1]:
      daemon.stop()
    elif 'restart' == sys.argv[1]:
      daemon.restart()
    else:
      print "Unknown command"
      sys.exit(2)
    sys.exit(0)
  else:
    print "usage: %s start|stop|restart" % sys.argv[0]
    sys.exit(2)
