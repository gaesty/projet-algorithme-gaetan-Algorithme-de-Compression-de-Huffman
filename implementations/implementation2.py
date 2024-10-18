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
        # Comparaison des nœuds par fréquence pour le tas
        return self.freq < other.freq

class HuffmanCompression:
    def __init__(self, texte):
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
        # Construction de l'arbre de Huffman
        heap = [HuffmanNode(freq, lettre) for lettre, freq in self.freq_lib.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            right = heapq.heappop(heap)
            left = heapq.heappop(heap)
            merged = HuffmanNode(left.freq + right.freq, None, left, right)
            heapq.heappush(heap, merged)
        
        self.root = heap[0]
        self._generate_codes(self.root)

    def _generate_codes(self, node, current_code=""):
        # Fonction récursive pour générer les codes de Huffman
        if node is None:
            return
        if node.symbol is not None:
            self.huffman_dict[node.symbol] = current_code
        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self):
        self.calculate_frequencies()
        self.build_tree()
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

# Utilisation de la classe
texte = input("Saisissez un mot : ")
huffman = HuffmanCompression(texte)
encoded_text = huffman.encode()
print("Texte encodé :", encoded_text)

decoded_text = huffman.decode(encoded_text)
print("Texte décodé :", decoded_text)

# Visualiser l'arbre de Huffman
huffman.visualize_tree()
