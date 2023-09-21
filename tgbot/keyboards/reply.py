import logging
from typing import Any


from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput


from tgbot.keyboards.states import States

logger = logging.getLogger(__name__)


async def check_in_reply(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logging.info("You are in check_in_reply")
    logging.info(f"button pressed: {button}")
    g = {
        "refresh": States.gate_state_1,
        "cancel": States.main_menu_state,
    }
    await dialog_manager.switch_to(g[button])


async def gate_1_reply(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logging.info("You are in gate_1_reply")
    logging.info(f"button pressed: {button}")
    dialog_manager.dialog_data.update(source=button)
    await dialog_manager.switch_to(States.gate_state_2)


async def gate_2_reply(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logging.info("You are in gate_2_reply")
    logging.info(f"button pressed: {button}")
    dialog_manager.dialog_data.update(source=button)
    await dialog_manager.switch_to(States.gate_state_3)


async def gate_3_reply(m: Message, input: MessageInput, dialog_manager: DialogManager):
    logging.info("You are in gate_3_reply")
    date = m.text
    logging.info(f"button pressed: {date}")
    await dialog_manager.switch_to(States.main_menu_state)


async def main_menu_reply(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logging.info("You are in main_menu")
    logging.info(f"button pressed: {button}")
    g = {
        "menu": States.menu_sections_state,
        "admin_panel": States.admin_panel_state,
    }
    await dialog_manager.switch_to(g[button])


async def menu_sections_reply(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logging.info("You are in menu_sections_reply")
    logging.info(f"button pressed: {button}")
    dialog_manager.dialog_data.update(section_photo=button)
    dialog_manager.start_data.get("chat_id")
    await dialog_manager.switch_to(States.section_photo_state)


async def admin_panel_reply(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, admin_option: str
):
    logger.info("You are in admin_panel_reply")
    dialog_manager.dialog_data.update(admin_option=admin_option)
    g = {
        "add": States.add_item_state,
        "delete": States.delete_item_state,
    }
    await c.answer()
    await dialog_manager.switch_to(g[admin_option])


async def add_menu_reply(
    m: Message, input: MessageInput, dialog_manager: DialogManager
):
    logger.info("You are in add_photo_reply")

    dialog_manager.start_data.get("user_id")
    dialog_manager.start_data.get("user_name")
    anim_id = m.animation
    logger.info(f"anim_id: {anim_id}")
    # item_photo = m.photo[-1].file_id
    # downloaded_photo = await m.bot.download(item_photo, destination=BytesIO())
    # form = aiohttp.FormData(quote_fields=False)
    # form.add_field(secrets.token_urlsafe(8), downloaded_photo)
    # new_session = aiohttp.ClientSession()
    # response = await new_session.post(
    #     os.getenv("BASE_TELEGRAPH_API_LINK").format(endpoint="upload"),
    #     data=form
    # )
    # logger.info(response.url)
    # json_response = await response.json()
    # photo_url = [UploadedFile.model_validate(obj) for obj in json_response][0].link
    # logger.info(f"photo_url: {photo_url}")
    # await new_session.close()
    #
    # dialog_manager.dialog_data.update(item_photo=item_photo)
    # dialog_manager.dialog_data.update(photo_url=photo_url)
    await m.answer(text="Photo was uploaded successfully!", parse_mode="HTML")
    # await dialog_manager.switch_to(States.admin_panel_state)
    await m.bot.answer_web_app_query()


# async def close_menu(c: CallbackQuery, widget: Any, dialog_manager: DialogManager):
#     await dialog_manager.done()


#
#
#
# async def filter_float(input_str):
#     pattern_comma = re.compile(r"^\d+(\,\d+)?$")
#     pattern_dot = re.compile(r"^\d+(\.\d+)?$")
#
#     if pattern_comma.match(input_str):
#         float_str = input_str.replace(',', '.')
#         try:
#             result = round(float(float_str), 2)
#             return result
#         except ValueError:
#             return None
#
#     elif pattern_dot.match(input_str):
#         try:
#             result = round(float(input_str), 2)
#             return result
#         except ValueError:
#             return None
#     else:
#         return None
#
# async def filter_int(input_str):
#     try:
#         check = int(input_str)
#         return check
#     except ValueError as e:
#         logger.error(e)
#         return None
#
#
#
# async def gate_reply(c: CallbackQuery, widget: Any, dialog_manager: DialogManager, access_button:str):
#     logging.info('You are in gate_reply')
#     await dialog_manager.switch_to(States.access_state)
#
#
# async def access_reply(m: Message, input: MessageInput, dialog_manager: DialogManager):
#     logger.info('You are in access_reply')
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     key = m.text
#     user_key = Users.get_user(user_id)[2]
#     friend = Users.find_user_by_key(key)
#     if key.isalnum() and len(key) == 8:
#         if friend:
#             Users.update_access_key(user_id, key)
#             Users.referral_bonus(key)
#             await m.reply(f"Access granted! Congratulations!!! - {user_name}!"
#                           f"\nYou was recommended to Our Shop_bot by user - {friend[1]}"
#                           f"\nPlease find below Your referral link that You can share with Your friends to get 10 extra points!"
#                           f"\nhttps://t.me/Clstl_bot?start={user_key}", parse_mode="HTML")
#             await dialog_manager.switch_to(States.main_menu_state)
#         else:
#             await m.reply(f"Unfortunately We can`t find Your key in Our base. "
#                           f"Ask a friend for an up-to-date access key or referral link.", parse_mode="HTML")
#     else:
#         await m.reply(f"Your key contains letters or has an incorrect length!\nPlease provide correct access key.",
#                       parse_mode="HTML")
#
#
#
#
# async def main_menu_reply(c: CallbackQuery, widget: Any, dialog_manager: DialogManager, menu_option: str):
#     dialog_manager.dialog_data.update(menu_option=menu_option)
#     chat_id = c.message.chat.id
#     logger.info('You are in main_menu_reply')
#     g = {
#         'contact': States.feedback_state,
#         'key': States.ref_link_state,
#         'admin_panel': States.admin_panel_state,
#
#     }
#     await dialog_manager.switch_to(g[menu_option])
#
#
# async def admin_panel_reply(c: CallbackQuery, widget: Any, dialog_manager: DialogManager, admin_option: str):
#     logger.info('You are in admin_panel_reply')
#     dialog_manager.dialog_data.update(admin_option=admin_option)
#     g = {
#         'add': States.add_item_state,
#         'delete': States.delete_item_state,
#     }
#     await dialog_manager.switch_to(g[admin_option])
#
#
#
# async def add_item_reply(m: Message, input: MessageInput, dialog_manager: DialogManager):
#     logger.info('You are in add_item_reply')
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_name = m.text
#     logger.info(item_name)
#     if 15 < len(item_name) < 200:
#         dialog_manager.dialog_data.update(item_name=item_name)
#         await dialog_manager.switch_to(States.add_description_state)
#     else:
#         await m.reply(text="Please provide the name of the item using only letters and digits, "
#                            "and make sure it's not empty and doesn't exceed 100 characters.\n Thanks!",
#                       parse_mode="HTML")
#
#
# async def add_description_reply(m: Message, input: MessageInput, dialog_manager: DialogManager):
#     logger.info('You are in add_description_reply')
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_description = m.text
#     if 50 < len(item_description) < 400:
#         dialog_manager.dialog_data.update(item_description=item_description)
#         await dialog_manager.switch_to(States.add_price_state)
#     else:
#         await m.reply(text="Please provide a description of the item using only letters and digits, "
#                            "ensuring it falls within the character limit of 50 to 400 characters.\nThanks!",
#                       parse_mode="HTML")
#
#
#
# async def add_price_reply(m: Message, input: MessageInput, dialog_manager: DialogManager):
#     logger.info('You are in add_price_reply')
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_price = m.text
#     correct_price_format = await filter_float(item_price)
#     if item_price and correct_price_format:
#         dialog_manager.dialog_data.update(item_price=correct_price_format)
#         await dialog_manager.switch_to(States.add_quantity_state)
#     else:
#         await m.reply(text="No no no, please type the price of the item, using format '0.0'. Thanks!",
#                       parse_mode="HTML")
#
#
#
# async def add_quantity_reply(m: Message, input: MessageInput, dialog_manager: DialogManager):
#     logger.info('You are in add_price_reply')
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_quantity = m.text
#     correct_quantity_format = await filter_int(item_quantity)
#     if item_quantity and correct_quantity_format:
#         dialog_manager.dialog_data.update(item_quantity=correct_quantity_format)
#         await dialog_manager.switch_to(States.add_photo_state)
#     else:
#         await m.reply(text="No no no, please type the quantity of the item, using format '123'. Thanks!",
#                       parse_mode="HTML")
#
#
#
# async def add_photo_reply(m: Message, input: MessageInput, dialog_manager: DialogManager):
#     logger.info('You are in add_photo_reply')
#
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_photo = m.photo[-1].file_id
#     downloaded_photo = await m.bot.download(item_photo, destination=BytesIO())
#     form = aiohttp.FormData(quote_fields=False)
#     form.add_field(secrets.token_urlsafe(8), downloaded_photo)
#     new_session = aiohttp.ClientSession()
#     response = await new_session.post(
#         os.getenv("BASE_TELEGRAPH_API_LINK").format(endpoint="upload"),
#         data=form
#     )
#     logger.info(response.url)
#     json_response = await response.json()
#     photo_url = [UploadedFile.model_validate(obj) for obj in json_response][0].link
#     logger.info(photo_url)
#     await new_session.close()
#
#     if item_photo:
#         dialog_manager.dialog_data.update(item_photo=item_photo)
#         dialog_manager.dialog_data.update(photo_url=photo_url)
#         await dialog_manager.switch_to(States.add_item_confirmation_state)
#     else:
#         await m.reply(text="Please upload correct photo, using one of the formats -> JPEG or PNG."
#                            "\nPlease refrain from uploading files larger than 20 mb, "
#                            "as it may affect the performance and usability of the bot. Thanks!",
#                       parse_mode="HTML")
#
#
#
# async def add_item_confirmation_reply(c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str):
#     logger.info("You are in add_item_confirmation_reply")
#     item_name = dialog_manager.dialog_data.get('item_name')
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_description = dialog_manager.dialog_data.get('item_description')
#     item_price = dialog_manager.dialog_data.get('item_price')
#     item_photo = dialog_manager.dialog_data.get('item_photo')
#     item_quantity = dialog_manager.dialog_data.get('item_quantity')
#     photo_url = dialog_manager.dialog_data.get('photo_url')
#     registry_datetime = datetime.now()
#     dialog_manager.dialog_data.update(button=button)
#     Items.add_item(item_name, photo_url, user_id, user_name, item_description, item_price, item_quantity, item_photo, registry_datetime)
#     g = {
#         'confirm': States.item_added_state,
#         'cancel': States.admin_panel_state,
#     }
#     await dialog_manager.switch_to(g[button])
#
# async def item_added_reply(c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str):
#     logger.info("You are in item_added_reply")
#
#
#     g = {
#         'admin_panel': States.admin_panel_state,
#     }
#     await dialog_manager.switch_to(g[button])
#
#
#
#
