# implementation1.py
from heapq import heappush, heappop, heapify  # Importation des fonctions nécessaires pour gérer un tas
from collections import defaultdict  # Importation de defaultdict pour stocker les fréquences des caractères

# texte : str = str(input("saissisez un mot : "))  # Ligne commentée pour permettre à l'utilisateur de saisir un mot
texte = "aabbccddbbccaa"  # Exemple de texte à compresser

# Dictionnaire pour stocker la fréquence de chaque caractère
freq_lib = defaultdict(int)    

# Calcul des fréquences des caractères dans le texte
for lettre in texte:
    freq_lib[lettre] += 1  # Incrémente la fréquence du caractère

# Création d'une liste pour représenter les nœuds de l'arbre de Huffman
# Chaque nœud est une liste contenant la fréquence et le symbole (caractère) associé à un code binaire
tree = [[frequence, [lettre, ""]] for lettre, frequence in freq_lib.items()]

print(tree)  # Affichage des nœuds de l'arbre avant l'utilisation du tas
heapify(tree)  # Transformation de la liste en un tas (min-heap)
print(tree)  # Affichage de l'arbre après la transformation en tas

# Construction de l'arbre de Huffman
while len(tree) > 1:
    right = heappop(tree)  # Extraction du nœud avec la plus petite fréquence
    left = heappop(tree)  # Extraction du deuxième nœud avec la plus petite fréquence
    # Mise à jour des codes binaires pour les nœuds extraits
    for pair in right[1:]:  
        pair[1] = '0' + pair[1]  # Ajout d'un '0' pour le sous-arbre droit
    for pair in left[1:]:  
        pair[1] = '1' + pair[1]  # Ajout d'un '1' pour le sous-arbre gauche
    # Fusion des nœuds extraits en un nouveau nœud, qui est ajouté au tas
    heappush(tree, [right[0] + left[0]] + right[1:] + left[1:])

# Récupération des codes de Huffman
huffman_list = right[1:] + left[1:]  # Combine les codes de Huffman
huffman_dict = {a[0]: str(a[1]) for a in huffman_list}  # Dictionnaire des symboles associés à leurs codes

# Encodage du texte en utilisant les codes de Huffman
encoded_text = ''.join(huffman_dict[lettre] for lettre in texte)  
print(encoded_text)  # Affichage du texte encodé

# Création d'un dictionnaire inverse pour le décodage
inverse_huffman_dict = {v: k for k, v in huffman_dict.items()}  
decoded_text = ""  # Chaîne pour stocker le texte décodé
current_bits = ""  # Chaîne pour stocker les bits courants

# Décodage du texte encodé
for bit in encoded_text:
    current_bits += bit  # Ajout du bit courant à la chaîne de bits
    if current_bits in inverse_huffman_dict:
        # Si la chaîne de bits correspond à un symbole, on l'ajoute au texte décodé
        decoded_text += inverse_huffman_dict[current_bits]  
        current_bits = ""  # Réinitialisation de la chaîne de bits courants

print(decoded_text)  # Affichage du texte décodé
