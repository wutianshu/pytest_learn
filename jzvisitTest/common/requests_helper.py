import traceback
import requests

# Disable https security warning
requests.packages.urllib3.disable_warnings()


class SharedAPI(object):
    def __init__(self, login_url, login_data):
        self.s = requests.session()
        self.login_url = login_url
        self.login_data = login_data
        self.header = {}

    def login(self):
        try:
            result = self.s.post(url=self.login_url,
                                 data=self.login_data,
                                 headers=self.header,
                                 verify=False)
            if int(result.status_code) == 200:
                pass
            else:
                raise Exception('login failed')
            return result
        except RuntimeError:
            traceback.print_exc()

    def post_api(self, url, **kwargs):
        return self.s.post(url, **kwargs)

    def get_api(self, url, **kwargs):
        return self.s.get(url, **kwargs)
