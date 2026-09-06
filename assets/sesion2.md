## **Sesión 2. Base de Datos Semiestructurada (XML)**

- **01. Definición de Datos Semiestructurados**
- **02. Introducción a XML***
- **03. Consultando Datos con XPath, XQuery y SQL/XML**
- **04. Motores de Consulta XML**

### **¿Por qué las bases de datos relacionales no siempre son suficientes para modelar toda la información empresarial?**

Las **bases de datos relacionales** han sido durante décadas la principal tecnología para almacenar y gestionar información empresarial. Su modelo basado en tablas, filas y columnas permite organizar los datos de forma estructurada, garantizar la integridad de la información y realizar consultas eficientes mediante SQL.

Sin embargo, el crecimiento de las organizaciones y la transformación digital han generado nuevos tipos de datos y necesidades que no siempre pueden ser representados eficientemente mediante un modelo relacional tradicional.

### Limitaciones de las Bases de Datos Relacionales

#### Estructura Rígida

Las bases de datos relacionales requieren un esquema previamente definido. Esto significa que todas las tablas deben tener una estructura fija y que cualquier cambio puede requerir modificaciones complejas en el diseño de la base de datos.

Por ejemplo, si una empresa necesita agregar nuevos atributos a miles de registros, puede ser necesario modificar la estructura de las tablas existentes.

#### Dificultad para Manejar Datos Heterogéneos

La información empresarial moderna proviene de múltiples fuentes y formatos, tales como:

- Correos electrónicos.
- Redes sociales.
- Documentos PDF.
- Archivos XML y JSON.
- Imágenes y videos.
- Registros de sensores IoT.

Muchos de estos datos no encajan fácilmente en filas y columnas tradicionales.

#### Problemas de Escalabilidad

Cuando el volumen de información crece considerablemente, las bases de datos relacionales pueden enfrentar desafíos relacionados con:

- Rendimiento.
- Almacenamiento.
- Procesamiento distribuido.
- Disponibilidad en tiempo real.

Esto es especialmente común en entornos de Big Data.

#### Relaciones Complejas

Algunos dominios presentan estructuras de datos altamente interconectadas.

Por ejemplo:

- Redes sociales.
- Sistemas de recomendación.
- Redes de transporte.
- Sistemas de detección de fraude.

Modelar estas relaciones mediante tablas y múltiples uniones (*JOINs*) puede resultar complejo y afectar el rendimiento.

### Nuevas Necesidades Empresariales

Las organizaciones actuales necesitan trabajar con:

- Grandes volúmenes de datos.
- Datos generados en tiempo real.
- Información semiestructurada.
- Datos provenientes de múltiples plataformas.
- Sistemas distribuidos y escalables.

Estas necesidades han impulsado el desarrollo de nuevas tecnologías complementarias a las bases de datos relacionales.

### Soluciones Alternativas

#### Bases de Datos NoSQL

Permiten almacenar información con estructuras más flexibles.

Ejemplos:

- MongoDB
- Cassandra
- Redis

Ventajas:

- Escalabilidad horizontal.
- Flexibilidad en los datos.
- Alto rendimiento para grandes volúmenes de información.

#### Bases de Datos de Grafos

Están diseñadas para representar relaciones complejas entre entidades.

Ejemplos:

- Neo4j
- Amazon Neptune

Aplicaciones:

- Redes sociales.
- Recomendación de productos.
- Detección de fraudes.

#### Big Data

Tecnologías como Hadoop y Spark permiten procesar enormes cantidades de información que superan la capacidad de los sistemas tradicionales.

#### Bases de Datos Semiestructuradas

Utilizan formatos como XML y JSON para almacenar datos con estructuras variables.

Beneficios:

- Mayor flexibilidad.
- Fácil intercambio de información.
- Integración con aplicaciones modernas.

#### Ejemplo Empresarial

Supongamos una empresa de comercio electrónico que desea analizar:

