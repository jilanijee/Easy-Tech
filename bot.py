import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🔍 Fault & Symptom", callback_data="fault"),
            InlineKeyboardButton("⚠️ Error Code", callback_data="error"),
        ],
        [
            InlineKeyboardButton("📐 3D Diagrams", callback_data="diagram"),
            InlineKeyboardButton("🧰 Testing Guide", callback_data="testing"),
        ],
        [
            InlineKeyboardButton("🛠️ Service & Maintenance", callback_data="service"),
            InlineKeyboardButton("🔌 Wiring & Connection", callback_data="wiring"),
        ],
        [
            InlineKeyboardButton("📚 Model Wise Info", callback_data="model"),
            InlineKeyboardButton("👑 Premium Library", callback_data="premium"),
        ],
        [
            InlineKeyboardButton("📞 Help", callback_data="help"),
            InlineKeyboardButton("ℹ️ About Us", callback_data="about"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "👑 *EASY TECH PRO*\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "🔧 *Technician ka Smart Saathi*\n\n"
        "AC • Fridge • Washing Machine • Water Dispenser\n\n"
        "🔎 Kisi bhi *Fault ya Symptom* ko search karein.\n"
        "📐 3D Diagram • ⚡ Testing • 🔌 Wiring • 🛠️ Service\n\n"
        "✨ *Better Service | Better Performance | Easy Tech*\n\n"
        "✍️ *Abdul*"
    )

    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "fault": "🔍 *Fault & Symptom*\n\nAppliance ka symptom likhiye.\nExample: AC cooling nahi kar raha.",
        "error": "⚠️ *Error Code*\n\nAppliance ka Error Code bhejiye.\nExample: E1, E4, F1...",
        "diagram": "📐 *3D Diagrams*\n\nYahan appliance parts ke 3D diagrams aur working explanation milenge.",
        "testing": "🧰 *Testing Guide*\n\nMultimeter se motor, sensor, capacitor aur other parts ko check karne ki guide.",
        "service": "🛠️ *Service & Maintenance*\n\nRegular service aur maintenance ki technician guide.",
        "wiring": "🔌 *Wiring & Connection*\n\nConnection, pin details aur safety information.",
        "model": "📚 *Model Wise Info*\n\nModel number bhejiye. Model-wise information yahan add ki jayegi.",
        "premium": "👑 *Premium Library*\n\nAdvanced diagnosis, 3D diagrams, testing values aur step-by-step repair guides.\n\n⭐ Premium section coming soon.",
        "help": "❓ *Help*\n\nApna appliance, model number aur problem detail mein bhejiye.",
        "about": "ℹ️ *About Easy Tech Pro*\n\nTechnicians ke liye practical appliance service knowledge.\n\n✍️ Abdul",
    }

    await query.edit_message_text(
        messages.get(query.data, "Please select an option."),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        )
    )


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await start_from_callback(update, context)


async def start_from_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🔍 Fault & Symptom", callback_data="fault"),
            InlineKeyboardButton("⚠️ Error Code", callback_data="error"),
        ],
        [
            InlineKeyboardButton("📐 3D Diagrams", callback_data="diagram"),
            InlineKeyboardButton("🧰 Testing Guide", callback_data="testing"),
        ],
        [
            InlineKeyboardButton("🛠️ Service & Maintenance", callback_data="service"),
            InlineKeyboardButton("🔌 Wiring & Connection", callback_data="wiring"),
        ],
        [
            InlineKeyboardButton("📚 Model Wise Info", callback_data="model"),
            InlineKeyboardButton("👑 Premium Library", callback_data="premium"),
        ],
    ]

    await update.callback_query.edit_message_text(
        "👑 *EASY TECH PRO*\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "🔧 *Technician ka Smart Saathi*\n\n"
        "AC • Fridge • Washing Machine • Water Dispenser\n\n"
        "🔎 Fault • Error Code • 3D Diagram • Testing\n"
        "🛠️ Service • Wiring • Model Information\n\n"
        "✍️ *Abdul*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN secret is missing.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons, pattern="^(?!home$).+"))
    app.add_handler(CallbackQueryHandler(home, pattern="^home$"))

    print("Easy Tech Pro Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
