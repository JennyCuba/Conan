# ConAn - Asistente Generador de Contenido Publicitario

ConAn es una aplicación diseñada para generar contenido publicitario de alta calidad para productos artesanales. Utiliza tecnologías avanzadas como OpenAI y Gemini para generar descripciones, imágenes y consejos de fotografía de manera eficiente.

## Características

- **Generación de Descripciones**: Crea descripciones atractivas y detalladas para productos artesanales.
- **Resúmenes de Texto**: Convierte descripciones en prompts ideales para generar imágenes.
- **Generación de Imágenes**: Genera imágenes publicitarias basadas en prompts y estilos personalizados.
- **Consejos de Fotografía**: Proporciona tips prácticos para tomar fotografías de productos.
- **Análisis de Imágenes**: Genera descripciones basadas en imágenes subidas por el usuario.

## Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web interactivas.
- **[OpenAI](https://openai.com/)**: Para generación de texto e imágenes.
- **[Google Gemini](https://ai.google/)**: Para análisis y generación de contenido basado en imágenes.
- **[Python](https://www.python.org/)**: Lenguaje de programación principal.
- **[dotenv](https://pypi.org/project/python-dotenv/)**: Para manejar variables de entorno.

## Requisitos Previos

1. Python 3.8 o superior.
2. Claves API para OpenAI y Gemini.
3. Archivo `.env` con las siguientes variables:
   ```
   API_KEY=<tu_openai_api_key>
   GEMINI_API_KEY=<tu_gemini_api_key>
   ```

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/conan.git
   cd conan
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las claves API en un archivo `.env` en la raíz del proyecto:
   ```plaintext
   API_KEY=<tu_openai_api_key>
   GEMINI_API_KEY=<tu_gemini_api_key>
   ```

## Uso

1. Ejecuta la aplicación:
   ```bash
   streamlit run main.py
   ```

2. Accede a la aplicación en tu navegador en `http://localhost:8501`.

3. Selecciona una de las opciones:
   - **Ingresar datos manualmente**: Proporciona los materiales, tipo de producto y estilo deseado para generar contenido.
   - **Subir una imagen**: Sube una imagen del producto para generar contenido basado en ella.

## Estructura del Proyecto

```
app/
├── config.py               # Configuración de las APIs y logging
├── openai_utils.py         # Funciones relacionadas con OpenAI
├── gemini_utils.py         # Funciones relacionadas con Gemini
├── main.py                 # Punto de entrada principal de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── .gitignore              # Archivos y carpetas ignorados por Git
└── README.md               # Documentación del proyecto
```

## Archivos Clave

- **`config.py`**: Configura las claves API y el sistema de logging.
- **`openai_utils.py`**: Contiene funciones para generar descripciones, resúmenes, imágenes y tips de fotografía usando OpenAI.
- **`gemini_utils.py`**: Contiene funciones para generar descripciones basadas en imágenes usando Gemini.
- **`main.py`**: Implementa la interfaz de usuario con Streamlit.

## Ejemplo de Uso

### Generación Manual
1. Ingresa los materiales del producto, el tipo de producto y el estilo deseado.
2. Haz clic en "Generar Contenido".
3. Obtendrás:
   - Una descripción detallada.
   - Un resumen para generar imágenes.
   - Una imagen publicitaria.
   - Consejos de fotografía.

### Generación Basada en Imágenes
1. Sube una imagen del producto.
2. Ingresa el estilo deseado para la nueva imagen.
3. Haz clic en "Generar Contenido desde Imagen".
4. Obtendrás:
   - Una descripción basada en la imagen.
   - Un resumen para generar imágenes.
   - Una nueva imagen publicitaria.
   - Consejos de fotografía.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme:
- **Email**: jenny.cuba.c@gmail.com
- **GitHub**: [tu-usuario](https://github.com/JennyCuba)
