## **Sesión 3. Base de Datos Semiestructurada (XML) y Cómputo en la nube**

- **01. Motores de consulta XML**

### **Cómputo en la nube**
- **2.1 Introducción al cómputo en la nube***
- **2.1.1 Características**
- **2.1.2 Riesgos y beneficios**
- **2.1.3 Cómputo en la nube en México y en el mundo**

### Motores de Consulta XML

Los **motores de consulta XML** son herramientas especializadas que permiten buscar, filtrar, analizar y recuperar información almacenada en documentos XML de manera eficiente. Estas herramientas facilitan el acceso a los datos sin necesidad de revisar manualmente todo el contenido del documento.

Los motores de consulta XML utilizan diferentes tecnologías y lenguajes diseñados específicamente para trabajar con estructuras jerárquicas de información, permitiendo localizar elementos, atributos y relaciones dentro de un archivo XML.

#### Principales Tecnologías Utilizadas

#### XPath

**XPath (XML Path Language)** es un lenguaje de navegación que permite localizar elementos y atributos dentro de un documento XML mediante rutas de acceso.

**Ejemplo:**

```xpath
/biblioteca/libro/titulo
```

Esta expresión selecciona todos los elementos `<titulo>` que se encuentran dentro de los elementos `<libro>`.

#### XQuery

**XQuery (XML Query Language)** es un lenguaje más avanzado que permite consultar, filtrar, ordenar y transformar documentos XML.

**Ejemplo de aplicaciones:**

- Buscar información específica.
- Filtrar datos mediante condiciones.
- Ordenar resultados.
- Generar nuevos documentos XML.
- Integrar información de múltiples documentos XML.

#### APIs de Programación

Además de XPath y XQuery, muchos lenguajes de programación ofrecen bibliotecas para manipular y consultar documentos XML.

**Ejemplos:**

- Python (`xml.etree.ElementTree`)
- Java DOM y SAX
- JavaScript XML Parser
- C# LINQ to XML

Estas herramientas permiten automatizar consultas y procesar grandes cantidades de información de forma eficiente.

#### Ventajas de los Motores de Consulta XML

- Acceso rápido a información específica.
- Automatización de procesos de búsqueda.
- Filtrado eficiente de grandes volúmenes de datos.
- Integración entre sistemas empresariales.
- Transformación y reutilización de información.
- Soporte para estructuras de datos complejas y jerárquicas.

#### Aplicaciones Comunes

Los motores de consulta XML son utilizados en:

- Sistemas empresariales.
- Intercambio de información entre organizaciones.
- Servicios web.
- Sistemas de gestión documental.
- Bases de datos semiestructuradas.
- Procesamiento de catálogos y archivos de configuración.

### ¿Qué es XQuery?

**XQuery (XML Query Language)** es un lenguaje diseñado para **consultar, extraer, filtrar, ordenar y transformar** datos almacenados en documentos XML.

Su principal objetivo es facilitar la recuperación de información dentro de estructuras XML, permitiendo realizar consultas avanzadas de manera similar a como SQL trabaja con bases de datos relacionales.

#### Función Principal

XQuery permite:

- Buscar información específica dentro de documentos XML.
- Filtrar datos mediante condiciones.
- Ordenar resultados.
- Contar elementos.
- Extraer atributos y valores.
- Generar nuevos documentos XML.
- Integrar información proveniente de múltiples archivos XML.

#### Relación con SQL

La función de XQuery es muy similar a la de SQL en las bases de datos relacionales:

```text
SQL    → Consulta tablas
XQuery → Consulta documentos XML
```

Mientras que SQL trabaja sobre tablas compuestas por filas y columnas, XQuery trabaja sobre documentos XML organizados mediante elementos, atributos y estructuras jerárquicas.

#### Ejemplo Conceptual

#### Documento XML

```xml
<biblioteca>
    <libro>
        <titulo>Introducción a XML</titulo>
        <precio>350</precio>
    </libro>
    <libro>
        <titulo>Base de Datos Avanzadas</titulo>
        <precio>1200</precio>
    </libro>
</biblioteca>
```

#### Consulta XQuery

```xquery
for $libro in /biblioteca/libro
where $libro/precio > 1000
return $libro/titulo
```

#### Resultado

```text
Base de Datos Avanzadas
```

### Ventajas de XQuery

- Permite realizar consultas complejas sobre XML.
- Facilita el manejo de grandes volúmenes de datos semiestructurados.
- Puede combinar información de varios documentos XML.
- Permite transformar datos y generar nuevos documentos XML.
- Ofrece una gran flexibilidad para el análisis y procesamiento de información.

