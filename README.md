# RESTAURANTE PIZZERIA ESPACIAL
## Sistema de Gestion de Pedidos

Sistema completo de gestion de pedidos para restaurantes desarrollado en Python con interfaz de consola. Incluye modulos separados para clientes y administradores, validaciones robustas y persistencia de datos en JSON.

---

## Descripcion del Proyecto

Sistema modular que permite:
- **Clientes**: Registrarse, ver menu, hacer pedidos y consultar historial
- **Administradores**: Gestionar menu (CRUD), gestionar pedidos, cambiar estados y ver estadisticas de ventas

El proyecto esta desarrollado siguiendo las mejores practicas de programacion, con validaciones inmediatas, manejo completo de errores y arquitectura modular.

---

## Requisitos del Sistema

- **Python**: 3.6 o superior
- **Librerias**: Solo modulos estandar (json, os, datetime, platform)
- **Sistema Operativo**: Windows, Linux o macOS

---

## Instalacion y Uso

### 1. Clonar o descargar el proyecto
```bash
# Descargar todos los archivos .py en una misma carpeta
```

### 2. Ejecutar el sistema
```bash
python main.py
```

### 3. Inicio automatico
El sistema crea automaticamente:
- Archivos JSON necesarios
- Menu inicial con 10 productos de pizzeria
- Carpetas para tickets y reportes
- Usuario administrador por defecto

---

## Credenciales por Defecto

### Administrador:
- **Usuario**: admin
- **Contrasena**: admin123

### Clave de Registro (para nuevos admins):
- **Clave**: admin2025

---

## Funcionalidades Principales

### Modo Cliente:
- Registro con validacion de datos
- Inicio de sesion seguro
- Ver menu completo organizado por categorias
- Hacer pedidos con carrito interactivo
- Ver historial de pedidos personales
- Generacion automatica de tickets en TXT

### Modo Administrador:
- Gestion completa del menu (Agregar, Modificar, Eliminar, Listar)
- Gestion de pedidos (Ver todos, Filtrar por estado)
- Cambio de estados de pedidos (Pendiente > En preparacion > Listo > Entregado)
- Estadisticas de ventas (Total ventas, Promedio, Top 5 productos)
- Exportacion de reportes detallados en TXT

---

## Flujo de Uso Tipico

### Cliente:
1. Registrarse o iniciar sesion
2. Ver menu disponible
3. Seleccionar productos y cantidades
4. Confirmar pedido
5. Recibir ticket con numero de pedido
6. Consultar estado del pedido

### Administrador:
1. Iniciar sesion con credenciales
2. Gestionar menu (agregar/modificar/eliminar productos)
3. Ver pedidos nuevos
4. Cambiar estado de pedidos a "En preparacion"
5. Marcar como "Listo" cuando termine
6. Cambiar a "Entregado" cuando el cliente recoja
7. Consultar estadisticas de ventas

---

## Solución de Problemas

**Error: "No se puede crear carpeta tickets/"**
- Verificar permisos de escritura en la carpeta
- Ejecutar como administrador si es necesario

**Error: "Error al leer archivo JSON"**
- Eliminar archivos .json corruptos
- El sistema los recreara al iniciar

**Los cambios no se guardan:**
- Verificar que no haya otro programa editando los archivos JSON
- Cerrar y reiniciar el programa

---

## Autor

Proyecto educativo - Sistema de Gestion de Pedidos para Restaurantes

**Version**: 2.0
**Fecha**: 2026
**Licencia**: Codigo abierto para uso educativo

---

## Contacto

Para preguntas o sugerencias sobre el proyecto, revisar el codigo fuente.
Todos los archivos estan comentados y organizados para facilitar el aprendizaje.