- Transacciones de compra.
- Comentarios de clientes.
- Fotografías de productos.
- Interacciones en redes sociales.
- Datos de navegación web.

Mientras que las transacciones pueden almacenarse fácilmente en una base de datos relacional, los comentarios, imágenes y publicaciones en redes sociales requieren modelos más flexibles y tecnologías especializadas para su almacenamiento y análisis.

### 1.1 Definición de Datos Semiestructurados

Los **datos semiestructurados** son aquellos que no siguen un esquema rígido y predefinido como el de una base de datos relacional, pero que sí poseen una organización interna que permite identificar y relacionar los datos mediante etiquetas, atributos o claves.

En este tipo de datos, la estructura puede variar entre registros sin necesidad de modificar un esquema global, lo que proporciona flexibilidad para almacenar información heterogénea.

#### Características Principales

- No requieren un esquema fijo de filas y columnas.
- Utilizan etiquetas, atributos o pares clave-valor para organizar la información.
- Permiten almacenar datos con estructuras variables.
- Facilitan el intercambio de información entre diferentes sistemas.
- Son más flexibles que los modelos relacionales tradicionales.
- Pueden ser procesados tanto por personas como por aplicaciones informáticas.

#### Ejemplos de Datos Semiestructurados

Los formatos más utilizados para representar datos semiestructurados son:

- XML (eXtensible Markup Language)
- JSON (JavaScript Object Notation)
- Correos electrónicos
- Documentos HTML
- Archivos de configuración

#### Ejemplo en XML

```xml
<empleado>
    <nombre>Ana López</nombre>
    <departamento>Recursos Humanos</departamento>
    <correo>ana.lopez@empresa.com</correo>
</empleado>
```

#### Ejemplo en JSON

```json
{
    "nombre": "Ana López",
    "departamento": "Recursos Humanos",
    "correo": "ana.lopez@empresa.com"
}
```

#### Ventajas

- Mayor flexibilidad en el almacenamiento de información.
- Adaptación sencilla a cambios en los datos.
- Intercambio eficiente de información entre aplicaciones.
- Facilitan la integración de diferentes fuentes de datos.
- Son ampliamente utilizados en aplicaciones web y servicios en la nube.

#### Definición de Datos

| Tipo de dato | Características | Ejemplos |
|--------------|----------------|----------|
| **Estructurados** | Esquema fijo, filas y columnas. | SQL Server, Oracle, PostgreSQL, Excel. |
| **Semiestructurados** | Estructura flexible y jerárquica. | XML, JSON, YAML. |
| **No estructurados** | Sin estructura definida. | Imágenes, videos, correos electrónicos, PDF. |

#### Descripción General

#### Datos Estructurados
Los datos estructurados siguen un esquema predefinido y se almacenan en filas y columnas dentro de tablas. Son fáciles de consultar y analizar mediante lenguajes como SQL.

#### Datos Semiestructurados
Los datos semiestructurados poseen una organización interna basada en etiquetas, atributos o pares clave-valor. Aunque no requieren una estructura rígida, mantienen cierto orden que facilita su procesamiento.

#### Datos No Estructurados
Los datos no estructurados carecen de un esquema fijo y pueden presentarse en múltiples formatos. Generalmente requieren herramientas especializadas para su almacenamiento, procesamiento y análisis.

#### Ejemplos por Categoría

- **Estructurados:** bases de datos relacionales, hojas de cálculo e inventarios.
- **Semiestructurados:** documentos XML, archivos JSON y configuraciones YAML.
- **No estructurados:** fotografías, videos, audios, documentos PDF y publicaciones en redes sociales.


### Desventajas de las Bases de Datos Semiestructuradas

Aunque las bases de datos semiestructuradas ofrecen una gran flexibilidad para almacenar información, también presentan algunos desafíos que deben considerarse durante su implementación y uso.

#### Principales Desventajas

#### Consultas Potencialmente Más Complejas

