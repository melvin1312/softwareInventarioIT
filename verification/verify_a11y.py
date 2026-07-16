import os
from playwright.sync_api import sync_playwright

def test_a11y():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = os.path.abspath("stitch_gesti_n_de_activos_it/stitch_gesti_n_de_activos_it/inventario_de_activos/code.html")
        page.goto(f"file://{file_path}")

        # 1. Skip Link
        page.keyboard.press("Tab")
        page.screenshot(path="verification/1_skip_link_focus.png")

        # 2. Search Input
        search_input = page.get_by_role("textbox", name="Buscar activos")
        search_input.focus()
        page.screenshot(path="verification/2_search_focus.png")

        # 3. Notification Button
        notif_btn = page.get_by_role("button", name="Notificaciones")
        notif_btn.focus()
        page.screenshot(path="verification/3_notif_focus.png")

        # 4. Table Action Button
        action_btns = page.get_by_role("button", name="Más acciones")
        action_btns.first.focus()
        page.screenshot(path="verification/4_table_action_focus.png")

        # 5. Pagination
        page.get_by_role("button", name="Página 2").focus()
        page.screenshot(path="verification/5_pagination_focus.png")

        browser.close()

if __name__ == "__main__":
    test_a11y()
