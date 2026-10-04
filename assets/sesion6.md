# Base de datos para Ciencia de Datos

## Sesión 6. Plataformas y Tipos de Servicios

---

# 2.4 Tipos de Servicio

## 2.4.1 Software como Servicio (SaaS)

## 2.4.2 Plataforma como Servicio (PaaS)

## 2.4.3 Infraestructura como Servicio (IaaS)

## 2.5 Uso de aplicaciones

---

# 2.4.2 Platform as a Service (PaaS)

PaaS (Platform as a Service) es un modelo de computación en la nube que ofrece una plataforma completa para desarrollar, probar, implementar y administrar aplicaciones sin preocuparse por la infraestructura.

---

# Arquitectura PaaS

## 1. Infraestructura física

Es el hardware real donde funciona todo el sistema: servidores, almacenamiento, redes y centros de datos.

**Ejemplo:** Los servidores que tiene Microsoft Azure, AWS o Google Cloud.

**En PaaS:** El proveedor administra completamente esta capa.

## 2. Sistema Operativo

Es el software base que permite que las aplicaciones funcionen sobre el hardware.

**Ejemplos:** Linux, Windows Server.

**En PaaS:** El proveedor instala, actualiza y mantiene el sistema operativo.

## 3. Base de Datos

Es donde se almacena y organiza la información que utiliza la aplicación.

**Ejemplos:** MySQL, PostgreSQL, SQL Server, Oracle.

**En PaaS:** Generalmente la base de datos ya viene configurada y lista para usarse.

## 4. Herramientas de Desarrollo

Son las herramientas y servicios que facilitan la creación, prueba y despliegue de aplicaciones.

**Ejemplos:**

- Git
- Visual Studio
- SDKs
- Frameworks (Django, Spring Boot, .NET)

**En PaaS:** El proveedor ofrece entornos y herramientas listas para desarrollar y publicar.

## 5. Código del Desarrollador

Es el programa que escriben los desarrolladores para resolver una necesidad de negocio.

**Ejemplo:** Una aplicación en Python para controlar inventarios o una API en Java.

**En PaaS:** El desarrollador se enfoca principalmente en esta capa.

## 6. Aplicación

Es el producto final que utiliza el usuario.

**Ejemplos:**

- Sistema de ventas
- Portal web institucional
- Aplicación móvil
- Sistema de encuestas

**En PaaS:** La aplicación se ejecuta sobre toda la plataforma administrada por el proveedor.

---

# Ejemplos de PaaS

## Microsoft Azure

- Azure App Service
- Azure SQL Database
- Azure Functions

## Google Cloud

- App Engine

## AWS

- Elastic Beanstalk

## Salesforce

- Salesforce Platform

---

# Ventajas de PaaS

### Rapidez

Se puede desarrollar sin configurar servidores.

### Menor costo inicial

No requiere comprar hardware.

### Escalabilidad

La plataforma aumenta recursos automáticamente.

### Mayor productividad

Los desarrolladores se enfocan únicamente en programar.

---

# Desventajas de PaaS

- Menor control sobre la infraestructura.
- Dependencia del proveedor.
- Restricciones tecnológicas.

---

# Actividad 1

## Analizar un Servicio

### Investigar

- Azure App Service
- AWS Elastic Beanstalk
- Google App Engine

### Responder

- ¿Qué lenguaje soporta?
- ¿Qué base de datos puede utilizar?
- ¿Cómo escala?

---

# Respuestas

| Servicio | Lenguajes principales | Base de datos | Escalado |
|-----------|----------------------|---------------|-----------|
| Azure App Service | .NET, Java, Python, Node.js | SQL Database, MySQL, PostgreSQL | Automático |
| AWS Elastic Beanstalk | Java, Python, .NET, Node.js, Docker | RDS, Aurora, DynamoDB | Automático |
| Google App Engine | Python, Java, Go, Node.js | Cloud SQL, Firestore | Automático |

**Conclusión:** Dentro del modelo PaaS la plataforma aumenta o reduce recursos automáticamente según la demanda, sin que el desarrollador administre la infraestructura física.

---

# Actividad 2

Somos una empresa de streaming.

### Preguntas

- ¿Qué aplicación desarrollarían?
- ¿Por qué usarían PaaS?
- ¿Qué proveedor elegirían?

### Respuesta

Como empresa de streaming desarrollaríamos una plataforma web y móvil para que los usuarios puedan ver películas y series en línea, administrar sus perfiles y recibir recomendaciones de contenido.

Utilizaríamos una solución PaaS porque reduce el trabajo de administración de infraestructura, acelera el desarrollo y permite escalar la aplicación automáticamente cuando aumenta la demanda.

Elegiríamos Azure App Service debido a su facilidad de uso, integración con otros servicios de Azure y capacidad para soportar grandes cantidades de usuarios de forma segura y eficiente.

---

# Conclusión PaaS

