from sarufi import Sarufi
from decouple import config


def create():
    if not (config("CLIENT_ID", None) or config("CLIENT_SECRET", None)):
        raise Exception("Did you forget to add [CLIENT_ID, CLIENT_SECRET] as environment variables. Create a .env "
                        "file instead.")

    sarufi = Sarufi(config("CLIENT_ID"), config("CLIENT_SECRET"))

    if config("BOT_ID", None) is not None:
        response = sarufi.update_from_file(
            intents="data/intents.yaml",
            flow="data/flows.yaml",
            metadata="data/metadata.yaml",
            id=config("BOT_ID", cast=int)
        )
    else:
        response = sarufi.create_from_file(
            intents="data/intents.yaml",
            flow="data/flows.yaml",
            metadata="data/metadata.yaml",
        )

    print(response)


if __name__ == "__main__":
    create()
