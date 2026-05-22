import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

ruta_imagen = None


def clasificar_danio(porcentaje):
    if porcentaje < 1:
        return "BAJO"
    elif porcentaje < 3:
        return "MEDIO"
    else:
        return "ALTO"


def seleccionar_imagen():
    global ruta_imagen

    ruta_imagen = filedialog.askopenfilename(
        filetypes=[
            ("Imágenes", "*.jpg *.jpeg *.png *.bmp")
        ]
    )

    if ruta_imagen:
        imagen = Image.open(ruta_imagen)

        imagen.thumbnail((400, 300))

        foto = ImageTk.PhotoImage(imagen)

        etiqueta_imagen.config(image=foto)
        etiqueta_imagen.image = foto

        resultado_label.config(text="Imagen cargada")


def analizar_imagen():
    global ruta_imagen

    if not ruta_imagen:
        messagebox.showwarning(
            "Advertencia",
            "Seleccione una imagen primero"
        )
        return

    imagen = cv2.imread(ruta_imagen)

    gris = cv2.cvtColor(
        imagen,
        cv2.COLOR_BGR2GRAY
    )

    gris = cv2.GaussianBlur(
        gris,
        (5, 5),
        0
    )

    grietas = cv2.Canny(
        gris,
        50,
        150
    )

    pixeles_grieta = np.count_nonzero(grietas)

    total_pixeles = (
        grietas.shape[0] *
        grietas.shape[1]
    )

    porcentaje = (
        pixeles_grieta /
        total_pixeles
    ) * 100

    nivel = clasificar_danio(porcentaje)

    resultado_label.config(
        text=(
            f"Área afectada: {porcentaje:.2f}%\n"
            f"Nivel de daño: {nivel}"
        )
    )

    cv2.imshow(
        "Grietas Detectadas",
        grietas
    )


ventana = tk.Tk()
ventana.title(
    "Sistema de Detección de Grietas"
)

ventana.geometry("600x550")

titulo = tk.Label(
    ventana,
    text="Detección de Grietas en Infraestructuras",
    font=("Arial", 14, "bold")
)

titulo.pack(pady=10)

btn_cargar = tk.Button(
    ventana,
    text="Seleccionar Imagen",
    command=seleccionar_imagen
)

btn_cargar.pack(pady=5)

etiqueta_imagen = tk.Label(
    ventana
)

etiqueta_imagen.pack(pady=10)

btn_analizar = tk.Button(
    ventana,
    text="Analizar Imagen",
    command=analizar_imagen
)

btn_analizar.pack(pady=5)

resultado_label = tk.Label(
    ventana,
    text="Sin análisis",
    font=("Arial", 12)
)

resultado_label.pack(pady=15)

ventana.mainloop()
