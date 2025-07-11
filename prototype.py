print("原因")

出力

TitleScreen(start_ga




仮設定

import pyxel

class App:
    def __init__(self):
        self.state = "title"  # タイトル   
        self.frog_y = 0

        pyxel.init(160, 120, title="Fortune Frog")
        pyxel.load("frog.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        # スタート位置
        if self.selected_x is None and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            line_positions = [40, 80, 120]
            for x in line_positions:
                # カエル　０，０から１５，１５
                if x - 8 <= mx <= x + 8:
                    self.selected_x = x
                    self.frog_y = 0
                    break

    def draw(self):
        pyxel.cls(7)  ７はしろ

        # あみだ線　たて
        for x in [40, 80, 120]:
            pyxel.line(x, 20, x, 100, 0)

        # あみだ線　よこ
        pyxel.line(40, 40, 80, 40, 0)
        pyxel.line(80, 60, 120, 60, 0)
        pyxel.line(40, 80, 80, 80, 0)

        # カエル描画
        if self.selected_x is not None:
            pyxel.blt(self.selected_x - 8, self.frog_y + 20, 0, 0, 0, 16, 16, 1)

if __name__ == "__main__":
    App()