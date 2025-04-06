import streamlit as st
import logging
from config import *  # Configuración de APIs
from openai_utils import generate_description, summarize_text, generate_image, generate_photography_tips
from gemini_utils import generate_description_from_image_gemini

logging.basicConfig(level=logging.INFO)
logging.info("Application started.")

def main():
    logging.info("Main function started.")
    st.title("ConAn")
    st.write("Asistente generador de contenido publicitario ¡Genera descripciones, imágenes y tips de fotografía para productos artesanales!")

    option = st.radio("Selecciona cómo quieres generar el contenido:", ("Ingresar datos manualmente", "Subir una imagen"))

    if option == "Ingresar datos manualmente":
        logging.info("Manual content generation selected.")
        with st.form("manual_content_generator"):
            tags = st.text_input("Materiales del producto:", value="", placeholder="Ejemplo: esferas de citrino, tanza, mosquetón perita, separador de plata 925")
            product_type = st.text_input("Tipo de producto:", value="", placeholder="Ejemplo: collar artesanal")
            style = st.text_input("Estilo de la imagen:", value="", placeholder="Ejemplo: minimalista y elegante")
            submit = st.form_submit_button("Generar Contenido")

        if submit:
            logging.info("Manual content generation form submitted.")
            with st.spinner("Generando contenido... ⏳"):
                description = generate_description(tags, product_type)
                if description:
                    logging.info("Description generated successfully.")
                    st.subheader("Descripción:")
                    st.write(description)

                    summary = summarize_text(description)
                    if summary:
                        logging.info("Summary generated successfully.")
                        st.subheader("Resumen:")
                        st.write(summary)

                        image_url, prompt_used = generate_image(summary, style)
                        if image_url:
                            logging.info("Image generated successfully.")
                            st.subheader("Imagen publicitaria:")
                            st.image(image_url, caption="Imagen Publicitaria", use_container_width=True)

                            tips = generate_photography_tips(prompt_used)
                            if tips:
                                logging.info("Photography tips generated successfully.")
                                st.subheader("Tips de Fotografía:")
                                st.write(tips)

    else:  # Subir imagen
        logging.info("Image-based content generation selected.")
        uploaded_image = st.file_uploader("Sube una imagen del producto", type=["jpg", "jpeg", "png"])
        if uploaded_image:
            logging.info("Image uploaded successfully.")
            st.image(uploaded_image, caption="Imagen subida", use_container_width=True)
            style = st.text_input("Estilo deseado para la nueva imagen:", value="", placeholder="Ejemplo: minimalista y elegante")
            if st.button("Generar Contenido desde Imagen"):
                logging.info("Image-based content generation button clicked.")
                with st.spinner("Analizando imagen y generando contenido... ⏳"):
                    description = generate_description_from_image_gemini(uploaded_image)
                    if description:
                        logging.info("Description from image generated successfully.")
                        st.subheader("Descripción basada en imagen:")
                        st.write(description)

                        summary = summarize_text(description)
                        if summary:
                            logging.info("Summary from image description generated successfully.")
                            st.subheader("Resumen generado:")
                            st.write(summary)

                            new_image_url, prompt_used = generate_image(summary, style)
                            if new_image_url:
                                logging.info("New image generated successfully.")
                                st.subheader("Nueva Imagen Publicitaria Mejorada:")
                                st.image(new_image_url, caption="Imagen mejorada basada en la descripción", use_container_width=True)

                            tips = generate_photography_tips(summary)
                            if tips:
                                logging.info("Photography tips from image description generated successfully.")
                                st.subheader("Tips de Fotografía:")
                                st.write(tips)

if __name__ == "__main__":
    main()
    logging.info("Application finished.")

