# Hackathon 2023 - Nicaragua | Backend (REST API)

Ejecuta el proyecto usando "flask run" y luego ve a la ruta:
- http://localhost:500/docs - Esa es la ruta en que se encuentra la documentacion de la REST API implementada con Swagger UI.

## ¿Como realizar las migraciones?

1. Crea el archivo con el modelo que se creara.
2. Cuando el modelo este listo agrega la clase al archivo __init__.py del modulo "models".
3. Automaticamente los modelos se cargaran y estaran listos para las migraciones.
4. Ejecuta en la terminal o consola "flask db migrate". Esto realizara la migracion a la base de datos pero no aplicara los cambios
5. Para aplicar los cambios luego de la migracion usa "flask db upgrade". Con esto los cambios ya estaran reflejados en la base de datos.

NOTA: Si se elimina la carpeta "migrations" del proyecto, puedes generar nuevamente la carpeta con el comando "flask db init". Luego realiza los
comandos para las migraciones "flask db migrate" y "flask db upgrade".
