# Analyse des Complexités de l'Algorithme de Huffman

## Introduction
Cette analyse compare deux implémentations de l'algorithme de Huffman pour la compression de données. La première implémentation est fonctionnelle, tandis que la deuxième est orientée objet. Nous examinerons les complexités temporelles et spatiales de chaque implémentation et comparerons leurs performances.

## 1. Première Implémentation (Fonctionnelle)

### Complexité Temporelle
- **Calcul des Fréquences**: 
  - \(O(n)\) où \(n\) est la longueur du texte.
  
- **Construction de l'Arbre de Huffman**: 
  - \(O(m \log m)\) où \(m\) est le nombre de symboles distincts.
  
- **Génération des Codes**: 
  - \(O(m)\).

- **Encodage du Texte**: 
  - \(O(n)\).
  
- **Décodage du Texte**: 
  - \(O(n)\).

**Complexité Totale**: 
\[ O(n + m \log m) \]

### Complexité Spatiale
- **Fréquence des Lettres**: \(O(m)\)
- **Arbre de Huffman**: \(O(m)\)
- **Code de Huffman**: \(O(m)\)
- **Texte Encodé**: \(O(n)\)

**Complexité Spatiale Totale**: 
\[ O(n + m) \]

## 2. Deuxième Implémentation (Orientée Objet)

### Complexité Temporelle
- **Calcul des Fréquences**: 
  - \(O(n)\)
  
- **Construction de l'Arbre de Huffman**: 
  - \(O(m \log m)\)

- **Génération des Codes**: 
  - \(O(m)\)

- **Encodage du Texte**: 
  - \(O(n)\)

- **Décodage du Texte**: 
  - \(O(n)\)

**Complexité Totale**: 
\[ O(n + m \log m) \]

### Complexité Spatiale
- **Fréquence des Lettres**: \(O(m)\)
- **Arbre de Huffman**: \(O(m)\) (en mémoire avec les objets `HuffmanNode`)
- **Code de Huffman**: \(O(m)\)
- **Texte Encodé**: \(O(n)\)

**Complexité Spatiale Totale**: 
\[ O(n + m) \]

## Comparaison des Performances

1. **Lisibilité et Maintenabilité**:
   - La deuxième implémentation (orientée objet) est généralement plus lisible et maintenable grâce à l'encapsulation de la logique.

2. **Performance**:
   - Les deux implémentations ont des complexités équivalentes. Cependant, la version orientée objet pourrait être légèrement plus lente en raison de la surcharge liée à l'utilisation de classes.

3. **Flexibilité**:
   - La version orientée objet est plus facile à étendre avec des fonctionnalités supplémentaires en raison de sa structure modulaire.

## Conclusion
Les deux implémentations offrent des performances similaires, mais la version orientée objet est préférable en raison de sa lisibilité et de sa maintenabilité. Le choix entre les deux dépendra des exigences spécifiques du projet.
