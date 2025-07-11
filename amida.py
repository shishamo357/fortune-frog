import pyxel
import random

class Amida:
    def __init__(self, cols=3, rows=10, cell_w=24, cell_h=10, start_x=30, start_y=10):
        # あみだくじの基本設定
        self.cols = cols
        self.rows = rows
        self.cell_w = cell_w
        self.cell_h = cell_h
        self.start_x = start_x
        self.start_y = start_y

        self.num_steps = rows  # ChatGPTのアドバイスで追加←アニメーション時に必要 そのまま採用

        self.vertical_lines = [] # 縦線　これは固定で
        self.horizontal_lines = [] # 横線はランダムに生成
        self.x_positions = [start_x + i * cell_w for i in range(cols)]
        
        self._generate_lines() # 横線を自動生成

    def _generate_lines(self):
        # 縦線の生成
        for i in range(self.cols):
            x = self.start_x + i * self.cell_w
            self.vertical_lines.append((x, self.start_y, x, self.start_y + self.rows * self.cell_h))

        # 横線の生成をランダムで
        for i in range(self.rows):
            y = self.start_y + i * self.cell_h
            a = random.randint(0, self.cols - 2)
            x1 = self.start_x + a * self.cell_w
            x2 = x1 + self.cell_w
            self.horizontal_lines.append((x1, y, x2, y))

    def get_column_index(self, xpos):

        # クリックしてどこからスタートしたか
        for i, x in enumerate(self.x_positions):
            if abs(xpos - x) < 12:
                return i
        return None

    def draw(self):

        # 縦線かくかなー
        for x1, y1, x2, y2 in self.vertical_lines:
            pyxel.line(x1, y1, x2, y2, 0)
        
        # 横線
        for x1, y1, x2, y2 in self.horizontal_lines:
            pyxel.line(x1, y1, x2, y2, 0)

    def get_path_points(self, col_index):
        """
        カエルるんのアニメーション移動用のルートを計算
        ChatGPTのアイデアを元に,できるかぎり調整
        """
        path = []
        x = self.x_positions[col_index]
        y = self.start_y

        for i in range(self.num_steps):
            # 下に少しずつ落ちる
            for dy in range(10):
                path.append((x - 6, y + dy))
            y += 10

            # 横に分岐があれば左右に移動
            for (x1, y1, x2, y2) in self.horizontal_lines:
                if y1 == y and (x == x1 or x == x2):
                    if x == x1:
                        for dx in range(1, x2 - x1 + 1):
                            path.append((x - 6 + dx, y))
                        x = x2
                    else:
                        for dx in range(1, x1 - x2 + 1):
                            path.append((x - 6 - dx, y))
                        x = x1
                    break

        return path
