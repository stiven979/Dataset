import streamlit as st
import numpy as np
import joblib

# Cargar el modelo
modelo_path = "random_forest_emprender_final (1).pkl"  # Cambia por la ruta de tu modelo
modelo = joblib.load(modelo_path)

# Obtener las características que espera el modelo
caracteristicas_modelo = modelo.feature_names_in_

# Título de la aplicación
st.title("Predicción de Intención Emprendedora")

# Formulario: Datos personales
st.header("Datos personales")
semestre = st.slider("Semestre", 1, 10, 1)
edad = st.number_input("Edad", min_value=18, max_value=100, value=25)
genero = st.selectbox("Género", options=["Masculino", "Femenino"], index=0)
estado_civil = st.selectbox("Estado Civil", options=["Soltero/a", "Casado/a", "Otro"], index=0)
escolaridad_madre = st.slider("Escolaridad de la Madre (1: Ninguna o primaria incompleta - 6: Posgrado)", 1, 6, 3)
escolaridad_padre = st.slider("Escolaridad del Padre (1: Ninguna o primaria incompleta - 6: Posgrado)", 1, 6, 3)
actividad_madre = st.slider("Actividad Laboral de la Madre (1: Desempleada - 5: Empresaria)", 1, 5, 3)
actividad_padre = st.slider("Actividad Laboral del Padre (1: Desempleado - 5: Empresario)", 1, 5, 3)
hermanos = st.number_input("Número de Hermanos (0 a 20)", min_value=0, max_value=20, value=2)

# Formulario: Habilidades y actitudes
st.header("Habilidades y actitudes")
detectar_oportunidades = st.slider("Habilidad para detectar oportunidades de negocio en el mercado (1: Muy baja - 5: Muy alta)", 1, 5, 3)
realizar_deberes = st.slider("Cumplimiento de deberes en plazos establecidos (1: Nunca - 5: Siempre)", 1, 5, 3)
persistencia = st.slider("Nivel de persistencia profesional (1: Muy bajo - 5: Muy alto)", 1, 5, 3)
creatividad = st.slider("Capacidad para encontrar soluciones creativas (1: Muy baja - 5: Muy alta)", 1, 5, 3)
liderazgo = st.slider("Frecuencia con la que eres elegido como líder (1: Nunca - 5: Siempre)", 1, 5, 3)
respetar_opinion = st.slider("Percepción de respeto hacia tu opinión (1: Muy baja - 5: Muy alta)", 1, 5, 3)
motivar = st.slider("Habilidad para motivar a personas desmotivadas (1: Muy baja - 5: Muy alta)", 1, 5, 3)
convencer_equipo = st.slider("Capacidad para resolver conflictos y liderar equipos (1: Muy baja - 5: Muy alta)", 1, 5, 3)




# Planeación
st.header("Planeación")
siempre_planeo = st.slider("Hábito de planificar todas las actividades (1: Nunca - 5: Siempre)", 1, 5, 3)
defino_pasos = st.slider("Definir metas y analizar los pasos necesarios (1: Nunca - 5: Siempre)", 1, 5, 3)
defino_metas = st.slider("Definir metas a corto, mediano y largo plazo (1: Nunca - 5: Siempre)", 1, 5, 3)
me_gustan_objetivos = st.slider("Preferencia por establecer objetivos desafiantes (1: Muy baja - 5: Muy alta)", 1, 5, 3)

# Creatividad y cambio
st.header("Creatividad y cambio")
prefiero_novedades = st.slider("Preferencia por trabajos con novedades frente a actividades rutinarias (1: Muy baja - 5: Muy alta)", 1, 5, 3)
me_gusta_cambiar = st.slider("Gusto por cambiar la forma de trabajar siempre que sea posible (1: Muy baja - 5: Muy alta)", 1, 5, 3)
mejorar_convencional = st.slider("Interés en mejorar métodos convencionales sin seguir etapas estrictas (1: Muy bajo - 5: Muy alto)", 1, 5, 3)
creatividad_proyectos = st.slider("Confianza en la creatividad al realizar proyectos o actividades (1: Muy baja - 5: Muy alta)", 1, 5, 3)

