# import os
# import qrcode
import random
import string
import time
import uuid
from typing import Dict, List

from py3xui import Api, Client, Inbound

from config import (
    HOST,
    INBOUND_ID,
    PASSWORD,
    USERNAME,
    VERIFY_SSL,
    #     XUI_EXTERNAL_IP,
    #     SERVER_PORT,
    #     MAIN_REMARK,
)


def get_random_string(length):
    # Выбираем буквы из набора (строчные + заглавные)
    letters = string.ascii_letters
    # Генерация строки
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


class XUIService:
    def __init__(self):
        self.api = Api(
            host=HOST, username=USERNAME, password=PASSWORD, use_tls_verify=VERIFY_SSL
        )
        self.api.login()

    # ===== CLIENT SEARCH =====

    def get_inbound(self) -> Inbound:
        return self.api.inbound.get_by_id(INBOUND_ID)

    def get_inbounds(self) -> List[Inbound]:
        return self.api.inbound.get_list()

    def get_inbounds_ids(self) -> List[int]:
        list_of_inbounds = self.api.inbound.get_list()
        result = [inbound.id for inbound in list_of_inbounds]
        return result

    def get_user_uids_by_sub(self, sub_id) -> Dict[str, int]:
        inbound_ids = self.get_inbounds_ids()
        result = {}
        for inbound_id in inbound_ids:
            inbound = self.api.inbound.get_by_id(inbound_id)
            for c in inbound.settings.clients:
                # print(inbound_id, c.sub_id, c.email)
                if c.sub_id == sub_id:
                    result[f"{inbound_id}"] = c.id
        return result

    def get_users_by_sub(self, sub_id) -> List[Client]:
        inbound_ids = self.get_inbounds_ids()
        result = []
        for inbound_id in inbound_ids:
            inbound = self.api.inbound.get_by_id(inbound_id)
            for c in inbound.settings.clients:
                # print(inbound_id, c.sub_id, c.email)
                if c.sub_id == sub_id:
                    result.append(c)
        return result

    def find_client_by_email(self, email: str) -> Client | None:
        inbound = self.get_inbound()

        for c in inbound.settings.clients:
            if c.email == email:
                return c

        return None

    def add_user(self, inbound_id: int, sub_id: str, comment: str) -> Dict | None:
        id = str(uuid.uuid4())
        email = str(uuid.uuid4())
        extiry_time = int(time.time() * 1000) + 259200000
        try:
            new_client = Client(
                email=email,
                subId=sub_id,
                enable=True,
                id=id,
                comment=comment,
                password=sub_id,
                expiryTime=extiry_time,
            )
            self.api.client.add(inbound_id=inbound_id, clients=[new_client])
            return {"sub id": sub_id, "inbound id": inbound_id, "state": "added"}
        except Exception as e:
            print(f"Was {e} excepion")
            return None

    def remove_user(self, inbound_id, uuid):
        return self.api.client.delete(inbound_id=inbound_id, client_uuid=uuid)

    def update_user(self, user: Client):
        print(user.id)
        id = str(uuid.uuid4())
        new_client = self.api.client.get_by_email(user.email)
        new_client.expiry_time = new_client.expiry_time + 2678400000
        new_client.id = id
        new_client.comment = user.sub_id

        # new_user = Client(email=user.email, id=user.id,
        # enable=user.enable, password=user.password,
        # expiryTime=user.expiry_time + 2678400000)
        self.api.client.update(client_uuid=user.id, client=new_client)

    def server_status(self):
        status = self.api.server.get_status()
        return {
            "cpu": status.cpu,
            "mem_current": status.mem.current,
            "mem_total": status.mem.total,
            "uptime": status.uptime,
        }

    def create_backup(self, path="backup.db"):
        self.api.server.get_db(path)
        return path
