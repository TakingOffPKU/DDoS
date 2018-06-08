import re
from http.server import BaseHTTPRequestHandler
from io import StringIO
import urllib


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = bytes(request_text, 'utf-8')
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


# request_text = (
#     'GET /who/ken/trust.html HTTP/1.1\r\n'
#     'Host: cm.bell-labs.com\r\n'
#     'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n'
#     'Accept: text/html;q=0.9,text/plain\r\n'
#     '\r\n'
# )

request_text = ('GET /course/jiaoxuewang/images/video/rang.jpg HTTP/1.1\r\n'
                'Host: courseweb.pku.edu.cn\r\n'
                'Connection: keep-alive\r\n'
                'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\r\n'
                'Accept: image/webp,image/apng,image/*,*/*;q=0.8\r\n'
                'Referer: http://courseweb.pku.edu.cn/course/EditorAction.do?dispatch=jiaoxuewangIndexInit&course_id_4jiaoxuewangvideo=104&longa=3&editor_view=jiaoxuewang&page_suffix=_bb9\r\n'
                'Accept-Encoding: gzip, deflate\r\n'
                'Accept-Language: zh-CN,zh;q=0.9'
                'Cookie: JSESSIONID=E0B12B7E634885D72DB56E685EE141CA; UM_distinctid=1623ccadfb83ce-01c5b1a1f367f6-b353461-144000-1623ccadfb943c\r\n'
                '\r\n')

request = HTTPRequest(request_text)
print(request)
print(request.request_version)
print(request.command)

