
# Préface 

J'ai voulu garder le code simple et lisible. C'est pour cela
que je n'ai pas utilisé de commentaires à travers le code.
Cependant je l'ai quand même documenté en partie à travers ce fichier.

Le code est open source sous license MIT (voir fichier license).

J'ai aussi voulu complexifier la chose (ou bloater le programme (mais si je dit ça, ça fait cliché utilisateurs gnu/linux)). Donc l'interface est très simple: 3 champs de texte, un bouton quitter, et un petit message pour la gui qui explique que le programme peut être démarré sous d'autres formes.

# 1- Entrée (main.py)

Quand on entre dans le programme on vérifie les arguments dans la fonction `arg_update`, on vérifie si on a:

- tui: pour l'interface textuelle.
- con: pour la forme de console (sous forme de question).
- gui: pour l'interface graphique.
- help: affiche l'aide.

Depuis l'argument on va démarrer le 'backend' pour l'action demandée. Ou afficher l'aide.

Par défaut nous utilisons toujours le backend gui.

# 2 - Converter (converter.py)

Tout ce qui est dans le fichier `converter.py` permet de convertir des valeurs en hexadécimal/binaire/décimal
et de convertir des strings hexadécimal/binaire/décimal en valeurs intégrales.
> Pour résumer on peut faire:
> hex/dec/bin -> string -> hex/dec/bin

Les bases sont utilisés pour les conversions et simplifier le code et de le rendre extensible:
- 10: base décimale
- 16: base héxadécimale
- 2: base binaire
- 8: base octale (non implémentée)

## La variable `str_xdigits: str[]`

Permet de convertir un nombre de 0-16 en un caractère que l'on peut utiliser dans un string.
Par exemple:

```py
str_xdigits[0] = '0'
str_xdigits[3] = '3'
str_xdigits[15] = 'f'
str_xdigits[11] = 'b'
```

## La fonction `convert_digit(value: int, base: int) -> str` 

Fonction qui permet d'avoir le premier chiffre correspondant à un nombre donné avec sa base.

Par exemple:
```py
convert_digit(0, 10) -> '0'
convert_digit(13, 10) -> '3'
convert_digit(0xfa, 16) -> 'a'
convert_digit(0b101, 2) -> '1'
```

## La fonction `convert_to_val(value: int, base: int) -> str`

Fonction qui convertit une valeur intégrale en une chaine de caractère avec une base précise.
Si une valeur `None` est donnée, alors la fonction retourne `"Error"`

> soit int -> string

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
Ce qui permet de boucler chiffre par chiffre de droite à gauche.

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

> Soit string -> int

### Fonctionnement

Premièrement on met en lower case la valeur (pour se simplifier la vie avec les valeurs hexadécimales).

Ensuite on boucle sur chaque caractère du string et on fait pour chaque caractère:

- On vérifie si il est valide 
- On met le résultat à `resultat * base + str_xdigits.index(caracter)`
  - C'est comme si on insérait un chiffre à la droite du string:
    - ici par exemple on rajoute 3 à 12 (de base 10): $(12 * 10) + 3 \rightarrow (120 + 3) \rightarrow 123$
  - Le `str_xdigits.index(caracter)` pemet de transformer un caractère: '0', '1', 'b', '5'... vers son chiffre correspondant.

Donc imaginons que l'on a la valeur `"123"` avec la base `10`.

```yaml
--
- current: "123"
- c: 1
- result: result(=0) * 10 + 1 = 1
--
- current: "123"
- c: 2
- result: result(=1) * 10 + 2 = 12
--
- current: "123"
- c: 3
- result: result(=12) * 10 + 3 = 123
--
```


## Les fonctions `val_from_hex(value: str) -> int` `val_from_bin` et `val_from_dec`

Ces fonctions permettent de convertir un string en une valeur. Elles appellent direcement la fonction `val_from_str` avec les bases correspondantent.
Elles peuvent aussi supprimer les préfixes: "0b" et "0x" des nombres binaires ou hexadécimaux

# 3 - GUI (gui.py)

Dans ce fichier on peut retrouver le code pour faire fonctionner le convertisseur avec une interface graphique.
L'interface fonctionne avec tkinter. 

## Initialisation de la fenêtre

Dans le code il y a l'initialisation de la fenêtre:

- la variable: `bin_box` représente la boite de texte pour le nombre binaire.
- la variable: `hex_box` représente la boite de texte pour le nombre hexadécimal.
- la variable: `dec_box` représente la boite de texte pour le nombre décimal.
- la variable: `info` est un champs de texte qui explique à l'utilisateur qu'il peut utiliser d'autres modes de rendus.
- la variable: `qui_button` permet de tuer l'application. (rip)

Chaque élément a un padding de 10 pour éviter que tout soit collé.

## La mise à jour des champs de texte

Quand on appelle la fonction `gui_run` pour démarrer la partie graphique on active la fenêtre et on appelle la fonction `gui_update` dans 100 ms.

En sachant que la fonction `gui_update` demande à tkinter de la rappeler dans 100 ms ce qui permet d'avoir les changements de valeur 10 fois pas seconde.

Donc la fonction `gui_update` obient l'élément qui est utilisé par l'utilisateurs. En gros il donne le widget qui est séléctionné. Ce qui permet de savoir qu'elle boite il édite.

Il y a la fonction `get_box_value` qui permet d'avoir la valeur de la boite de texte qui est séléctionner par l'utilisateurs;

Il y a ausi la fonction `update_other_box` qui récupère la valeur à partir de `get_box_value`, et elle met a jour les autres boites de texte en convertissant la valeur de la boite de texte séléctionné.

# 4 - Console.py

Ce fichier est pour l'utilisation d'une sorte de console pour la conversion de nombre.

La console est très simple. 
C'est une boucle qui lit une action, qui peut être: 
- 'q': quitter
- 'b': convertir depuis du binaire
- 'd': convertir depuis du décimal
- 'x': convertir depuis de l'héxadécimal

Une fois l'action sélectionné le programme demande à l'utilisateur de rentrer une valeur.

Cette valeur serra alors écrite en décimale, héxadécimale et binaire.

# 5 - Tui.py

Ce fichier est utile pour l'utilisation d'une interface textuelle (comme en 90's).

> je n'ai pas eu le temps de totallement documenter ce fichier donc vous pourrez trouver de l'aide dans les commentaires contenus dedans
