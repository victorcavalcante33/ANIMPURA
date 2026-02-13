from anima_pura.combat import Inimigo, simular_turno
from anima_pura.meta_humano import criar_meta_humano
from anima_pura.models import PlayerState


def test_simular_turno_retorna_estado_valido():
    meta = criar_meta_humano("Ayla", 8, "fogo", "dragão")
    player = PlayerState(meta_humano=meta)
    inimigo = Inimigo(nome="Drone", hp=20, ataque=5, defesa=2)

    resultado = simular_turno(player, inimigo)

    assert resultado["dano_jogador"] >= 1
    assert resultado["dano_inimigo"] >= 1
    assert 0 <= resultado["hp_player"] <= player.hp
    assert 0 <= resultado["hp_inimigo"] <= inimigo.hp
