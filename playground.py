from sarufi import Sarufi
from decouple import config


def run():
    if not (config("CLIENT_ID", None) or config("CLIENT_SECRET", None),
            config("BOT_ID", None)):
        raise Exception("Did you forget to add [CLIENT_ID,CLIENT_SECRET] as environment variables. Create a .env "
                        "file instead.")

    sarufi = Sarufi(config("CLIENT_ID"), config("CLIENT_SECRET"))
    chatbot = sarufi.get_bot(config("BOT_ID", cast=int))

    print("Dialog. Press Ctrl + c to quit.")
    while True:
        message = input("message > ")
        print("response > ", chatbot.respond(message)["message"])


if __name__ == "__main__":
    run()
