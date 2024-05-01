import random

if __name__ == "__main__":
    header = """---
    marp: true
    theme: uncover
    style: |
        h1 {
            font-size: 150px;
        }
    """

    with open("words.txt", "r") as f:
        words = f.read().split("\n")
        words = list(set(words))

    random.seed(0)
    random.shuffle(words)

    content = header

    for word in words:
        content += "---\n"
        content += f"# {word}\n"

    with open("content.md", "w") as f:
        f.write(content)
