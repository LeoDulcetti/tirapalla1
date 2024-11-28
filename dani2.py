import streamlit as st
from PIL import Image

# Set the page title and layout
st.set_page_config(page_title="Tirapallá", layout="wide")

# Load Images
logo_path = "Screenshot 2024-11-27 at 21.54.30.png"  # Path to the logo
background_path = "background.png"  # Path to the background image

logo = Image.open(logo_path)

# Background Image Styling
st.markdown(f"""
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            background-image: url("{background_path}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center center;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }}
        
        .title {{
            color: #FFA500;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-top: 5px;
        }}
        
        .subtitle {{
            color: black;
            font-size: 18px;
            text-align: center;
        }}
        
        .event-card {{
            background-color: rgba(240, 248, 255, 0.8);
            border-radius: 10px;
            padding: 15px;
            margin-top: 15px;
            text-align: center;
        }}
        
        .profile-section {{
            border: 2px dashed #4682B4;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.8);
        }}
        
        .logo-container {{
            display: flex;
            justify-content: flex-end;
            align-items: flex-end;
            height: 0px;
            margin-top: 20px;
        }}

        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #808080;
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px 0;
        }}
    </style>
""", unsafe_allow_html=True)

# Display Logo
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.image(logo, width=1000)
st.markdown('</div>', unsafe_allow_html=True)

# App Title and Subtitle
st.markdown("""
    <div class="title"> Descubre el Aragón escondido</div>
    <div class="title"> Conoce tu tierra como nunca la has conocido</div>
    <div class="title"> Dejanos conocerte un poquito más...</div>
    <div class="subtitle">Busca eventos según tus preferencias </div>
""", unsafe_allow_html=True)

