from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.acordes import acorde as _acorde
from notas_musicais.escalas import escala as _escala

console = Console()
app = Typer()


@app.command()
def escala(
    tonica: str = Argument("c", help="Tônica da escala"),
    tonalidade: str = Argument("maior", help="Tonalidade da escala"),
):
    """Gera uma escala a partir de uma tônica e uma tonalidade."""
    table = Table(show_header=True, header_style="bold magenta")
    notas, graus = _escala(tonica, tonalidade).values()
    table.caption = f"Notas da escala de {tonica} {tonalidade}"

    for grau in graus:
        table.add_column(grau, justify="center", style="cyan")

    table.add_row(*notas)
    console.print(table)


@app.command()
def acorde(
    cifra: str = Argument("C", help="Cifra do acorde"),
):
    """Gera um acorde a partir de uma cifra."""
    table = Table(show_header=True, header_style="bold magenta")
    notas, graus = _acorde(cifra).values()
    table.caption = f"Tríade de {cifra}"
    for grau in graus:
        table.add_column(grau, justify="center", style="cyan")

    table.add_row(*notas)
    console.print(table)
