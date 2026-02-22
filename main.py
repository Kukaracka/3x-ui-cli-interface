from service import XUIService
from ui import input_email, menu


def main():
    service = XUIService()

    while True:
        menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            inbound = service.get_inbound()
            for c in inbound.settings.clients:
                print(f"{c.email} | UUID: {c.id} | Limit: {c.total_gb}")

        if choice == "2":
            inbounds = service.get_inbounds()
            for inbound in inbounds:
                print(f"\n{inbound.port, inbound.id}\n")
                for c in inbound.settings.clients:
                    print(
                        f"{c.email} | Sub ID: {c.sub_id} | Time Left: {c.expiry_time / 1000} seconds"
                    )

        if choice == "3":
            name = input(
                "Введите имя пользователя, которое будет использоваться для sub_id и comment: "
            )
            inbound_id = int(input("Введите inbound_id: "))
            result = service.add_user(inbound_id=inbound_id, sub_id=name, comment=name)
            print(result)

        if choice == "4":
            name = input(
                "Введите имя пользователя, которое будет использоваться для sub_id и comment: "
            )
            for inbound_id in service.get_inbounds_ids():
                result = service.add_user(
                    inbound_id=inbound_id, sub_id=name, comment=name
                )
                print(result)

        if choice == "5":
            name = input(
                "Введите sub_id пользователя, который будет удален из всех инбаундов: "
            )
            uids = service.get_user_uids_by_sub(sub_id=name)
            for inbound_id in uids:
                print(inbound_id, uids[f"{inbound_id}"])
                service.remove_user(inbound_id=inbound_id, uuid=uids[f"{inbound_id}"])

        if choice == "6":
            name = input(
                "Введите имя пользователя, которому вы хотите продлить время: "
            )
            users = service.get_users_by_sub(sub_id=name)
            for user in users:
                service.update_user(user)

        elif choice == "0":
            break

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
