#### 2.3 Plataformas

###### ¿Qué es una plataforma en la nube?

Una plataforma en la nube es un conjunto de recursos tecnológicos que permiten desarrollar, desplegar, administrar y escalar aplicaciones, servicios o soluciones de datos sin preocuparse por la infraestructura física subyacente.

###### Beneficios

- Reducción de costos en infraestructura.
- Escalabilidad bajo demanda.
- Alta disponibilidad.
- Acceso desde cualquier ubicación.
- Seguridad administrada por el proveedor.
- Actualizaciones continuas.

---

###### ¿Qué ofrece una plataforma?

###### Computación
Capacidad de procesamiento mediante servidores físicos o virtuales para ejecutar aplicaciones y servicios.

###### Almacenamiento
Espacio para guardar archivos, respaldos, imágenes, videos y grandes volúmenes de información.

###### Bases de Datos
Motores administrados para almacenar y consultar información de manera eficiente.

###### Inteligencia Artificial
Servicios especializados para desarrollar soluciones inteligentes y automatizadas.

###### Analítica
Herramientas para transformar datos en información útil para la toma de decisiones.

###### Machine Learning
Plataformas que permiten entrenar modelos predictivos a partir de datos históricos.

###### Internet de las Cosas (IoT)
Conexión y monitoreo de dispositivos físicos capaces de generar datos en tiempo real.

---

###### Arquitectura General de una Plataforma Cloud

```text
Usuarios
   │
Aplicaciones
   │
Servicios Cloud
   │
Bases de Datos
   │
Almacenamiento
   │
Infraestructura Física
```

Las organizaciones consumen los servicios sin necesidad de administrar directamente los servidores físicos.

---

###### 2.3.1 Plataformas Básicas

Las plataformas básicas son servicios de propósito general orientados a cubrir la mayor parte de las necesidades tecnológicas de una organización.

###### Características

- Amplio catálogo de servicios.
- Infraestructura global.
- Escalabilidad automática.
- Seguridad empresarial.
- Integración con múltiples tecnologías.
- Disponibilidad de servicios de análisis e inteligencia artificial.

##### Ejemplos

- Microsoft Azure
- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)

---

##### Microsoft Azure

Plataforma de servicios en la nube desarrollada por Microsoft.

##### Servicios Relevantes

##### Azure Virtual Machines (VM)

Permite crear y administrar servidores virtuales Windows o Linux.

**Casos de uso:**
- Hosting de aplicaciones.
- Ambientes de desarrollo.
- Bases de datos empresariales.

##### Azure SQL Database

Base de datos relacional administrada.

**Ventajas:**
- Respaldos automáticos.
- Alta disponibilidad.
- Escalabilidad automática.

##### Azure Storage

Servicio de almacenamiento para:

- Archivos
- Imágenes
- Videos
- Respaldos
- Big Data

##### Azure Databricks

Plataforma basada en Apache Spark.

Permite:

- Procesamiento masivo de datos.
- ETL.
- Ciencia de datos.
- Analítica avanzada.

##### Azure Machine Learning

Servicio especializado para:

- Entrenar modelos.
- Implementar modelos.
- Monitorear predicciones.
- Administrar proyectos de IA.

##### Fortalezas de Azure

- Integración con Microsoft 365.
- Seguridad empresarial.
- Gobierno de datos.
- Integración nativa con Power BI.
- Excelente adopción corporativa.

---

##### Amazon Web Services (AWS)

Plataforma cloud líder del mercado.

##### Servicios Relevantes

##### EC2 (Elastic Compute Cloud)

Máquinas virtuales en la nube.

##### S3 (Simple Storage Service)

Almacenamiento seguro y escalable.

##### Redshift

Data Warehouse para análisis masivo de datos.

##### Lambda

Servicio serverless para ejecutar código sin administrar servidores.

##### SageMaker

Plataforma para Machine Learning y modelos predictivos.

