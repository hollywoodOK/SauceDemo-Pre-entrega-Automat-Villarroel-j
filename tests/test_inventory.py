from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_verificacion_catalogo(driver):
    # 1. Usamos la clase que armamos en login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Pasamos a la página del inventario
    inventory_page = InventoryPage(driver)
    
    # 3. Lo validamos mediante el título de la página
    assert inventory_page.obtener_titulo() == "Products", "El título de la página no coincide"

    # 4. Validamos con elementos de la interfaz
    assert inventory_page.elementos_interfaz_presentes(), "Falta el menú o el filtro"
        
    # 5. Validamos con la presencia de productos
    assert inventory_page.hay_productos_visibles(), "No se cargaron productos en el catálogo"
    
    # 6. Requerimiento: Listar nombre y precio del primero
    nombre, precio = inventory_page.obtener_datos_primer_producto()
    
    # Imprimimos los datos para el reporte
    print("\n--- DATOS DEL PRIMER PRODUCTO ---")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print("----------------------------------")