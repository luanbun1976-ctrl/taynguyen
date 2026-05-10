# =========================
# AUTO FILTER ACC BOT FULL
# =========================

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

import os
import re

# =========================
# TOKEN BOT
# =========================

TOKEN = "8090475899:AAERw7Ktpu4hEzDc-qjaIAjCEZDD0oSPENo"

# =========================
# THƯ MỤC
# =========================

BASE_PATH = "/storage/emulated/0/filter_bot"

if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)

# =========================
# GHI FILE
# =========================

def save_file(path, lines):

    with open(path, "w", encoding="utf-8") as f:

        for line in lines:

            f.write(line.strip() + "\n")

# =========================
# GỬI FILE
# =========================

async def send_file(chat_id, bot, filepath):

    if not os.path.exists(filepath):
        return

    with open(filepath, "r", encoding="utf-8") as f:

        total = len(f.readlines())

    if total == 0:
        return

    await bot.send_document(
        chat_id=chat_id,
        document=open(filepath, "rb"),
        caption=f"📂 {os.path.basename(filepath)}\n📊 Có {total} acc"
    )

# =========================
# AUTO FILTER
# =========================

async def auto_filter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = await update.message.reply_text(
        "🔍 Đang đọc file..."
    )

    file = await update.message.document.get_file()

    input_path = f"{BASE_PATH}/input.txt"

    await file.download_to_drive(input_path)

    with open(input_path, "r", encoding="utf-8") as f:

        data = f.readlines()

    total_acc = len(data)

    await msg.edit_text(
        f"✅ Đọc file thành công\n📂 Tổng Acc: {total_acc}\n⚡ Đang lọc acc..."
    )

    # =========================
    # LIST
    # =========================

    skin_0_99 = []
    skin_100_199 = []
    skin_200_299 = []
    skin_300_399 = []
    skin_400_499 = []
    skin_500_599 = []
    skin_600_699 = []
    skin_700_799 = []
    skin_800_899 = []
    skin_900_999 = []
    skin_1000 = []

    tuong_1_50 = []
    tuong_51_99999 = []

    ss_list = []
    sss_list = []
    anime_list = []
    other_list = []

    level_30 = []
    qh_100 = []
    so_1000 = []
    nap_100 = []

    rank_dong = []
    rank_bac = []
    rank_vang = []
    rank_bk = []
    rank_kc = []
    rank_ct = []

    vn = []
    us = []

    fb_live = []

    email_yes = []
    cccd_yes = []
    authen_yes = []
    sdt_yes = []

    clean = []

    # =========================
    # FILTER
    # =========================

    for line in data:

        # =========================
        # CLEAN
        # =========================

        match_name = re.search(r"Name:\s*([^|]+)", line)

        if match_name:

            clean.append(match_name.group(1).strip())

        # =========================
        # SKIN
        # =========================

        match_skin = re.search(r"Skin:\s*(\d+)", line)

        if match_skin:

            skin = int(match_skin.group(1))

            if 0 <= skin <= 99:
                skin_0_99.append(line)

            elif 100 <= skin <= 199:
                skin_100_199.append(line)

            elif 200 <= skin <= 299:
                skin_200_299.append(line)

            elif 300 <= skin <= 399:
                skin_300_399.append(line)

            elif 400 <= skin <= 499:
                skin_400_499.append(line)

            elif 500 <= skin <= 599:
                skin_500_599.append(line)

            elif 600 <= skin <= 699:
                skin_600_699.append(line)

            elif 700 <= skin <= 799:
                skin_700_799.append(line)

            elif 800 <= skin <= 899:
                skin_800_899.append(line)

            elif 900 <= skin <= 999:
                skin_900_999.append(line)

            elif skin >= 1000:
                skin_1000.append(line)

        # =========================
        # TƯỚNG
        # =========================

        match_tuong = re.search(r"Tướng:\s*(\d+)", line)

        if match_tuong:

            tuong = int(match_tuong.group(1))

            if 1 <= tuong <= 50:
                tuong_1_50.append(line)

            elif tuong >= 51:
                tuong_51_99999.append(line)

        # =========================
        # SS
        # =========================

        match_ss = re.search(r"SS:\s*(\d+)", line)

        if match_ss:

            ss = int(match_ss.group(1))

            if ss >= 1:
                ss_list.append(line)

        # =========================
        # SSS
        # =========================

        match_sss = re.search(r"SSS:\s*(\d+)", line)

        if match_sss:

            sss = int(match_sss.group(1))

            if sss >= 1:
                sss_list.append(line)

        # =========================
        # ANIME
        # =========================

        match_anime = re.search(r"Anime:\s*(\d+)", line)

        if match_anime:

            anime = int(match_anime.group(1))

            if anime >= 1:
                anime_list.append(line)

        # =========================
        # OTHER
        # =========================

        match_other = re.search(r"Other:\s*(\d+)", line)

        if match_other:

            other = int(match_other.group(1))

            if other >= 1:
                other_list.append(line)

        # =========================
        # LEVEL
        # =========================

        match_level = re.search(r"Level:\s*(\d+)", line)

        if match_level:

            level = int(match_level.group(1))

            if level >= 30:
                level_30.append(line)

        # =========================
        # QUÂN HUY
        # =========================

        match_qh = re.search(r"Quân Huy:\s*(\d+)", line)

        if match_qh:

            qh = int(match_qh.group(1))

            if qh >= 100:
                qh_100.append(line)

        # =========================
        # SÒ
        # =========================

        match_so = re.search(r"Sò:\s*(\d+)", line)

        if match_so:

            so = int(match_so.group(1))

            if so >= 1000:
                so_1000.append(line)

        # =========================
        # LỊCH SỬ NẠP
        # =========================

        match_nap = re.search(r"Lịch Sử Nạp:\s*(\d+)", line)

        if match_nap:

            nap = int(match_nap.group(1))

            if nap >= 100:
                nap_100.append(line)

        # =========================
        # RANK
        # =========================

        if "Đồng" in line:
            rank_dong.append(line)

        if "Bạc" in line:
            rank_bac.append(line)

        if "Vàng" in line:
            rank_vang.append(line)

        if "Bạch Kim" in line:
            rank_bk.append(line)

        if "Kim Cương" in line:
            rank_kc.append(line)

        if "Cao Thủ" in line:
            rank_ct.append(line)

        # =========================
        # QUỐC GIA
        # =========================

        if "Quốc Gia: VN" in line:
            vn.append(line)

        if "Quốc Gia: US" in line:
            us.append(line)

        # =========================
        # FB
        # =========================

        if "FB: Live" in line:
            fb_live.append(line)

        # =========================
        # EMAIL
        # =========================

        if "Email: Yes" in line:
            email_yes.append(line)

        # =========================
        # CCCD
        # =========================

        if "CCCD: Yes" in line:
            cccd_yes.append(line)

        # =========================
        # AUTHEN
        # =========================

        if "Authen: Yes" in line:
            authen_yes.append(line)

        # =========================
        # SĐT
        # =========================

        if "SĐT: Yes" in line:
            sdt_yes.append(line)

    # =========================
    # SAVE FILE
    # =========================

    save_file(f"{BASE_PATH}/skin_0_99.txt", skin_0_99)
    save_file(f"{BASE_PATH}/skin_100_199.txt", skin_100_199)
    save_file(f"{BASE_PATH}/skin_200_299.txt", skin_200_299)
    save_file(f"{BASE_PATH}/skin_300_399.txt", skin_300_399)
    save_file(f"{BASE_PATH}/skin_400_499.txt", skin_400_499)
    save_file(f"{BASE_PATH}/skin_500_599.txt", skin_500_599)
    save_file(f"{BASE_PATH}/skin_600_699.txt", skin_600_699)
    save_file(f"{BASE_PATH}/skin_700_799.txt", skin_700_799)
    save_file(f"{BASE_PATH}/skin_800_899.txt", skin_800_899)
    save_file(f"{BASE_PATH}/skin_900_999.txt", skin_900_999)
    save_file(f"{BASE_PATH}/skin_1000.txt", skin_1000)

    save_file(f"{BASE_PATH}/tuong_1_50.txt", tuong_1_50)
    save_file(f"{BASE_PATH}/tuong_51_99999.txt", tuong_51_99999)

    save_file(f"{BASE_PATH}/ss.txt", ss_list)
    save_file(f"{BASE_PATH}/sss.txt", sss_list)
    save_file(f"{BASE_PATH}/anime.txt", anime_list)
    save_file(f"{BASE_PATH}/other.txt", other_list)

    save_file(f"{BASE_PATH}/level_30.txt", level_30)
    save_file(f"{BASE_PATH}/qh_100.txt", qh_100)
    save_file(f"{BASE_PATH}/so_1000.txt", so_1000)
    save_file(f"{BASE_PATH}/nap_100.txt", nap_100)

    save_file(f"{BASE_PATH}/rank_dong.txt", rank_dong)
    save_file(f"{BASE_PATH}/rank_bac.txt", rank_bac)
    save_file(f"{BASE_PATH}/rank_vang.txt", rank_vang)
    save_file(f"{BASE_PATH}/rank_bk.txt", rank_bk)
    save_file(f"{BASE_PATH}/rank_kc.txt", rank_kc)
    save_file(f"{BASE_PATH}/rank_ct.txt", rank_ct)

    save_file(f"{BASE_PATH}/vn.txt", vn)
    save_file(f"{BASE_PATH}/us.txt", us)

    save_file(f"{BASE_PATH}/fb_live.txt", fb_live)

    save_file(f"{BASE_PATH}/email_yes.txt", email_yes)
    save_file(f"{BASE_PATH}/cccd_yes.txt", cccd_yes)
    save_file(f"{BASE_PATH}/authen_yes.txt", authen_yes)
    save_file(f"{BASE_PATH}/sdt_yes.txt", sdt_yes)

    save_file(f"{BASE_PATH}/clean.txt", clean)

    # =========================
    # THỐNG KÊ
    # =========================

    text = f"""
✅ LỌC THÀNH CÔNG

📂 Tổng Acc: {total_acc}

🎮 Skin 0-99: {len(skin_0_99)}
🎮 Skin 100-199: {len(skin_100_199)}
🎮 Skin 200-299: {len(skin_200_299)}
🎮 Skin 300-399: {len(skin_300_399)}
🎮 Skin 400-499: {len(skin_400_499)}
🎮 Skin 500-599: {len(skin_500_599)}

🦸 Tướng 1-50: {len(tuong_1_50)}
🦸 Tướng 51+: {len(tuong_51_99999)}

⭐ SS: {len(ss_list)}
🌌 SSS: {len(sss_list)}
🎌 Anime: {len(anime_list)}
🎁 Other: {len(other_list)}

📧 Email Yes: {len(email_yes)}
🪪 CCCD Yes: {len(cccd_yes)}
🔐 Authen Yes: {len(authen_yes)}
📱 SĐT Yes: {len(sdt_yes)}

💰 QH >=100: {len(qh_100)}
🪙 Sò >=1000: {len(so_1000)}
📈 Nạp >=100: {len(nap_100)}
🎚 Level >=30: {len(level_30)}
"""

    await msg.edit_text(text)

    # =========================
    # GỬI FILE
    # =========================

    files = os.listdir(BASE_PATH)

    for f in files:

        if f.endswith(".txt") and f != "input.txt":

            await send_file(
                update.effective_chat.id,
                context.bot,
                f"{BASE_PATH}/{f}"
            )

