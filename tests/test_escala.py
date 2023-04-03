"""
AAA -  3A - A3

AAA - Arrange, Act, Assert
Arrumar, Agir, Afirmar(garantir)
"""

from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_escala_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Agir
    result = escala(tonica, tonalidade)

    # Afirma
    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    # Arrumar
    tonica = 'x'
    tonalidade = 'maior'
    mensagem_de_erro = (
        f'Essa nota não existe, tente uma das seguintes: {NOTAS}'
    )

    # Agir
    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    # Afirma
    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'
    mensagem_de_erro = (
        'Essa escala não existe ou ainda não foi implementada.'
        f' Tente uma dessas: {list(ESCALAS.keys())}'
    )

    # Agir
    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    # Afirma
    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'tonica,esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('D#', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('E', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('F#', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('G', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('G#', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('A', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('A#', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('B', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    tonica = 'C'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    resultado = escala(tonica, tonalidade)
    assert resultado['graus'] == esperado