La recuperación de información puede requerir consultas más elaboradas debido a la estructura flexible de los datos. En algunos casos, navegar entre diferentes niveles jerárquicos puede incrementar la complejidad del análisis.

#### Menor Eficiencia en Ciertas Operaciones Comparadas con Bases Relacionales

Para determinadas operaciones transaccionales o consultas altamente estructuradas, las bases de datos relacionales suelen ofrecer un mejor rendimiento y optimización.

#### Riesgo de Inconsistencias si No Existen Reglas de Validación

La ausencia de un esquema rígido puede provocar diferencias en la forma en que se almacenan los datos. Si no se implementan mecanismos de validación adecuados, pueden generarse registros inconsistentes o incompletos.

#### Estructuras Demasiado Flexibles Pueden Dificultar la Gobernanza de Datos

La flexibilidad excesiva puede complicar la administración, documentación y control de la información, especialmente en organizaciones que manejan grandes volúmenes de datos o múltiples fuentes de información.

#### **Ejemplos de datos semiestructurados**

- Catálogo de productos
- Publicaciones científicas
- Configuración de aplicaciones

#### Ejemplos

Dependiendo de la información que se requiere obtener, los datos pueden categorizarse como **estructurados** o **semiestructurados**. La elección del modelo dependerá de la naturaleza de los datos y de la flexibilidad necesaria para almacenarlos y procesarlos.

| Caso | Estructurado | Semiestructurado |
|--------|-------------|------------------|
| **Catálogo de productos** | Tabla `Productos` (id, nombre, precio). | XML o JSON donde cada producto puede tener atributos distintos. |
| **Publicaciones científicas** | Tabla de artículos con campos fijos. | XML o JSON con autores, referencias y anexos variables. |
| **Configuración de aplicaciones** | Tabla de parámetros. | Archivos XML o JSON con estructura jerárquica. |

#### Análisis de los Casos

#### Catálogo de Productos

Cuando todos los productos comparten los mismos atributos (identificador, nombre, precio, categoría, etc.), una base de datos relacional resulta adecuada.

Sin embargo, si cada producto puede tener características diferentes, como:

- Talla y color para ropa.
- Capacidad y procesador para computadoras.
- Peso y dimensiones para electrodomésticos.

Un formato semiestructurado como XML o JSON ofrece mayor flexibilidad.

#### Publicaciones Científicas

Las publicaciones pueden contener una cantidad variable de:

- Autores.
- Referencias bibliográficas.
- Palabras clave.
- Anexos.
- Archivos complementarios.

Debido a esta variabilidad, los formatos semiestructurados facilitan el almacenamiento de información sin imponer una estructura rígida.

#### Configuración de Aplicaciones

Las aplicaciones suelen manejar configuraciones jerárquicas con múltiples niveles de parámetros.

Por ejemplo:

```json
{
  "servidor": {
    "host": "localhost",
    "puerto": 8080
  },
  "seguridad": {
    "autenticacion": true
  }
}
```

Este tipo de información puede modelarse  

# 1.2 Introducción a XML

## ¿Qué son XML y JSON?

**XML (eXtensible Markup Language)** y **JSON (JavaScript Object Notation)** son formatos ampliamente utilizados para representar, almacenar e intercambiar información entre aplicaciones y sistemas.

### Características Principales

1. **Son formatos para representar datos semiestructurados.**

   Permiten almacenar información que no necesariamente sigue un esquema rígido de filas y columnas, ofreciendo mayor flexibilidad que las bases de datos relacionales tradicionales.

2. **Son autodescriptivos.**

   La información incluye etiquetas o claves que describen el significado de cada dato, facilitando su interpretación tanto por personas como por sistemas informáticos.

3. **Permiten estructuras jerárquicas.**

   Los datos pueden organizarse en distintos niveles, estableciendo relaciones padre-hijo para representar información compleja de forma natural.

