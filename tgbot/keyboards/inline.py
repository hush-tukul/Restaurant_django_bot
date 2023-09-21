import logging

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from environs import Env


logger = logging.getLogger(__name__)

env = Env()


async def check_in_inline(dialog_manager: DialogManager, **kwargs):
    title = (
        "I see👀 that Your answers for Our questions not complete"
        "\nor out of date 🤔..."
        "\nMaybe You want to refresh it?🔄"
    )
    check_in_buttons = [
        ("🔄 Refresh data", "refresh"),
        ("❌ Cancel", "cancel"),
    ]
    gif_url = MediaAttachment(
        ContentType.ANIMATION,
        file_id=MediaId(
            file_id="CgACAgQAAxkBAAIB8GT8hCf_j5fNsrlIeoMu-InlaWYAA2gPAAIGi-BTUtaXG4aDlVwwBA",
            file_unique_id="AgADaA8AAgaL4FM",
        ),
    )
    return {
        "gif_url": gif_url,
        "title": title,
        "check_in_buttons": check_in_buttons,
    }


async def gate_1_inline(dialog_manager: DialogManager, **kwargs):
    gate_1_title = (
        "Welcome, My Friend, to the Restaurant-bot! 🍽️😃 We're ready to serve and help You with Your wishes. 🤖🛎️"
        "\nPlease answer some questions, We're so happy to get to know You better! 😊📝"
        "\n---------------------------------------------"
        "\nWhere from do You know about Us? 🌐🤔"
    )
    gate_1_buttons = [
        ("😄 Friends", "friends"),
        ("👍 Facebook", "facebook"),
        ("📷 Instagram", "instagram"),
        ("✉️ Telegram", "telegram"),
    ]
    return {
        "gate_1_title": gate_1_title,
        "gate_1_buttons": gate_1_buttons,
    }


async def gate_2_inline(dialog_manager: DialogManager, **kwargs):
    gate_2_title = "Thank You🙏, and tell Us please," "\nHow can I address you??🤔"
    gate_2_buttons = [
        ("🕴️ Mr.", "mr"),
        ("💃 Miss/Mrs.", "miss_mrs"),
    ]
    return {
        "gate_2_title": gate_2_title,
        "gate_2_buttons": gate_2_buttons,
    }


async def gate_3_inline(dialog_manager: DialogManager, **kwargs):
    gate_3_title = (
        "🎉 And last one...Promise😊" "\n🍰 We'll be happy to know when is Your Birthday?"
    )

    return {
        "gate_3_title": gate_3_title,
    }


async def main_menu_inline(dialog_manager: DialogManager, **kwargs):
    logger.info("You are in main_menu_inline")
    user_id = dialog_manager.start_data.get("user_id")
    logger.info(user_id)
    title = "━━ 🍽️ Main Menu 🍽️ ━━"
    main_menu = [
        ("📝 Menu 📝", "menu"),
        ("🕹️Admin panel🕹️", "admin_panel")
        if user_id in list(map(int, env.list("ADMINS")))
        else None,
    ]

    return {"title": title, "main_menu": main_menu if main_menu[1] else main_menu[:1]}


async def menu_sections_inline(dialog_manager: DialogManager, **kwargs):
    logger.info("You are in menu_sections_inline")
    user_id = dialog_manager.start_data.get("user_id")
    logger.info(user_id)
    title = "━━ 📚 Menu Sections 📚 ━━"
    menu_sections = [
        ("🍽️ Starters 🍽️", "starters"),
        ("🥗 Salads 🥗", "salads"),
        ("🍲 Main Dishes 🍲", "main_dishes"),
        ("🍜 Soups 🍜", "soups"),
        ("🍣 Sushi 🍣", "sushi"),
        ("🍹 Cocktails 🍹", "cocktails"),
        ("🍺 Other drinks 🍺", "other_drinks"),
    ]

    return {
        "title": title,
        "menu_sections_1": menu_sections[:2],
        "menu_sections_2": menu_sections[2:4],
        "menu_sections_3": menu_sections[4:6],
        "menu_sections_4": menu_sections[6:],
    }