##### Fortalezas de AWS

- Gran variedad de servicios.
- Cobertura global.
- Ecosistema maduro.
- Amplia documentación.
- Gran comunidad de usuarios.

---

##### Google Cloud Platform (GCP)

Plataforma cloud desarrollada por Google.

##### Servicios Relevantes

### BigQuery

Motor analítico para grandes volúmenes de información.

**Ventajas:**

- Consultas SQL rápidas.
- Escalabilidad automática.
- Alta integración con análisis de datos.

##### Vertex AI

Plataforma especializada en Inteligencia Artificial.

##### Cloud Storage

Almacenamiento de objetos y archivos.

##### Compute Engine

Máquinas virtuales para ejecutar aplicaciones.

##### Fortalezas de GCP

- Analítica avanzada.
- Big Data.
- Inteligencia Artificial.
- Machine Learning.
- Tecnologías derivadas de Google.

---

##### Comparativa de Plataformas

| Característica | Azure | AWS | GCP |
|---------------|--------|--------|--------|
| Integración empresarial | Alta | Media | Media |
| Big Data | Alta | Alta | Muy Alta |
| Machine Learning | Alta | Alta | Muy Alta |
| Facilidad de uso | Alta | Media | Alta |
| Número de servicios | Alto | Muy Alto | Medio |

---

##### Actividad 1: Caso Universidad

##### Requerimientos

Una universidad necesita:

- Portal web institucional.
- Sistema escolar.
- Data Warehouse.
- Predicción de deserción estudiantil mediante IA.

##### Plataforma Recomendada

##### Microsoft Azure

##### Servicios Propuestos

- Azure App Service
- Azure SQL Database
- Azure Data Factory
- Azure Data Lake Storage
- Azure Synapse Analytics
- Azure Databricks
- Azure Machine Learning
- Power BI

##### Justificación

La solución centraliza aplicaciones, almacenamiento, procesos analíticos y modelos de inteligencia artificial dentro de una misma plataforma escalable y segura.

---

##### 2.3.2 Plataformas Especializadas

Son plataformas enfocadas en resolver necesidades específicas.

##### Ventajas

- Mayor rendimiento para tareas especializadas.
- Herramientas enfocadas en un dominio concreto.
- Procesamiento optimizado.

---

##### Databricks

Plataforma especializada en:

- Big Data.
- Ciencia de Datos.
- Analítica Avanzada.
- Machine Learning.

##### Funcionalidades

##### Apache Spark

Motor de procesamiento distribuido para grandes volúmenes de datos.

##### ETL

Procesos de:

- Extracción
- Transformación
- Carga

##### Ciencia de Datos Colaborativa

Permite trabajo conjunto entre analistas e ingenieros de datos.

---

##### Snowflake

Plataforma especializada para:

- Data Warehouse.
- Data Lake.
- Compartición segura de datos.

##### Beneficios

- Separación entre almacenamiento y cómputo.
- Escalabilidad independiente.
- Alto rendimiento.

---

##### Vertex AI

Plataforma de IA de Google.

##### Especialidades

##### Entrenamiento de Modelos

Creación de modelos predictivos.

##### MLOps

Automatización del ciclo de vida de modelos.

##### IA Generativa

Desarrollo de asistentes inteligentes y modelos generativos.

---

##### Azure Machine Learning

Especializada en:

- Entrenamiento de modelos.
- Implementación.
- Monitoreo.
- Gobernanza de IA.

---

##### Comparación de Plataformas Especializadas

| Plataforma | Especialidad |
|------------|-------------|
| Databricks | Big Data |
| Snowflake | Data Warehouse |
| Vertex AI | Machine Learning |
| Azure ML | MLOps |

---

##### Actividad 2: Telecomunicaciones

##### Escenario

Una empresa genera:

- 20 TB diarios.
- Monitoreo de redes.
- Predicción de abandono de clientes.

