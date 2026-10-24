import os
import threading
import asyncio
import gradio as gr
from telegram_bot import start_bot


def run_bot_in_thread():
    """Telegram botni alohida threadda async loop bilan ishga tushiradi."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(start_bot())
    except Exception as e:
        print(f"Bot xatolik: {e}")


# --- Telegram botni orqa fonda ishga tushirish ---
bot_thread = threading.Thread(target=run_bot_in_thread, daemon=True)
bot_thread.start()

# --- Render.com PORT env variable'dan oladi ---
port = int(os.environ.get("PORT", 7860))

# --- Gradio UI (UptimeRobot shu sahifani ping qiladi) ---
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Sci-Fi Rejissyor Boti")
    gr.Markdown("✅ Bot 24/7 faol ishlamoqda!")
    gr.Markdown("Telegram'da `/ssenariy [mavzu]` buyrug'ini yuboring.")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=port)
