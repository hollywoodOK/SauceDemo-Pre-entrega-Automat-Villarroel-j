from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_flujo_carrito_completo(driver):
    # 1. Login Exitoso
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    # Se captura el nombre del primer producto antes de agregarlo para poder compararlo al final
    nombre_esperado, _ = inventory_page.obtener_datos_primer_producto()

    # 2. Añadimos el producto al carrito
    inventory_page.agregar_primer_producto_al_carrito()

    # 3. VALIDACIÓN 1: Verificar que el contador del carrito se incremente a 1
    assert inventory_page.obtener_contador_carrito() == "1", "El contador del carrito no se actualizó a 1"

    # 4. Navegar al carrito
    inventory_page.ir_al_carrito()

    # 5. VALIDACIÓN 2: Comprobamos que el producto en el carrito sea el correcto
    cart_page = CartPage(driver)

    # Verificación extra: Comprobamos que estémos en la URL del carrito
    assert "/cart.html" in driver.current_url, "No estámos en la URL del carrito"

    # Verificación del item
    nombre_en_carrito = cart_page.obtener_nombre_producto_en_carrito()
    assert nombre_en_carrito == nombre_esperado, f"El producto en el carrito ({nombre_en_carrito}) no es el que agregamos ({nombre_esperado})"

    print(f"\n--- REQUERIMIENTO COMPLETADO ---")
    print(f"Producto verificado con éxito: {nombre_en_carrito}")
    print("--------------------------------")
