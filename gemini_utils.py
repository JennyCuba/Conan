import streamlit as st
from PIL import Image
import io
import google.generativeai as genai
import logging

def generate_description_from_image_gemini(uploaded_image):
    logging.info("Generando una descripcion a partir de la imagen utilizando Gemini.")
    try:
        image_bytes = uploaded_image.read()
        model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")
        response = model.generate_content(
            [
                "Describe en español y de manera atractiva el producto de la imagen. Resalta sus materiales, colores, estilo y posibles usos en no más de 150 palabras.",
                Image.open(io.BytesIO(image_bytes))
            ]
        )
        description = response.text.strip()
        logging.info("Decripcion generarada correctamente.")
        return description
    except Exception as e:
        logging.error("Error al generar la descripcion a partir de la imagen: %s", e)
        st.error(f"Error generando descripción a partir de la imagen (Gemini): {e}")
        return None