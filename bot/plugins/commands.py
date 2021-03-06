#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
from pyrogram.errors import PeerIdInvalid
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
#adding force subscribe option to bot
    update_channel = FORCESUB_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("ð¤­ Sorry Dude, You are **B A N N E D ð¤£ð¤£ð¤£**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text=""" <b> â ï¸ YOU HAVE NOT SUBSCRIBED OUR CHANNELâ ï¸
Join on our channel to get movies â
â ï¸à´¤à´¾à´àµà´àµ¾ à´à´àµà´à´³àµà´àµ à´à´¾à´¨àµ½ à´¸à´¬àµà´¸àµà´àµà´°àµà´¬àµ à´àµà´¯àµà´¤à´¿à´àµà´àµ à´à´²àµà´² ! â ï¸
à´à´àµà´à´³àµà´àµ à´à´¾à´¨à´²à´¿àµ½ à´àµà´¯à´¿àµ» à´àµà´¯àµà´¯à´¤à´¾àµ½ à´¤à´¾à´àµà´àµ¾à´àµà´àµ movies à´à´¿à´àµà´àµà´¨àµà´¨à´¤àµ à´à´£àµ â\nð¼ðð©ðð§ ðð¤ðð£ðð£ð ðð¡ððð  ð¤ð£ ð©ðð ððð¡ð ððªð©ð©ð¤ð£ ðð£ ðð§ð¤ðªð¥ ðð£ð ð®ð¤ðª ð¬ðð¡ð¡ ððð© ððð¡ð.
â¬ï¸Channel linkâ¬ï¸ </b>""",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="â¡ ðððð ððð ðððð â¡ï¸", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption =f''' <b>Join <a href="https://t.me/worldmoviesaj">MOVIE HUB HDâ¬ï¸â¼ï¸â¾ï¸âªï¸</a>\n\n <code>{file_name}</code>\n\n<a href="https://t.me/AJmovieLINKS ">ð¼ðð ðððððð ð¼ðð¿ ðððððð ðð¿</a>\n\nÂ© Powered by <a href="https://t.me/AJmovieLINKS ">ðð¾ð ðð´ððð´ðð ðð´ ð¿ðð¾ðð¸ð³ð´</a></b> \n@worldmoviesaj\n@AJmovieLINKS''',
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'â½ð ð¼ð¿ð² ð ð¼ðð¶ð²ðâ½', url="https://t.me/worldmoviesaj"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption =  f" <code> {file_name} <code> \n <b> @worldmoviesaj <b> \n  â»â¬ Powered by â¬â¼  @AJmovieLINKS ",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'â½ð ð¼ð¿ð² ð ð¼ðð¶ð²ðâ½', url="https://t.me/worldmoviesaj"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption =  f" <code>{file_name}<code> \n <b> @worldmoviesaj <b> \n â»â¬ Powered by â¬â¼  @AJmovieLINKS ",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'â½ð ð¼ð¿ð² ð ð¼ðð¶ð²ðâ½', url="https://t.me/worldmoviesaj"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('â½ð ð¼ð¿ð² ð ð¼ðð¶ð²ðâ½', url='https://t.me/worldmoviesaj'),
        InlineKeyboardButton('ð¦ð¢ð¨ð¥ðð ðð¢ðð ð§¾', url ='https://t.me/AJmovieLINKS')],                               
     [
        InlineKeyboardButton('ð¦ð¨ð£ð£ð¢ð¥ð§ ð ', url='https://t.me/AJmovieLINKS')
    ],[
        InlineKeyboardButton('ðððð£ â', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=False,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('ðð¢ð ð â¡', callback_data='start'),
        InlineKeyboardButton('ððð¢ð¨ð§ ð©', callback_data='about')
    ],[
        InlineKeyboardButton('ððð¢ð¦ð ð', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('ðð¢ð ð â¡', callback_data='start'),
        InlineKeyboardButton('ððð¢ð¦ð ð', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
@Client.on_message(filters.command(["cast"]) & filters.chat(1082159563), group=1)
async def cast(bot, update):
  msg = '<b>' + update.text[6:] + '</b>'
  success=0

  async for member in bot.iter_chat_members(chat_id=-1001503369898) :
    try:
      await bot.send_message(text=msg, chat_id=member.user.id, parse_mode="html")
      success+=1
    except PeerIdInvalid :
      pass
    except Exception as e :
         print(e)
         

  await bot.send_message(
    text=f"Successfully Broadcasted Message To {success} members !!",
    chat_id=1082159563
    )
