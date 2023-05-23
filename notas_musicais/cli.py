from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.escalas import escala

console = Console()
app = Typer()


@app.command()
def escalas(
    tonica: str = Argument('c', help='Tônica da escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da escala'),
):
    table = Table(show_header=True, header_style='bold magenta')
    notas, graus = escala(tonica, tonalidade).values()
    table.caption = f'Notas da escala de {tonica} {tonalidade}'

    for grau in graus:
        table.add_column(grau, justify='center', style='cyan')

    table.add_row(*notas)
    console.print(table)