#### Aplicaciones Comunes

XQuery es utilizado en:

- Bases de datos

### Expresiones FLWOR

Las **expresiones FLWOR** constituyen el núcleo del lenguaje **XQuery** y permiten realizar consultas complejas sobre documentos XML. Su funcionamiento es muy similar al de una consulta SQL, ya que permiten recorrer, filtrar, ordenar y devolver información específica.

El nombre **FLWOR** proviene de las iniciales de cinco palabras clave utilizadas en XQuery:

#### F - FOR

La cláusula **FOR** recorre los elementos de un documento XML de manera similar a un ciclo `for` en programación.

#### Función

- Iterar sobre una colección de elementos XML.
- Procesar cada elemento individualmente.
- Asignar temporalmente cada elemento a una variable.

#### Ejemplo

```xquery
for $libro in /biblioteca/libro
return $libro/titulo
```

---

#### L - LET

La cláusula **LET** asigna un valor a una variable sin necesidad de recorrer elementos.

#### Función

- Guardar resultados intermedios.
- Reducir repeticiones en las consultas.
- Mejorar la legibilidad del código.

#### Ejemplo

```xquery
let $precio := 1000
return $precio
```

---

#### W - WHERE

La cláusula **WHERE** permite filtrar resultados utilizando condiciones específicas.

#### Función

- Seleccionar únicamente los elementos que cumplen ciertos criterios.
- Reducir el conjunto de resultados.
- Aplicar lógica de filtrado.

#### Ejemplo

```xquery
for $libro in /biblioteca/libro
where $libro/precio > 1000
return $libro/titulo
```

---

#### O - ORDER BY

La cláusula **ORDER BY** organiza los resultados en función de uno o más criterios.

#### Función

- Ordenar datos de forma ascendente.
- Ordenar datos de forma descendente.
- Facilitar la presentación de información.

#### Ejemplo

```xquery
for $libro in /biblioteca/libro
order by $libro/precio
return $libro/titulo
```

---

#### R - RETURN

La cláusula **RETURN** devuelve el resultado final de la consulta.

#### Función

- Mostrar la información seleccionada.
- Generar nuevos documentos XML.
- Construir estructuras de salida personalizadas.

#### Ejemplo

```xquery
for $libro in /biblioteca/libro
return $libro/titulo
```

---

#### Estructura General de una Consulta FLWOR

```xquery
for $elemento in expresion
let $variable := valor
where condicion
order by criterio
return resultado
```

---

#### Ejemplo Completo

Supongamos el siguiente documento XML:

```xml
<biblioteca>
    <libro>
        <titulo>XML Básico</titulo>
        <precio>500</precio>
    </libro>

    <libro>
        <titulo>Bases de Datos Avanzadas</titulo>
        <precio>1200</precio>
    </libro>

    <libro>
        <titulo>XQuery Profesional</titulo>
        <precio>1500</precio>
    </libro>
</biblioteca>
```

Consulta XQuery:

```xquery
for $libro in /biblioteca/libro
where $libro/precio > 1000
order by $libro/titulo
return $libro/titulo
```

Resultado:

```text
Bases de Datos Avanzadas
XQuery Profesional
```

---

#### Relación entre FLWOR y SQL

| FLWOR (XQuery) | SQL |
|--------------|------|
| FOR | FROM |
| LET | Variable temporal |
| WHERE | WHERE |
| ORDER BY | ORDER BY |
| RETURN | SELECT |

---

#### Ventajas de las Expresiones FLWOR

- Permiten realizar consultas complejas sobre XML.
- Facilitan el filtrado y ordenamiento de datos.
- Mejoran la organización y legibilidad de las consultas.
- Posibilitan generar nuevos documentos XML.
- Son fundamentales para el procesamiento de información semiestructurada.


#### Diferencia entre XPath y XQuery

Tanto **XPath** como **XQuery** son tecnologías utilizadas para trabajar con documentos XML. Sin embargo, cada una tiene objetivos y capacidades distintas. Mientras XPath está orientado principalmente a la navegación y localización de información, XQuery ofrece funcionalidades más avanzadas para consultar, filtrar y transformar datos.

#### Comparación General

| XPath | XQuery |
|---------|---------|
| Navega por el XML. | Consulta y transforma documentos XML. |
| Es más simple y fácil de aprender. | Es más potente y ofrece mayores capacidades. |
| Solo localiza nodos y elementos. | Puede consultar, transformar y generar nuevos documentos XML. |
| Funciona de manera similar a una ruta de acceso. | Funciona de manera similar a SQL. |

