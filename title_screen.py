import pyxel

class TitleScreen:
    def __init__(self, start_callback):
        self.start_callback = start_callback  # Appからー
        self.start_clicked = False            # スタートボタンがクリックされたか

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y

            # ボタンの範囲クリックで成功で。
            if 50 <= mx <= 110 and 85 <= my <= 105:
                self.start_clicked = True
                self.start_callback()  # App側のstart_game()

    def draw(self):
        pyxel.cls(13)  # 背景グレー

        # タイトル
        pyxel.text(40, 30, "FORTUNE", pyxel.COLOR_WHITE)
        pyxel.text(40, 40, "FROG", pyxel.COLOR_WHITE)

        # サブタイトル
        pyxel.text(35, 60, "～ カエルの運勢占い ～", 7)  # 薄い白

        # スタートボタン
        pyxel.rect(50, 85, 60, 20, 6)   # ボタンのなか青
        pyxel.rectb(50, 85, 60, 20, 1)  # ボタン黒
        pyxel.text(70, 92, "スタート", 1)  # ボタン文字黒
