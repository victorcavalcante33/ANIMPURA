from __future__ import annotations

from anima_pura.models import MetaHumano

_CLASSES = {
    "fogo": "Arconte Ígneo",
    "água": "Oráculo Abissal",
    "ar": "Vidente Celeste",
    "terra": "Guardião Rúnico",
    "éter": "Tecelão Astral",
}

_HABILIDADES = {
    "fogo": "Explosão Solar",
    "água": "Manto das Marés",
    "ar": "Lâmina de Vento",
    "terra": "Pulso Sísmico",
    "éter": "Ressonância da Alma",
}


def _normalizar_elemento(elemento: str) -> str:
    e = elemento.strip().lower()
    if e not in _CLASSES:
        return "éter"
    return e


def _codigo_da_alma(nome: str, numero: int, elemento: str, arquetipo: str) -> str:
    base = f"{nome[:3].upper()}-{arquetipo[:3].upper()}-{elemento[:2].upper()}"
    assinatura = (sum(ord(c) for c in nome + arquetipo) + numero * 33) % 999
    return f"{base}-{assinatura:03d}"


def criar_meta_humano(
    nome: str,
    numero_principal: int,
    elemento: str,
    arquetipo: str,
) -> MetaHumano:
    elemento_ok = _normalizar_elemento(elemento)
    classe = _CLASSES[elemento_ok]
    habilidade = _HABILIDADES[elemento_ok]

    historia = (
        f"{nome} nasceu sob o número {numero_principal} e foi marcado pelo arquétipo "
        f"{arquetipo}. Desde cedo, desenvolveu afinidade com {elemento_ok}."
    )
    destino = (
        "Unificar tecnologia perdida e magia ancestral nas Ilhas Fraturadas, "
        "restaurando o equilíbrio entre facções." 
    )
    codigo = _codigo_da_alma(nome, numero_principal, elemento_ok, arquetipo)

    return MetaHumano(
        nome=nome,
        numero_principal=numero_principal,
        elemento=elemento_ok,
        arquetipo=arquetipo,
        classe_mistica=classe,
        codigo_da_alma=codigo,
        historia=historia,
        destino=destino,
        habilidade_inicial=habilidade,
    )
