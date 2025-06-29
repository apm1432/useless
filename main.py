# ✅ PATCHED: Resume from same index after /token
# ✅ PATCHED: Only rotate token on 'NoneType' object is not iterable

import os
import asyncio
from pyrogram.types import Message

async def try_all_tokens_with_retry(process_func, m: Message, *args):
    global token_list
    original_tokens = token_list.copy()

    for token in original_tokens:
        try:
            result = await process_func(token, *args)

            if result and isinstance(result, tuple) and all(result):
                return result

            raise TypeError("'NoneType' object is not iterable")

        except Exception as e:
            if "NoneType" in str(e) and "iterable" in str(e):
                print(f"⚠️ Token failed due to NoneType: {token}")
                token_list.remove(token)
                with open(TOKEN_LIST_PATH, "w") as f:
                    for t in token_list:
                        f.write(t + "\n")
            else:
                print(f"🚫 Error (non-token related): {e}")
                raise e

    await m.reply_text(
        "❌ All tokens failed. Send new token with `/token your_token` or `/stop` to cancel."
    )

    while True:
        try:
            response = await bot.listen(m.chat.id)
            text = response.text.strip()

            if text.startswith("/token"):
                new_tokens = text.split(maxsplit=1)[1].split(",,")
                token_list.extend([t.strip() for t in new_tokens if t.strip()])
                with open(TOKEN_LIST_PATH, "w") as f:
                    for t in token_list:
                        f.write(t + "\n")
                await m.reply_text("✅ Token received. Retrying...")
                return await try_all_tokens_with_retry(process_func, m, *args)

            elif text == "/stop":
                await m.reply_text("🛑 Stopped as per your request.")
                raise Exception("User stopped the process.")

        except asyncio.TimeoutError:
            await m.reply_text("⏰ Timeout. Stopping.")
            raise

# 🔁 Updated loop structure for batch video processing (e.g., /drm)

def run_batch_download(links, arg, bot, m, channel_id):
    index = arg - 1
    count = arg
    failed_count = 0

    async def process_link(index):
        url = links[index]
        try:
            # Example wrapper function for token usage
            async def get_keys_with_token(token, url):
                return await helper.get_mps_and_keys2(f"https://your-api.com?url={url}&token={token}")

            mpd, keys = await try_all_tokens_with_retry(get_keys_with_token, m, url)
            url = mpd
            keys_string = " ".join([f"--key {key}" for key in keys])

            # Your video decryption and upload logic here
            # res_file = await helper.decrypt_and_merge_video(url, keys_string, ...)
            # await helper.send_vid(bot, m, ..., res_file, ...)

            await m.reply_text(f"✅ Video {count} processed successfully.")
            return True

        except Exception as e:
            await bot.send_message(channel_id, f"⚠️ Failed on {count}) {url} — {str(e)}")
            return False

    async def start():
        nonlocal index, count, failed_count
        while index < len(links):
            success = await process_link(index)
            if not success:
                failed_count += 1
            count += 1
            index += 1
            await asyncio.sleep(1)

        await bot.send_message(
            channel_id,
            f"<b>-┈━═.•°✅ Completed ✅°•.═━┈-</b>
"
            f"<blockquote>🔗 Total URLs: {len(links)}
"
            f"🔴 Failed: {failed_count}
🟢 Success: {len(links) - failed_count}</blockquote>",
            parse_mode="html"
        )

    return start()
