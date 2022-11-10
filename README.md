# tournoi
Finalement, au lieu de rechercher dans mes archives, tout est encore sur Internet:
Voici le lien (http://mapage.noos.fr/r.ferreol/atelecharger/textes/tournoi%20de%20belote.pdf) vers la problématique du tournoi de belote, qui peut facilement être adaptée au badminton lorsque l'on joue en double à 4 joueurs et que j'ai déjà mis en œuvre avec succès. Dans ce PDF, est cité M. Wojciech BIENIA avec qui j'avais échangé (il est décédé depuis) ainsi qu'un lien vers les tables de Durango Bill's toujours accessible.
Voici la demande que j'avais formulé à Wojciech BIENIA:

Bonjour Monsieur,
Je vous contacte car votre nom apparaît dans une publication de Robert Ferreol concernant l'organisation d'un tournoi de belote dans lequel on joue une seule fois avec un même partenaire et deux fois contre un même adversaire. En m'aidant des tables de Durango, je réussi à le mettre en oeuvre pour l'organisation d'un tournoi de Badminton. Mais je souhaiterai ajouter une contrainte supplémentaire. Cette solution ne fonctionne pas si je veux organiser un tournoi mixte pour lequel  le nombre de joueurs est bien un multiple de 4, mais que cette population soit pour moitié des hommes et pour autre moitié des femmes et que chaque paire soit constituée d'un homme et d'une femme. Avez-vous connaissance de l'existence d'une documentation ou un peu de temps pour m'aider à résoudre ce problème?

Je t'ai parlé de débutants et d'expérimentés la problématique est identique si l'on souhaite crée des équipes mixtes.
Si ça t’intéresse, je peux te faire suivre les échanges que j'ai eu avec WB, mais d'une part la première solution qu'il m'avait donné ne satisfaisait pas ma demande et d'autre part, les solutions apportées ensuite lors de ces échanges risque de t'orienter vers la même démarche intellectuelle...
Tu verras, au premier abord, ce problème n'a pas l'air d'être trop difficile à résoudre mais tous ceux à qui je l'ai soumis n'ont pas trouvé de solutions aussi simple que le tournoi de belote!
Bon courage,
Bernard

J'ai lu ton mail avant de me coucher hier soir et j'avoue que je me suis mis à réfléchir et que le sommeil n'est pas venu tout de suite.
Pour m'assurer de la bonne compréhension du problème, je te livre mes premières remarques:
Dans le cas du tournoi de belote, il apparaît 3 contraintes:
- on veut que toutes les paires de joueurs joue une partie et une seule (c1).
- on veut que à chaque ronde tous les concurrents puissent jouer (c2)
- on veut que chaque concurrent joue le même nombre de fois contre un autre concurrent (c3 =  tournoi parfait)

Avec (c1) pour n joueurs, on a le nombre de paires de joueurs qui est égal à [2 parmi n] = n*(n-1)/2
Donc le nombre de partie np = n*(n-1)/4. Pour que ce nombre soit entier, il faut que n ou n-1 soit divisible par 4 (n et n-1 ne peuvent être chacun divisible par 2).
Le point (c2) est traité par des cycles.
Le point (c3) est traité en choisissant des cycles particuliers.
Pour (c3), on peut calculer le nombre de fois que chaque joueur affronte au minimum le même adversaire. Lors de chaque partie si A+B affronte C+D on a 4 affrontements A-C, A-D, B-C, B-D.
Comme on a np parties, cela fait n*(n-1) affrontements. Comme le nombre de paires de joueur est n*(n-1)/2 cela signifie que en moyenne chaque joueur affronte 2 fois le même joueur.
Donc si on peut trouver une solution qui répond à (c3) cela signifie que chaque concurrent va jouer 2 fois le même joueur. On voit bien que c'est le cas dans les exemples du pdf.

Dans le cas du tournoi mixte (groupe 1 (A,B,C,...X), groupe 2 (a,b,c,...x)) avec les 3 mêmes contraintes on arrive à une impossibilité entre (c1) et (c3). On ne peut donc pas répondre à la contrainte (c3) au sens strict. Il n'y a pas de tournoi parfait.
Pourquoi ?
Avec (c1) pour n joueurs (n/2 du groupe 1 et n/2 du groupe 2) on a (n/2)*(n/2) = n*n/4 paires et donc n*n/8 matchs
Avec (c3) si chaque joueur du groupe 1 rencontre une fois et une seule chaque autre joueur du groupe 1 on a (n/2)*(n/2-1)/2 rencontres = n*(n-2)/8 rencontres < n*n/8 matchs, donc chaque joueur doit rencontrer plus d'une seule fois un joueur de son groupe. S'il le rencontre 2 fois, on à n*(n-2)/4 rencontres > n*n/8  . Donc 1 est trop petit et 2 est trop grand sauf pour n=4 avec 2 matchs Aa - Bb, Ab - Ba).
