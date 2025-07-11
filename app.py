import pyxel
from amida import Amida
from title_screen import TitleScreen
import random

class App:
    def __init__(self):
        pyxel.init(200, 180, title="Fortune Frog")
        pyxel.load("frog.pyxres")

        self.state = "title"
        self.title_screen = TitleScreen(self.start_game)

        # あみだの生成　←細かいのはNotionサブの方にメモしてある
        self.amida = Amida(cols=3, rows=10, cell_w=24, cell_h=10)
        self.selected_x = None
        self.frog_x = None
        self.frog_y = None
        self.frog_path = []
        self.frog_index = 0
        self.frog_moving = False
        self.transition_frames = 0

        # 運勢のリスト←pixelは日本語対応してなかった～
        self.fortunes = ["Great Luck", "Good Luck" , "Small Luck" ]
        self.result = None
        self.retry_button = (70, 140, 60, 20)  # 基本的に(x, y, w, h)

        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

     # タイトルクリックから移動
    def start_game(self):
        self.state = "game"
        self.transition_frames = 0

    def prepare_frog_path(self, col_index):
        self.frog_path = self.amida.get_path_points(col_index)
        self.frog_index = 0
        self.frog_moving = True
        if self.frog_path:
            self.frog_x, self.frog_y = self.frog_path[0]

    def update(self):
        if self.state == "title":
            self.title_screen.update()
            if self.title_screen.start_clicked:
                self.state = "game"
            return

        if self.state == "result":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                mx, my = pyxel.mouse_x, pyxel.mouse_y
                x, y, w, h = self.retry_button
                if x <= mx <= x + w and y <= my <= y + h:
                    
                 return

        # 移動後にクリック事故起きた
        # ChatGPT案：クリック誤反応防止のための初期遅延
        if self.transition_frames < 3:
            self.transition_frames += 1
            return

        if self.frog_moving:
            if self.frog_index < len(self.frog_path):
                self.frog_x, self.frog_y = self.frog_path[self.frog_index]
                self.frog_index += 1
            else:
                self.frog_moving = False
                # 結果表示
                self.state = "result"
                self.result = random.choice([ "Great Luck","Good Luck","Small Luck","Future Luck","Bad Luck","Worst Luck"])
            return

        if self.selected_x is None and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mouse_x = pyxel.mouse_x
            col = self.amida.get_column_index(mouse_x)
            if col is not None:
                self.selected_x = col
                self.prepare_frog_path(col)

    def draw(self):
        pyxel.cls(7)

        if self.state == "title":
            self.title_screen.draw()
            return

        self.amida.draw()

        if self.frog_x is not None and self.frog_y is not None:
            pyxel.blt(self.frog_x, self.frog_y, 0, 0, 0, 16, 16, 1)

        if self.state == "result":
            #if self.result is not None:
            pyxel.text(100, 90, f"Result: {self.result}", 8)
            x, y, w, h = self.retry_button
            # pyxel.rect(60, 140, 80, 10, 1)← これを使うとボタンの背景が描画されるけど没
            pyxel.text(x + 10, y + 6, "Retry", 7)
           # pyxel.text(100, 100, "TEST", 8)

App()
