import requests
import random
import json
import time


class ProxyRequest(object):
    @staticmethod
    def generate_ip_list():
        # Source of IP addresses
        source = "https://spys.me/socks.txt"

        ip_data = requests.get(source).text

        ip_data = ip_data.strip()
        ip_tmp_list = ip_data.split("\n")

        ip_list = []

        # Strip the intro from txt
        ip_tmp_list = ip_tmp_list[6:]
        for row in ip_tmp_list:
            # Only add High Anonymity servers
            if "-H" in row:
                row = row.split(" ")[0]
                ip_list.append(row)

        return ip_list

    def update_ip_list(self):
        while True:
            # Check if 30mins have passed since last update
            if time.time() - self.last_update > 1800:
                # Update IP list
                self.ip_list = ProxyRequest.generate_ip_list()
                # Update last_update to now
                self.last_update = time.time()
                # Go to sleep to not check every microsecond
                time.sleep(60)

    # comment
    def __init__(self):
        self.ip_list = ProxyRequest.generate_ip_list()
        self.lastidx = []
        self.range = list(range(0, len(self.ip_list)))
        self.last_update = time.time()
        self.update = self.update_ip_list()

    def get_idx(self):
        # When list of indices is empty, create a new one
        if len(self.range) == 0:
            self.range = list(range(0, len(self.ip_list)))
        # Pop first element & return it
        idx = self.range.pop(0)
        return idx

    def get(self, url, headers=None, throttle=None):
        idx = self.get_idx()
        proxies = {"socks": f"socks5://{self.ip_list[idx]}"}
        session = requests.session()
        session.proxies.update(proxies)
        try:
            response = session.get(url, headers=headers, proxies=proxies)
        except:
            response = requests.Response()
            response.status_code = 403

        if throttle:
            time.sleep(random.uniform(throttle * 0.8, throttle * 1.2))

        return response
