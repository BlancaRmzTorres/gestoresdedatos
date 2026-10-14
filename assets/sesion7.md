# 3. Bases de Datos para la Toma de Decisiones

## Introducción

Las organizaciones generan grandes cantidades de datos a través de sus operaciones diarias. Para convertir esos datos en información útil para la toma de decisiones se utilizan tecnologías como los Data Warehouse y OLAP.

---

# Contenido

1. Data Warehouse
2. OLAP
3. Operaciones OLAP
4. Granularidad
5. Esquema Estrella
6. Tipos de OLAP
7. KPI
8. Ventajas y Desventajas

---

# Data Warehouse

## ¿Qué es?

Un Data Warehouse es un repositorio centralizado que integra información proveniente de múltiples sistemas para apoyar el análisis y la toma de decisiones.

### Características

- Integración de datos.
- Información histórica.
- Optimizado para análisis.
- Fuente única de información confiable.
- Soporte para Business Intelligence.

### ETL

**Extract, Transform, Load**

1. Extraer datos.
2. Transformar datos.
3. Cargar datos.

### Data Mart

Subconjunto especializado del Data Warehouse orientado a un área específica del negocio.

Ejemplos:
- Ventas
- Finanzas
- Recursos Humanos
- Producción

---

# OLAP (Online Analytical Processing)

Permite analizar grandes volúmenes de datos desde diferentes perspectivas.

## Beneficios

- Consultas rápidas.
- Análisis multidimensional.
- Exploración interactiva.
- Soporte a la toma de decisiones.

---

# Operaciones OLAP

## Drill Down

Permite pasar de un nivel general a uno más detallado.

Ejemplo:

Ventas Anuales → Trimestrales → Mensuales → Diarias

## Roll Up

Proceso inverso al Drill Down.

Ventas Diarias → Mensuales → Trimestrales → Anuales

## Slice

Filtrado sobre una dimensión.

Ejemplo: Año = 2026.

## Dice

Filtrado sobre varias dimensiones.

Ejemplo:

- Año = 2026
- Producto = Laptop
- Estado = Aguascalientes

---

# Granularidad

Representa el nivel de detalle de los datos.

## Granularidad Alta

Mayor detalle y precisión.

## Granularidad Baja

Mayor velocidad y menor almacenamiento.

---

# Esquema Estrella

Modelo dimensional formado por:

- Tabla de hechos.
- Tablas de dimensiones.

## Tabla de Hechos

Contiene medidas del negocio:

- Ventas
- Costos
- Cantidades
- Utilidades

## Dimensiones

### Tiempo
- Año
- Mes
- Día

### Producto
- Producto
- Categoría
- Marca

### Geografía
- País
- Estado
- Ciudad

### Tienda
- Región
- Sucursal

---

# Tipos de OLAP

## MOLAP

Cubos multidimensionales precalculados.

### Ventajas
- Consultas muy rápidas.

### Desventajas
- Mayor almacenamiento.

## ROLAP

Análisis directamente sobre bases relacionales.

### Ventajas
- Escalable.

### Desventajas
- Menor velocidad.

## HOLAP

Combina MOLAP y ROLAP.

---

# KPI

KPI significa Key Performance Indicator (Indicador Clave de Desempeño).

Ejemplos:

- Ventas totales.
- Rentabilidad.
- Crecimiento porcentual.
- Participación de mercado.
- Satisfacción del cliente.

---

# Flujo de Información

```text
Datos Operacionales
        ↓
      ETL
        ↓
 Data Warehouse
        ↓
 Modelo Dimensional
        ↓
   Cubo OLAP
        ↓
 Operaciones OLAP
        ↓
      KPI
        ↓
Toma de Decisiones
```

---

# Conclusión

El Data Warehouse y OLAP son tecnologías fundamentales dentro de la Inteligencia de Negocios. Permiten integrar información, analizar grandes volúmenes de datos, generar indicadores y apoyar decisiones estratégicas basadas en evidencia. Mientras que el Data Warehouse organiza y almacena la información histórica, OLAP facilita su exploración desde distintas perspectivas para descubrir patrones, tendencias y oportunidades de mejora.
