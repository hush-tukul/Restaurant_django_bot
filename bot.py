import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_dialog import Dialog, setup_dialogs

from tgbot.config import load_config
from tgbot.handlers.admin import admin_router
from tgbot.handlers.echo import echo_router

from tgbot.handlers.user import user_router
from tgbot.keyboards.windows import (
    gate_window_1,
    gate_window_2,
    gate_window_3,
    main_menu_window,
    admin_window,
    menu_sections_window,
    add_item_window,
    section_photo_window,
    check_in_window,
)

from tgbot.middlewares.config import ConfigMiddleware
from tgbot.services import broadcaster


logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    filename="bot.log",  # Specify the file name and location
    filemode="a",
)


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Bot has been started!")


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def main():
    logger = logging.getLogger(__name__)
    logger.info("Starting bot!")
    config = load_config(".env")
    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)
    dialog = Dialog(
        check_in_window,
        gate_window_1,
        gate_window_2,
        gate_window_3,
        main_menu_window,
        menu_sections_window,
        section_photo_window,
        admin_window,
        add_item_window,
    )
    routers = [
        admin_router,
        user_router,
        echo_router,
    ]

    dp.include_routers(*routers, dialog)
    setup_dialogs(dp)
    register_global_middlewares(dp, config)
    await bot.delete_webhook(drop_pending_updates=True)
    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot was shut down!")