4. **Se utilizan para el intercambio e integración de información.**

   Son ampliamente empleados para compartir datos entre aplicaciones, servicios web, bases de datos y sistemas distribuidos.

## Aplicaciones Comunes

- Integración de sistemas empresariales.
- Servicios web y APIs.
- Intercambio de datos entre organizaciones.
- Almacenamiento de configuraciones.
- Aplicaciones móviles y web.
- Bases de datos semiestructuradas.

## Ejemplo en XML

```xml
<empleado>
    <nombre>Ana López</nombre>
    <departamento>Recursos Humanos</departamento>
</empleado>
```

## Ejemplo en JSON

```json
{
    "nombre": "Ana López",
    "departamento": "Recursos Humanos"
}
```

# ¿Cómo se Conforma un XML?

Un documento **XML (eXtensible Markup Language)** está compuesto por diferentes elementos que permiten organizar la información de manera jerárquica y estructurada. Gracias a estos componentes, XML puede representar datos complejos de forma clara y flexible.

## Componentes de un Documento XML

### 1. Declaración XML

Es la primera línea del documento y especifica la versión de XML y la codificación utilizada.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

### 2. Elemento Raíz

Es el elemento principal que contiene a todos los demás elementos del documento. Todo documento XML debe tener un único elemento raíz.

```xml
<pacientes>
    ...
</pacientes>
```

### 3. Elementos

Son las etiquetas que almacenan la información dentro del documento XML.

```xml
<nombre>Juan Pérez</nombre>
<edad>45</edad>
<sexo>M</sexo>
```

### 4. Atributos

Los atributos proporcionan información adicional sobre un elemento y se incluyen dentro de la etiqueta de apertura.

```xml
<paciente id="1001">
```

En este caso, **id** es un atributo del elemento **paciente**.

### 5. Texto

Corresponde al contenido almacenado dentro de los elementos.

```xml
<diagnostico>Diabetes</diagnostico>
```

El texto contenido es:

```text
Diabetes
```

### 6. Relaciones Padre-Hijo-Hermano

La estructura XML es jerárquica, por lo que existen relaciones entre sus elementos.

#### Relación Padre-Hijo

```xml
<paciente>
    <nombre>Juan Pérez</nombre>
</paciente>
```

- **paciente** es el elemento padre.
- **nombre** es el elemento hijo.

#### Relación entre Hermanos

```xml
<paciente>
    <nombre>Juan Pérez</nombre>
    <edad>45</edad>
    <sexo>M</sexo>
</paciente>
```

Los elementos **nombre**, **edad** y **sexo** son hermanos porque comparten el mismo elemento padre.

#### Ejemplo Completo de XML

```xml
<?xml version="1.0" encoding="UTF-8"?>

<pacientes>

    <paciente id="1001">
        <nombre>Juan Pérez</nombre>
        <edad>45</edad>
        <sexo>M</sexo>
        <diagnostico>Diabetes</diagnostico>
    </paciente>

    <paciente id="1002">
        <nombre>María López</nombre>
        <edad>32</edad>
        <sexo>F</sexo>
        <diagnostico>Hipertensión</diagnostico>
    </paciente>

    <paciente id="1003">
        <nombre>Carlos Ruiz</nombre>
        <edad>58</edad>
        <sexo>M</sexo>
        <diagnostico>Diabetes</diagnostico>
    </paciente>

</pacientes>
```

#### Estructura Jerárquica

```text
pacientes
│
├── paciente (id=1001)
│   ├── nombre
│   ├── edad
│   ├── sexo
│   └── diagnostico
│
├── paciente (id=1002)
│   ├── nombre
│   ├── edad
│   ├── sexo
│   └── diagnostico
│
└── paciente (id=1003)
    ├── nombre
    ├── edad
    ├── sexo
    └── diagnostico
```

### ¿Cómo se Conforma un JSON?

