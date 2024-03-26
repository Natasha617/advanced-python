import click
import sys
from typing import Generator


def read_file(path: str) -> Generator[str, None, None]:
    with open(path, "rt", encoding="utf-8") as file:
        for line in file:
            yield line


@click.command()
@click.argument('path_file', default=".", nargs=1, type=click.Path(exists=True))
def nl_func(path: str) -> None:
    if path == '.':
        lines = sys.stdin.readlines()
    else:
        lines = read_file(path)

    for idx, line in enumerate(lines, start=1):
        print(f'{idx}\t{line.rstrip()}')


if __name__ == '__main__':
    nl_func()
