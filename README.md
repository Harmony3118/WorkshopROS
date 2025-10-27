README
---

## 1-3. Première partie 

Dans notre publisher, on a défini des constantes : 

```
COMPUTER = os.name
ID = 3
```

*(grâce à l'import os)*

On a aussi utilisé le compteur temporel :

```
timer_period = 0.42  # seconds
self.timer = self.create_timer(timer_period, self.timer_callback)
self.i = 0
```

On a pu les utiliser dans le message, en utilisant aussi le compteur suivant le tuto :

``msg.data = f'Ordi: {COMPUTER};\t ID: {ID};\t Compteur = {self.i}'``

Et on a bien pu afficher le résultat :

``[INFO] [1761561213.078884697] [minimal_subscriber]: I heard: "Ordi: posix;	 ID: 3;	 Compteur = 42"``


## 4. Définir un message personnalisé

Suite au tuto, on a créé *ComputerInfo.msg* comme indiqué. Ensuite, on a redéfini le **publisher** en ajoutant l'appel de msg dans l'init : 

```
self.msg = ComputerInfo()
self.msg.counter = 0
self.msg.computer_name = COMPUTER
self.msg.domain_id = ID
self.get_logger().info(f'Publishing: {self.msg.computer_name};\t ID: {self.msg.domain_id};\t ')
```

Ensuite, dans le timer_callback, on a mis le compteur qui s'actualise : 

```
self.get_logger().info('Counter: "%d"' % self.msg.counter)
```

Dans le **subscriber**, on a utilisé les données en utilisant le suffixe *msg* avant de pérciser les données coulues, comme indiqué dans notre fichier *ComputerInfo.msg*.


## 5. Plusieurs subscribers

Pour cette partie, on a duppliqué notre listener, qu'on a nommé *subscriber_transform_function.py*. Dedans, on a récupéré les données utiles et on les as transformé avant de les afficher :


```
name = msg.computer_name.upper()
domain = msg.domain_id + 1
self.get_logger().info(f'I heard: Name = {name} ; \t ID = {domain} ;')
```
 
 Ensuite, dans le *setup.py* de py\_pubsup, on a ajouté un nouvel entry point, notre nouveau listener. Comme on en avait 2, on a renommé le 1 listener\_1 et le second listener\_2. 
 
```
'listener_1 = py_pubsub.subscriber_member_function:main',
'listener_2 = py_pubsub.subscriber_transform_function:main',
```

Ensuite, on a lancé les deux listeners dans des terminaux séparés, et le message original s'est affiché, ainsi que le message transformé.

**Original**
```
[INFO] [1761576975.528546610] [minimal_subscriber]: I heard: Name = student ; 	 ID = 3 ; 	 Counter = 107
```

**Transformé**
```
[INFO] [1761577403.928865035] [minimal_subscriber]: I heard: Name = STUDENT ; 	 ID = 4 ;
```


## 6. Paramètres dans un node

Pour cette partie, on a modifié notre second listener, en ajoutant une condition : si le compteur vaut 0, alors on affiche le bon ordi et le bon numéro d'ID.

On a aussi mis à jour le publisher avec les nouvelles données, qu'on a défini au préalable dans *ComputerInfo.msg*.

Quand on a relancé, on a bien vu u changement au lancement : 

```
[INFO] [1761579646.208506130] [minimal_subscriber]: I heard: Name = student ; 	 ID = 3 ;
[INFO] [1761579646.628492421] [minimal_subscriber]: I heard: Name = STUDENT ; 	 ID = 4 ;
[INFO] [1761579647.048553779] [minimal_subscriber]: I heard: Name = STUDENT ; 	 ID = 4 ;

```

## 7. Service client/serveur