---

#### ¿Cuándo Utilizar XPath?

XPath es recomendable cuando se necesita:

- Localizar elementos específicos.
- Navegar por la estructura de un XML.
- Acceder rápidamente a nodos o atributos.
- Realizar consultas simples.

#### Ejemplo de uso

```xpath
//libro/titulo
```

---

#### ¿Cuándo Utilizar XQuery?

XQuery es recomendable cuando se necesita:

- Filtrar datos complejos.
- Ordenar información.
- Generar nuevos XML.
- Integrar información de múltiples documentos.
- Realizar transformaciones avanzadas.

#### Ejemplo

```xquery
for $libro in /biblioteca/libro
where $libro/precio > 1000
return $libro/titulo
```
#### **Conclusión**

Los motores de consulta XML permiten recuperar información específica de documentos XML de forma rápida y eficiente. XPath facilita la búsqueda de nodos mediante expresiones de consulta, mientras que Python permite automatizar estas consultas utilizando el módulo xml.etree.ElementTree. Estas herramientas son fundamentales cuando se trabaja con grandes volúmenes de datos almacenados en formato XML.

## **Cómputo en la nube ##

### 1.1 Introducción

El **cómputo en la nube (Cloud Computing)** es un modelo tecnológico que permite acceder a recursos informáticos a través de Internet sin necesidad de instalar, administrar o mantener una infraestructura física propia.

Mediante este modelo, los usuarios y organizaciones pueden utilizar servicios tecnológicos de forma remota, pagando únicamente por los recursos que consumen y accediendo a ellos desde cualquier lugar con conexión a Internet.

#### Recursos que Pueden Ofrecerse en la Nube

Los servicios de cómputo en la nube pueden incluir:

- Servidores.
- Almacenamiento.
- Bases de datos.
- Redes.
- Software.
- Herramientas de análisis de datos.
- Aplicaciones empresariales.
- Servicios de inteligencia artificial.

#### Ventajas del Cómputo en la Nube

- Reduce los costos de infraestructura física.
- Facilita el acceso remoto a los servicios.
- Permite aumentar o disminuir recursos según la demanda.
- Mejora la disponibilidad y continuidad de los sistemas.
- Simplifica la administración y mantenimiento tecnológico.

#### Ejemplos de Servicios en la Nube

Algunos de los principales proveedores de servicios de cómputo en la nube son:

- Microsoft Azure.
- Amazon Web Services (AWS).
- Google Cloud Platform (GCP).

Estos proveedores ofrecen soluciones para almacenamiento, procesamiento de datos, desarrollo de aplicaciones, inteligencia artificial y análisis de grandes volúmenes de información.

#### Aplicaciones del Cómputo en la Nube

Actualmente, el cómputo en la nube se utiliza en diversos sectores:

- Educación.
- Salud.
- Gobierno.
- Comercio electrónico.
- Finanzas.
- Telecomunicaciones.

Gracias a esta tecnología, las organizaciones pueden implementar soluciones más flexibles, escalables y eficientes para responder a las necesidades de un entorno digital en constante evolución.

#### Tipos de Nube

El cómputo en la nube puede implementarse mediante diferentes modelos, dependiendo de las necesidades de seguridad, control, costos y acceso a los recursos. Los principales tipos de nube son la **nube pública**, la **nube privada** y la **nube híbrida**.

---

#### Nube Pública

La **nube pública** es un modelo en el que los servicios e infraestructuras son proporcionados por un proveedor externo y compartidos entre múltiples clientes a través de Internet.

#### Características

- Los recursos son administrados por un proveedor externo.
- La infraestructura es compartida entre varios usuarios.
- Permite reducir costos de adquisición y mantenimiento.
- Ofrece escalabilidad bajo demanda.
- El acceso se realiza mediante Internet.

#### Ejemplos de Proveedores

- Microsoft Azure
- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)

#### Ventajas

- Menor inversión inicial.
- Fácil implementación.
- Alta disponibilidad.
- Escalabilidad rápida.

---

#### Nube Privada

La **nube privada** es una infraestructura de cómputo exclusiva para una sola organización. Los recursos no se comparten con otras empresas o usuarios.

#### Características

- La infraestructura pertenece a una organización específica.
- Mayor control sobre los datos y aplicaciones.
- Mayor nivel de seguridad y privacidad.
- Permite personalizar los servicios según las necesidades institucionales.

#### Ejemplo

