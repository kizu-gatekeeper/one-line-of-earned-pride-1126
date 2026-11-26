"""Entry for make.fun: One Line of Earned Pride.

A quiet, earned moment of pride, in one concrete scene.
"""
import os

LINE = "After three failed driving tests, she practiced at dawn for a year; today she parallel-parked first try, and her instructor cried before she did."
MAX_CHARS = 240


def write_entry(out_dir):
    assert LINE.strip() and "\n" not in LINE and len(LINE) <= MAX_CHARS
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
