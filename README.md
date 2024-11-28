# Generador de historias con API local usando text-generation-webui

1. Selección de modelos

   Comenzamos eligiendo los modelos, vamos a utilizar los siguientes:

   * Qwen/Qwen2.5-1.5B-Instruct
   * TheBloke/Mistral-7B-v0.1-GGUF
   
   ![Modelos descargados](images/models.png)

2. Accedemos mediante la terminal al directorio del repositorio, donde crearemos un entorno virtual de python.

   ![Creación entorno virtual](images/env_terminal.png)

3. Pasamos a text-generation-webui, donde haremos una primera prueba de los modelos.
   
   Pedimos una historia donde el personaje principal es un profesor, el secundario un alumno, tiene lugar en una piscina y la acción es comer.

   El primer modelo lo solicitamos con más tokens que el segundo. Recibiendo las siguientes respuestas, respectivamente:

   ![Qwen story](images/qwen_story.png)

   ![Mistral story](images/mistral_story.png)

4.  