# Sidebar for Profile Picture Upload
st.sidebar.title("Tu Perfil")
uploaded_file = st.sidebar.file_uploader("Sube tu foto de perfil:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    profile_image = Image.open(uploaded_file)
    st.sidebar.image(profile_image, caption="Tu Foto de Perfil", use_container_width=True)
else:
    st.sidebar.markdown("""
        <div class="profile-section">
            <p>No seas timido/a! No has subido una foto de perfil.</p>
            <p>¡Sube una para personalizar tu experiencia!</p>
        </div>
    """, unsafe_allow_html=True)


# Input fields for user information
name = st.text_input("Tu Nombre:")
surname = st.text_input("Tu Apellido:")
location = st.selectbox("Resido en:", ["Zaragoza", "Huesca", "Teruel"])
travel_companion = st.selectbox("Viajo con:", ["Amigos", "Familia", "Con mi pareja ❤️", "Solo :("])
hobbies = ["Naturaleza", "Música", "Vinos", "Patrimonio Cultural", "Restaurante"]
hobby = st.selectbox("¿Cuál es tu hobby favorito?", hobbies)

# Event recommendations with images and descriptions
recommendations = {
    "Naturaleza": [
        {"title": "Cantavieja - El Rebollar",
         "description": "Agradable recorrido que reúne un cierto desnivel y termina en una zona de ocio y descanso muy apetecible, sobre todo para ir con niños a disfrutar de una jornada sin alejarse de Cantavieja. Durante el itinerario se disfruta de la perspectiva de la localidad “colgada” sobre la montaña. El recorrido señalizado sale de Cantavieja por la ermita del Loreto y, por debajo de las escuelas, prosigue por una pista asfaltada. Pronto se convierte en pista de tierra y luego en sendero que, entre muros de piedra, desciende hasta la antigua carretera..",
         "image": "IMG_1627.jpg"},
        {"title": "Camino de los pilones",
         "description": "Es un itinerario muy curioso porque se encuentra jalonado con más de cien pilones de piedra, construidos en el siglo XVIII, que servían para orientarse en época de nieves y entre las frecuentes nieblas a esta altitud. El camino está declarado Bien de Interés Cultural (BIC). Se conoce también como Camino de Jaime I porque se tiene constancia de que este rey lo recorrió en algunas ocasiones marchando hacia la conquista de Valencia. Desde Allepuz, se asciende el resalte rocoso por encima del caserío, hasta alcanzar el peirón de San Cristóbal.",
         "image": "IMG_1615.jpeg"}
    ],
    "Música": [
        {"title": "Musicamino",
         "description": "Vilafranca organiza un excelente festival de música clásica, folclórica y de jazz en la primera semana de agosto. En este festival actúan intérpretes internacionales y nacionales; siendo el momento más destacado el realizado en un anfiteatro natural de rocas en las Cuevas del Forcall, uno de los parajes naturales más emblemáticos del municipio, al que sólo se accede caminando.",
         "image": "IMG_1621.jpeg"},
        {"title": "Bureo por el pueblo",
         "description": "La palabra bureo significa: entretenimiento, diversión, juerga, encuentros etc. También son reuniones festivas celebradas en las masías donde se reunían de diferentes lugares para celebrar algún acontecimiento festivo y también en las matanzas. La mayoría de los masoveros que es como se llamaba a los que en ellas vivían se sentían algo distantes con la gente del pueblo, por eso, estas reuniones eran organizadas por ellos y para ellos.",
         "image": "IMG_1623.jpeg"}
    ],
    "Vinos": [
        {"title": "Visita guiada a Almazara BSI ",
         "description": "Incluye cata de tres vinos y de aceite de oliva virgen extra,Tapa individual de embutido de la región, Una botella de vino para dos personas, La experiencia puede ser para dos, cuatro o seis рах. Horario de la actividad: visitas limitadas a sábados y domingos exclusivamente a las 11 horas sin posibilidad de cambio de día u hora. Visita apta para todas las edades, excepción de niños menores de 6 años que se deberá consultar previamente en la bodega.",
         "image": "IMG_1625.jpeg"}
    ],
    "Patrimonio Cultural": [
        {"title": "Danza Guerrera de Tolodella",
         "description": "Los pueblos de Maestrazgo-Els Ports todavía mantienen una rica tradición folclórica con danzas populares que van desde las jotas aragonesas, la jota tortosina y las danzas del Maestrazgo de Castellón al ritmo de la dulzaina y el tabal. Entre las danzas populares destaca la Danza Guerrera de Todolella, declarada Patrimonio Histórico Artístico desde 1989. En esta danza secular ocho guerreros vestidos con indumentaria típica bailan trece pasos imitando una lucha con espadas, bastones y escudos. ",
         "image": "IMG_1616.jpeg"},
        {"title": "Fiesta de San Antonio ",
         "description": "Se trata de una fiesta invernal de origen medieval (o incluso más antiguo con raíces paganas), en la que el fuego juega siempre un papel protagonista dentro de las innumerables variantes de cada pueblo. Las fiestas de San Antonio están presentes, de una manera u otra, en todas las comarcas de Maestrazgo-Els Ports. Dependiendo de los pueblos, además del fuego aparecen actos relacionados con las bendiciones de los animales domésticos y las figuras de los demonios o dimonis que tientan al santo en diferentes representaciones teatrales o asustan de manera juguetona a los niños y parroquianos con sus máscaras, siempre alrededor del fuego y en algunos casos con petardos. ",
         "image": "IMG_1617.jpeg"}
    ]
}

# Display Recommendations
if st.button("¡Recomiéndame!"):
    if name and surname and hobby:
        st.markdown(f"### Hola {name} {surname}! Estas son las recomendaciones que tenemos para ti hoy!:")
        events = recommendations.get(hobby, [])

        for event in events:
            st.markdown(f"""
                <div class="event-card">
                    <h4>{event["title"]}</h4>
                    <p>{event["description"]}</p>
                </div>
            """, unsafe_allow_html=True)

            # Display event image
            try:
                event_image = Image.open(event["image"])
                st.image(event_image, caption=event["title"])
            except FileNotFoundError:
                st.error(f"No se pudo cargar la imagen para {event['title']}.")

            # Add call button
            st.button(f"Llamar: +34 644874087 para {event['title']}")

    else:
        st.error("Por favor, completa todos los campos para obtener recomendaciones.")

# Footer
st.markdown("""
    <style>
        /* Increase specificity to ensure the footer style is applied */
        .footer, .css-1d391kg {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #808080; /* Grey */
            background-color: #FFEB3B; /* Yellow */
            padding: 10px 0;
        }
    </style>
    <div class="footer">Made with ❤️ in Zaragoza</div>
""", unsafe_allow_html=True)
