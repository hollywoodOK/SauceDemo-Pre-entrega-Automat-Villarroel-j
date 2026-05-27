from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_login_exitoso(driver):
    """Prueba 1: Validar inicio de sesión correcto"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    assert "/inventory.html" in driver.current_url, "No se redirigió a la página de inventario"

def test_verificación_catalogo(driver):
    """Prueba 2: Validar componentes del catálogo (Título, Interfaz y Productos)"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_titulo() == "Products", "El título es incorrecto"
    assert inventory_page.elementos_interfaz_presentes(), "Faltan elementos en la interfaz"
    assert inventory_page.hay_productos_visibles(), "No se encontraron productos"

    # Mostramos el primer producto en consola
    nombre, precio = inventory_page.obtener_datos_primer_producto()
    print(f"\n[CATÁLOGO] Primer producto: {nombre} - Precio: {precio}")

def test_flujo_carrito_completo(driver):
    """Prueba 3: Validar adición de producto y verificación en el carrito"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    nombre_esperado, _ = inventory_page.obtener_datos_primer_producto()

    inventory_page.agregar_primer_producto_al_carrito()
    assert inventory_page.obtener_contador_carrito() == "1", "El carrito no se actualizó"

    inventory_page.ir_al_carrito()
    assert "/cart.html" in driver.current_url, "No se redirigió a la página del carrito"

    cart_page = CartPage(driver)
    assert cart_page.obtener_nombre_producto_en_carrito() == nombre_esperado, "El producto no coincide"