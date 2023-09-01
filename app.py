import telegram
import openai

# Token API Telegram Bot Anda
telegram_token = '6546417479:AAEaiGzDUAMlrqGrBQIweE3DUkbFuERvtiQ'
# Token API ChatGPT Anda
chatgpt_api_key = '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'

# Inisialisasi klien Telegram Bot
bot = telegram.Bot(token=telegram_token)

# Inisialisasi klien ChatGPT
openai.api_key = chatgpt_api_key

# Fungsi untuk menangani pesan dari pengguna
def handle_message(update, context):
    user_message = update.message.text
    
    # Mengirim pesan ke ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_message,
        max_tokens=50  # Sesuaikan dengan panjang yang Anda inginkan
    )
    
    # Mengirim jawaban dari ChatGPT kembali ke pengguna
    update.message.reply_text(response.choices[0].text)

# Fungsi untuk menghubungkan bot ke Telegram dan menangani pesan
def main():
    updater = telegram.ext.Updater(token=telegram_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()