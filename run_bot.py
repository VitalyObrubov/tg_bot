import asyncio
import datetime
import os
import yaml

from bot.base import Bot


def run():
    config_path=os.path.join(os.path.dirname(__file__), 'config.yml')
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)
    bot_token = raw_config["bot"]["token"]
    loop = asyncio.get_event_loop()

    bot = Bot(bot_token, 2)
    try:
        print('bot has been started')
        loop.create_task(bot.start())
        loop.run_forever()
    except KeyboardInterrupt:
        print("\nstopping", datetime.datetime.now())
        loop.run_until_complete(bot.stop())
        print('bot has been stopped', datetime.datetime.now())


if __name__ == '__main__':
    run()
