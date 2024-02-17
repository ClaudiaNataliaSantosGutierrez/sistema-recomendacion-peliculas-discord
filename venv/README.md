# Sistema de Recomendación de Películas en Discord

Este proyecto consiste en un bot de Discord que proporciona recomendaciones de películas a los usuarios basadas en el género especificado. Los usuarios pueden solicitar recomendaciones utilizando comandos de texto en el servidor de Discord donde está activo el bot, sin embargo tambien el programa ejecuta uno que otro juego con el usuario mientras escoje la pelucula de su gusto

## Funciones

### 1. Comando de Recomendación
- El bot responde a un comando de texto (`>recomendacion <genero>`) donde `<genero>` es el género de la película que el usuario desea.
- Proporciona una recomendación aleatoria de una película del género especificado.
- Si el género proporcionado no está en la lista predefinida de géneros, el bot responde con un mensaje de error y hace una pequeña sugerencia de busqueda con el comando (`>youtube <busqueda>`)
- Si no quieres escoger pelicula puedes interactuar con el bot mediante el comando (`>info`) para saber un poco de datos sobre chat_bot
- tambien podrias jugar un rato a sumar cantidades con el comando (`>sum`) o incluso a lanzar respuestas predeterminadas (`>ping`)

## Tecnologías Utilizadas
- Python
- Discord.py: Una biblioteca para la creación de bots de Discord en Python.
- Flask: Un marco web ligero utilizado para posibles futuras expansiones de la funcionalidad del bot.
- numpy, pandas, scikit-learn: Utilizadas para el análisis de datos y la implementación de algoritmos de recomendación más avanzados.
- SQLAlchemy: Utilizada para interactuar con bases de datos SQL para el almacenamiento de datos de películas.

## Configuración y Uso
1. Clona este repositorio.
2. Instala las dependencias del proyecto utilizando `pip install -r requirements.txt`.
3. Obtén el token de tu bot de Discord y configúralo en el archivo `bot.py`.
4. Ejecuta el bot utilizando `python bot.py`.

## Contribución
Si deseas contribuir a este proyecto, siéntete libre de abrir una solicitud de extracción (pull request) con tus mejoras o correcciones.

¡Gracias por tu interés en el Sistema de Recomendación de Películas en Discord!