async def section_photo_inline(dialog_manager: DialogManager, **kwargs):
    logger.info("You are in menu_sections_inline")
    user_id = dialog_manager.start_data.get("user_id")
    section_photo = dialog_manager.dialog_data.get("section_photo")

    logger.info(user_id)
    menu = {
        "starters": "https://telegra.ph//file/d804cf0420321005602b2.jpg",
        "salads": "https://telegra.ph//file/7951a8916884fbcd998bf.jpg",
        "main_dishes": "https://telegra.ph//file/7914468bf7ad0b353739a.jpg",
        "soups": "https://telegra.ph//file/7daac15523621202a7f48.jpg",
        "sushi": "https://telegra.ph//file/7bdb178b0c883e1b704e0.jpg",
        "cocktails": "https://telegra.ph//file/9e257aa5023c3d09ed463.jpg",
        "other_drinks": "https://telegra.ph//file/e6d1edfe43a5780b8f68c.jpg",
    }
    return {
        "section_photo": MediaAttachment(ContentType.PHOTO, url=menu[section_photo]),
    }


async def admin_panel_inline(dialog_manager: DialogManager, **kwargs):
    dialog_manager.start_data.get("user_id")
    title = "🕹️Admin panel🕹️"
    admin_buttons = [
        ("➕ Add item ➕", "add"),
        ("❌ Delete item ❌", "delete"),
    ]

    return {
        "title": title,
        "admin": admin_buttons,
    }


async def add_menu_inline(dialog_manager: DialogManager, **kwargs):
    dialog_manager.start_data.get("user_id")
    title = "➕ Add item ➕"
    condition = "\n\nPlease send a picture"
    return {
        "title": title,
        "condition": condition,
    }