# Tolerancia al riesgo
st.header("Tolerancia al riesgo")
asumir_deuda = st.slider("Disposición para asumir una deuda a largo plazo por las ventajas de una oportunidad de negocio (1: Muy baja - 5: Muy alta)", 1, 5, 3)
admito_riesgo = st.slider("Aceptación de correr riesgos a cambio de posibles beneficios (1: Muy baja - 5: Muy alta)", 1, 5, 3)
fuera_confort = st.slider("Toma de decisiones fuera de la zona de confort (1: Muy baja - 5: Muy alta)", 1, 5, 3)
mayor_riesgo = st.slider("Creencia de que los riesgos más altos generan resultados más impactantes (1: Muy baja - 5: Muy alta)", 1, 5, 3)

# Relaciones sociales
st.header("Relaciones sociales")
contactos_importantes = st.slider("Importancia de los contactos sociales para mi vida personal (1: Muy baja - 5: Muy alta)", 1, 5, 3)
conozco_ayuda = st.slider("Conocimiento de personas que podrían ayudarme profesionalmente (1: Muy bajo - 5: Muy alto)", 1, 5, 3)
me_relaciono_facil = st.slider("Facilidad para relacionarme con otras personas (1: Muy baja - 5: Muy alta)", 1, 5, 3)
mantengo_contacto = st.slider("Búsqueda de mantener contacto constante con mi red de relaciones (1: Muy baja - 5: Muy alta)", 1, 5, 3)

