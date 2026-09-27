__version__ = "1.0"

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp


class MainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.04, 0.25, 0.65, 1)
            self.background = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

        title = Label(
            text="БАРНОМАИ",
            font_size=dp(26),
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, None),
            height=dp(45),
            pos_hint={"top": 0.95}
        )
        self.add_widget(title)

        title2 = Label(
            text="ШАРИФБЕК",
            font_size=dp(38),
            bold=True,
            color=(1, 0.85, 0.05, 1),
            size_hint=(1, None),
            height=dp(55),
            pos_hint={"top": 0.90}
        )
        self.add_widget(title2)

        subtitle = Label(
            text="Маълумоти худро ворид кунед",
            font_size=dp(15),
            color=(1, 1, 1, 0.9),
            size_hint=(1, None),
            height=dp(35),
            pos_hint={"top": 0.85}
        )
        self.add_widget(subtitle)

        with self.canvas:
            Color(1, 1, 1, 1)
            self.card = RoundedRectangle(
                pos=(dp(20), dp(25)),
                size=(dp(320), dp(470)),
                radius=[dp(28)]
            )

        self.content = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=[dp(30), dp(22), dp(30), dp(15)],
            size_hint=(None, None),
            size=(dp(320), dp(460)),
            pos=(dp(20), dp(30))
        )

        name_label = Label(
            text="Ном",
            font_size=dp(18),
            bold=True,
            color=(0.04, 0.12, 0.35, 1),
            size_hint_y=None,
            height=dp(32),
            halign="left",
            valign="middle"
        )
        name_label.bind(size=name_label.setter("text_size"))
        self.content.add_widget(name_label)

        self.name_input = TextInput(
            hint_text="Масалан: Шарифбек",
            multiline=False,
            font_size=dp(17),
            padding=[dp(15), dp(12)],
            background_color=(0.94, 0.96, 1, 1),
            foreground_color=(0.05, 0.08, 0.20, 1),
            cursor_color=(0.05, 0.40, 0.90, 1),
            size_hint_y=None,
            height=dp(52)
        )
        self.content.add_widget(self.name_input)

        age_label = Label(
            text="Синну сол",
            font_size=dp(18),
            bold=True,
            color=(0.04, 0.12, 0.35, 1),
            size_hint_y=None,
            height=dp(32),
            halign="left",
            valign="middle"
        )
        age_label.bind(size=age_label.setter("text_size"))
        self.content.add_widget(age_label)

        self.age_input = TextInput(
            hint_text="Масалан: 21",
            multiline=False,
            input_filter="int",
            font_size=dp(17),
            padding=[dp(15), dp(12)],
            background_color=(0.94, 0.96, 1, 1),
            foreground_color=(0.05, 0.08, 0.20, 1),
            cursor_color=(0.05, 0.40, 0.90, 1),
            size_hint_y=None,
            height=dp(52)
        )
        self.content.add_widget(self.age_input)

        self.result_container = FloatLayout(
            size_hint_y=None,
            height=dp(70)
        )

        with self.result_container.canvas.before:
            Color(0.88, 0.97, 0.91, 1)
            self.result_background = RoundedRectangle(
                pos=self.result_container.pos,
                size=self.result_container.size,
                radius=[dp(16)]
            )

        self.result_container.bind(
            pos=self.update_result_background,
            size=self.update_result_background
        )

        self.result = Label(
            text="Натиҷа дар ин ҷо пайдо мешавад",
            font_size=dp(15),
            bold=True,
            color=(0.05, 0.45, 0.20, 1),
            halign="center",
            valign="middle",
            size_hint=(1, 1)
        )
        self.result.bind(size=self.result.setter("text_size"))
        self.result_container.add_widget(self.result)
        self.content.add_widget(self.result_container)

        self.button = Button(
            text="НАТИҶА  →",
            font_size=dp(19),
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0, 0, 0, 0),
            size_hint_y=None,
            height=dp(58)
        )

        with self.button.canvas.before:
            Color(0.04, 0.40, 0.85, 1)
            self.button_background = RoundedRectangle(
                pos=self.button.pos,
                size=self.button.size,
                radius=[dp(16)]
            )

        self.button.bind(
            pos=self.update_button,
            size=self.update_button
        )
        self.button.bind(on_press=self.show_result)
        self.content.add_widget(self.button)

        self.clear_button = Button(
            text="Тоза кардан",
            font_size=dp(14),
            bold=True,
            color=(0.15, 0.30, 0.55, 1),
            background_color=(0, 0, 0, 0),
            size_hint_y=None,
            height=dp(32)
        )
        self.clear_button.bind(on_press=self.clear_fields)
        self.content.add_widget(self.clear_button)

        self.add_widget(self.content)

        self.bind(
            size=self.update_layout,
            pos=self.update_layout
        )

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size

    def update_layout(self, *args):
        card_width = self.width - dp(40)
        self.card.pos = (dp(20), dp(25))
        self.card.size = (card_width, dp(470))
        self.content.pos = (dp(20), dp(30))
        self.content.size = (card_width, dp(460))

    def update_result_background(self, *args):
        self.result_background.pos = self.result_container.pos
        self.result_background.size = self.result_container.size

    def update_button(self, *args):
        self.button_background.pos = self.button.pos
        self.button_background.size = self.button.size

    def show_result(self, instance):
        name = self.name_input.text.strip()
        age_text = self.age_input.text.strip()

        if not name:
            self.result.text = "Лутфан номро ворид кунед!"
            return

        if not age_text:
            self.result.text = "Лутфан синну солро ворид кунед!"
            return

        age = int(age_text)

        if age < 0:
            self.result.text = "Синну сол нодуруст аст!"
        elif age < 18:
            self.result.text = "Салом, " + name + "!\nТу ноболиғ ҳастӣ."
        elif age < 60:
            self.result.text = "Салом, " + name + "!\nТу калонсол ҳастӣ."
        else:
            self.result.text = "Салом, " + name + "!\nТу 60-сола ё аз он боло ҳастӣ."

    def clear_fields(self, instance):
        self.name_input.text = ""
        self.age_input.text = ""
        self.result.text = "Натиҷа дар ин ҷо пайдо мешавад"


class SharifbekApp(App):

    def build(self):
        self.title = "Барномаи Шарифбек"
        return MainScreen()


SharifbekApp().run()
