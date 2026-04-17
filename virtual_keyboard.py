from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.containers import Horizontal

second_row = [
    'q','w','e','r','t','y','u','i','o','p'
]

third_row = ['a','s','d','f','g','h','j','k','l']
fourth_row = ['z','x','c','v','b','n','m']
class KeyboardApp(App):
    CSS_PATH = 'keys.tcss'
    def compose(self):
        for k in second_row:
            yield Button(k, classes="second_row", id=k)
        for k in third_row:
            yield Button(k, classes="third_row", id=k)
        for k in fourth_row:
            yield Button(k, classes="fourth_row", id=k)

        

if __name__ == '__main__':
    app = KeyboardApp()
    app.run()