
# 1- Entrée (main.py)

Quand on entre dans le programme on vérifie les arguments, on vérifie si on a:

- tui 
- con
- gui
- help

Depuis l'argument on va démarrer le 'backend' pour l'action demandée. Ou afficher l'aide.

# 2 - Converter (converter.py)


Tout ce qui est dans le fichier `converter.py` permet de convertir des valeurs en hexadécimal/binaire/décimal
et de convertir des strings hexadécimal/binaire/décimal en valeurs intégrales

les bases sont utilisés pour les conversions et simplifier le code et de le rendre extensible:
- 10: base décimale
- 16: base héxadécimale
- 2: base binaire
- 8: base octale (non implémentée)

## La variable `str_xdigits: str[]`

Permet de convertir un nombre de 0-16 en un caractère que l'on peut utiliser dans un string.

## La fonction `convert_digit(value: int, base: int) -> str` 

Fonction qui permet d'avoir le chiffre correspondant à un nombre donné avec sa base.

## La fonction `convert_to_val(value: int, base: int) -> str`

Fonction qui convertit une valeur intégrale en une chaine de caractère avec une base précise.
Si une valeur "None" est donnée, alors la fonction retourne `"Error"`

### Fonctionnement 

On fait une boucle qui permet de lire tout les chiffres de droite a gauche de la valeur. 
```py 
while current != 0:
        result = result + convert_digit(current, base)
        current = current // base
```

Son fonctionnement peut être vu comme ceci:

- on prend la valeur
- on prend le premier chiffre (le modulo est géré par `convert_digit`)
- on divise par la base
- on refait la boucle jusqu'a ce que la valeur soit à 0

Donc imaginons que l'on a la valeur `123` avec la base `10`.

```yaml
--
- current: 123
- result: ""
--
- current: 12 
- result: "3"
--
- current: 1
- result: "32"
--
- current: 0
- result: "321"

- current est à 0 on arrête la loop
```

Cependant le résultat est inversé car on boucle de droite a gauche, donc on inverse le résultat:

```py
    return result[::-1]  # reverse string
```

## Les fonctions `val_to_hex(value: int) -> str` `val_to_bin` et `val_to_dec`

Ces fonctions permettent de convertir une valeur en un string (binaire, hexadécimal, et décimal).
Elles appellent directement `convet_to_val` avec les bases correspondantes et rajoutent: "0b" ou "0x" si c'est nécéssaire.

## La fonction `val_from_str(value: str, base: int) -> int`

Cette fonction permet de convertir une valeur/chaine de caractère avec une base en une valeur intégrale.

### Fonctionnement

Premièrement on met en lower case la valeur (pour se simplifier la vie avec les valeurs hexadécimales)

Ensuite on boucle sur chaque caractère du string et on fait pour chaque caractère:

- On vérifie si il est valide ()
- on met le résultat à `resultat * base + str_xdigits.index(caracter)`
  - Le `str_xdigits.index(caracter)` pemet de transformer un caractère: '0', '1', 'b', '5'... vers son chiffre correspondant

Donc imaginons que l'on a la valeur `"123"` avec la base `10`.

```yaml
--
- current: "123"
- c: 1
- result: result (=0)o * 10 + 1 = 1
--
- current: "123"
- c: 2
- result: result (=1) * 10 + 2 = 12
--
- current: "123"
- c: 3
- result: result (12) * 10 + 3 = 123
--
```


## Les fonctions `val_from_hex(value: str) -> int` `val_from_bin` et `val_from_dec`

Ces fonctions permettent de convertir un string en une valeur. Elles appellent direcement la fonction `val_from_str` avec les bases correspondantent.
Elles peuvent aussi supprimer les préfixs: "0b" et "0x" des nombres binaires ou hexadécimaux

# 3 - GUI (gui.py)

Dans ce fichier on peut retrouver le code pour faire fonctionner le convertisseur avec tkinter. 

\[...]: TODO: finir la documentation et corriger les fautes très probables (majuscules + points inclus)
