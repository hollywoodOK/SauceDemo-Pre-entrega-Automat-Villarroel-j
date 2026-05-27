# Proyecto de Automatización de Pruebas - SauceDemo

Este proyecto es un framework de automatización de pruebas de interfaz de usuario para la plataforma de práctica SauceDemo, usando Page Object Model (POM).

## Propósito del Proyecto
Validar los flujos críticos del negocio de la aplicación web de extremo a extremo, asegurando la estabilidad de los componentes principales:
- Autenticación de usuarios con manejo de estados válidos.
- Navegación, visualización de productos y control de interfaces del catálogo.
- Flujo completo de adición de productos al carrito de compras y consistencia de datos.

## Tecnologías Utilizadas
- **Python 3.11+**: Lenguaje de programación base.
- **Selenium WebDriver**: Herramienta para la automatización y control de navegadores web.
- **Pytest**: Framework para la gestión, estructuración y ejecución de los casos de prueba.
- **Webdriver-Manager**: Gestor automatizado de controladores binarios (Drivers) para el navegador.
- **Pytest-HTML**: Extensión para la generación de reportes gráficos y estadísticos en formato web.

## Instalación de Dependencias

1. Tener un entorno virtual activo dentro de la carpeta raíz del proyecto:
   ```bash
   python -m venv venv
   # En Windows (PowerShell):
   .\venv\Scripts\activate