import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://kaspi.kz/mc/#/orders?status=NEW")
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

            # 4. Нажимаем на категорию (например, Украшения → Бижутерия → Колье)
            await page.click('text="Украшения"')
            await page.wait_for_timeout(500)
            await page.click('text="Бижутерия"')
            await page.wait_for_timeout(500)
            await page.click('text="Колье"')
            await page.wait_for_timeout(1000)

            # 5. Кнопка "Далее"
            await page.click('button:has-text("Далее")')
            await page.wait_for_timeout(3000)

            print("[✓] Готово. Страница заполнения карточки открыта.")
        except Exception as e:
            print(f"[!] Ошибка при кликах: {e}")

        await asyncio.sleep(99999)

asyncio.run(main())