# Motivación emprendedora
st.header("Motivación emprendedora")
listo_emprender = st.slider("Estoy listo para hacer todas las actividades necesarias para ser empresario (1: No estoy listo - 5: Totalmente listo)", 1, 5, 3)
esfuerzos_empresa = st.slider("Haré todos los esfuerzos necesarios para crear y mantener mi propia empresa (1: Ningún esfuerzo - 5: Todos los esfuerzos)", 1, 5, 3)
sueno_empresa = st.slider("Aunque trabaje para otras empresas, nunca abandonaría mi sueño de abrir mi negocio (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
mayor_logro = st.slider("Mi mayor logro será tener mi propio negocio (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
intencion_empresa = st.slider("Tengo la intención de abrir una empresa en los próximos años (1: No tengo intención - 5: Totalmente decidido)", 1, 5, 3)

# Ambiente universitario
st.header("Ambiente universitario")
uni_oportunidades = st.slider("El ambiente universitario me ayudó a detectar oportunidades de negocio y ser persistente (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
uni_liderazgo = st.slider("El ambiente universitario desarrolló mis habilidades de liderazgo, por medio de trabajos en grupo (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
uni_planificacion = st.slider("El ambiente universitario me proporcionó herramientas de planificación y estrategia en diferentes disciplinas, desarrollando mi capacidad de planear (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
uni_creatividad = st.slider("El ambiente universitario ha mejorado mi creatividad y capacidad de innovar (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
uni_riesgos = st.slider("El ambiente universitario me ha capacitado para relacionar y analizar las variables que influyen en el resultado de un problema, aumentando mi capacidad de asumir riesgos calculados (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
uni_contactos = st.slider("El ambiente universitario me proporcionó diversos contactos importantes personal y profesionalmente (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)
uni_motivacion = st.slider("El ambiente universitario me motivó a querer abrir mi propio negocio (1: Totalmente en desacuerdo - 5: Totalmente de acuerdo)", 1, 5, 3)

# Conversión de datos de entrada
genero_val = 1 if genero == "Masculino" else 0
estado_civil_val = {"Soltero/a": 0, "Casado/a": 1, "Otro": 2}[estado_civil]



st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/vector-gratis/fondo-escritorio-moderno-vector-diseno-azul-geometrico_53876-135923.jpg");
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True
)


# Crear un diccionario con los datos de entrada
entrada_dict = {
    "Semestre": semestre,
    "Edad": edad,
    "Género": genero_val,
    "Estado Civil": estado_civil_val,
    "Escolaridad Madre": escolaridad_madre,
    "Escolaridad Padre": escolaridad_padre,
    "Actividad laboral Madre": actividad_madre,
    "Actividad laboral Padre": actividad_padre,
    "Hermanos": hermanos,
    "[Creo que tengo una buena habilidad en detectar oportunidades de negocio en el mercado.]": detectar_oportunidades,
    "[Realizo mis deberes correctamente, respetando los plazos establecidos.]": realizar_deberes,
    "[Profesionalmente, me considero una persona mucho más persistente que las demás.]": persistencia,
    "[Siempre encuentro soluciones creativas para problemas con los que me encuentro.]": creatividad,
    "[A menudo, soy elegido líder en actividades escolares o profesionales.]": liderazgo,
    "[Las personas respetan mi opinión]": respetar_opinion,
    "[Soy capaz de estimular a las personas a realizar tareas para las que están desmotivadas]": motivar,
    "[Puedo convencer a las personas a superar los conflictos y trabajar en equipo con el objetivo de alcanzar un determinado resultado.]": convencer_equipo,
    "En relación con las afirmaciones a seguir, seleccione según su preferencia [Siempre planeo muy bien todo lo que hago.]": siempre_planeo,
    "En relación con las afirmaciones a seguir, seleccione según su preferencia [Defino donde quiero llegar y analizo todos los pasos que debo seguir.]": defino_pasos,
    "En relación con las afirmaciones a seguir, seleccione según su preferencia [Defino mis metas de corto, mediano y largo plazo.]": defino_metas,
    "En relación con las afirmaciones a seguir, seleccione según su preferencia [Me gusta establecer objetivos y metas para sentirme desafiado]": me_gustan_objetivos,
    "[Prefiero un trabajo repleto de novedades a una actividad rutinaria.]": prefiero_novedades,
    "[Me gusta cambiar mi forma de trabajo siempre que sea posible.]": me_gusta_cambiar,
    "[Me gusta mejorar la manera convencional y correcta de las actividades, no siguiendo estrictamente etapas]": mejorar_convencional,
    "[Apuesto a la creatividad en el momento de elaborar proyectos / actividades.]": creatividad_proyectos,
    "[Asumiría una deuda a largo plazo, creyendo en las ventajas que una oportunidad de negocio me traería.]": asumir_deuda,
    "[Admito correr riesgos a cambio de posibles beneficios.]": admito_riesgo,
    "[Mis decisiones no son basadas en mi zona de confort]": fuera_confort,
    "[Creo que involucrarse en situaciones de mayor riesgo ocasionará resultados más impactantes.]": mayor_riesgo,
    "[Los contactos sociales que tengo son muy importantes para mi vida personal.]": contactos_importantes,
    "[Conozco a varias personas que podrían ayudarme profesionalmente, en caso de requerir de su ayuda.]": conozco_ayuda,
    "[Me relaciono muy fácilmente con otras personas.]": me_relaciono_facil,
    "[Busco mantener contacto constante con las personas de mi red de relaciones.]": mantengo_contacto,
    "[Estoy listo para hacer todas las actividades para ser un empresario.]": listo_emprender,
    "[Haré todos los esfuerzos para crear y mantener mi propia empresa.]": esfuerzos_empresa,
    "[Aunque trabaje para otras empresas, nunca abandonaría mi sueño de abrir mi negocio.]": sueno_empresa,
    "[Mi mayor logro será tener mi propio negocio.]": mayor_logro,
    "[Tengo la intención de abrir una empresa en los próximos años.]": intencion_empresa,
    "[El ambiente universitario me ayudó a detectar oportunidades de negocio y ser persistente.]": uni_oportunidades,
    "[El ambiente universitario desarrolló mis habilidades de liderazgo, por medio de trabajos en grupo.]": uni_liderazgo,
    "[El ambiente universitario me proporcionó herramientas de planificación y estrategia en diferentes disciplinas, desarrollando mi capacidad de planear.]": uni_planificacion,
    "[El ambiente universitario ha mejorado mi creatividad y capacidad de innovar.]": uni_creatividad,
    "[El ambiente universitario me ha capacitado para relacionar y analizar las variables que influyen en el resultado de un problema, aumentando mi capacidad de asumir riesgos calculados.]": uni_riesgos,
    "[El ambiente universitario me proporcionó diversos contactos importantes personal y profesionalmente.]": uni_contactos,
    "[El ambiente universitario me motivó a querer abrir mi propio negocio.]": uni_motivacion
}





# Crear un array ordenado para alimentar al modelo
entrada = np.array([entrada_dict[feature] for feature in caracteristicas_modelo]).reshape(1, -1)

# Predicción
if st.button("Predecir"):
    proba = modelo.predict_proba(entrada)[0][1]  # Probabilidad de emprender
    st.write("Probabilidad de intención emprendedora:")
    st.progress(int(proba * 100))
    if proba > 0.5:
        st.success("¡La persona tiene una alta probabilidad de emprender!")
    else:
        st.error("La persona tiene una baja probabilidad de emprender.")
