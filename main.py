print("Bot Telegram iniciando...")
from bot_telegram_2 import *
# Iniciar o bot
if __name__ == '__main__':
    try:
        schedule_messages()
        keep_bot_running()
        keep_bot_running()
    except Exception as e:
        print(f'Erro ao iniciar o bot: {e}')
