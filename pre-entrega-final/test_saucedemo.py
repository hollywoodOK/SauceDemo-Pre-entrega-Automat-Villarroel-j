from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_login_exitoso(driver):
    """Prueba 1: Validar inicio de sesión correcto"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    assert "/inventory.html" in driver.current_url, "No se redirigió a la página de inventario"

def test_flujo_carrito_completo(driver):
    """Prueba 2: Validar adición de producto y verificación en el carrito"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    nombre_esperado, _ = inventory_page.obtener_datos_primer_producto()

    inventory_page.agregar_primer_producto_al_carrito()
    assert inventory_page.obtener_contador_carrito() == "1", "El carrito no se actualizó"

    inventory_page.ir_al_carrito()
    
    cart_page = CartPage(driver)
    assert "/cart.html" in driver.current_url, "No se redirigió a la página del carrito"
    assert cart_page.obtener_nombre_producto_en_carrito() == nombre_esperado, "El producto no coincide"