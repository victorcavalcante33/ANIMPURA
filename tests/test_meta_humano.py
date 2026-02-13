from anima_pura.meta_humano import criar_meta_humano


def test_criacao_meta_humano_campos_principais():
    meta = criar_meta_humano("Victor", 33, "éter", "lobo cósmico")
    assert meta.nome == "Victor"
    assert meta.classe_mistica == "Tecelão Astral"
    assert meta.habilidade_inicial == "Ressonância da Alma"
    assert meta.codigo_da_alma.startswith("VIC-LOB-ÉT-")
