from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso(driver):
    # 1. Navegar a la página y ejecutar el login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Espera de validación
    wait = WebDriverWait(driver, 10)

    # 2. Primera validación: URL redirigida a /inventory.html
    # Se espera a que la URL cambie
    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "La URL no contiene /inventory.html"

    # 3. Segunda Validación: Presencia del texto "Products" y "Swag Labs"
    # Validamos el título "Products" usando la clase 'title'
    titulo_productos = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo_productos.text == "Products", "No se encoentró el título 'Products'"

    # Adicionalmente validamos el logo "Swag Labs" usando la clase 'app_logo'
    logo_swag = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    assert logo_swag.text == "Swag Labs", "No se encontró el texto 'Swag Labs'"