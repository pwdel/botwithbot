import cherrypy

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return "Hello, World!"

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), '/', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 8080}})