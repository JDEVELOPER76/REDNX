# 🔥 REDNX -- Web App para Remover Fondos con FastAPI + Rembg

REDNX es una aplicación web ligera que permite **eliminar el fondo de
imágenes** usando `rembg` y un backend en **FastAPI**.\
Incluye una interfaz limpia en HTML/CSS/JS y un servidor rápido en
Python, ideal para proyectos personales, demos o integraciones.

------------------------------------------------------------------------

## 🚀 Características

-   🖼 **Elimina fondos** de imágenes PNG/JPG automáticamente\
-   ⚡ **Backend rápido con FastAPI**\
-   🎨 **Frontend simple y responsive**\
-   📁 Soporte para arrastrar y soltar imágenes\
-   📦 Fácil de instalar y desplegar\
-   🔄 Respuestas en tiempo real desde la API

------------------------------------------------------------------------

## 🛠 Tecnologías usadas

-   **Python 3.10+**\
-   **FastAPI**\
-   **Rembg** (modelo U²Net)\
-   **HTML + CSS + JavaScript**\
-   **Fetch API** para comunicación con el backend

------------------------------------------------------------------------

## 📥 Instalación

Clona el repositorio:

``` bash
git clone https://github.com/JDEVELOPER76/REDNX.git
cd REDNX
```

Instala los requisitos:

``` bash
pip install -r requirements.txt
```

> Si usas Windows y hay problemas con `rembg`, instala también:
>
> ``` bash
> pip install onnxruntime
> ```

------------------------------------------------------------------------

## ▶️ Ejecución del servidor

``` bash
python server.py
```

o si usas Uvicorn directamente:

``` bash
uvicorn server:app --reload
```

El servidor estará en:

👉 http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🖥 Uso

1.  Abre la app en tu navegador\
2.  Sube o arrastra una imagen\
3.  Espera a que el backend procese el fondo\
4.  La imagen se descarga automaticamente

------------------------------------------------------------------------


## 👤 Autor

**JDeveloper76**\
💻 GitHub: https://github.com/JDEVELOPER76\
🚀 Proyecto: REDNX

------------------------------------------------------------------------

## 📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.\
Puedes usarlo y modificarlo como quieras.

------------------------------------------------------------------------

⭐ **Si te gustó el proyecto, dale una estrella en GitHub.**
