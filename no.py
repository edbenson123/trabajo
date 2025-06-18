import streamlit as st
import pyttsx3

# Inicializa el motor de voz
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Simulación de tarjetas y columnas
tablero = {
    "📥 Pendientes": ["Estudiar Python", "Leer documentación de Trello"],
    "🛠 En Progreso": ["Crear demo en Streamlit"],
    "✅ Hecho": ["Diseñar interfaz de accesibilidad"]
}

# Configuración de la app
st.set_page_config(page_title="AccesoLab Trello Demo", layout="wide")
st.title(" AccesoLab | Demo de Accesibilidad tipo Trello")

# ✅ Descripción del proyecto
st.markdown("""
---

## 🎯 Funciones de Accesibilidad de esta Aplicación

Esta app fue diseñada como una **demostración de accesibilidad digital** para personas con discapacidad visual, inspirada en herramientas como Trello. Estas son sus funciones principales:

✅ **Lectura de tarjetas y columnas mediante TTS (Texto a Voz)**  
Las tareas pueden ser leídas en voz alta haciendo clic en el botón 🔊.

✅ **Comandos de voz (simulados) para crear, mover y comentar tareas**  
Puedes escribir comandos como "crear tarea", "mover tarea" o "comentar" para simular acciones por voz.

✅ **Atajos de teclado accesibles y configurables**  
Se muestran los atajos básicos y pueden leerse en voz alta para mejorar la navegación.

✅ **Retroalimentación auditiva para cada acción realizada**  
Cada comando ejecutado tiene una respuesta en voz que confirma la acción.

---
""")

# Mostrar columnas y tarjetas
st.subheader("🧾 Tablero de Tareas (lectura TTS)")
for columna, tareas in tablero.items():
    with st.expander(columna):
        for tarea in tareas:
            st.write("•", tarea)
            if st.button(f"🔊 Leer: {tarea}", key=f"{columna}_{tarea}"):
                speak(f"Tarea en {columna}: {tarea}")
                st.success("✔ Tarea leída en voz alta")

# Comandos de voz simulados
st.subheader("🎤 Comandos por Voz (simulado)")
comando = st.text_input("Escribe un comando (crear, mover, comentar):")

if st.button(" Ejecutar comando"):
    if "crear" in comando.lower():
        speak("Nueva tarea creada")
        st.success("Tarea creada (simulada)")
    elif "mover" in comando.lower():
        speak("Tarea movida con éxito")
        st.success("Tarea movida (simulada)")
    elif "comentar" in comando.lower():
        speak("Comentario añadido")
        st.success("Comentario agregado (simulado)")
    else:
        speak("Comando no reconocido")
        st.warning("!!! Comando desconocido")

# Simulación de atajos de teclado
st.subheader("⌨️ Atajos de Teclado (simulados)")
st.markdown("""
- **Ctrl + N**: Crear nueva tarea  
- **Ctrl + M**: Mover tarea  
- **Ctrl + C**: Comentar tarea  
""")

if st.button("🔊 Leer atajos"):
    speak("Control N para crear tarea, Control M para mover tarea, Control C para comentar tarea")
    st.info("✔ Atajos leídos")