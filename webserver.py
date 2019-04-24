from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

clas webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/catalog"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "You have landed on the catalog page!"
                output += "</body></html>"
                self.wfile.write(output)
                print (output)


            else:
                self.send_error(404, "File Not Found %s" % self.path)



def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print ("Web server running on port %s" % port)
        server.serve_forever()





    except KeyboardInterrupt:
        print ("^C entered, stopping web server...")
        server.socket.close()







if __name__ == 'main':
    main()
