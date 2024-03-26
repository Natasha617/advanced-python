import click


@click.command()
@click.argument('input_file', type=click.File('r', encoding='utf-8'), default='-')
def nl(input_file):
    lines = []

    if input_file.name == '<stdin>':
        try:
            while True:
                lines.append(input())
        except EOFError:
            pass
    else:
        lines = input_file.readlines()

    for i, line in enumerate(lines, start=1):
        click.echo(f"\t{i}\t{line}")


if __name__ == "__main__":
    nl()
