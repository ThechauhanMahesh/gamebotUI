#ChauhanMahesh/Vasusen/COL/DroneBots

from telethon import events, Button
from .. import bot as Drone

AGREE = False
CRYPTO = False
UPI = False

@Drone.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))
async def compin(event):
    global AGREE
    if AGREE:
        tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
        await event.reply(
            f"Hello {tag}, Ready to make some money? Join the contests soon, they're live.\n\nPlay DEMO to improve your skills.",
            buttons=[
                [Button.inline("JOIN CONTEST 💰", data="contest"),
                Button.inline("PLAY DEMO 🕹", data="demo")],
                [Button.url("TUTORIAL 📹", url="t.me/maheshchauhan")]])
    else:
        await event.reply(
        "Do you agree with our terms and conditions?",
        buttons=[
            [Button.inline("I AGREE ✅", data="agree")]]
        )

@Drone.on(events.NewMessage(incoming=True, pattern="/deposit"))
async def deposit(event):
    if CRYPTO:
        await event.reply("Deposit coins.", buttons=[[Button.inline("X coins - Y USDT", data="None")]])
    else:
        await event.reply("Deposit coins.", buttons=[[Button.inline("X coins - Y INR", data="None")]])

@Drone.on(events.NewMessage(incoming=True, pattern="/withdraw"))
async def withdraw(event):
    if CRYPTO:
        await event.reply("withdraw coins.", buttons=[[Button.inline("X coins - Y USDT", data="None")]])
    else:
        await event.reply("withdraw coins.", buttons=[[Button.inline("X coins - Y INR", data="None")]])

@Drone.on(events.callbackquery.CallbackQuery(data="agree"))
async def agree(event):
    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await event.edit(
        f"Hello {tag}, Ready to make some money? Join the contests soon, they're live.\n\nPlay DEMO to improve your skills.",
        buttons=[
            [Button.inline("JOIN CONTEST 💰", data="contest"),
             Button.inline("PLAY DEMO 🕹", data="demo")],
            [Button.inline("TUTORIAL 📹")]])
    
    
@Drone.on(events.callbackquery.CallbackQuery(data="demo"))
async def demo(event):
    await event.edit("Launching demo gamee...")

@Drone.on(events.callbackquery.CallbackQuery(data="contest"))
async def contest(event):
    if not UPI and not CRYPTO:
        await event.edit(
            "Choose your payment mode for deposit and withdrawals.",
            buttons=[
                [Button.inline("CRYPTO 🪙", data="crypto")],
                [Button.inline("UPI 🇮🇳", data="UPI")]]
            )
    else:
        await event.edit(
            "Choose a pool to join ongoing contests\n\nX Coins available.",
            buttons=[
                [Button.inline("MINI Pool - Amount", data="None")],
                [Button.inline("JUMBO POOl - Amount", data="None")],
                [Button.inline("MAXI POOl - Amount", data="None")],
                [Button.inline("DEPOSIT 🔽", data="deposit")]]
            )
        
@Drone.on(events.callbackquery.CallbackQuery(data="UPI"))
async def upi(event):
    global UPI
    UPI = True
    await event.edit("Deposit coins.", buttons=[[Button.inline("X coins - Y INR", data="None")]])

@Drone.on(events.callbackquery.CallbackQuery(data="crypto"))
async def crpto(event):
    global CRYPTO
    CRYPTO = True
    await event.edit("Deposit coins.", buttons=[[Button.inline("X coins - Y USDT", data="None")]])

@Drone.on(events.callbackquery.CallbackQuery(data="deposit"))
async def deposit(event):
    if CRYPTO:
        await event.edit("Deposit coins.", buttons=[[Button.inline("X coins - Y USDT", data="None")]])
    else:
        await event.edit("Deposit coins.", buttons=[[Button.inline("X coins - Y INR", data="None")]])
