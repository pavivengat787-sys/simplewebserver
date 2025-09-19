from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>device</title>
    </head>   
    <body>
        <h1>Device specification = 25017909</h1>
        <table border="1">
            <tr>
                <th>s.no</th>
                <th>device specification</th>
                <th>propertice</th>
            </tr>
            <tr>
                <td>1</td>
                <td>storage</td>
                <td>945 GB</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Graphics card</td>
                <td>128 MB</tb>
            </tr>
            <tr>
                <td>3</td>
                <td>installed ram</td>
                <td>16.0</td>
             </tr>
            <tr>
                <td>4</td>
                <td>processor</td>
                <td>5125H</td>
            </tr>
            <tr>
                <td>5</td>
                <td>device name</td>
                <td>TMP215-75-G2</td>
            </tr>
        </table>
     </body> 
 </html>                          
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()