Un banco que almacena información financiera de sus clientes en servidores exclusivos y con estrictos controles de acceso.

#### Ventajas

- Mayor control administrativo.
- Mayor seguridad de la información.
- Cumplimiento de normativas y regulaciones.
- Personalización de recursos tecnológicos.

---

#### Nube Híbrida

La **nube híbrida** combina los servicios de una nube pública y una nube privada, permitiendo utilizar las ventajas de ambos modelos.

#### Características

- Integra recursos privados y públicos.
- Permite distribuir cargas de trabajo.
- Ofrece flexibilidad y escalabilidad.
- Mantiene información sensible en infraestructuras privadas.

#### Ejemplo

Una universidad que almacena expedientes académicos y datos personales de los estudiantes en una nube privada, mientras utiliza Microsoft Azure, Google Cloud o AWS para alojar plataformas educativas y recursos de aprendizaje.

#### Ventajas

- Equilibrio entre seguridad y flexibilidad.
- Optimización de costos.
- Mejor aprovechamiento de recursos.
- Mayor capacidad de adaptación a las necesidades del negocio.

---

#### Comparación de los Tipos de Nube

| Tipo de Nube | Característica Principal |
|--------------|-------------------------|
| **Nube Pública** | Los servicios son ofrecidos por un proveedor externo y compartidos entre múltiples clientes. |
| **Nube Privada** | La infraestructura pertenece exclusivamente a una organización. |
| **Nube Híbrida** | Combina una nube pública y una nube privada. |

---

#### ¿Cuál Elegir?

La elección del tipo de nube dependerá de factores como:

- Nivel de seguridad requerido.
- Presupuesto disponible.
- Requisitos de cumplimiento normativo.
- Necesidades de escalabilidad.
- Tipo de información que se almacena.

#### 2.1.1 Características del Cómputo en la Nube

#### 1. Autoservicio Bajo Demanda

Una de las características fundamentales del **cómputo en la nube** es el **autoservicio bajo demanda**, que permite a los usuarios solicitar y utilizar recursos tecnológicos cuando los necesiten, sin requerir la intervención directa del proveedor del servicio.

Esto significa que una persona o una organización puede aprovisionar recursos informáticos de forma rápida y autónoma mediante plataformas web o aplicaciones de administración.

#### Recursos que Pueden Solicitarse

- Máquinas virtuales.
- Espacio de almacenamiento.
- Bases de datos.
- Aplicaciones empresariales.
- Servicios de análisis de datos.
- Recursos de inteligencia artificial.

#### Beneficios

- Disponibilidad inmediata de recursos.
- Reducción de tiempos de espera.
- Mayor autonomía para los usuarios.
- Incremento de la productividad.
- Implementación rápida de proyectos tecnológicos.

#### Ejemplo

Crear una máquina virtual en **Microsoft Azure** en cuestión de minutos sin necesidad de contactar a un técnico o administrador del proveedor.

---

#### Ejemplo de la Vida Real

Cuando una persona se suscribe a **Netflix** desde una computadora, tableta o teléfono móvil, realiza todo el proceso de manera autónoma:

1. Crea una cuenta.
2. Selecciona un plan de suscripción.
3. Ingresa los datos de pago.
4. Comienza a utilizar el servicio inmediatamente.

En ningún momento es necesario comunicarse con un representante de la empresa para activar el servicio.

Este comportamiento ejemplifica perfectamente el concepto de **autoservicio bajo demanda**, ya que el usuario obtiene y utiliza los recursos cuando los necesita, de forma rápida y automática.

---

#### 2. Acceso Amplio a la Red

Los servicios de cómputo en la nube pueden utilizarse desde cualquier dispositivo con conexión a Internet. Esto permite que los usuarios accedan a la misma información y aplicaciones desde diferentes lugares y equipos.

#### Dispositivos Compatibles

- Computadoras de escritorio.
- Laptops.
- Tablets.
- Smartphones.
- Televisores inteligentes.

#### Beneficios

- Acceso desde cualquier lugar.
- Mayor movilidad.
- Facilidad para el trabajo remoto.
- Disponibilidad continua de los servicios.

#### Ejemplo

Un estudiante puede consultar sus tareas en Microsoft Teams desde su computadora en casa, continuar trabajando desde su teléfono móvil y revisar nuevamente la información desde una tableta.

---

#### Ejemplo de la Vida Real: Netflix

Una persona puede comenzar a ver una película de Netflix en su Smart TV, pausarla y continuar viéndola desde su teléfono móvil o computadora exactamente donde la dejó.