#
#
#
# async def gate_inline(dialog_manager: DialogManager, **kwargs):
#     user_name = dialog_manager.start_data.get('user_name')
#     access_denied_info = f"Access denied for user {user_name}!\nPlease provide access code below or use invite link to access the bot: " \
#                          f"\n(In other case please subscribe on Our channel https://t.me/+4fBl3YZ4Vrc3MTU0 to get access to bot)"
#     access_button = [
#             ('🔑 Access key', 'access'),
#         ]
#     return {
#             "access_denied_info": access_denied_info,
#             "access_button": access_button,
#         }
#
#
# async def access_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     user_data = Users.get_user(user_id)
#     header = "Please provide 8-character access code below or use invite link to access the bot: " \
#              f"\n(In other case please subscribe on Our channel https://t.me/+4fBl3YZ4Vrc3MTU0 to get access to bot)"
#
#     return {
#         "header": header,
#     }
#
#
#
#
#
# async def main_window_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     logger.info(user_id)
#     title = "┏━━━━━ 🛍️ Main Menu 🛍️ ━━━━━┓"
#     main_menu = [
#          ('📝 Feedback / Contact 📝', 'contact'), ('🔗 Referral link / key 🔐', 'key'),
#                  ('🕹️Admin panel🕹️', 'admin_panel') if user_id in list(map(int, env.list("ADMINS"))) else None
#     ]
#
#     return {
#         "title": title,
#         "main_menu": main_menu if main_menu[2] else main_menu[:2]
#
#     }
#
#
#
# async def ref_link_inline(dialog_manager: DialogManager, **kwargs):
#     logger.info("You are in ref_link_inline")
#     user_id = dialog_manager.start_data.get('user_id')
#     user_data = Users.get_user(user_id)
#
#     logger.info(user_id)
#     title = "┏━━━━━ 🔗 Referral link / key 🔐 ━━━━━┓"
#     ref_info = (f"Please find Your invite-link and key for friends below: "
#                 f"\n(🎉🎉Remember that You get 10 extra points for each friend"
#                 f"\nthat use Your link to join this Bot🤝🤖🎉🎉)"
#                 f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#                 f"\n<b>Invite-link:</b> {os.getenv('BOT_LINK')}?start={user_data[2]}"
#                 f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#                 f"\n<b>Invite-key:</b> {user_data[2]}")
#
#     return {
#         "title": title,
#         "ref_info": ref_info
#
#     }
#
#
# async def feedback_inline(dialog_manager: DialogManager, **kwargs):
#     logger.info("You are in feedback_inline")
#     user_id = dialog_manager.start_data.get('user_id')
#     user_data = Users.get_user(user_id)
#
#     logger.info(user_id)
#     title = "┏━━━━━ 📝 Feedback / Contact 📝 ━━━━━┓"
#     contact = (f"<b>\n❗For specific infoℹ️ or bug report🚩 please contact - @emperor_priferiti❗</b>")
#
#     return {
#         "title": title,
#         "contact": contact
#
#     }
#
#
#
# async def admin_panel_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     user_data = Users.get_user(user_id)
#     title = "🕹️Admin panel🕹️"
#     admin_buttons = [
#         ('➕ Add item ➕', 'add'), ('❌ Delete item ❌', 'delete'),
#         ('📋 Items list 📋', 'items_list')
#     ]
#
#     return {
#         "title": title,
#         "admin_1": admin_buttons[:2],
#         "admin_2": admin_buttons[2:],
#     }
#
#
#
#
# # async def item_info_inline(dialog_manager: DialogManager, **kwargs):
# #     user_id = dialog_manager.start_data.get('user_id')
# #     user_name = dialog_manager.start_data.get('user_name')
# #     user_data = Users.get_user(user_id)
# #     title = "📝 Item info 📝"
# #     item_buttons = [
# #         ('➕ Buy item ➕', 'buy')
# #     ]
# #
# #     return {
# #         "title": title,
# #         "item_buttons": item_buttons,
# #     }
#
# async def add_item_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     user_data = Users.get_user(user_id)
#     title = "➕ Add item ➕"
#     condition = "\n\nPlease enter item name with no special signs."
#
#     return {
#         "title": title,
#         "condition": condition,
#     }
#
#
#
# async def add_description_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_name = dialog_manager.dialog_data.get('item_name')
#     user_data = Users.get_user(user_id)
#     title = "➕ Add item ➕"
#     title_item = f"Item name: {item_name}"
#     condition = "\n\nGood! Please type some description for item with no special signs."
#
#     return {
#         "title": title,
#         "title_item": title_item,
#         "condition": condition,
#     }
#
#
# async def add_price_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_name = dialog_manager.dialog_data.get('item_name')
#     item_description = dialog_manager.dialog_data.get('item_description')
#     user_data = Users.get_user(user_id)
#     title = "➕ Add item ➕"
#     title_item = f"Item name: {item_name}"
#     title_description = f"Item description: {item_description}"
#     condition = "\n\nAwesome!! Please enter the price of item with no special signs."
#
#     return {
#         "title": title,
#         "title_item": title_item,
#         "title_description": title_description,
#         "condition": condition,
#     }
#
# async def add_quantity_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_name = dialog_manager.dialog_data.get('item_name')
#     item_description = dialog_manager.dialog_data.get('item_description')
#     item_price = dialog_manager.dialog_data.get('item_price')
#     user_data = Users.get_user(user_id)
#     title = "➕ Add item ➕"
#     title_item = f"Item name: {item_name}"
#     title_description = f"Item description: {item_description}"
#     title_price = f"Item price: {item_price}"
#     condition = "\n\nAwesome!! Please enter the quantity of item with no special signs."
#
#     return {
#         "title": title,
#         "title_item": title_item,
#         "title_description": title_description,
#         "title_price": title_price,
#         "condition": condition,
#     }
#
#
#
# async def add_photo_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_name = dialog_manager.dialog_data.get('item_name')
#     item_description = dialog_manager.dialog_data.get('item_description')
#     item_price = dialog_manager.dialog_data.get('item_price')
#     item_quantity = dialog_manager.dialog_data.get('item_quantity')
#     user_data = Users.get_user(user_id)
#     title = "➕ Add item ➕"
#     title_item = f"Item name: {item_name}"
#     title_description = f"Item description: {item_description}"
#     title_price = f"Item price: {item_price}"
#     title_quantity = f"Item quantity: {item_quantity}"
#     condition = "\n\nExcellent! Please add a photo of item, so We could see it."
#
#     return {
#         "title": title,
#         "title_item": title_item,
#         "title_description": title_description,
#         "title_price": title_price,
#         "title_quantity": title_quantity,
#         "condition": condition,
#     }
#
#
#
#
# async def add_item_confirmation_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_name = dialog_manager.dialog_data.get('item_name')
#     item_description = dialog_manager.dialog_data.get('item_description')
#     item_price = dialog_manager.dialog_data.get('item_price')
#     item_photo = dialog_manager.dialog_data.get('item_photo')
#     user_data = Users.get_user(user_id)
#     title = "➕ Add item ➕"
#     title_photo = MediaAttachment(ContentType.PHOTO, file_id=MediaId(item_photo))
#     title_item = f"Item name: {item_name}"
#     title_description = f"Item description: {item_description}"
#     title_price = f"Item price: {item_price}"
#     condition = "Good job! Please confirm that all data is correct: "
#     buttons = [
#         ('👍 Confirm item', 'confirm'), ('🗑️ Cancel', 'cancel'),
#     ]
#
#
#     return {
#         "title": title,
#         "title_photo": title_photo,
#         "title_item": title_item,
#         "title_description": title_description,
#         "title_price": title_price,
#         "condition": condition,
#         "buttons": buttons,
#     }
#
#
#
# async def item_added_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     item_name = dialog_manager.dialog_data.get('item_name')
#     item_description = dialog_manager.dialog_data.get('item_description')
#     item_price = dialog_manager.dialog_data.get('item_price')
#     item_photo = dialog_manager.dialog_data.get('item_photo')
#     user_data = Users.get_user(user_id)
#     title = "➕ Add item ➕"
#     title_photo = MediaAttachment(ContentType.PHOTO, file_id=MediaId(item_photo))
#     title_item = f"Item name: {item_name}"
#     title_description = f"Item description: {item_description}"
#     title_price = f"Item price: {item_price}"
#     condition = "Item was added successfully!"
#     buttons = [
#         ('To Admin Panel', 'admin_panel'),
#     ]
#
#     return {
#         "title": title,
#         "title_photo": title_photo,
#         "title_item": title_item,
#         "title_description": title_description,
#         "title_price": title_price,
#         "condition": condition,
#         "buttons": buttons,
#     }
#
#
# async def delete_item_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     user_data = Users.get_user(user_id)
#     title = "❌ Delete item ❌"
#     description = "Please enter item name with no special signs."
#
#     return {
#         "title": title,
#         "description": description,
#     }
#
#
# async def confirmed_item_delete_inline(dialog_manager: DialogManager, **kwargs):
#     user_id = dialog_manager.start_data.get('user_id')
#     user_name = dialog_manager.start_data.get('user_name')
#     user_data = Users.get_user(user_id)
#     title = "🙆‍♂️➡️🗑️ Item was successfully deleted!👍"
#
#     return {
#         "title": title,
#     }
#


