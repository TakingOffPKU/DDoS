import re
from http.server import BaseHTTPRequestHandler
from io import StringIO
import urllib
import time

TIME_INTERVAL = 1
TIME_COUNTS = 20


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = bytes(request_text, 'utf-8')
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


class Timer:
    def __init__(self):
        self.time_buffer = []

    def new_access(self):
        cur_time = time.time()
        ori_len = len(self.time_buffer)
        if ori_len >= TIME_COUNTS:
            self.time_buffer.pop(0)
        self.time_buffer.append(cur_time)

    def is_abnormal(self):
        return len(self.time_buffer) >= TIME_COUNTS and (self.time_buffer[-1] - self.time_buffer[0]) < TIME_INTERVAL


class HTTPFilter:
    def __init__(self):
        self.timer_map = {}
        self.black_list = {}

    def is_abnormal(self, src):
        if self.black_list[src] >= 3:
            return True

        if src not in self.timer_map.keys():
            self.timer_map[src] = Timer()

        timer = self.timer_map[src]
        timer.new_access()
        result = timer.is_abnormal()
        if result:
            self.black_list[src] += 1
        return result
