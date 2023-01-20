import cherrypy

class Countdown(object):
    @cherrypy.expose
    def index(self):
        return '''
            <html>
                <body>
                    <form method="get" action="countdown">
                        <input type="submit" value="Start Countdown"/>
                    </form>
                    <div id="timer"></div>
                    <script>
                        function countdown() {
                            var seconds = 10;
                            var timer = setInterval(function() {
                                seconds--;
                                document.getElementById("timer").innerHTML = seconds;
                                if (seconds == 0) {
                                    clearInterval(timer);
                                }
                            }, 1000);
                        }
                    </script>
                </body>
            </html>
        '''

    @cherrypy.expose
    def countdown(self):
        return '''
            <html>
                <body onload="countdown()">
                    <form method="get" action="countdown">
                        <input type="submit" value="Start Countdown"/>
                    </form>
                    <div id="timer"></div>
                    <script>
                        function countdown() {
                            var seconds = 10;
                            var timer = setInterval(function() {
                                seconds--;
                                document.getElementById("timer").innerHTML = seconds;
                                if (seconds == 0) {
                                    clearInterval(timer);
                                }
                            }, 1000);
                        }
                    </script>
                </body>
            </html>
        '''

if __name__ == '__main__':
    cherrypy.quickstart(Countdown())