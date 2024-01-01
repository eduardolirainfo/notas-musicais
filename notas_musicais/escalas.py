"""
Módulo das escalas musicais.

Attributes:
   ESCALAS: Escalas implementadas usando a notação de inteiros
   NOTAS: Notas musicais

# ESCALAS

As escalas estão implementadas em uma constante chamada `ESCALAS`. Que é um dicionário onde as chaves são os nomes das escalas. Se quiser ver todas as escalas implementadas pode usar:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import ESCALAS
>>> ESCALAS
{'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)...}

```

A notação inteira para as escalas foi retirada da página [List of musical scales and modes](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes) na wikipedia.

tip: Dica!
    Você pode contribuir com novas escalas usando a notação inteira:
    [Escalas wikipedia](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes).
    Todos os Pull Requests serão bem vindos! :heart:

# NOTAS

As notas estão sendo definidas em uma constante `NOTAS`. Foi optado por menter somente as notas no formato Natural e o Sustenido (#) para a simplificação do fluxo de trabalho. Embora não esteja totalmente correto. Para ver as 12 notas você pode:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import NOTAS
>>> NOTAS
['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

```
"""
NOTAS = []
NOTAS_ESCALA = "C C# D D# E F F# G G# A A# B".split()
ESCALAS = {"maior": (0, 2, 4, 5, 7, 9, 11), "menor": (0, 2, 3, 5, 7, 8, 10)}


def associar_intervalos_tom_semitom(intervalos, tom=2, semitom=1):
    """Associa os intervalos com tom e semitom."""
    intervalos_associados = []

    for intervalo in intervalos:
        if intervalo == tom:
            intervalos_associados.append(tom)
        elif intervalo == semitom:
            intervalos_associados.append(semitom)

    return intervalos_associados


def converte_escala(intervalo: list) -> list:
    """Converte a escala de notação inteira para intervalos."""
    if not intervalo:
        return []

    intervalos = []
    for i in range(len(intervalo) - 1):
        intervalos.append(intervalo[i + 1] - intervalo[i])

    return intervalos


def ajustar_acidente(
    nota_atual: str,
    nota_alterada: str,
    nota_anterior: str,
    intervalos_associados: list[int],
) -> str:
    """
    Ajusta o acidente da nota atual baseado na nota anterior.

    Args:
        nota_atual: Nota que precisa ter o acidente ajustado.
        nota_anterior: Nota anterior na escala.
        intervalos: Os intervalos da escala.

    Returns:
        A nota atual ajustada em relação à nota anterior.
    """
    # print(nota_atual, nota_alterada, nota_anterior)

    if nota_anterior == "":
        return nota_atual

    if nota_anterior not in NOTAS_ESCALA:
        tonica_nome = nota_anterior[0]
        nota_anterior = (
            tonica_nome if tonica_nome in NOTAS_ESCALA else nota_anterior[:-1]
        )

    if len(nota_atual) > 2:
        tonica_nome = nota_atual[0]
        if len(nota_atual) > 2:
            nota_atual = tonica_nome
        else:
            nota_atual = tonica_nome + "b"

    intera_intervalo = len(NOTAS)

    intervalo = intervalos_associados[intera_intervalo - 1]

    tonica = NOTAS[0] if len(NOTAS) > 0 else ""
    nota_anterior = NOTAS[-1] if len(NOTAS) > 0 else ""

    result = nota_atual

    if intervalo == 1:
        if nota_alterada[0] == nota_anterior[0]:
            result = nota_atual + "b"
    elif nota_alterada[0] == nota_anterior[0] or (
        nota_alterada[0] != nota_atual[0] and "#" not in nota_anterior
    ):
        print(intervalo, nota_atual, nota_anterior, NOTAS, sep=" - ")
        if nota_atual == "Eb" and nota_anterior == "Db":
            result = "Ebb"
        elif nota_atual.count("b") == 1 and nota_anterior.count("b") == 2:
            result = nota_atual + "b"
        elif nota_atual == "Ab" and nota_anterior == "Gb":
            result = "Abb"
        else:
            result = nota_atual[0] + "b"
    elif "#" in tonica:
        print(intervalo, nota_atual, nota_anterior, NOTAS, sep=" - ")
        if nota_atual == "F" and nota_anterior == "D#":
            result = "E#"
        elif nota_atual == "D" and nota_anterior == "B#":
            result = "C##"
        elif nota_atual == "C" and nota_anterior == "B#":
            result = "C##"
        elif nota_atual == "C" and nota_anterior == "A#":
            result = "B#"
        elif nota_atual == "D" and nota_anterior == "B":
            result = "C##"
        elif nota_atual == "G" and nota_anterior == "E":
            result = "F##"
        elif nota_atual == "A" and nota_anterior == "F#":
            result = "G#"
        elif nota_atual == "F" and nota_anterior == "E#":
            result = "F##"
        elif nota_atual == "C" and nota_anterior == "B":
            result = "C##"
        elif nota_atual == "A" and nota_anterior == "G":
            result = "G##"
        elif nota_atual == "G" and nota_anterior == "E#":
            result = "F##"
        elif nota_atual.count("#") == 0 and nota_anterior.count("#") == 2:
            result = nota_atual + "##"

    return result


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica da escala.
        tonalidade: Tonalidade da escala.

    Returns:
        Um dicionário com as notas da escala e os graus.

    Raises:
        ValueError: Caso a tônica não seja uma nota válida.
        KeyError: Caso a escala não exista ou não tenha sido implementada.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    tonica_simbolo = ""
    if tonica not in NOTAS_ESCALA:
        tonica_nome = tonica[0]
        tonica_simbolo = tonica[1].lower() if len(tonica) > 1 else ""
        tonica = tonica_nome if tonica_nome in NOTAS_ESCALA else tonica[:-1]

    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS_ESCALA.index(tonica)
    except ValueError:
        raise ValueError(
            f"Essa nota não existe, tente uma dessas {NOTAS_ESCALA}"
        ) from None
    except KeyError as exc:
        raise KeyError(
            f"Essa escala não existe ou não foi implementada. Tente uma dessas {list(ESCALAS.keys())}"
        ) from exc

    temp = []
    nota_anterior = ""

    for nota in range(7):
        nota_pos = (tonica_pos + intervalos[nota]) % len(NOTAS_ESCALA)

        nota_nome = NOTAS_ESCALA[nota_pos]
        nota_alterada = nota_nome + tonica_simbolo if len(nota_nome) > 0 else ""

        intervalos_associados = converte_escala(intervalos)
        if len(temp) > 0:
            if nota_nome[0] in temp[-1][0]:
                nota_pos = (nota_pos + 1) % len(NOTAS_ESCALA)
                nota_nome = NOTAS_ESCALA[nota_pos]

        nota_saida = ajustar_acidente(
            nota_nome + tonica_simbolo,
            nota_alterada,
            nota_anterior,
            intervalos_associados,
        )

        temp.append(nota_saida)
        nota_anterior = temp[-1] if temp[-1] else ""
        NOTAS.append(nota_saida)

    return {"notas": temp, "graus": ["I", "II", "III", "IV", "V", "VI", "VII"]}
