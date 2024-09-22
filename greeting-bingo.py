import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 質問
QUESTIONS = [
    "芸能人",
    "動物",
    "食べ物",
    "国",
    "サークル",
    "出身地",
    "スポーツ",
    "趣味",
    "誕生月",
]
# 生成するカードの枚数
CARD_COUNT = 60
# 各学年の比率
GRADE_RATIO = {
    "B3": 0.25,
    "B4": (1 - 0.35) / 3,
    "M1": (1 - 0.35) / 3,
    "M2": (1 - 0.35) / 3,
    "D、先生": 0.10,
}

# 描画に関するパラメータ
HEIGHT = 297 * 5
WIDTH = 210 * 5
MARGIN = WIDTH / 12
TILE_COUNT = 3
TILE_SIZE = (WIDTH - MARGIN * 2) / TILE_COUNT
MAIN_COLOR = (30, 30, 30)
Y_OFFSET = 60


def get_font(size: int) -> ImageFont:
    return ImageFont.truetype("ヒラギノ丸ゴ ProN W4.ttc", size=size)


def sample_grade() -> str:
    return np.random.choice(list(GRADE_RATIO.keys()), p=list(GRADE_RATIO.values()))


def sample_grades() -> list[str]:
    while True:
        grades = [sample_grade() for _ in range(TILE_COUNT**2)]
        if len(set(grades)) == len(GRADE_RATIO):
            return grades


def main() -> None:
    images = []

    for seed in range(CARD_COUNT):
        np.random.seed(seed)
        questions = list(QUESTIONS)
        np.random.shuffle(questions)

        grades = sample_grades()

        im = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        # ビンゴの枠線を描画
        for i in range(TILE_COUNT + 1):
            x1 = MARGIN
            x2 = WIDTH - MARGIN
            y = HEIGHT / 2 + (i - TILE_COUNT / 2) * TILE_SIZE + Y_OFFSET
            draw.line((x1, y, x2, y), fill=MAIN_COLOR, width=2)
        for j in range(TILE_COUNT + 1):
            x = WIDTH / 2 - (j - TILE_COUNT / 2) * TILE_SIZE
            y1 = HEIGHT / 2 - TILE_COUNT * TILE_SIZE / 2 + Y_OFFSET
            y2 = HEIGHT / 2 + TILE_COUNT * TILE_SIZE / 2 + Y_OFFSET
            draw.line((x, y1, x, y2), fill=MAIN_COLOR, width=2)

        # 質問をマスに書く
        for i in range(TILE_COUNT):
            for j in range(TILE_COUNT):
                x = MARGIN + (WIDTH - MARGIN * 2) * (j + 0.5) / TILE_COUNT
                y = HEIGHT / 2 + (i - TILE_COUNT / 2) * TILE_SIZE + 20 + Y_OFFSET
                draw.text(
                    (x, y),
                    questions[i * TILE_COUNT + j],
                    anchor="mt",
                    fill=MAIN_COLOR,
                    font=get_font(32),
                )
                draw.text(
                    (x, y + 40),
                    f"学年：{grades[i * TILE_COUNT + j]}",
                    anchor="mt",
                    fill=MAIN_COLOR,
                    font=get_font(24),
                )

        # タイトルを書く
        draw.text(
            (WIDTH / 2, MARGIN + 40 + Y_OFFSET),
            "秋キックオフレク　挨拶ビンゴ",
            anchor="mt",
            fill=MAIN_COLOR,
            font=get_font(40),
        )
        draw.text(
            (WIDTH / 2, MARGIN + 40 + 24 + 40 + Y_OFFSET),
            "名前：_______________　学年：_____",
            anchor="mt",
            fill=MAIN_COLOR,
            font=get_font(40),
        )

        images.append(im)

    images[0].save(
        "greeting-bingo.pdf",
        "PDF",
        quality=100,
        save_all=True,
        append_images=images[1:],
        optimize=True,
    )


if __name__ == "__main__":
    assert len(QUESTIONS) == TILE_COUNT**2
    main()