Esto demuestra la característica de **acceso amplio a la red**, ya que el servicio está disponible desde múltiples dispositivos conectados a Internet.

---

#### 3. Compartición de Recursos

La infraestructura física del proveedor se comparte entre múltiples usuarios y organizaciones de manera segura, asignando recursos según las necesidades de cada cliente.

#### Beneficios

- Reducción de costos.
- Uso eficiente de la infraestructura.
- Optimización de recursos.
- Mayor capacidad de servicio.

#### Ejemplo

Una empresa no necesita comprar servidores propios porque utiliza la infraestructura compartida de Microsoft Azure o AWS junto con miles de organizaciones adicionales.

---

#### Ejemplo de la Vida Real: Netflix

Millones de usuarios utilizan Netflix simultáneamente alrededor del mundo compartiendo la misma infraestructura en la nube.

Aunque todos utilizan los mismos centros de datos, cada usuario accede únicamente a su propia cuenta, historial y recomendaciones personalizadas.

Esto ejemplifica la **compartición de recursos**, donde múltiples clientes utilizan una misma infraestructura física sin interferir entre sí.

---

#### 4. Escalabilidad

La escalabilidad permite aumentar o disminuir los recursos tecnológicos según las necesidades del momento.

#### Beneficios

- Adaptación al crecimiento.
- Optimización de costos.
- Mayor disponibilidad.
- Mejor rendimiento de las aplicaciones.

#### Ejemplo

Una tienda en línea incrementa la capacidad de sus servidores durante el Buen Fin para soportar un mayor número de visitantes.

---

#### Ejemplo de la Vida Real: Netflix

Cuando se estrena una serie muy popular, millones de personas intentan acceder a Netflix al mismo tiempo.

La plataforma incrementa la capacidad de procesamiento, almacenamiento y ancho de banda para atender la demanda sin afectar la experiencia de los usuarios.

Cuando el tráfico vuelve a la normalidad, los recursos pueden reducirse nuevamente.

---

#### 5. Elasticidad Rápida

La elasticidad rápida permite asignar o liberar recursos automáticamente en cuestión de segundos o minutos.

A diferencia de la escalabilidad, la elasticidad ocurre de forma automática y casi inmediata.

#### Beneficios

- Respuesta rápida ante cambios inesperados.
- Menor intervención administrativa.
- Continuidad operativa.
- Uso eficiente de recursos.

#### Ejemplo

Un sitio web recibe repentinamente miles de visitas debido a una publicación viral y el proveedor de nube aumenta automáticamente los recursos disponibles.

---

#### Ejemplo de la Vida Real: Netflix

Durante las celebraciones de Año Nuevo o el lanzamiento de una película muy esperada, el tráfico de usuarios puede aumentar drásticamente.

Netflix ajusta automáticamente la capacidad de sus servicios para evitar interrupciones y garantizar la reproducción continua del contenido.

Esto representa la característica de **elasticidad rápida**, ya que el ajuste ocurre prácticamente en tiempo real.

---

#### 6. Servicio Medible

Los recursos consumidos pueden monitorearse y registrarse continuamente.

Esto permite que los clientes paguen únicamente por lo que utilizan.

#### Métricas Comunes

- Uso de CPU.
- Memoria utilizada.
- Espacio de almacenamiento.
- Tráfico de red.
- Tiempo de ejecución de aplicaciones.

## Beneficios

- Transparencia en el consumo.
- Control de costos.
- Optimización de recursos.
- Facturación basada en uso real.

#### Ejemplo

Una empresa puede consultar cuánta capacidad de almacenamiento utilizó durante el mes y pagar únicamente por ese consumo.

---

#### Ejemplo de la Vida Real: Netflix

Netflix monitorea constantemente:

- Cantidad de usuarios conectados.
- Horas de reproducción.
- Tráfico de video generado.
- Consumo de recursos de sus servidores.

Gracias a esta medición continua, puede optimizar su infraestructura y garantizar la calidad del servicio.

---

#### Resumen de las Características del Cómputo en la Nube

| Característica | Descripción | Ejemplo Real |
|---------------|-------------|--------------|
| Autoservicio bajo demanda | El usuario solicita recursos cuando los necesita. | Crear una cuenta y comenzar a usar Netflix inmediatamente. |
| Acceso amplio a la red | Acceso desde múltiples dispositivos conectados a Internet. | Ver Netflix desde TV, celular o computadora. |
| Compartición de recursos | Infraestructura compartida entre múltiples usuarios. | Millones de usuarios usan simultáneamente Netflix. |
| Escalabilidad | Los recursos aumentan o disminuyen según la demanda. | Netflix incrementa capacidad durante estrenos populares. |
| Elasticidad rápida | Ajuste automático e inmediato de recursos. | Netflix responde automáticamente a picos repentinos de tráfico. |
| Servicio medible | El consumo de recursos puede monitorearse. | Netflix registra uso, tráfico y demanda para optimizar sus servicios. |

