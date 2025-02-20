import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

kivy.require('2.1.0')

class ConversorApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Criando o layout interno (GridLayout)
        layout = GridLayout(cols=2, padding=10, spacing=10, row_default_height=40, size_hint_y=None)
        
        # Label e Spinner para tipo de conversão
        self.label_tipo = Label(text="Escolha o tipo de conversão:", font_size=14, size_hint=(None, None), width=200)
        layout.add_widget(self.label_tipo)
        
        self.combo_tipo = Spinner(text="Distância", values=["Distância", "Peso", "Temperatura", "Tempo"], size_hint=(None, None), height=30)
        self.combo_tipo.bind(text=self.atualizar_unidades)
        layout.add_widget(self.combo_tipo)
        
        # Label e campo de entrada para o valor
        self.label_valor = Label(text="Insira o valor:", font_size=14, size_hint=(None, None), width=200)
        layout.add_widget(self.label_valor)
        
        self.entry_valor = TextInput(multiline=False, font_size=14, size_hint_y=None, height=30)
        layout.add_widget(self.entry_valor)
        
        # Label e Spinners para as unidades
        self.label_unidades = Label(text="Escolha as unidades:", font_size=14, size_hint=(None, None), width=200)
        layout.add_widget(self.label_unidades)
        
        self.combo_unidade_origem = Spinner(text="Metros", values=["Metros", "Kilômetros", "Milhas"], size_hint=(None, None), height=30)
        layout.add_widget(self.combo_unidade_origem)
        
        self.combo_unidade_destino = Spinner(text="Kilômetros", values=["Metros", "Kilômetros", "Milhas"], size_hint=(None, None), height=30)
        layout.add_widget(self.combo_unidade_destino)
        
        # Botão para converter
        self.botao_converter = Button(text="Converter", font_size=14, background_color=(0.2, 0.8, 0.2, 1), size_hint=(None, None), height=40)
        self.botao_converter.bind(on_press=self.converter)
        layout.add_widget(self.botao_converter)
        
        # Adicionando o layout ao scrollview
        scrollview = ScrollView()
        scrollview.add_widget(layout)
        
        self.root.add_widget(scrollview)

        # Layout para a mensagem de erro
        self.error_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=40, padding=[55, 0])
        self.label_resultado = Label(text="Resultado:", font_size=16, bold=True, size_hint=(None, None), width=200, halign='right')
        self.error_layout.add_widget(self.label_resultado)

        
        self.root.add_widget(self.error_layout)

        return self.root

    def converter(self, instance):
        try:
            valor = float(self.entry_valor.text)
            tipo_conversao = self.combo_tipo.text
            unidade_origem = self.combo_unidade_origem.text
            unidade_destino = self.combo_unidade_destino.text

            if tipo_conversao == "Distância":
                if unidade_origem == "Metros" and unidade_destino == "Kilômetros":
                    resultado = valor / 1000
                elif unidade_origem == "Kilômetros" and unidade_destino == "Metros":
                    resultado = valor * 1000
                elif unidade_origem == "Metros" and unidade_destino == "Milhas":
                    resultado = valor * 0.000621371
                elif unidade_origem == "Milhas" and unidade_destino == "Metros":
                    resultado = valor / 0.000621371

            elif tipo_conversao == "Peso":
                if unidade_origem == "Quilos" and unidade_destino == "Gramas":
                    resultado = valor * 1000
                elif unidade_origem == "Gramas" and unidade_destino == "Quilos":
                    resultado = valor / 1000
                elif unidade_origem == "Quilos" and unidade_destino == "Libras":
                    resultado = valor * 2.20462
                elif unidade_origem == "Libras" and unidade_destino == "Quilos":
                    resultado = valor / 2.20462

            elif tipo_conversao == "Temperatura":
                if unidade_origem == "Celsius" and unidade_destino == "Fahrenheit":
                    resultado = (valor * 9/5) + 32
                elif unidade_origem == "Fahrenheit" and unidade_destino == "Celsius":
                    resultado = (valor - 32) * 5/9
                elif unidade_origem == "Celsius" and unidade_destino == "Kelvin":
                    resultado = valor + 273.15
                elif unidade_origem == "Kelvin" and unidade_destino == "Celsius":
                    resultado = valor - 273.15

            elif tipo_conversao == "Tempo":
                if unidade_origem == "Horas" and unidade_destino == "Minutos":
                    resultado = valor * 60
                elif unidade_origem == "Minutos" and unidade_destino == "Horas":
                    resultado = valor / 60
                elif unidade_origem == "Segundos" and unidade_destino == "Minutos":
                    resultado = valor / 60
                elif unidade_origem == "Horas" and unidade_destino == "Segundos":
                    resultado = valor * 3600
                elif unidade_origem == "Segundos" and unidade_destino == "Horas":
                    resultado = valor / 3600

            self.label_resultado.text = f"Resultado: {resultado:.2f} {unidade_destino}"
            self.error_layout.clear_widgets()
            self.error_layout.add_widget(self.label_resultado)
        except ValueError:
            self.label_resultado.text = "Por favor, insira um valor numérico válido!"
            self.error_layout.clear_widgets()
            self.error_layout.add_widget(self.label_resultado)

    def atualizar_unidades(self, instance, value):
        tipo = self.combo_tipo.text
        if tipo == "Distância":
            unidades = ["Metros", "Kilômetros", "Milhas"]
        elif tipo == "Peso":
            unidades = ["Quilos", "Gramas", "Libras"]
        elif tipo == "Temperatura":
            unidades = ["Celsius", "Fahrenheit", "Kelvin"]
        elif tipo == "Tempo":
            unidades = ["Horas", "Minutos", "Segundos"]

        self.combo_unidade_origem.values = unidades
        self.combo_unidade_destino.values = unidades
        self.combo_unidade_origem.text = unidades[0]
        self.combo_unidade_destino.text = unidades[1]

if __name__ == "__main__":
    ConversorApp().run()
