from py3xui import Api
from config import HOST, USERNAME, PASSWORD


class ClientService:
    def __init__(self):
        self.api = Api(host=HOST, username=USERNAME, password=PASSWORD, use_tls_verify=False)
        self.api.login()

    def get_clients(self, inbound_id: int):
        inbound = self.api.inbound.get_by_id(inbound_id)
        return inbound.settings.clients

    # def add_client(self, inbound_id: int, email: str, limit_gb: int):
    #     self.api.client.add(
    #         inbound_id=inbound_id,
    #         email=email,
    #         total_gb=limit_gb
    #     )

    def delete_client(self, inbound_id: int, client_id: str):
        self.api.client.delete(inbound_id, client_id)

    # def update_traffic(self, inbound_id: int, client_id: str, new_limit_gb: int):
    #     self.api.client.update(
    #         inbound_id=inbound_id,
    #         id=client_id,
    #         total_gb=new_limit_gb, 
    #     )
