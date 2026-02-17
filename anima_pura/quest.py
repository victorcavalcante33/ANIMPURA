from dataclasses import dataclass

from anima_pura.models import MetaHumano


@dataclass(frozen=True)
class Quest:
    titulo: str
    objetivo: str
    recompensa_xp: int
    recompensa_item: str


def gerar_quest_inicial(meta_humano: MetaHumano) -> Quest:
    ilha = "Ilha das Runas Quebradas"
    return Quest(
        titulo=f"Sinal em {ilha}",
        objetivo=(
            f"Investigue o farol arcano de {ilha} e derrote o sentinela corrompido "
            f"usando {meta_humano.habilidade_inicial}."
        ),
        recompensa_xp=120,
        recompensa_item="Fragmento de Imortalis",
    )