# 2.1.2 Beneficios y Riesgos del Cómputo en la Nube

El cómputo en la nube ofrece múltiples ventajas para organizaciones y usuarios, permitiendo acceder a recursos tecnológicos de manera flexible y eficiente. Sin embargo, también implica ciertos riesgos que deben considerarse al implementar este modelo.

---

# Beneficios del Cómputo en la Nube

## 1. Reducción de Costos

Las organizaciones no necesitan invertir en servidores físicos, centros de datos ni equipos especializados.

### Beneficios

- Menor inversión inicial.
- Reducción de gastos de mantenimiento.
- Menores costos de actualización tecnológica.

### Ejemplo

Una pequeña empresa puede utilizar Microsoft Azure o AWS sin tener que comprar servidores propios.

---

## 2. Escalabilidad

Los recursos pueden aumentar o disminuir según las necesidades del negocio.

### Beneficios

- Adaptación al crecimiento.
- Optimización de recursos.
- Mejor atención a la demanda.

### Ejemplo

Una tienda en línea incrementa su capacidad durante el Buen Fin para atender más clientes.

---

## 3. Alta Disponibilidad

Los proveedores de nube cuentan con infraestructura redundante que reduce el riesgo de interrupciones.

### Beneficios

- Continuidad operativa.
- Menor tiempo de inactividad.
- Mayor confiabilidad.

### Ejemplo

Google Drive continúa disponible incluso si falla uno de los centros de datos del proveedor.

---

## 4. Acceso Remoto

La información y las aplicaciones pueden utilizarse desde cualquier lugar con conexión a Internet.

### Beneficios

- Trabajo remoto.
- Acceso móvil.
- Colaboración entre equipos distribuidos.

### Ejemplo

Los estudiantes pueden acceder a Microsoft Teams desde su hogar, escuela o cualquier otro lugar.

---

## 5. Actualizaciones Automáticas

Los proveedores realizan actualizaciones de software y seguridad de forma periódica.

### Beneficios

- Menor carga administrativa.
- Mayor seguridad.
- Acceso a nuevas funcionalidades.

### Ejemplo

Microsoft 365 incorpora nuevas funciones sin que los usuarios tengan que instalar actualizaciones manualmente.

---

## 6. Recuperación ante Desastres

Los datos suelen almacenarse en múltiples ubicaciones geográficas.

### Beneficios

- Protección contra pérdidas de información.
- Recuperación rápida ante fallas.
- Mayor continuidad del negocio.

### Ejemplo

Si ocurre una falla en un centro de datos, los respaldos permiten restaurar la información desde otra ubicación.

---

#### Riesgos del Cómputo en la Nube

#### 1. Dependencia de Internet

El acceso a los servicios depende de una conexión estable a Internet.

#### Consecuencias

- Interrupción temporal del acceso.
- Disminución de productividad.
- Problemas para trabajar remotamente.

#### Ejemplo

Si una empresa pierde su conexión a Internet, sus empleados podrían no acceder a aplicaciones alojadas en la nube.

---

#### 2. Seguridad y Privacidad

Existe el riesgo de accesos no autorizados, robo de información o ataques informáticos.

#### Medidas de Protección

- Cifrado de datos.
- Firewalls.
- Autenticación multifactor.
- Monitoreo continuo.

#### Ejemplo

Un atacante podría intentar acceder a cuentas corporativas utilizando credenciales robadas.

---

#### 3. Dependencia del Proveedor

Las organizaciones pueden llegar a depender de las tecnologías específicas de un proveedor de nube.

#### Consecuencias

- Migraciones complejas.
- Costos de cambio elevados.
- Dependencia tecnológica.

#### Ejemplo

Una empresa que desarrolla toda su infraestructura en Azure puede enfrentar dificultades para migrar posteriormente a AWS.

---

#### 4. Cumplimiento Normativo

Algunos sectores deben cumplir estrictas regulaciones relacionadas con la protección de datos.

#### Retos

- Protección de datos personales.
- Ubicación geográfica de la información.
- Cumplimiento de normativas nacionales e internacionales.

