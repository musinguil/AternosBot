from python_aternos import Client


class AternosServer():
    username = 'guigui201'
    password = '3WCpiR6p4Yql'
    def __init__(self):
        self.client = Client.from_credentials('guigui201', '3WCpiR6p4Yql')
    def enableServer(server_link):
        server_list = self.client.list_servers()
        #for server in server_list:
        #    if server.address == server_link:
        #        server.start()