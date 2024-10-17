texte : str = "abcdcba"

def dict_of_frequency(texte : str) -> dict:
    frequence_des_caracteres : dict = {}

    for lettre in texte:
        if lettre in frequence_des_caracteres:
            frequence_des_caracteres[lettre] += 1 
        else:
            frequence_des_caracteres[lettre] = 1
    return frequence_des_caracteres

def key_of_min(dict: dict) -> str:
    return min(dict, key = dict.get)

print(key_of_min(dict_of_frequency(texte)))

def tree_from_dict(dict : dict) :
    tree = {}
    