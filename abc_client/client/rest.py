from abc_client.client import client


class REST(client.Client):
    def init(self):
        self.post('init')