#### Ejemplo

Un hospital debe garantizar que los expedientes clínicos cumplan con las leyes de privacidad y protección de datos.

---

#### 5. Interrupciones del Servicio

Aunque poco frecuentes, los proveedores pueden experimentar fallas técnicas.

#### Consecuencias

- Servicios temporalmente indisponibles.
- Pérdida de productividad.
- Impacto en operaciones críticas.

#### Ejemplo

Una caída temporal de un proveedor de nube puede afectar aplicaciones de comercio electrónico o plataformas de aprendizaje virtual.

---

#### Resumen de Beneficios y Riesgos

| Beneficios | Riesgos |
|------------|----------|
| Reducción de costos. | Dependencia de Internet. |
| Escalabilidad. | Riesgos de seguridad y privacidad. |
| Alta disponibilidad. | Dependencia del proveedor. |
| Acceso remoto. | Cumplimiento normativo. |
| Actualizaciones automáticas. | Posibles interrupciones del servicio. |
| Recuperación ante desastres. | Complejidad de migración entre proveedores. |

---

### 2.1.3 Cómputo en la Nube en México y el Mundo

#### Situación Mundial

El mercado global de servicios en la nube ha experimentado un crecimiento significativo durante los últimos años debido a la necesidad de las organizaciones de digitalizar sus procesos, mejorar su competitividad y aprovechar tecnologías avanzadas para el análisis y procesamiento de datos.

Actualmente, millones de empresas en todo el mundo utilizan servicios de nube para almacenar información, ejecutar aplicaciones, desarrollar sistemas inteligentes y ofrecer servicios digitales a sus clientes.

#### Principales Factores que Impulsan el Crecimiento de la Nube

- Transformación Digital.
- Inteligencia Artificial (IA).
- Big Data.
- Internet de las Cosas (IoT).

---

#### Transformación Digital

La transformación digital consiste en la incorporación de tecnologías digitales para modernizar procesos, productos y servicios dentro de una organización.

#### Ejemplos

- Digitalización de trámites gubernamentales.
- Comercio electrónico.
- Plataformas educativas en línea.
- Banca digital.

#### Impacto de la Nube

La nube proporciona la infraestructura necesaria para implementar estas soluciones de manera rápida y escalable.

---

#### Inteligencia Artificial (IA)

La Inteligencia Artificial requiere grandes volúmenes de datos y una alta capacidad de procesamiento para entrenar modelos y generar predicciones.

#### Aplicaciones

- Asistentes virtuales.
- Sistemas de recomendación.
- Reconocimiento de imágenes.
- Traducción automática.
- Chatbots.

#### Relación con la Nube

Los servicios de nube permiten ejecutar algoritmos de IA sin necesidad de contar con infraestructura propia de gran capacidad.

---

#### Big Data

Big Data hace referencia al procesamiento y análisis de enormes cantidades de información provenientes de múltiples fuentes.

#### Ejemplos de Fuentes de Datos

- Redes sociales.
- Sistemas financieros.
- Comercio electrónico.
- Sensores IoT.
- Aplicaciones móviles.

#### Relación con la Nube

La nube facilita el almacenamiento y procesamiento de grandes volúmenes de datos mediante plataformas escalables y distribuidas.

---

#### Internet de las Cosas (IoT)

El **Internet de las Cosas (IoT)** conecta dispositivos físicos capaces de recopilar y transmitir información a través de Internet.

#### Características

- Generación continua de datos.
- Comunicación entre dispositivos.
- Automatización de procesos.
- Monitoreo en tiempo real.

#### Ejemplos de la Vida Real

#### Reloj Inteligente (Smartwatch)

Un smartwatch puede:

- Medir la frecuencia cardíaca.
- Registrar la actividad física.
- Monitorear patrones de sueño.
- Enviar información a una aplicación móvil.

Los datos generados se almacenan y procesan frecuentemente en servicios de nube.

#### Casa Inteligente

Una casa inteligente puede incluir:

- Focos conectados a Internet.
- Cámaras de vigilancia.
- Sensores de movimiento.
- Termostatos inteligentes.

Estos dispositivos pueden controlarse desde un teléfono móvil y almacenar información en plataformas de nube para su monitoreo y administración.

---

#### Principales Proveedores de Nube a Nivel Mundial

Las empresas líderes en servicios de cómputo en la nube son:

- Amazon Web Services (AWS).
- Microsoft Azure.
- Google Cloud Platform (GCP).

Estas organizaciones ofrecen soluciones para:

