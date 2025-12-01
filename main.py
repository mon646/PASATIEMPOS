from kivy.app import App                # Importa la clase principal de Kivy
from kivy.uix.screenmanager import Screen, ScreenManager  # Para manejar pantallas
from kivy.lang import Builder           # Para cargar el archivo .kv
from kivy.core.window import Window     # Para controlar tamaño/propiedades de la ventana


# Definimos una pantalla básica
class MainScreen(Screen):
    pass


class FondoApp(App):
    def build(self):
        # Carga el archivo .kv
        return Builder.load_file("Pasatiempo.kv")


if __name__ == "__main__":
    # Cambia el tamaño de la ventana aquí (ancho, alto) en píxeles.
    # Modifica los valores a los que necesites, por ejemplo (1024, 768) o (800, 600).
    Window.size = (500, 650)
    FondoApp().run()
