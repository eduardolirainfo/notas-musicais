from pytest import mark

from notas_musicais.acordes import acorde


@mark.parametrize(
    'nota, esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
    ],
)
def test_acorde_deve_retornar_as_notas_correspondentes_ao_acorde(
    nota, esperado
):
    notas, _ = acorde(nota).values()
    assert esperado == notas


@mark.parametrize(
    'cifra, esperado',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)
def test_acorde_deve_retornar_as_graus_correspondentes_ao_acorde(
    cifra, esperado
):
    _, graus = acorde(cifra).values()
    assert esperado == graus