PaaS nos permite enfocarnos en el desarrollo de software mientras el proveedor administra la plataforma tecnológica, simplificando la creación de soluciones innovadoras y escalables.

---

# 2.4.3 Infraestructura como Servicio (IaaS)

Infraestructura como Servicio (IaaS) proporciona recursos de cómputo virtualizados a través de Internet.

En IaaS, los recursos de cómputo son virtualizados porque se crean versiones virtuales de servidores, almacenamiento y redes a partir de la infraestructura física del proveedor.

---

# Arquitectura IaaS

IaaS es un modelo de nube donde el proveedor proporciona la infraestructura tecnológica, como servidores, almacenamiento y redes, mientras que el cliente administra el sistema operativo y las aplicaciones.

Esto permite reducir costos de hardware y desplegar recursos de forma rápida y escalable.

---

# Ejemplos de IaaS

## AWS

- EC2 (Elastic Compute Cloud)
- EBS (Elastic Block Store)
- VPC (Virtual Private Cloud)

## Azure

- Virtual Machines
- Virtual Network
- Storage Account

## Google Cloud

- Compute Engine

---

# Componentes principales de IaaS en AWS

(Contenido representado mediante diagramas e imágenes en la presentación.)

---

# Conclusión IaaS

IaaS permite aprovechar infraestructura tecnológica de manera eficiente y flexible, manteniendo un mayor control sobre los recursos y aplicaciones, sin necesidad de invertir en centros de datos o equipos físicos propios.

---

# SaaS vs PaaS vs IaaS

La principal diferencia entre SaaS, PaaS e IaaS es el nivel de responsabilidad que tiene el usuario sobre la tecnología.

A medida que avanzamos de SaaS hacia IaaS, el usuario obtiene más control, pero también más responsabilidades de administración.

---

# Flujo de Desarrollo y Despliegue de una Aplicación en la Nube

## Conceptos Clave

1. Desarrollo local en Python.
2. Conversión a API mediante FastAPI.
3. Empaquetado en Docker.
4. Despliegue en PaaS o IaaS.
5. Escalamiento y disponibilidad para múltiples usuarios.

### Idea clave

La nube no cambia lo que hace la aplicación; cambia cómo se ejecuta, se administra y crece para atender a más usuarios.

---

# API con FastAPI

La aplicación recibe datos JSON, los procesa mediante código Python y devuelve una respuesta JSON.

Es un ejemplo típico de PaaS, donde el desarrollador se concentra en la lógica de negocio mientras la plataforma administra la infraestructura.

---

# Tecnologías de Contenedores

- 🐳 Docker
- 📦 Podman
- ⚙️ Containerd
- 🚀 CRI-O
- 🐧 LXC
- 🖥️ LXD
- ☁️ Singularity (Apptainer)
- 🔷 rkt (Rocket)

---

# Operación de una Aplicación en PaaS

Aspectos importantes:

- Variables de entorno
- Health Checks
- Logs y monitoreo
- Autoescalamiento
- CI/CD
- Gestión de secretos

### Idea clave

En PaaS no desaparece la administración; simplemente cambia de administrar servidores a administrar la configuración, seguridad y monitoreo de la aplicación.

---

# Operación de una Aplicación en IaaS

Responsabilidades del usuario:

- Instalar sistema operativo
- Instalar Python
- Configurar dependencias
- Administrar servidores
- Gestionar seguridad
- Dar mantenimiento

### Idea clave

El proveedor administra la infraestructura, mientras que el usuario administra gran parte del software.

---

# Caso de Estudio

## ¿Qué modelo elegirías?

**PaaS**, porque permite desarrollar y desplegar rápidamente mientras el proveedor administra la infraestructura.

## ¿Dónde ejecutarías la aplicación?

- Azure App Service
- Google App Engine
- AWS Elastic Beanstalk

## ¿Dónde almacenarías los datos?

- Azure SQL Database
- Amazon RDS
- Google Cloud SQL

## ¿Cómo escalarías la solución?

Mediante Auto Scaling.

## Aspectos importantes de seguridad

- Credenciales
- Contraseñas
- Datos de usuarios
- Llaves de base de datos
- API Keys
- Respaldos

## Mejor equilibrio entre costo, control y simplicidad

**PaaS**

Ventajas:

- Menor administración que IaaS
- Más flexibilidad que SaaS
- Escalabilidad integrada
- Despliegue rápido
- Costos moderados

---

# Conclusión General

La evolución desde aplicaciones locales hacia arquitecturas basadas en la nube permite construir soluciones escalables para ciencia de datos, inteligencia artificial y sistemas empresariales.

La selección entre SaaS, PaaS e IaaS depende del equilibrio requerido entre control, complejidad administrativa, costos y velocidad de despliegue.

Comprender estas diferencias permite diseñar arquitecturas tecnológicas más eficientes y alineadas con los objetivos del negocio.

---

# Segunda Entrega

**10 de octubre**

---

# Gracias
