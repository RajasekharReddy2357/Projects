from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

class TicTacToe(GridLayout):
    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        self.cols = 3
        self.size_hint = (1, 1)
        self.game_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[Button(text='', font_size=24, size_hint=(1, 1)) for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.bind(on_press=lambda button, x=row, y=col: self.player_move(x, y, button))
                self.add_widget(button)

    def player_move(self, row, col, button):
        if self.game_board[row][col] == ' ':
            self.game_board[row][col] = 'o'
            button.text = 'O'
            if self.check_victory('o'):
                self.display_end_game('Congratulations, You won! Well played!')
                return
            self.draw_move()  # Removing the delay and calling draw_move directly

    def draw_move(self):
        free_fields = [(r, c) for r in range(3) for c in range(3) if self.game_board[r][c] == ' ']
        if free_fields:
            row, col = random.choice(free_fields)
            self.game_board[row][col] = 'x'
            self.buttons[row][col].text = 'X'
            if self.check_victory('x'):
                self.display_end_game('I won! Better luck next time.')
                return
        if not any(' ' in row for row in self.game_board):
            self.display_end_game("It's a draw! Try again for a rematch.")

    def check_victory(self, sign):
        for n in range(3):
            if all(self.game_board[n][c] == sign for c in range(3)) or all(self.game_board[r][n] == sign for r in range(3)):
                return True
        if all(self.game_board[i][i] == sign for i in range(3)) or all(self.game_board[i][2-i] == sign for i in range(3)):
            return True
        return False

    def display_end_game(self, message):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(300, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label = Label(text="Do you want to play one more game?", font_size=20)
        yes_button = Button(text="Yes", size_hint=(None, None), size=(100, 50))
        no_button = Button(text="No", size_hint=(None, None), size=(100, 50))
        buttons_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        buttons_layout.add_widget(yes_button)
        buttons_layout.add_widget(no_button)
        layout.add_widget(label)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)
        yes_button.bind(on_press=self.reset_game)
        no_button.bind(on_press=self.quit_game)

    def reset_game(self, instance):
        self.clear_widgets()
        self.__init__()

    def quit_game(self, instance):
        App.get_running_app().stop()

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()

if __name__ == '__main__':
    TicTacToeApp().run()
