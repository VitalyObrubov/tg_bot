import asyncio
import os
import yaml

from clients.tg import TgClient


async def run_echo():
    config_path=os.path.join(os.path.dirname(__file__), 'config.yml')
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)
    bot_token = raw_config["bot"]["token"]

    c = TgClient(bot_token)
    offset = 0
    while True:
        res = await c.get_updates_in_objects(offset=offset, timeout=60)
        for item in res.result:
            offset = item.update_id + 1
            await c.send_message(item.message.chat.id, item.message.text)


if __name__ == "__main__":
    asyncio.run(run_echo())
