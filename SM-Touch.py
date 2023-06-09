from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime


class CalculatorApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical')

        # Visor da calculadora
        self.display = TextInput(
            multiline=False, readonly=True, halign='right', font_size=55
        )
        layout.add_widget(self.display)

        # Layout dos botões
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]

        # Adiciona os botões ao layout
        for row in buttons:
            button_row = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    on_press=self.on_button_press,
                    background_color=(1, 1, 1, 1)
                )
                button_row.add_widget(button)
            layout.add_widget(button_row)

        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = 'Error'
        else:
            self.display.text += instance.text


class ClockApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical')

        # Visor do relógio
        self.display = Label(font_size=80)
        layout.add_widget(self.display)

        # Atualiza o relógio a cada segundo
        Clock.schedule_interval(self.update_clock, 1)

        return layout

    def update_clock(self, *args):
        self.display.text = datetime.now().strftime('%H:%M:%S')


class MobileOSApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical')

        # Botões dos aplicativos
        calculator_button = Button(
            text='Calculadora',
            on_press=self.open_calculator_app
        )
        layout.add_widget(calculator_button)

        clock_button = Button(
            text='Relógio',
            on_press=self.open_clock_app
        )
        layout.add_widget(clock_button)

        return layout

    def open_calculator_app(self, instance):
        calculator_app = CalculatorApp()
        calculator_app.run()

    def open_clock_app(self, instance):
        clock_app = ClockApp()
        clock_app.run()


if __name__ == '__main__':
    MobileOSApp().run()
