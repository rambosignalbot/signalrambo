import time
import datetime
import pytz
import random

# ============== SETTING TIMEZONE INDONESIA ==============
tz = pytz.timezone("Asia/Jakarta")

# ============== SIMULASI DATA CANDLE (NANTI GANTI API NYATA) ==============
def get_latest_candle():
    open_price = random.uniform(1.1000, 1.1200)
    close_price = open_price + random.choice([-0.0005, 0.0004])
    return {
        "open": open_price,
        "close": close_price
    }

# ============== STRATEGI: AUTO PILIH NORMAL / TERBALIK ==============
def decide_op(candle, mode="auto"):
    open_p = candle["open"]
    close_p = candle["close"]
    arah = "BUY" if close_p > open_p else "SELL"
    
    if mode == "terbalik":
        return "SELL" if arah == "BUY" else "BUY"
    return arah

# ============== PENENTUAN STRATEGI ==============
def auto_strategy(current_minute):
    # Contoh logika: jam genap = normal, ganjil = terbalik
    if current_minute % 2 == 0:
        return "normal"
    return "terbalik"

# ============== FORMAT SINYAL ==============
def format_signal(jam_target, arah):
    return f"{jam_target} – {arah} – Mode AUTO SOBATCU – RAMBO SIGNAL JUARA"

# ============== MAIN LOOP TIAP DETIK ==============
def run_bot():
    print(">> RAMBO BOT SIAP PANTAU 24/7")

    last_sent_minute = None

    while True:
        now = datetime.datetime.now(tz)
        detik = now.second
        menit = now.minute
        jam = now.hour

        if 50 <= detik <= 53:
            if last_sent_minute != menit:
                candle = get_latest_candle()
                strategi = auto_strategy(menit)
                arah = decide_op(candle, mode=strategi)

                # Waktu target OP = menit berikutnya
                target_time = now + datetime.timedelta(minutes=1)
                jam_target = target_time.strftime("%H.%M.00")

                sinyal = format_signal(jam_target, arah)
                print(sinyal)

                last_sent_minute = menit

        time.sleep(0.5)

if __name__ == "__main__":
    run_bot()