##### Solución

##### Plataforma Básica

- Azure Data Lake Storage
- Azure Databricks

##### Plataforma Especializada

- Azure Machine Learning

##### Justificación

Permite almacenar grandes volúmenes de datos, procesarlos en tiempo real y generar modelos predictivos para reducir la pérdida de clientes.

---

##### 2.4 Tipos de Servicios Cloud

Los servicios cloud se clasifican según el nivel de responsabilidad compartida entre proveedor y cliente.

##### Tipos Principales

##### IaaS
Infrastructure as a Service.

##### PaaS
Platform as a Service.

##### SaaS
Software as a Service.

---

##### Comparación de Responsabilidades

| Componente | SaaS | PaaS | IaaS |
|------------|------|------|------|
| Aplicación | Proveedor | Usuario | Usuario |
| Datos | Usuario | Usuario | Usuario |
| Runtime | Proveedor | Proveedor | Usuario |
| Sistema Operativo | Proveedor | Proveedor | Usuario |
| Infraestructura | Proveedor | Proveedor | Proveedor |

---

##### IaaS

Infraestructura como Servicio.

El proveedor entrega:

- Servidores.
- Almacenamiento.
- Redes.

El usuario administra:

- Sistema Operativo.
- Aplicaciones.
- Datos.

##### Ejemplos

- AWS EC2
- Azure Virtual Machines

##### Ventajas

- Máximo control.
- Flexibilidad.

##### Desventajas

- Mayor responsabilidad administrativa.

---

##### PaaS

Plataforma como Servicio.

El proveedor administra la infraestructura y el sistema operativo.

El usuario solo desarrolla y publica aplicaciones.

##### Ejemplos

- Azure App Service
- Google App Engine

##### Ventajas

- Desarrollo rápido.
- Menor administración.

##### Desventajas

- Menor control de configuración.

---

##### SaaS

Software como Servicio.

Las aplicaciones son consumidas directamente a través de Internet.

##### Ejemplos

- Microsoft 365
- Gmail
- Salesforce
- Power BI Service

---

##### Características de SaaS

- Acceso mediante navegador.
- Pago por suscripción.
- Actualizaciones automáticas.
- Escalabilidad inmediata.
- Multitenencia.

##### ¿Qué es Multitenancy?

Es un modelo donde varios clientes utilizan la misma aplicación mientras sus datos permanecen aislados y protegidos.

---

##### Ventajas de SaaS

- Menor inversión inicial.
- Implementación rápida.
- Acceso desde cualquier lugar.
- Menor mantenimiento.

##### Desventajas de SaaS

- Dependencia del proveedor.
- Dependencia de Internet.
- Menor personalización.
- Posible lock-in tecnológico.

---

##### Caso de Estudio

##### Situación Actual

La empresa utiliza:

- Excel local.
- Servidor propio.
- Correos internos.

##### Migración

- Microsoft 365.
- SharePoint Online.
- Power BI Service.

##### Beneficios

- Colaboración en tiempo real.
- Acceso remoto.
- Menor infraestructura local.
- Mayor disponibilidad.

##### Riesgos

- Dependencia de Internet.
- Migración de datos.
- Gestión de accesos.

##### Costos

##### Disminuyen

- Hardware.
- Mantenimiento.
- Energía eléctrica.

##### Aumentan

- Licencias.
- Suscripciones.
- Almacenamiento cloud.

---

##### Conclusiones

- Las plataformas básicas permiten implementar casi cualquier solución empresarial.
- Las plataformas especializadas se enfocan en áreas concretas como Big Data o Inteligencia Artificial.
- Azure, AWS y GCP son los principales proveedores cloud.
- IaaS ofrece mayor control.
- PaaS acelera el desarrollo.
- SaaS proporciona aplicaciones listas para usar.
- La elección depende de las necesidades técnicas y del presupuesto de la organización.
