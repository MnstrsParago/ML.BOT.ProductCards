import asyncio
from playwright.async_api import async_playwright
from db_handler import get_product_data

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://kaspi.kz/mc/#/orders?status=NEW")
        await page.click('text="Телефон"')
        await page.wait_for_selector('#user_phone_field', timeout=30000)
        await page.fill('#user_phone_field', '77713362613')
        await page.click('button:has-text("Продолжить")')

        print("[✓] Kaspi кабинет открыт. Войди вручную и нажми ENTER в консоли, когда будешь на главной панели.")
        input()

        try:
            # 1. Кликаем на "Управление товарами"
            await page.click('text="Управление товарами"')
            await page.wait_for_timeout(2000)

            # 2. Кликаем на "Добавить товар"
            await page.click('text="Добавить товар"')
            await page.wait_for_timeout(1000)

            # 3. Кликаем на "Создать новый товар"
            await page.click('text="Создать новый товар"')
            await page.wait_for_timeout(2000)

            # 4. Выбор категорий: Украшения → Бижутерия → Колье
            kolye_buttons = page.locator('text="Колье"')
            await kolye_buttons.nth(0).click()
            await page.wait_for_timeout(500)
            await kolye_buttons.nth(1).click()



            # 5. Кнопка "Далее"
            await page.click('button:has-text("Далее")')
            await page.wait_for_timeout(3000)

            print("[✓] Готово. Страница заполнения карточки открыта.")
            # Ждём, пока появится поле "Название товара"
            await page.wait_for_selector('xpath=//div[contains(text(), "Название товара")]/following::input[@type="text" and contains(@class, "input")]', timeout=60000)

            product = get_product_data("AZIMA-Parago-00034")
            if not product:
                print("[!] Ошибка: товар не найден в БД.")
                return

            # Заполняем только "Название товара"
            await page.fill(
                'xpath=//div[contains(text(), "Название товара")]/following::input[@type="text" and contains(@class, "input")]',
                product["kaspi_code"]
            )

            print("[✓] Название товара успешно заполнено.")



            # 6. Подтверждение перед заполнением следующих полей
            print("\n[Данные для подтверждения]")
            print(f"Бренд: {product['brand']}")
            print(f"Описание товара:\n{product['description']}")
            confirm = input("Продолжить заполнение? (Y/N): ")
            if confirm.strip().upper() != "Y":
                print("[⛔] Операция отменена пользователем.")
                return

            # 7. Заполнение бренда
            await page.click('xpath=//div[contains(text(), "Бренд")]/following::input[@type="text"][1]')
            await page.fill('xpath=//div[contains(text(), "Бренд")]/following::input[@type="text"][1]', product["brand"])
            await page.wait_for_timeout(1000)  # даем время на подгрузку выпадающего списка
            await page.click(f'text="{product["brand"]}"')
            print("[✓] Бренд заполнен.")

            # 8. Заполнение описания
            await page.fill('xpath=//div[contains(text(), "Описание товара")]/following::textarea[1]', product["description"])
            print("[✓] Описание товара заполнено.")



        except Exception as e:
            print(f"[!] Ошибка во время выполнения: {e}")

        await asyncio.sleep(99999)

asyncio.run(main())

async def click_category_chain(page, categories: list[str]):
    for i=0, i<len(categories), i++:
        cat = categories[i]
        await page.click(f'text="{cat}"')
        await page.wait_for_timeout(500)
        if i=1:
            if 
