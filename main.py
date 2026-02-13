from anima_pura.combat import Inimigo, simular_turno
from anima_pura.meta_humano import criar_meta_humano
from anima_pura.models import PlayerState
from anima_pura.quest import gerar_quest_inicial


def run_demo() -> None:
    meta = criar_meta_humano(
        nome="Victor",
        numero_principal=33,
        elemento="éter",
        arquetipo="lobo cósmico",
    )

    player = PlayerState(meta_humano=meta)
    quest = gerar_quest_inicial(meta)
    boss = Inimigo(nome="Sentinela Necrorúnico", hp=80, ataque=12, defesa=7)

    print("=== ANIMA PURA :: MVP Loop ===")
    print(f"Meta-Humano: {meta.nome} | Classe: {meta.classe_mistica}")
    print(f"Código da Alma: {meta.codigo_da_alma}")
    print(f"Quest: {quest.titulo}")
    print(f"Objetivo: {quest.objetivo}")
    print("--- Combate (1 turno de simulação) ---")

    turno = simular_turno(player, boss)
    print(f"Você causou {turno['dano_jogador']} de dano.")
    print(f"Inimigo causou {turno['dano_inimigo']} de dano.")
    print(f"HP restante jogador: {turno['hp_player']}")
    print(f"HP restante inimigo: {turno['hp_inimigo']}")


if __name__ == "__main__":
    run_demo()
