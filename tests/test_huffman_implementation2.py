import pytest
# from implementations.implementation2 import HuffmanCompression

import heapq
from collections import defaultdict
from graphviz import Digraph

class HuffmanNode:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # Fréquence du symbole
        self.symbol = symbol  # Symbole (caractère)
        self.left = left  # Sous-arbre gauche
        self.right = right  # Sous-arbre droit

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCompression:
    def __init__(self, texte=""):
        self.texte = texte
        self.freq_lib = defaultdict(int)
        self.huffman_dict = {}
        self.inverse_huffman_dict = {}
        self.root = None

    def calculate_frequencies(self):
        for lettre in self.texte:
            self.freq_lib[lettre] += 1
        return self.freq_lib

    def build_tree(self):
        if not self.freq_lib:
            raise ValueError("La fréquence des caractères est vide, impossible de construire l'arbre.")
        
        heap = [HuffmanNode(freq, lettre) for lettre, freq in self.freq_lib.items()]
        heapq.heapify(heap)
    
        while len(heap) > 1:
            right = heapq.heappop(heap)
            left = heapq.heappop(heap)
            merged = HuffmanNode(left.freq + right.freq, None, left, right)
            heapq.heappush(heap, merged)
    
        self.root = heap[0]

    def _generate_codes(self, node, current_code=""):
        if node is None:
            return
        if node.symbol is not None:
            self.huffman_dict[node.symbol] = current_code
        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self):
        self.calculate_frequencies()
        self.build_tree()
        self._generate_codes(self.root)  # Ajouté
        return ''.join(self.huffman_dict[lettre] for lettre in self.texte)

    def decode(self, encoded_text):
        self.inverse_huffman_dict = {v: k for k, v in self.huffman_dict.items()}
        decoded_text = ""
        current_bits = ""
        for bit in encoded_text:
            current_bits += bit
            if current_bits in self.inverse_huffman_dict:
                decoded_text += self.inverse_huffman_dict[current_bits]
                current_bits = ""
        return decoded_text

    def visualize_tree(self):
        dot = Digraph()
        self._add_edges(dot, self.root)
        dot.render('huffman_tree', format='png', view=True)

    def _add_edges(self, dot, node, parent_id=None, edge_label=""):
        if node is None:
            return

        node_id = str(id(node))
        label = f'{node.symbol if node.symbol else "Node"}\n{node.freq}'
        dot.node(node_id, label)

        if parent_id:
            dot.edge(parent_id, node_id, label=edge_label)

        self._add_edges(dot, node.left, node_id, '0')
        self._add_edges(dot, node.right, node_id, '1')



def test_calculate_frequencies():
    huffman = HuffmanCompression("hello world")
    frequencies = huffman.calculate_frequencies()
    expected_frequencies = defaultdict(int, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    assert frequencies == expected_frequencies

def test_build_tree():
    huffman = HuffmanCompression("hello world")
    huffman.calculate_frequencies()
    huffman.build_tree()
    assert huffman.root is not None

def test_encode_decode():
    huffman = HuffmanCompression("hello world")
    encoded_text = huffman.encode()
    decoded_text = huffman.decode(encoded_text)
    assert decoded_text == "hello world"

def test_empty_string():
    huffman = HuffmanCompression("")
    with pytest.raises(ValueError):
        huffman.build_tree()

def test_single_character():
    huffman = HuffmanCompression("a")
    encoded_text = huffman.encode()
    decoded_text = huffman.decode(encoded_text)
    assert decoded_text == "a"

def test_multiple_same_characters():
    huffman = HuffmanCompression("aaaaaa")
    encoded_text = huffman.encode()
    decoded_text = huffman.decode(encoded_text)
    assert decoded_text == "aaaaaa"

def test_frequencies_for_repeated_chars():
    huffman = HuffmanCompression("aaabbb")
    frequencies = huffman.calculate_frequencies()
    expected_frequencies = defaultdict(int, {'a': 3, 'b': 3})
    assert frequencies == expected_frequencies

def test_huffman_codes():
    huffman = HuffmanCompression("aab")
    huffman.encode()
    assert 'a' in huffman.huffman_dict
    assert 'b' in huffman.huffman_dict
    assert len(huffman.huffman_dict) == 2

def test_visualize_tree(capsys):
    huffman = HuffmanCompression("hello")
    huffman.encode()
    huffman.visualize_tree()
    captured = capsys.readouterr()
    assert True

if __name__ == "__main__":
    pytest.main()
