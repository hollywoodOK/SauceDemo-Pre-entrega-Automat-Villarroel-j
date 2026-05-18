from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def obtener_titulo(self):
        titulo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return titulo.text
    
    def hay_productos_visibles(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        productos = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        return len(productos) > 0
    
    def obtener_datos_primer_producto(self):
        nombre = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        return nombre, precio
    
    def elementos_interfaz_presentes(self):
        menu_presente = self.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
        filtro_presente = self.driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
        return menu_presente and filtro_presente
    
    def agregar_primer_producto_al_carrito(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    def obtener_contador_carrito(self):
        badge = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        return badge.text
    
    def ir_al_carrito(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()