**JSON (JavaScript Object Notation)** es un formato de intercambio de datos ligero y ampliamente utilizado para representar información semiestructurada. Su estructura se basa en pares **clave-valor**, lo que facilita la lectura tanto para las personas como para los sistemas informáticos.

#### Componentes de un JSON

#### Objetos `{}`

Los objetos son la estructura principal en JSON y se representan mediante llaves `{}`. Un objeto contiene uno o más pares clave-valor.

```json
{
  "nombre": "Juan Pérez"
}
```

#### Claves

Las claves son los identificadores que describen cada dato almacenado dentro del objeto.

```json
{
  "nombre": "Juan Pérez",
  "edad": 45
}
```

En este ejemplo, **nombre** y **edad** son claves.

#### Valores

Los valores corresponden a la información asociada a cada clave.

```json
{
  "nombre": "Juan Pérez",
  "edad": 45
}
```

Los valores son:

- "Juan Pérez"
- 45

#### Arreglos `[]`

Los arreglos permiten almacenar múltiples valores dentro de una misma clave.

```json
{
  "telefonos": [
    "4491234567",
    "4497654321"
  ]
}
```

#### Objetos Anidados

Un objeto JSON puede contener otros objetos en su interior, permitiendo crear estructuras jerárquicas.

```json
{
  "paciente": {
    "nombre": "Juan Pérez",
    "edad": 45
  }
}
```

#### Ejemplo Completo

```json
{
  "id": 1001,
  "nombre": "Juan Pérez",
  "edad": 45,
  "diagnostico": "Diabetes",
  "medicamentos": [
    "Metformina",
    "Insulina"
  ],
  "contacto": {
    "telefono": "4491234567",
    "correo": "juan@email.com"
  }
}
```

#### Estructura Jerárquica

```text
Paciente
│
├── id
├── nombre
├── edad
├── diagnostico
├── medicamentos
│   ├── Metformina
│   └── Insulina
│
└── contacto
    ├── telefono
    └── correo
```

#### Características de JSON

- Se basa en pares **clave-valor**.
- Utiliza una sintaxis simple y fácil de leer.
- Permite almacenar información jerárquica.
- Soporta arreglos y objetos anidados.
- Es ampliamente utilizado en APIs y aplicaciones web.
- Facilita el intercambio de información entre sistemas.

#### Comparación con XML
 
| JSON | XML |
|--------|--------|
| Sintaxis más simple y compacta. | Sintaxis basada en etiquetas. |
| Utiliza pares clave-valor. | Utiliza elementos y atributos. |
| Menor tamaño de almacenamiento. | Generalmente más extenso. |
| Muy utilizado en APIs modernas. | Muy utilizado en integración empresarial y documentos estructurados. |

### Equivalencias XML vs JSON

Tanto **XML** como **JSON** son formatos utilizados para representar e intercambiar datos semiestructurados. La elección entre uno y otro dependerá de las necesidades específicas del proyecto, los requisitos de interoperabilidad y las características de los sistemas involucrados.

#### XML

**XML (eXtensible Markup Language)** es una tecnología ampliamente utilizada en entornos empresariales debido a sus capacidades de validación y organización de información compleja.

#### Principales características

- Alta interoperabilidad entre sistemas.
- Adecuado para documentos complejos y extensos.
- Permite validación mediante DTD y XML Schema.
- Facilita la representación de estructuras jerárquicas.
- Utilizado en estándares empresariales y gubernamentales.

#### Casos de uso

- Intercambio de información entre organizaciones.
- Sistemas empresariales (ERP, CRM).
- Documentos electrónicos.
- Facturación electrónica.
- Servicios web basados en SOAP.

---

### JSON

**JSON (JavaScript Object Notation)** es un formato ligero diseñado para el intercambio eficiente de datos entre aplicaciones.

#### Principales características

- Sintaxis simple y fácil de leer.
- Menor tamaño comparado con XML.
- Procesamiento más rápido.
- Fácil integración con aplicaciones web.
- Altamente utilizado en APIs y microservicios.