# """"""
# """REGISTER"""
# async def register_inline(dialog_manager: DialogManager, **kwargs):
#     phone_permission = 'Confirm phone number'
#
#
# async def main_window_inline(dialog_manager: DialogManager, **kwargs):
#     header = 'Welcome to Winbot33!' \
#              '\nAgent-free, Exclusive & Direct HQ'\
#              '\nPlease select an option below :'
#     pic = 'AgACAgUAAxkBAAIBmmTH_Q9wDWVJw9E0_aIGEYDbiG26AAJ-tzEbMPpAViqBFy2ZJ2o5AQADAgADcwADLwQ'
#     image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(pic))
#     main_options = [
#         ('\U0001F4B0 REGISTER & CLAIM FREE \U0001F4B0', 'reg'),
#     ]
#     return {
#             'header': header,
#             'pic': image,
#             "main_options": main_options,
#         }


# async def register_window_inline(dialog_manager: DialogManager, **kwargs):
#     header = 'Please tap on REGISTER Winbot33 & CLAIM FREE ANGPAO'
#
#     return {
#         'header': header
#     }


# async def main_menu_inline(dialog_manager: DialogManager, **kwargs):
#     user_lang = dialog_manager.start_data.get('user_lang')
#     logging.info(user_lang)
#     title_name = title(user_lang)[0][0]
#     t_buttons = title_buttons(user_lang)
#     return {
#         "title": title_name,
#         "title_buttons_1": t_buttons[:3],
#         "title_buttons_2": t_buttons[3:],
#     }
#
#
#
# # async def menu_option_inline(dialog_manager: DialogManager, **kwargs):
# #     user_lang = dialog_manager.start_data.get('user_lang')
# #     option = dialog_manager.dialog_data.get('main_menu_option')
# #     title_name = option_title(user_lang, option)[0][0]
# #     lang_option_buttons = option_buttons(user_lang, option)
# #     return {
# #         "title": title_name,
# #         'lang_option_buttons': lang_option_buttons
# #     }
#
# async def links_list_inline(dialog_manager: DialogManager, **kwargs):
#     dialog_manager.dialog_data.update(chosen_link='add_link')
#     user_lang = dialog_manager.start_data.get('user_lang')
#     option = dialog_manager.dialog_data.get('main_menu_option')
#     user_id = dialog_manager.start_data.get('user_id')
#     links_info = links_list(user_lang, option, user_id)
#     logging.info(user_lang, option, user_id)
#     return {
#         "links_title": links_info[0],
#         'links_info': links_info[1],
#     }
#
#
# async def add_link_inline(dialog_manager: DialogManager, **kwargs):
#     user_lang = dialog_manager.start_data.get('user_lang')
#     option = dialog_manager.dialog_data.get('main_menu_option')
#     action = 'change_link'
#     confirm_button = action_confirm_button(user_lang, option, action)
#     logging.info(confirm_button)
#     return {
#         'title': confirm_button[0][0],
#         'confirm_button': confirm_button[1][0][0]
#     }
#
#
#
#
#
# async def link_options_inline(dialog_manager: DialogManager, **kwargs):
#     user_lang = dialog_manager.start_data.get('user_lang')
#     option = dialog_manager.dialog_data.get('main_menu_option')
#     user_id = dialog_manager.start_data.get('user_id')
#     link_id = dialog_manager.dialog_data.get('chosen_link')
#     orig_link = Reflink.get_original_link_by_user_id(user_id, link_id)
#     link_option_buttons = option_buttons(user_lang, option)
#     return {
#         'title': orig_link,
#         'link_option_buttons': link_option_buttons
#     }
#
#
# async def option_action_inline(dialog_manager: DialogManager, **kwargs):
#     link_id = dialog_manager.dialog_data.get('chosen_link')
#     user_lang = dialog_manager.start_data.get('user_lang')
#     option = dialog_manager.dialog_data.get('main_menu_option')
#     action = dialog_manager.dialog_data.get('chosen_option')
#
#     logging.info(f"option_action_inline/option: {option}")
#     logging.info(f"option_action_inline/action: {action}")
#     confirm_button = action_confirm_button(user_lang, option, action)
#     option_action_data = ''
#     if action == 'show_ref_link':
#         redirect_url = f"http://89.117.54.23:5000/{link_id}"
#         option_action_data = redirect_url
#     return {
#         'title': confirm_button[0][0],
#         'confirm_button': confirm_button[1][0][0],
#         'option_action_data': option_action_data
#     }
#
#
# async def del_action_inline(dialog_manager: DialogManager, **kwargs):
#     user_lang = dialog_manager.start_data.get('user_lang')
#     option = dialog_manager.dialog_data.get('main_menu_option')
#     action = dialog_manager.dialog_data.get('chosen_option')
#     confirm_button = action_confirm_button(user_lang, option, action)
#     return {
#         'title': confirm_button[0][0],
#         'confirm_button': confirm_button[1]
#     }


# Second state - MAIN PARAMETERS:
#          "Your links"
#     -     "Ваші посилання"    -> provides to Third state - List of links
#          "Ваши ссылки"
#
#          "Global statistics"
#     -     "Загальна статистика"  -> provides to Third state - "Global statistics parameters for all user links"
#          "Общая статистика"
#
#          "Instruction"
#     -     "Інструкція"   -> provides to Third state - "Instruction and info about each service of this bot"
#          "Инструкция"
#
#
#          "Change lang"
#     -    "Змінити мову" -> provides to Third state - ""
#          "Поменять язык"
#
#
#          "Contact Us"
#     -    "Контакти"   -> provides to Third state - "Contact window to save request/questions/asks from users"
#          "Контакты"
