# Prototipo de recepción de mercadería

## Autor
- Nombre: Anderson Cruz 
- Curso: Fundamentos de programacion 
- Docente: Danny M

## Contexto
Proyecto académico basado en la observación del proceso de
recepción de mercadería en un restaurante KFC.

Es un sistema oficial de la empresa.

## Problema identificado
El registro manual en un cuaderno depende de que el responsable
copie y revise los datos con exactitud.

Esto puede generar errores de transcripción, demoras en las
consultas y diferencias con el sistema digital.

Si el cuaderno se extravía, se moja o se deteriora, puede
perderse el único registro de los productos recibidos,
los responsables y las diferencias reportadas al proveedor.

## Objetivo
Digitalizar el registro de recepción de mercadería mediante
un prototipo que permita registrar, consultar y conservar
las entregas y sus diferencias.

## Caso de referencia
Durante la observación se identificó una recepción de pollo
fresco troceado, presentado en cajas de 20 kg.

Se solicitaron 40 cajas y se recibieron 38.

La diferencia fue de 2 cajas faltantes.

El prototipo utiliza este caso como referencia para comprobar
el cálculo automático de diferencias.

Los datos ingresados durante las pruebas son de demostración.

## Alternativa seleccionada
Se desarrolló un programa propio para adaptar las funciones
de registro y consulta al proceso observado.

El mantenimiento y las mejoras quedan a cargo del desarrollador
o responsable del proyecto.

## Funcionalidades implementadas
- Registrar fecha y hora de recepción.
- Registrar proveedor y número de guía.
- Registrar producto y presentación.
- Registrar cantidades solicitadas y recibidas.
- Calcular faltantes y excedentes.
- Registrar observaciones.
- Registrar responsable y ubicación.
- Consultar todas las entregas.
- Buscar por guía, proveedor o producto.
- Mostrar un resumen de diferencias.
- Guardar y recuperar datos mediante un archivo JSON.
- Validar entradas obligatorias, fechas, horas y cantidades.
- Rechazar registros duplicados según la combinación de guía,
  proveedor, producto y presentación.

## Organización del proyecto
- main.py: menú principal e integración de los módulos.
- funciones.py: validaciones, registro, consultas y resumen.
- almacenamiento.py: validación estructural, lectura y guardado.
- README.md: documentación del proyecto.
- .gitignore: exclusión de archivos locales y temporales.

## Requisitos
- Python 3.
- No requiere bibliotecas externas.

## Ejecución
Abrir una terminal en la carpeta del proyecto y ejecutar:

python main.py

## Menú
1. Registrar entrega.
2. Mostrar entregas.
3. Buscar entrega.
4. Mostrar resumen.
5. Salir.

## Almacenamiento
Los datos se guardan en entregas.json.

El archivo se crea al guardar la primera entrega.

El programa escribe primero en un archivo temporal y después
reemplaza el archivo principal.

Si el archivo existente no puede cargarse o no cumple la
estructura esperada, el programa informa el error y se cierra
para evitar reemplazar los datos con una lista vacía.

## Pruebas realizadas

Completar los resultados después de ejecutar cada prueba.

| Prueba | Resultado esperado | Resultado obtenido |
|---|---|---|
| Registrar 40 solicitadas y 38 recibidas | 2 faltantes y 0 excedentes | Se registró la entrega con 40 solicitadas y 38 recibidas; se mostraron 2 faltantes y 0 excedentes.
 |
| Consultar registros | Mostrar la entrega guardada |  Se mostró la entrega guardada con 40 solicitadas y 38 recibidas.|
| Buscar PRUEBA-001 | Encontrar el registro | Se encontró el registro PRUEBA-001. |
| Consultar resumen después de la primera entrega | Mostrar un registro con faltantes | Se mostró un registro con faltantes. |
| Cerrar y volver a abrir | Conservar el registro | El registro se conservó después de cerrar y volver a abrir el programa.|
| Ingresar letras en una cantidad | Rechazar y solicitar un entero | Se rechazó el texto abc y se solicitó nuevamente un número entero. |
| Ingresar una cantidad negativa | Rechazar el valor | Se rechazó la cantidad negativa -5. |
| Ingresar 31/02/2026 | Rechazar la fecha | Se rechazó 31/02/2026 y se solicitó una fecha válida.|

## Cumplimiento de la consigna
- Estructuras de control: if, elif, else, while y for.
- Funciones: validaciones, registro, búsqueda y almacenamiento.
- Arreglos: listas de Python para entregas y resultados.
- Cadenas: textos y métodos strip, upper y casefold.
- Archivos: lectura y escritura en formato JSON.
- Módulos reutilizables: funciones.py y almacenamiento.py.
- Git y GitHub: commits que registran los avances.

## Desarrollo progresivo
1. Documentación del problema y objetivo.
2. Implementación del almacenamiento.
3. Implementación de funciones y validaciones.
4. Integración mediante un menú principal.
5. Pruebas y documentación de resultados.

## Privacidad
Los archivos entregas.json y entregas.tmp se excluyen del
repositorio mediante .gitignore.

No deben publicarse datos reales sin la autorización
correspondiente.

## Limitaciones
- No registra salidas de productos.
- No calcula las existencias actuales del almacén.
- No incluye usuarios, permisos ni firma digital.
- No se integra con el sistema digital del restaurante.
- No administra lotes, vencimientos o temperaturas en campos
  estructurados.
- No permite editar ni eliminar registros desde el menú.
- No gestiona reposiciones posteriores de faltantes.
- Está diseñado para uso local por una persona a la vez.
- El archivo local no sustituye una estrategia de respaldo.
- El registro no reemplaza una guía firmada ni demuestra por
  sí solo la conformidad del proveedor.

## Estado
Código del prototipo completado.

Los resultados de ejecución deben registrarse en la tabla
de pruebas.

