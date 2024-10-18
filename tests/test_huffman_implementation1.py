import pytest
from collections import defaultdict

# Fonction que tu peux extraire de ton code original
def huffman_encode(texte):
    freq_lib = defaultdict(int)    
    for lettre in texte:
        freq_lib[lettre] += 1

    tree = [[frequence, [lettre, ""]] for lettre, frequence in freq_lib.items()]
    heapify(tree)
    
    while len(tree) > 1:
        right = heappop(tree)
        left = heappop(tree)
        for pair in right[1:]:  
            pair[1] = '0' + pair[1]
        for pair in left[1:]:  
            pair[1] = '1' + pair[1]
        heappush(tree, [right[0] + left[0]] + right[1:] + left[1:])
    
    huffman_list = right[1:] + left[1:]
    huffman_dict = {a[0]: str(a[1]) for a in huffman_list}
    encoded_text = ''.join(huffman_dict[lettre] for lettre in texte)
    
    return encoded_text, huffman_dict

def huffman_decode(encoded_text, huffman_dict):
    inverse_huffman_dict = {v: k for k, v in huffman_dict.items()}
    decoded_text = ""
    current_bits = ""
    for bit in encoded_text:
        current_bits += bit
        if current_bits in inverse_huffman_dict:
            decoded_text += inverse_huffman_dict[current_bits]
            current_bits = ""
    return decoded_text

# Tests unitaires
def test_huffman():
    texte = "hello"
    encoded_text, huffman_dict = huffman_encode(texte)
    decoded_text = huffman_decode(encoded_text, huffman_dict)
    
    assert decoded_text == texte

    # Tester pour un texte vide
    texte_vide = ""
    encoded_text_vide, huffman_dict_vide = huffman_encode(texte_vide)
    decoded_text_vide = huffman_decode(encoded_text_vide, huffman_dict_vide)

    assert decoded_text_vide == texte_vide

