from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class myApp(App):
    def build(self):
        self.expression = ""  # Store the current expression
        root_widget = BoxLayout(orientation='vertical')
        output_label = TextInput(font_size=50, multiline=False)
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        button_grid = GridLayout(cols=4, size_hint_y=None, height=100)

        for symbol in button_symbols:
            button = Button(text=symbol)
            if symbol == '=':
                button.bind(on_press=self.calculate_result)
            else:
                button.bind(on_press=self.add_to_expression)
            button_grid.add_widget(button)

        clear_button = Button(text='Clear', size_hint_y=None, height=100)
        clear_button.bind(on_press=self.clear_label)

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)
        return root_widget

    def add_to_expression(self, instance):
        self.expression += instance.text
        self.root.children[0].text = self.expression

    def calculate_result(self, instance):
        try:
            result = str(eval(self.expression))
            self.root.children[0].text = result
            self.expression = result
        except (SyntaxError, ZeroDivisionError):
            self.root.children[0].text = 'Error'

    def clear_label(self, instance):
        self.expression = ""
        self.root.children[0].text = ""


if __name__ == '__main__':
    myApp().run()