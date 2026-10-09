import os
from playwright.sync_api import sync_playwright

def test_inventory_a11y():
    file_path = os.path.abspath('stitch_gesti_n_de_activos_it/stitch_gesti_n_de_activos_it/inventario_de_activos/code.html')
    url = f'file://{file_path}'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Test skip link
        page.keyboard.press('Tab')
        skip_link = page.locator('a[href="#main-content"]')
        assert skip_link.is_visible(), "Skip link should be visible when focused"

        page.keyboard.press('Enter')
        main_focused = page.evaluate('document.activeElement.id')
        assert main_focused == 'main-content', f"Expected main-content focused, got {main_focused}"

        # Test search input
        search_input = page.locator('input[aria-label="Buscar por ID, dispositivo o usuario"]')
        assert search_input.count() == 1, "Search input should have aria-label"

        # Test pagination nav
        pagination_nav = page.locator('nav[aria-label="Paginación de inventario"]')
        assert pagination_nav.count() == 1, "Pagination nav should be present with aria-label"

        page.screenshot(path='/home/jules/inventory_a11y.png')
        print("Inventory A11y verification passed successfully!")
        browser.close()

if __name__ == '__main__':
    test_inventory_a11y()
