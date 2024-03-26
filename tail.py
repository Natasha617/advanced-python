import click
import sys


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def tail(files):
    display_count = 17 if not files else 10

    if not files:
        # Если файлы не переданы, считываем стандартный ввод
        lines_buffer = sys.stdin.readlines()
        display_count = min(display_count, len(lines_buffer))
        lines_to_display = lines_buffer[-display_count:]
        click.echo('\n'.join(lines_to_display))
    else:
        for file in files:
            click.echo(f"==> {file} <==")
            with open(file, 'r', encoding='utf-8') as f:
                lines_buffer = f.readlines()
                display_count = min(display_count, len(lines_buffer))
                lines_to_display = lines_buffer[-display_count:]
                click.echo('\n'.join(lines_to_display))


if __name__ == "__main__":
    tail()
