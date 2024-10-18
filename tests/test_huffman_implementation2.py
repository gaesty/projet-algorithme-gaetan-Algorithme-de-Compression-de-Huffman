import pytest
from implementations.implementation2 import HuffmanCompression

def test_huffman_compression():
    # Test de base avec un texte normal
    texte = "hello"
    huffman = HuffmanCompression(texte)
    encoded_text = huffman.encode()
    decoded_text = huffman.decode(encoded_text)
    assert decoded_text == texte

    # Tester pour un texte vide
    texte_vide = ""
    huffman_vide = HuffmanCompression(texte_vide)
    encoded_text_vide = huffman_vide.encode()
    decoded_text_vide = huffman_vide.decode(encoded_text_vide)
    assert decoded_text_vide == texte_vide

    # Tester avec des répétitions de caractères
    texte_repetitif = "aaaaaa"
    huffman_repetitif = HuffmanCompression(texte_repetitif)
    encoded_text_repetitif = huffman_repetitif.encode()
    decoded_text_repetitif = huffman_repetitif.decode(encoded_text_repetitif)
    assert decoded_text_repetitif == texte_repetitif

    # Tester avec des caractères spéciaux
    texte_special = "!@#$%^&*()"
    huffman_special = HuffmanCompression(texte_special)
    encoded_text_special = huffman_special.encode()
    decoded_text_special = huffman_special.decode(encoded_text_special)
    assert decoded_text_special == texte_special

    # Tester avec une chaîne contenant des espaces
    texte_espaces = "hello world"
    huffman_espaces = HuffmanCompression(texte_espaces)
    encoded_text_espaces = huffman_espaces.encode()
    decoded_text_espaces = huffman_espaces.decode(encoded_text_espaces)
    assert decoded_text_espaces == texte_espaces

    # Vérifier que le texte encodé n'est pas le même que le texte original
    assert encoded_text != texte
    assert encoded_text_special != texte_special

    # Tester la gestion d'une entrée invalide pour le décodage
    with pytest.raises(KeyError):
        huffman.decode("invalid_encoded_text")