- Almacenamiento.
- Bases de datos.
- Inteligencia Artificial.
- Big Data.
- Desarrollo de aplicaciones.
- Internet de las Cosas.

---

#### Sectores que Más Utilizan la Nube

La adopción de servicios en la nube se ha extendido a diversos sectores:

#### Educación

- Plataformas educativas.
- Videoconferencias.
- Gestión académica.

#### Salud

- Expedientes clínicos electrónicos.
- Telemedicina.
- Sistemas hospitalarios.

#### Gobierno

- Trámites en línea.
- Portales de servicios ciudadanos.
- Gestión documental.

#### Finanzas

- Banca digital.
- Pagos electrónicos.
- Análisis de riesgos.

#### Comercio Electrónico

- Tiendas en línea.
- Sistemas de pago.
- Gestión de inventarios.

---

#### Situación General en México

En México, la adopción del cómputo en la nube ha aumentado considerablemente debido a:

- La digitalización de empresas.
- El crecimiento del trabajo remoto.
- La modernización de servicios gubernamentales.
- El aumento del comercio electrónico.
- La necesidad de soluciones tecnológicas escalables.

Cada vez más organizaciones mexicanas utilizan servicios de nube para mejorar su eficiencia operativa y ofrecer mejores servicios a sus usuarios.

---

#### Conclusión

El cómputo en la nube se ha convertido en una tecnología fundamental para la transformación digital a nivel mundial. Factores como la Inteligencia Artificial, Big Data, el Internet de las Cosas y la digitalización de procesos han impulsado su crecimiento en prácticamente todos los sectores económicos. Tanto en México como en el resto del mundo, la nube continúa siendo una herramienta clave para la innovación, la competitividad y el desarrollo tecnológico de las organizaciones modernas.


### Evaluación del Proyecto Final

Como parte de la evaluación del proyecto final, cada equipo deberá presentar una propuesta clara y estructurada que permita comprender el problema a resolver, los datos que serán utilizados y el alcance de la solución propuesta.

### Elementos a Entregar

#### 1. Descripción del Proyecto

Presentar una explicación general del proyecto, indicando:

- Problema que se desea resolver.
- Contexto de aplicación.
- Importancia del análisis o solución propuesta.
- Beneficios esperados.

#### 2. Objetivo General y Objetivos Específicos

#### Objetivo General

Describe el propósito principal del proyecto y lo que se espera lograr al finalizar su desarrollo.

#### Objetivos Específicos

Definen las actividades o metas concretas necesarias para alcanzar el objetivo general.

#### 3. Alcance del Proyecto

Especificar claramente qué incluirá y qué no incluirá el proyecto.

El alcance debe considerar aspectos como:

- Datos que serán analizados.
- Tecnologías que se utilizarán.
- Funcionalidades de la solución propuesta.
- Limitaciones identificadas.

#### 4. Fuente de Obtención del Conjunto de Datos

Indicar el origen de los datos que se utilizarán en el proyecto.

Algunas posibles fuentes son:

- Kaggle.
- Datos Abiertos de México.
- Datos Abiertos del Gobierno Federal.
- INEGI.
- APIs públicas.
- Redes sociales.
- Conjuntos de datos académicos.
- Datos generados por la propia organización o institución.

Se deberá incluir:

- Nombre del conjunto de datos.
- Enlace o fuente de consulta.
- Descripción breve del contenido.
- Justificación de su utilización.

---

#### Formato de Entrega

La propuesta deberá entregarse en formato digital (PDF, Word o Markdown) y contener todos los elementos solicitados.

#### Fecha Límite de Entrega

📅 **A más tardar el 12 de septiembre.**

No se recibirán propuestas después de la fecha establecida, salvo situaciones previamente justificadas y autorizadas.

---

#### Criterios de Evaluación

| Elemento | Aspectos a Evaluar |
|-----------|-------------------|
| Descripción del proyecto | Claridad del problema y pertinencia de la solución |
| Objetivos | Coherencia entre objetivos y proyecto |
| Alcance | Definición clara de lo que se desarrollará |
| Fuente de datos | Calidad, relevancia y disponibilidad del conjunto de datos |
| Presentación | Organización, redacción y formato del documento |

#### Recomendaciones

- Seleccionar un problema que sea relevante y factible de desarrollar.
- Elegir una fuente de datos confiable.
- Definir objetivos claros y medibles.
- Delimitar adecuadamente el alcance del proyecto.
- Justificar las decisiones tecnológicas propuestas.

> **Fecha de entrega:** 12 de septiembre.


