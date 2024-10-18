# Implementation2.py
import heapq  # Importation de la bibliothèque heapq pour utiliser une structure de tas (priority queue)
from collections import defaultdict  # Importation de defaultdict pour gérer les fréquences des caractères
from graphviz import Digraph  # Importation de Digraph pour la visualisation de l'arbre de Huffman (non utilisé ici)

class HuffmanNode:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # Fréquence du symbole (nombre d'occurrences)
        self.symbol = symbol  # Symbole (caractère) que représente ce nœud
        self.left = left  # Sous-arbre gauche, représentant les symboles avec des codes binaires commençant par '0'
        self.right = right  # Sous-arbre droit, représentant les symboles avec des codes binaires commençant par '1'

    def __lt__(self, other):
        # Définition de l'ordre pour le tas : un nœud est "moins" qu'un autre s'il a une fréquence inférieure
        return self.freq < other.freq

class HuffmanCompression:
    def __init__(self, texte):
        self.texte = texte  # Texte à compresser
        self.freq_lib = defaultdict(int)  # Dictionnaire pour stocker la fréquence de chaque caractère
        self.huffman_dict = {}  # Dictionnaire pour stocker les codes de Huffman associés aux symboles
        self.inverse_huffman_dict = {}  # Dictionnaire inverse pour décoder
        self.root = None  # Racine de l'arbre de Huffman

    def calculate_frequencies(self):
        # Calcul des fréquences de chaque caractère dans le texte
        for lettre in self.texte:
            self.freq_lib[lettre] += 1  # Incrémente la fréquence du caractère
        return self.freq_lib  # Retourne le dictionnaire des fréquences

    def build_tree(self):
        # Construction de l'arbre de Huffman
        heap = [HuffmanNode(freq, lettre) for lettre, freq in self.freq_lib.items()]  # Création d'une liste de nœuds
        heapq.heapify(heap)  # Transforme la liste en un tas (min-heap)
        
        # Boucle jusqu'à ce qu'il ne reste qu'un seul nœud dans le tas
        while len(heap) > 1:
            right = heapq.heappop(heap)  # Extraction du nœud avec la plus petite fréquence
            left = heapq.heappop(heap)  # Extraction du deuxième nœud avec la plus petite fréquence
            # Création d'un nouveau nœud combinant les deux nœuds extraits
            merged = HuffmanNode(left.freq + right.freq, None, left, right)  
            heapq.heappush(heap, merged)  # Ajout du nœud combiné au tas
        
        self.root = heap[0]  # La racine de l'arbre de Huffman est le dernier nœud restant
        self._generate_codes(self.root)  # Génération des codes de Huffman à partir de la racine

    def _generate_codes(self, node, current_code=""):
        # Fonction récursive pour générer les codes de Huffman
        if node is None:
            return  # Si le nœud est vide, on sort
        if node.symbol is not None:
            # Si le nœud est une feuille (contient un symbole), on stocke son code
            self.huffman_dict[node.symbol] = current_code  
        # Appel récursif pour les sous-arbres gauche et droit, en ajoutant '0' ou '1' au code actuel
        self._generate_codes(node.left, current_code + "0")  
        self._generate_codes(node.right, current_code + "1")  

    def encode(self):
        # Fonction d'encodage du texte
        self.calculate_frequencies()  # Calcul des fréquences des caractères
        self.build_tree()  # Construction de l'arbre de Huffman
        # Retourne la chaîne encodée en utilisant les codes de Huffman
        return ''.join(self.huffman_dict[lettre] for lettre in self.texte)  

    def decode(self, encoded_text):
        # Fonction de décodage du texte encodé
        self.inverse_huffman_dict = {v: k for k, v in self.huffman_dict.items()}  # Création d'un dictionnaire inverse
        decoded_text = ""  # Chaîne pour stocker le texte décodé
        current_bits = ""  # Chaîne pour stocker les bits courants

        # Parcours des bits dans le texte encodé
        for bit in encoded_text:
            current_bits += bit  # Ajout du bit courant à la chaîne de bits
            if current_bits in self.inverse_huffman_dict:
                # Si la chaîne de bits correspond à un symbole, on l'ajoute au texte décodé
                decoded_text += self.inverse_huffman_dict[current_bits]  
                current_bits = ""  # Réinitialisation de la chaîne de bits courants
        return decoded_text  # Retourne le texte décodé

# Utilisation de la classe
texte = input("Saisissez un mot : ")  # Demande à l'utilisateur de saisir un texte
huffman = HuffmanCompression(texte)  # Création d'une instance de HuffmanCompression
encoded_text = huffman.encode()  # Encodage du texte
print("Texte encodé :", encoded_text)  # Affichage du texte encodé

decoded_text = huffman.decode(encoded_text)  # Décodage du texte encodé
print("Texte décodé :", decoded_text)  # Affichage du texte décodé
