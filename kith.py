import asyncio
import time
import json
import re
import os
import config
from os import system
from pyppeteer import launch
from pyppeteer_stealth import stealth
from dhooks import Webhook, Embed
def updatetab(cart,tasks,captcha,success,failed):
    system("title " + f"{config.user}'s HypeAIO[1.01][Tasks: {tasks}][{captcha} Pending Captcha][{cart} Carted][{success} Succesfully Checkout][{failed} Failed]")
def errorwebhook(user_hook,prodname, prodprice, checkorder, checkcolor, userpro, checktime, prodimage,proxy):
    hook = Webhook(user_hook)

    embed = Embed(
        description=checkorder,
        color=checkcolor,
        timestamp='now'  # sets the timestamp to current time
    )

    image1 = 'https://media.discordapp.net/attachments/'
    image2 = prodimage
    embed.set_author(name='Hype AIO V1.01', icon_url=image1)
    embed.add_field(name=prodname, value=prodprice)
    embed.add_field(name='Site:', value='Kith')
    embed.add_field(name='Profile:', value=userpro)

    embed.add_field(name='Checkout time:', value=checktime)
    embed.add_field(name='Proxy:', value=f'||{proxy}||')
    embed.set_footer(text='Mode: HumanPreload', icon_url=image1)

    embed.set_thumbnail(image1)
    embed.set_image(image2)

    hook.send(embed=embed)
def allusercheckouts(prodname, prodprice, checkorder, checkcolor, userpro, checktime, prodimage):
    hook = Webhook(checktime)

    embed = Embed(
        description=checkorder,
        color=checkcolor,
        timestamp='now'  # sets the timestamp to current time
    )

    image1 = 'https://media.discordapp.net/attachments/782329553107288095/831936574341644298/AIO.png?width=567&height=567'
    image2 = prodimage
    embed.set_author(name='Hype AIO V1.01', icon_url=image1)
    embed.add_field(name=prodname, value=prodprice)
    embed.add_field(name='Site:', value='Kith')
    embed.add_field(name='HH User:', value="Beta-User")
    embed.set_footer(text='Mode: HumanPreload', icon_url=image1)
    embed.set_thumbnail(image1)
    embed.set_image(image2)
    hook.send(embed=embed)
