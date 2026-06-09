from service import XUIService
from rich import print
import time
from ui import input_email, menu

def contains_substring(substring, string):
    return substring.casefold() in string.casefold()

def time_message(time_int: int) -> str:

    if time_int == 0:
        time_left = "Unlimited"
    else:
        time_left = f"Left {(time_int - int(time.time() * 1000)) / 1000 // 3600} hours"
    time_left += " " * (20 - len (time_left))
    return time_left

def main():
    service = XUIService()

    while True:
        menu()
        choice = input("Выберите пункт: ")


        if choice == "1":
            inbound = service.get_inbound()
            print(f"\nПорт работы инбаунда - [bold blue]{inbound.port}[/bold blue]")
            print(f"{'-'*80}")
            for c in inbound.settings.clients:
                time_left = time_message(c.expiry_time)
                print(
                    f"{c.email}{" " * (38 - len(c.email))}| [bold]{time_left}[/bold] | Sub ID: [red]{c.comment} [/red]"
                )


        elif choice == "3":
            name = input(
                "Введите имя пользователя, которое будет использоваться для sub_id и comment: "
            )
            for inbound_id in service.get_inbounds_ids():
                service.add_user(
                    inbound_id=inbound_id, sub_id=name, comment=name, endless=True
                )

            print(f"Ссылка на активацию подписки\n{'-'*20}")    
            print(f"https://nov.tmpan.ru:1339/subscription/{name}\n{'-'*20}")

        elif choice == "4":
            name = input(
                "Введите имя пользователя, которое будет использоваться для sub_id и comment: "
            )
            for inbound_id in service.get_inbounds_ids():
                service.add_user(
                    inbound_id=inbound_id, sub_id=name, comment=name
                )

            print(f"Ссылка на активацию подписки\n{'-'*20}")    
            print(f"https://nov.tmpan.ru:1339/subscription/{name}\n{'-'*20}")

        elif choice == "5":
            name = input(
                "Введите sub_id пользователя, который будет удален из всех инбаундов: "
            )
            uids = service.get_user_uids_by_sub(sub_id=name)
            for inbound_id in uids:
                print(inbound_id, uids[f"{inbound_id}"])
                service.remove_user(inbound_id=inbound_id, uuid=uids[f"{inbound_id}"])

        elif choice == "6":
            name = input(
                "Введите имя пользователя, которому вы хотите продлить время: "
            )
            users = service.get_users_by_sub(sub_id=name)
            for user in users:
                service.update_user(user)

        elif choice == "7":
            name = input(
                "Введите имя пользователя, которого хотите найти: "
            )
            inbounds = service.get_inbounds()
            for inbound in inbounds:
                print(f"\nПорт работы инбаунда - [bold blue]{inbound.port}[/bold blue]")
                print(f"{'-'*80}")
                for c in inbound.settings.clients:
                    if contains_substring(name, c.comment): 
                        time_left = time_message(c.expiry_time)
                        print(
                            f"{c.email}{" " * (38 - len(c.email))}| [bold]{time_left}[/bold] | Sub ID: [red]{c.sub_id} [/red]"
                        )
        else:
            break



if __name__ == "__main__":
    main()