# =========================
# LỆNH BAN
# =========================

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = await update.message.reply_text("🔍 Đang lọc acc ban...")

    input_path = f"{BASE_PATH}/input.txt"

    if not os.path.exists(input_path):

        await msg.edit_text("❌ Chưa có file.")
        return

    with open(input_path, "r", encoding="utf-8") as f:

        data = f.readlines()

    result = []

    for line in data:

        if "Ban: No" in line:

            result.append(line)

    path = f"{BASE_PATH}/ban_no.txt"

    save_file(path, result)

    await msg.edit_text(
        f"✅ Lọc thành công\n📂 Có {len(result)} acc"
    )

    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=open(path, "rb"),
        caption=f"🚫 Ban No | {len(result)} acc"
    )

# =========================
# LỆNH LỌC TRÙNG
# =========================

async def loctrung(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = await update.message.reply_text("🔍 Đang lọc trùng...")

    input_path = f"{BASE_PATH}/input.txt"

    if not os.path.exists(input_path):

        await msg.edit_text("❌ Chưa có file.")
        return

    with open(input_path, "r", encoding="utf-8") as f:

        data = f.readlines()

    result = list(dict.fromkeys(data))

    path = f"{BASE_PATH}/loc_trung.txt"

    save_file(path, result)

    await msg.edit_text(
        f"✅ Lọc xong\n📂 Còn {len(result)} acc"
    )

    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=open(path, "rb"),
        caption=f"♻️ Không Trùng | {len(result)} acc"
    )

# =========================
# MAIN
# =========================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.Document.ALL, auto_filter)
)

app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("loctrung", loctrung))

print("BOT ĐANG CHẠY...")

app.run_polling(close_loop=False)