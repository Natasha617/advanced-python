import click
import sys


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def wc(files):
    if not files:
        # Если файлы не переданы, считываем стандартный ввод
        content = sys.stdin.read()
        line_count = content.count('\n')
        word_count = len(content.split())
        char_count = len(content)
        click.echo(f"Кол-во строк: {line_count}\tКол-во слов: {word_count}\tКол-во букв:{char_count}")
    else:
        total_line_count = 0
        total_word_count = 0
        total_char_count = 0
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
                line_count = content.count('\n')
                word_count = len(content.split())
                char_count = len(content)
                total_line_count += line_count
                total_word_count += word_count
                total_char_count += char_count
                click.echo(f"Кол-во строк: {line_count}\tКол-во слов: {word_count}\tКол-во букв:{char_count}")

        # Выводим суммарную статистику, если передано больше одного файла
        if len(files) > 1:
            click.echo(f"Кол-во строк:{total_line_count}\tКол-во слов:{total_word_count}\tКол-во букв:{total_char_count}\ttotal")


if __name__ == "__main__":
    wc()
