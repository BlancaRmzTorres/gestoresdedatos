# Diccionario de datos preliminar — ATUS 2025

**Fuente:** INEGI, Accidentes de Tránsito Terrestre en Zonas Urbanas y Suburbanas (ATUS), conjunto anual 2025.

Este es un diccionario de trabajo por grupos de variables. Para asignar etiquetas y códigos válidos exactos, debe consultarse el diccionario oficial incluido en el ZIP del INEGI. Los códigos categóricos se conservan como códigos y no deben interpretarse sin esa referencia.

| Grupo | Variables | Tipo propuesto | Uso |
|---|---|---|---|
| Cobertura y geografía | `COBERTURA`, `CVEGEO`, `CVE_ENT`, `CVE_MUN` | Texto/código | Identificar cobertura, entidad y municipio sin perder ceros iniciales. |
| Tiempo | `ANIO`, `MES`, `ID_DIA`, `DIASEMANA`, `ID_HORA`, `ID_MINUTO` | Entero o código | Filtrar accidentes por año, mes, día de semana y hora. |
| Zona | `URBANA`, `SUBURBANA` | Código categórico | Distinguir el ámbito del registro. |
| Características del accidente | `TIPACCID`, `CAUSAACCI`, `CAPAROD`, `CLASACC`, `ESTATUS` | Código categórico | Consultar tipo, causa, características y clasificación del accidente. |
| Vehículos involucrados | `AUTOMOVIL`, `CAMPASAJ`, `MICROBUS`, `PASCAMION`, `OMNIBUS`, `TRANVIA`, `CAMIONETA`, `CAMION`, `TRACTOR`, `FERROCARRI`, `MOTOCICLET`, `BICICLETA`, `OTROVEHIC` | Conteo/código según diccionario | Analizar participación de tipos de vehículo. Confirmar en diccionario oficial si cada campo es conteo o indicador codificado. |
| Persona conductora | `SEXO`, `ALIENTO`, `CINTURON`, `ID_EDAD`, `CONDMUERTO`, `CONDHERIDO` | Código y entero | Analizar características de la persona conductora y resultados asociados. |
| Pasajeros | `PASAMUERTO`, `PASAHERIDO` | Conteo | Registrar pasajeros muertos y heridos. |
| Peatones | `PEATMUERTO`, `PEATHERIDO` | Conteo | Registrar peatones muertos y heridos. |
| Ciclistas | `CICLMUERTO`, `CICLHERIDO` | Conteo | Registrar ciclistas muertos y heridos. |
| Otras personas | `OTROMUERTO`, `OTROHERIDO` | Conteo | Registrar otras personas muertas y heridas. |
| Totales | `NEMUERTO`, `NEHERIDO` | Conteo | Totales de personas muertas y heridas conforme a la definición oficial. |

## Reglas de tipado
- Los códigos geográficos y las categorías se guardan como cadenas para preservar ceros iniciales.
- Los campos de año, mes, hora, minuto, edad y conteos se convierten a enteros cuando su valor lo permite.
- Los valores faltantes se representan como `null` en JSON y como celdas vacías en CSV.
- No se asignan etiquetas a códigos sin consultar el diccionario oficial.
