import hashlib
import logging
import os

from sqlalchemy import create_engine, DateTime, BigInteger, ForeignKey

from sqlalchemy import Column, String


from sqlalchemy.orm import sessionmaker, declarative_base


logger = logging.getLogger(__name__)
user, password, hostname, port, db_name = (
    os.getenv("POSTGRES_USER"),
    os.getenv("POSTGRES_PASSWORD"),
    os.getenv("POSTGRES_HOST"),
    os.getenv("POSTGRES_PORT"),
    os.getenv("POSTGRES_DB"),
)

engine = create_engine(f"postgresql://{user}:{password}@{hostname}:{port}/{db_name}")
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)
    user_tg_name = Column(String)
    user_key = Column(String)
    access_key = Column(String, default="")
    user_balance = Column(BigInteger)
    chat_id = Column(BigInteger)
    registry_datetime = Column(DateTime)

    @classmethod
    def _construct_userdata(cls, userdata):
        logger.info("You are in _construct_userdata")
        if isinstance(userdata, list):
            logger.info("if type(item_data) is list: ")
            userdata_list = [
                {
                    "user_id": str(i.user_id),
                    "user_tg_name": i.user_tg_name,
                    "user_key": i.user_key,
                    "access_key": i.access_key,
                    "user_balance": i.user_balance,
                    "chat_id": i.chat_id,
                    "registry_datetime": i.registry_datetime,
                }
                for i in userdata
            ]
            sorted_item_list = sorted(userdata_list, key=lambda x: x["item"])
            logger.info(f"sorted_item_list: {sorted_item_list} ")
            return sorted_item_list
        else:
            logger.info("else: ")
            userdata_list = {
                "user_id": str(userdata.user_id),
                "user_tg_name": userdata.user_tg_name,
                "user_key": userdata.user_key,
                "access_key": userdata.access_key,
                "user_balance": userdata.user_balance,
                "chat_id": userdata.chat_id,
                "registry_datetime": userdata.registry_datetime,
            }
            logger.info(f"item_list: {userdata_list} ")
            return userdata_list

    @classmethod
    def _create_user_key(cls, user_id, user_tg_name):
        logger.info("You are in _create_user_key")

        hash_object = hashlib.sha256(f"{user_id}{user_tg_name}".encode())
        hash_digest = hash_object.hexdigest()
        short_key = hash_digest[:8]
        return short_key

    @classmethod
    def add_user(cls, user_id, user_tg_name, user_balance, chat_id, registry_datetime):
        logger.info("You are in add_user")
        new_user = Users(
            user_id=user_id,
            user_tg_name=user_tg_name,
            user_key=cls._create_user_key(user_id, user_tg_name),
            user_balance=user_balance,
            chat_id=chat_id,
            registry_datetime=registry_datetime,
        )
        session.add(new_user)
        session.commit()
        logging.info("User successfully saved!")

    @classmethod
    def get_user_by_id(cls, user_id):
        logger.info("You are in get_user_by_id")
        logger.info(f"Trying to get item with id: {user_id}")
        userdata = session.query(Users).filter_by(user_id=user_id).first()
        logger.info(f"userdata: {userdata}")
        if userdata:
            sorted_userdata = cls._construct_userdata(userdata)
            logger.info(f"Item with id {user_id} was found")
            return sorted_userdata
        else:
            logger.info(f"No item found with id {user_id}.")
            return None

    @classmethod
    def get_user_by_key(cls, access_key):
        logger.info("You are in get_user_by_key")
        logger.info(f"Trying to get userdata with access_key: {access_key}")
        userdata = session.query(Users).filter_by(user_key=access_key).first()
        logger.info(f"userdata: {userdata}")
        if userdata:
            sorted_userdata = cls._construct_userdata(userdata)
            logger.info(f"User with key {userdata.user_key} was found")
            return sorted_userdata
        else:
            logger.info(f"No item found with id {access_key}.")
            return None


class UserStatistics(Base):
    __tablename__ = "user_statistics"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    user_source = Column(String)
    user_sex = Column(String)
    user_birthday = Column(String, default="")

    @classmethod
    def _construct_statistics_data(cls, statistics_data):
        if isinstance(statistics_data, list):
            return [
                {
                    "user_id": str(stats.user_id),
                    "user_source": stats.user_source,
                    "user_sex": stats.user_sex,
                    "user_birthday": stats.user_birthday,
                }
                for stats in statistics_data
            ]
        else:
            return {
                "user_id": str(statistics_data.user_id),
                "user_source": statistics_data.user_source,
                "user_sex": statistics_data.user_sex,
                "user_birthday": statistics_data.user_birthday,
            }

    @classmethod
    def add_user_statistics(cls, user_id, user_source, user_sex, user_birthday=""):
        new_stats = UserStatistics(
            user_id=user_id,
            user_source=user_source,
            user_sex=user_sex,
            user_birthday=user_birthday,
        )
        session.add(new_stats)
        session.commit()
        return new_stats

    @classmethod
    def get_user_statistic(cls, user_id):
        user_statistic = (
            session.query(UserStatistics).filter_by(user_id=user_id).first()
        )
        if user_statistic:
            sorted_data = cls._construct_statistics_data(user_statistic)
            return sorted_data
        else:
            logger.info(f"No user statistic found for user_id {user_id}.")
            return None


