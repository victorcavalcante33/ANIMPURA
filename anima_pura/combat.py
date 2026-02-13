from dataclasses import dataclass

from anima_pura.models import PlayerState


@dataclass(frozen=True)
class Inimigo:
    nome: str
    hp: int
    ataque: int
    defesa: int


def calcular_dano(ataque: int, defesa: int) -> int:
    bruto = ataque - (defesa // 2)
    return 1 if bruto < 1 else bruto


def simular_turno(player: PlayerState, inimigo: Inimigo) -> dict:
    dano_jogador = calcular_dano(player.ataque_total(), inimigo.defesa)
    dano_inimigo = calcular_dano(inimigo.ataque, player.defesa_total())

    hp_inimigo = max(0, inimigo.hp - dano_jogador)
    hp_player = max(0, player.hp - dano_inimigo)

    return {
        "dano_jogador": dano_jogador,
        "dano_inimigo": dano_inimigo,
        "hp_inimigo": hp_inimigo,
        "hp_player": hp_player,
    }
