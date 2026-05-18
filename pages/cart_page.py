from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_nombre_producto_en_carrito(self):
        item_name = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        return item_name.text