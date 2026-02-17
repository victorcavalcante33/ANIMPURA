from dataclasses import dataclass


@dataclass(frozen=True)
class MetaHumano:
    nome: str
    numero_principal: int
    elemento: str
    arquetipo: str
    classe_mistica: str
    codigo_da_alma: str
    historia: str
    destino: str
    habilidade_inicial: str


@dataclass
class PlayerState:
    meta_humano: MetaHumano
    nivel: int = 1
    hp: int = 100
    energia: int = 50
    ataque_base: int = 10
    defesa_base: int = 6

    def ataque_total(self) -> int:
        return self.ataque_base + self.nivel + (self.meta_humano.numero_principal % 5)

    def defesa_total(self) -> int:
        return self.defesa_base + (self.nivel // 2)
