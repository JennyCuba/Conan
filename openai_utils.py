import openai
import streamlit as st
import logging

def generate_description(tags, product_type):
    logging.info("Generating description for product type '%s' with tags '%s'.", product_type, tags)
    if not tags or not product_type:
        logging.error("Tags or product type is empty.")
        raise ValueError("Tags and product type cannot be empty.")
    
    prompt = f"Genera una descripción atractiva y detallada para la venta de {product_type} hecho con los siguientes materiales: {tags}. La descripción debe resaltar la calidad, la artesanía y la exclusividad del producto en no más de 150 palabras."
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en marketing y redacción de textos para productos artesanales."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        description = response.choices[0].message.content.strip()
        logging.info("Description generated successfully.")
        return description
    except Exception as e:
        logging.error("Error generating description: %s", e)
        st.error(f"Error generating description: {e}")
        return None

def summarize_text(text, example_summary=None):
    logging.info("Summarizing text.")
    if not text:
        logging.error("Text is empty.")
        raise ValueError("Text cannot be empty.")
    
    prompt = f"Resume el siguiente texto para convertirlo en un prompt ideal para generar una imagen con el modelo dall-e-3:\n{text}, en no más de 50 palabras."
    if example_summary:
        prompt += f"\nEjemplo de resumen: {example_summary}\nGenera un resumen similar."
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en procesamiento de texto y resumen de contenido."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        summary = response.choices[0].message.content.strip()
        logging.info("Text summarized successfully.")
        return summary
    except Exception as e:
        logging.error("Error summarizing text: %s", e)
        st.error(f"Error summarizing text: {e}")
        return None

def generate_image(prompt, style):
    logging.info("Generating image with prompt '%s' and style '%s'.", prompt, style)
    if not prompt or not style:
        logging.error("Prompt or style is empty.")
        raise ValueError("Prompt and style cannot be empty.")

    prompt_with_style = f"{prompt} El estilo de la imagen debe ser: {style}"
    try:
        response = openai.images.generate(
            prompt=prompt_with_style,
            n=1,
            size="1024x1024",
            model="dall-e-3",
            quality="standard"
        )
        image_url = response.data[0].url
        logging.info("Image generated successfully.")
        return image_url, prompt_with_style
    except Exception as e:
        logging.error("Error generating image: %s", e)
        st.error(f"Error generating image: {e}")
        return None, None

def generate_photography_tips(prompt_description):
    logging.info("Generating photography tips for prompt description '%s'.", prompt_description)
    if not prompt_description:
        logging.error("Prompt description is empty.")
        raise ValueError("Prompt description cannot be empty.")
    
    prompt = f"Basándote en la siguiente descripción de una imagen de un producto artesanal: '{prompt_description}', proporciona consejos prácticos para tomar fotografías de productos de manera sencilla para usuarios con poco conocimiento en fotografía. Incluye recomendaciones sobre iluminación, ángulos y fondo, en no más de 400 palabras."
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en fotografía de producto."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700
        )
        tips = response.choices[0].message.content.strip()
        logging.info("Photography tips generated successfully.")
        return tips
    except Exception as e:
        logging.error("Error generating photography tips: %s", e)
        st.error(f"Error generating photography tips: {e}")
        return None