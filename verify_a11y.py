import os
from playwright.sync_api import sync_playwright

def verify_accessibility():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get absolute path to the HTML file
        file_path = os.path.abspath("stitch_gesti_n_de_activos_it/stitch_gesti_n_de_activos_it/assettrack_enterprise_inventory_management/code.html")
        page.goto(f"file://{file_path}")

        # 1. Verify Skip Link exists and has correct href
        skip_link = page.get_by_role("link", name="Saltar al contenido principal")
        assert skip_link.count() == 1
        assert skip_link.get_attribute("href") == "#main-content"

        # 2. Verify Main content has correct ID and tabindex
        main_content = page.locator("#main-content")
        assert main_content.count() == 1
        assert main_content.get_attribute("tabindex") == "-1"

        # 3. Verify Header buttons have ARIA labels
        notif_btn = page.get_by_role("button", name="Notificaciones")
        assert notif_btn.count() == 1

        history_btn = page.get_by_role("button", name="Historial de actividad")
        assert history_btn.count() == 1

        # 4. Verify Search input has ARIA label
        search_input = page.get_by_label("Buscar activos, usuarios o tickets")
        assert search_input.count() == 1

        # 5. Visual verification: Focus the skip link and take a screenshot
        page.keyboard.press("Tab")
        page.screenshot(path="/home/jules/verification/skip_link_focus.png")

        print("Accessibility foundations verified successfully.")
        browser.close()

if __name__ == "__main__":
    os.makedirs("/home/jules/verification", exist_ok=True)
    verify_accessibility()
