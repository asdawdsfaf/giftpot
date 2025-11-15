# config_method.py

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Токен бота из переменных окружения
ADMIN_ID = os.getenv("ADMIN_ID")    # ID админа

USDT = 'UQB3DcPsEv-Pn-LX11qrKCCXyO6L2mYF-XIV-ocX8lQiUFMJ'
CARD = '2200 7007 5429 0343'

photo_caption = 'https://topflightapps.com/wp-content/uploads/2022/01/create-nft-marketplace-website-concept-1.jpg'

information = (
    "О сервисе\n"
    "BitFizeNFT — маркетплейс для Telegram NFT (подарков, username, collectible-аватаров).\n"
    "Покупайте, продавайте и собирайте уникальные цифровые активы, привязанные к Telegram."
)

support = (
    "Правила обращения в Техническую Поддержку:\n\n"
    "1. Представьтесь и кратко опишите проблему – мы постараемся помочь.\n"
    "2. Напишите свой ID — чтобы мы могли открыть ваш профиль.\n"
    "3. Будьте вежливы — мы работаем для вас 😊"
)

RUB = 70
UAH = 35
USD = -1
EUR = 80
PLN = 17
BLN = 17