#
#
#     @classmethod
#     def update_access_key(cls, user_id, access_key):
#         user = session.query(Users).filter_by(user_id=user_id).first()
#         if user:
#             user.access_key = access_key
#             session.commit()
#             logger.info("User_key updated successfully!")
#         else:
#             logger.warning("User not found.")
#
#     @classmethod
#     def referral_bonus(cls, access_key):
#         referrer = session.query(Users).filter_by(user_key=access_key).first()
#         if referrer:
#             referral_bonus_points = 10
#             referrer.user_balance += referral_bonus_points
#             session.commit()
#             logger.info(f"Referral bonus of {referral_bonus_points} points added to user {referrer.user_id} balance.")
#         else:
#             logger.warning("Referrer not found.")
#
#
#
#
#
#
#
# class Items(Base):
#     __tablename__ = 'items'
#     id = Column(BigInteger, primary_key=True, autoincrement=True)
#     item = Column(String)
#     item_url = Column(String)
#     user_id = Column(String)
#     user_tg_name = Column(String)
#     item_details = Column(String)
#     item_price = Column(String)
#     item_quantity = Column(BigInteger)
#     item_photo = Column(String)
#     registry_datetime = Column(DateTime)
#
#     @classmethod
#     def _construct_item_list(cls, item_data):
#         logger.info(f"You are in _construct_item_list")
#         if type(item_data) is list:
#             logger.info(f"if type(item_data) is list: ")
#             item_list = [{
#                 "id": str(i.id),
#                 "item": i.item,
#                 "item_url": i.item_url,
#                 "user_id": i.user_id,
#                 "user_tg_name": i.user_tg_name,
#                 "item_details": i.item_details,
#                 "item_price": i.item_price,
#                 "item_quantity": i.item_quantity,
#                 "item_photo": i.item_photo,
#                 "registry_datetime": i.registry_datetime
#             } for i in item_data]
#             sorted_item_list = sorted(item_list, key=lambda x: x["item"])
#             logger.info(f"sorted_item_list: {sorted_item_list} ")
#             return sorted_item_list
#         else:
#             logger.info(f"else: ")
#             item_list = {
#                 "id": str(item_data.id),
#                 "item": item_data.item,
#                 "item_url": item_data.item_url,
#                 "user_id": item_data.user_id,
#                 "user_tg_name": item_data.user_tg_name,
#                 "item_details": item_data.item_details,
#                 "item_price": item_data.item_price,
#                 "item_quantity": item_data.item_quantity,
#                 "item_photo": item_data.item_photo,
#                 "registry_datetime": item_data.registry_datetime
#             }
#             logger.info(f"item_list: {item_list} ")
#             return item_list
#
#
#     @classmethod
#     def add_item(cls, item, item_url, user_id, user_tg_name, item_details, item_price, item_quantity, item_photo, registry_datetime):
#         logger.info("Trying to save item.")
#
#         new_item = Items(item=item, item_url=item_url, user_id=user_id, user_tg_name=user_tg_name, item_details=item_details,
#                          item_price=item_price, item_quantity=item_quantity, item_photo=item_photo,
#                          registry_datetime=registry_datetime)
#         session.add(new_item)
#         session.commit()
#         logger.info("Item successfully saved!")
#     @classmethod
#     def get_items(cls):
#         logger.info("Trying to get all items")
#         item_data = session.query(Items).all()
#         if item_data:
#             sorted_item_list = cls._construct_item_list(item_data)
#             logger.info("All items were extracted")
#             return sorted_item_list
#         else:
#             return None
#
#     @classmethod
#     def delete_item(cls, item):
#         logger.info("Trying to delete item.")
#         item_to_delete = session.query(Items).filter_by(item=item).first()
#
#         if item_to_delete:
#             session.delete(item_to_delete)
#             session.commit()
#             logger.info("Item successfully deleted!")
#         else:
#             logger.warning("Item not found.")
#             return None
#
#     @classmethod
#     def get_items_by_letters(cls, first_letters):
#         logger.info(f"Trying to get items by first letter: {first_letters}")
#         item_data = session.query(Items).filter(Items.item.ilike(f"%{first_letters}%")).all()
#         logger.info(f"item_data: {item_data}")
#         if item_data:
#             sorted_item_list = cls._construct_item_list(item_data)
#             logger.info(f"Items by {len(first_letters)} letter(s) were extracted")
#             logger.info(f"sorted_item_list: {sorted_item_list}")
#             return sorted_item_list
#         else:
#             logger.info("No items found for the given first letter.")
#             return None
#
#     @classmethod
#     def get_item_by_id(cls, item_id):
#         logger.info(f"Trying to get item with id: {item_id}")
#         item_data = session.query(Items).filter_by(id=item_id).first()
#         logger.info(f"item_data: {item_data}")
#         if item_data:
#             sorted_item_list = cls._construct_item_list(item_data)
#             logger.info(f"Item with id {item_id} was found")
#             return sorted_item_list
#         else:
#             logger.info(f"No item found with id {item_id}.")
#             return None
#
#     @classmethod
#     def subtract_quantity(cls, item_id, quantity_to_subtract):
#         item_to_update = session.query(Items).filter_by(id=item_id).first()
#         if item_to_update:
#             item_to_update.item_quantity -= quantity_to_subtract
#             session.commit()
#             logger.info(
#                 f"Subtracted {quantity_to_subtract} from item with id {item_id}. New quantity: {item_to_update.item_quantity}")
#         else:
#             logger.info(f"No item found with id {item_id}.")
#
#
#
#
#
#
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.commit()
