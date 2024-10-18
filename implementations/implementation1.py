from heapq import heappush, heappop, heapify
from collections import defaultdict
texte : str = str(input("saissisez un mot : "))
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
print(encoded_text)
inverse_huffman_dict = {v: k for k, v in huffman_dict.items()}
decoded_text = ""
current_bits = ""
for bit in encoded_text:
    current_bits += bit
    if current_bits in inverse_huffman_dict:
        decoded_text += inverse_huffman_dict[current_bits]
        current_bits = ""
print(decoded_text)