from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("24671318")
APP_HASH = os.environ.get("a13a303efcd6cd1de98e4222b537f5c9")
BOT_USERNAME = os.environ.get("testyhombot")
session = os.environ.get("1BJWap1sBuwOwCAgPL8-FE_vxubmVVFPdOWQHkD_Re9vB45hNFceLwO79-TsGaCnNFIPX8WG9HSjuqTPyJlhn3gA0Ylpkm-goFTywohA8nyW55Ik8UkPbgFN-zU7hrR6RF-QdRyy4RIkNSS82rbeogYfMN9DFKydbvN1an__38VFyCcm4F4hnpZS6AfCRjno9DcbDMXYx9jV-KlM6x4ODnpRSo1x4H61Nj0ohVh43N3V0SXlwUxdhyB9ofgWnJA2TgrcX3sqeEZ7Qbo_Lb9L2rbAbvhcQInyejJBt3PsuI3_3oEzU5twMHTm4rdrd68u_iqt2cNBiLfhW2eWfFTv7Q6J888_As-k=")
SESSION = os.environ.get("1BJWap1sBuwOwCAgPL8-FE_vxubmVVFPdOWQHkD_Re9vB45hNFceLwO79-TsGaCnNFIPX8WG9HSjuqTPyJlhn3gA0Ylpkm-goFTywohA8nyW55Ik8UkPbgFN-zU7hrR6RF-QdRyy4RIkNSS82rbeogYfMN9DFKydbvN1an__38VFyCcm4F4hnpZS6AfCRjno9DcbDMXYx9jV-KlM6x4ODnpRSo1x4H61Nj0ohVh43N3V0SXlwUxdhyB9ofgWnJA2TgrcX3sqeEZ7Qbo_Lb9L2rbAbvhcQInyejJBt3PsuI3_3oEzU5twMHTm4rdrd68u_iqt2cNBiLfhW2eWfFTv7Q6J888_As-k=")
token = os.environ.get("6190359661:AAHeVjYrgAbwbpztQ-PUsBeNcqIDgnNUpKw")
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