async def kithmodule(task,profile,size,keyword,PROXY):
    config.tasks=config.tasks+1
    updatetab(config.cart,config.tasks,config.captcha,config.success,config.failed)
    site='kith.com'
    profile_data=profile
    json_file = open("scratch.txt", "r", encoding="utf-8")
    data = json.load(json_file)
    os.system("cls")
    hook=data['user_settings']['user_webhook']
    profile_firstname = data[profile]['first_name']
    profile_lastname = data[profile]['last_name']
    profile_address = data[profile]['street_address']
    profile_city = data[profile]['city']
    profile_zip = data[profile]['zip_code']
    profile_state = data[profile]['state']
    profile_phone = data[profile]['phone_number']
    profile_email = data[profile]['email']
    profile_card = re.findall('....',data[profile]['card'])
    profile_cardexpmonth = data[profile]['expiry_month']
    profile_cardexpyear = data[profile]['expiry_year']
    profile_cardcvv = data[profile]['card_cvv']
    try:
        driver_proxy = (PROXY.split(':'))
        browsargs = [
            f'--proxy-server={driver_proxy[0]}:{driver_proxy[1]}'
        ]
    except:
        pass
    browser = await launch(headless=True,args=browsargs)
    page = await browser.newPage()
    await stealth(page)
    try:
        await page.authenticate({'username':driver_proxy[2], 'password': driver_proxy[3]})
    except:
        pass
    print("\u001b[36m")
    print(f"[{site}] Task[{task}][{keyword}][{size}]PRELOADING CHECKOUT")
    await page.goto('https://kith.com/products/kith-classics-x-stance-crew-sock-grey?variant=50813173831')
    await page.click('[name="add"]')
    await page.waitForSelector('[name="checkout"]')
    await page.goto('https://kith.com/checkout')
    await page.waitForSelector('[id="checkout_shipping_address_first_name"]')
    await page.evaluate(f"""() => {{document.getElementById('checkout_shipping_address_first_name').value = '{profile_firstname}';}}""")
    await page.evaluate(f"""() => {{document.getElementById('checkout_shipping_address_last_name').value = '{profile_lastname}';}}""")
    await page.evaluate(f"""() => {{document.getElementById('checkout_shipping_address_address1').value = '{profile_address}';}}""")
    await page.evaluate(f"""() => {{document.getElementById('checkout_shipping_address_city').value = '{profile_city}';}}""")
    await page.evaluate(f"""() => {{document.getElementById('checkout_shipping_address_zip').value = '{profile_zip}';}}""")
    await page.evaluate(f"""() => {{document.getElementById('checkout_shipping_address_phone').value = '{profile_phone}';}}""")
    await page.type('[id="checkout_email"]', profile_email)
    await page.select('[id="checkout_shipping_address_province"]', profile_state)
    await page.click('[id="continue_button"]')
    await page.waitForSelector('[class="radio__label__primary"]')
    await asyncio.sleep(1)
    await page.click('[id="continue_button"]')
    await asyncio.sleep(1)
    await page.waitForSelector('[class="radio__label payment-method-wrapper "]')
    bypass_link = page.url
    await page.goto('https://www.kith.com/cart/change?line=1&quantity=0')
    print(f"[{site}] Task[{task}][{keyword}][{size}]PRELOAD COMPLETED")
    await page.goto(keyword)
    input(f"[{site}] Task[{task}][{keyword}][{size}]ENTER TO BEGIN SEARCHING")
    x=0
    while x==0:
        try:
            element = await page.xpath('/html/body/div[2]/main/div[2]/section/div[2]/h1')
            item_name = await page.evaluate('(element) => element.textContent', element[0])
            x=1
        except:
            await page.reload()
            print(f"[{site}] Task[{task}][{keyword}][{size}]PRODUCT NOT FOUND RETRYING")
    element = await page.xpath('/html/body/div[2]/main/div[2]/section/div[2]/div[1]/span')
    item_price = await page.evaluate('(element) => element.textContent', element[0])
    element = await page.xpath('/html/body/div[2]/main/div[2]/section/div[1]/div/div/div/div[1]/div/img')
    item_image = 'https://seeklogo.com/images/K/kith-logo-7EF91B70CE-seeklogo.com.png'
    print(f"[{site}] Task[{task}][{keyword}][{size}]PRODUCT FOUND ADDING \u001b[35m" + item_name + "\u001b[36m TO CART")
    start_time = time.time()
    await page.select('[id="SingleOptionSelector-0"]',size)
    await page.click('[name="add"]')
    config.cart = config.cart + 1
    updatetab(config.cart, config.tasks, config.captcha, config.success, config.failed)
    try:
        await page.waitForSelector('[name="checkout"]')
    except:
        print(f"[{site}] Task[{task}][{keyword}][{size}]PRODUCT OOS")
        exit()
    await page.goto(bypass_link)
    await page.waitForXPath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[2]/div/div/iframe')
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[2]/div/div/iframe")
    await elements[0].type(profile_firstname+profile_lastname)
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/div/div[1]/iframe")
    await elements[0].type(profile_card[0])
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[3]/div/div/iframe")
    await elements[0].type(profile_cardexpmonth)
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/div/div[1]/iframe")
    await elements[0].type(profile_card[1])
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[3]/div/div/iframe")
    await elements[0].type(profile_cardexpyear)
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/div/div[1]/iframe")
    await elements[0].type(profile_card[2])
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[4]/div/div[1]/iframe")
    await elements[0].type(profile_cardcvv)
    elements = await page.xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/div/div[1]/iframe")
    await elements[0].type(profile_card[3])
    await page.click('[id="continue_button"]')
    end_time = time.time()
    final_time = str(end_time - start_time)
    print(final_time)
    try:
        await asyncio.sleep(5)
        await page.waitForXPath("/html/body/div[2]/div/div[1]/div[2]/div[1]/div/form/div[1]/div[2]/div[2]")
        print(f"\u001b[31;1m[{site}] Task[{task}][{keyword}][{size}]PAYMENT ERROR CHECKOUT FAILED")
        print("\u001b[0m")
        config.failed = config.failed + 1
        updatetab(config.cart, config.tasks, config.captcha, config.success, config.failed)
        allusercheckouts(item_name, item_price, "DECLINE", 0xE74C3C, profile_data, 'https://discord.com/api/webhooks/', item_image)
        errorwebhook(hook,item_name, item_price, "Your card failed", 0xE74C3C, profile_data,final_time, item_image,PROXY)
    except:
        print(f"\u001b[32;1m[{site}] Task[{task}][{keyword}][{size}]CHECK EMAIL!")
        config.success = config.success + 1
        updatetab(config.cart, config.tasks, config.captcha, config.success, config.failed)
        errorwebhook(hook,item_name, item_price, "HIGH HYPE ON TOP YOU GOT IT", 0x00FF00, profile_data, final_time,item_image,PROXY)
        allusercheckouts(item_name, item_price, "COPPED!", 0x00FF00, profile_data, 'https://discord.com/api/webhooks/', item_image)
    await browser.close()
    config.tasks = config.tasks - 1
    updatetab(config.cart, config.tasks, config.captcha, config.success, config.failed)