#### Casos de uso

- APIs REST.
- Aplicaciones web y móviles.
- Microservicios.
- Servicios en la nube.
- Intercambio rápido de datos entre sistemas.

---

#### Comparación General

| Aspecto | XML | JSON |
|----------|------|------|
| Formato | Basado en etiquetas | Basado en pares clave-valor |
| Legibilidad | Más verboso | Más compacto |
| Tamaño | Mayor | Menor |
| Velocidad de procesamiento | Menor | Mayor |
| Validación | DTD, XML Schema | JSON Schema |
| Uso principal | Integración empresarial | APIs y aplicaciones web |
| Soporte para documentos complejos | Excelente | Bueno |

#### ¿Cuál Elegir?

La elección entre XML y JSON depende de los requisitos del proyecto:

#### Utilice XML cuando:

- Se requiera interoperabilidad empresarial.
- Existan estándares institucionales establecidos.
- Sea necesaria la validación rigurosa de documentos.
- Se trabaje con estructuras documentales complejas.

#### Utilice JSON cuando:

- Se desarrollen APIs modernas.
- Se implementen arquitecturas de microservicios.
- Se busque minimizar el tamaño de los datos.
- Se requiera un procesamiento rápido y eficiente.

### 1.3 Consultando Datos con XPath, XQuery y SQL/XML

#### ¿Qué es XPath?

**XPath (XML Path Language)** es un lenguaje de navegación utilizado para localizar y seleccionar elementos, atributos y datos dentro de un documento XML.

XPath permite recorrer la estructura jerárquica de un XML mediante rutas, de forma similar a como se navega entre carpetas en un sistema de archivos.

#### Analogía

XPath puede compararse con:

1. **Las rutas de carpetas en Windows o Linux** para localizar archivos y directorios.
2. **La cláusula SELECT en SQL**, utilizada para recuperar datos específicos de una base de datos.

---

#### ¿Para Qué Sirve XPath?

XPath permite:

- Seleccionar elementos específicos.
- Filtrar información mediante condiciones.
- Acceder a atributos.
- Navegar entre nodos padre, hijo o hermanos.
- Localizar información dentro de documentos XML complejos.

---

#### Ejemplo de Documento XML

```xml
<pacientes>

    <paciente id="1001">
        <nombre>Juan Pérez</nombre>
        <edad>45</edad>
        <diagnostico>Diabetes</diagnostico>
    </paciente>

    <paciente id="1002">
        <nombre>María López</nombre>
        <edad>32</edad>
        <diagnostico>Hipertensión</diagnostico>
    </paciente>

</pacientes>
```

---

#### Ejemplos de Expresiones XPath

#### Seleccionar todos los pacientes

```xpath
/pacientes/paciente
```

Resultado:

```text
paciente
paciente
```

#### Seleccionar todos los nombres

```xpath
/pacientes/paciente/nombre
```

Resultado:

```text
Juan Pérez
María López
```

#### Seleccionar el diagnóstico del primer paciente

```xpath
/pacientes/paciente[1]/diagnostico
```

Resultado:

```text
Diabetes
```

#### Seleccionar un paciente por atributo

```xpath
/pacientes/paciente[@id='1002']
```

Resultado:

```xml
<paciente id="1002">
    <nombre>María López</nombre>
    <edad>32</edad>
    <diagnostico>Hipertensión</diagnostico>
</paciente>
```

---

#### Navegación en XPath

#### Nodo Padre

```xpath
..
```

Permite regresar al elemento padre.

#### Nodo Actual

```xpath
.
```

Representa el elemento actual.

#### Todos los Hijos

```xpath
*
```

Selecciona todos los elementos hijos.

#### Búsqueda en Todo el Documento

```xpath
//nombre
```

Busca todos los elementos llamados **nombre** sin importar su ubicación dentro del XML.

---

