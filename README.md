# Détection de présence par vision par ordinateur

Projet académique de vision par ordinateur : détecter la présence de personnes
sur une image de salle de cours, et comparer deux méthodes de détection de
visages (une méthode classique et un réseau de neurones convolutif).

## Objectif

Automatiser l'appel en salle de cours : une caméra capture une image à la fin
de la séance, puis le programme détecte les visages présents pour indiquer
combien de personnes sont dans la salle.

## Méthodes comparées

| Méthode | Dossier | Principe |
|---|---|---|
| Haar Cascade | `haar_cascade/` | Détecteur classique d'OpenCV, basé sur des caractéristiques de Haar |
| CNN pré-entraîné | `CNN/` | Détecteur SSD + ResNet-10 chargé avec `cv2.dnn` |

## Structure du projet

```
projet-detection-presence/
├── haar_cascade/
│   ├── haar_detection.py
│   ├── test.jpg
│   └── resultat.jpg
├── CNN/
│   ├── cnn_detection.py
│   ├── old_pic.jpg
│   └── resultat_cnn.jpg
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Python 3.8 ou plus est recommandé.

```bash
git clone https://github.com/MarwaIdd/projet-detection-presence.git
cd projet-detection-presence
pip install -r requirements.txt
```

## Modèle CNN (à télécharger)

La méthode CNN utilise le détecteur de visages SSD + ResNet-10 d'OpenCV.
Les deux fichiers du modèle ne sont pas inclus dans ce dépôt. Téléchargez-les
et placez-les dans le dossier `CNN/` :

[res10_300x300_ssd_iter_140000.caffemodel](https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel)

Ou en ligne de commande, depuis le dossier `CNN/` :

```bash
curl -L -O https://raw.githubusercontent.com/opencv/opencv/3.4.0/samples/dnn/face_detector/deploy.prototxt
curl -L -O https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel
```
Remaque : Sous Windows PowerShell, utilisez curl.exe à la place de curl .

## Utilisation

Méthode Haar Cascade :

```bash
cd haar_cascade
python haar_detection.py
```

Méthode CNN :

```bash
cd CNN
python cnn_detection.py
```

Chaque script :
1. charge l'image du dossier ;
2. détecte les visages et les encadre ;
3. affiche le nombre de visages détectés dans le terminal ;
4. ouvre une fenêtre avec le résultat (appuyez sur une touche pour la fermer) ;
5. enregistre l'image annotée (`resultat.jpg` ou `resultat_cnn.jpg`).

Pour tester vos propres images, remplacez le nom du fichier dans l'appel
`cv2.imread(...)` du script.

> Les scripts utilisent `cv2.imshow`, qui nécessite un écran. Sur un serveur
> sans interface graphique, supprimez les lignes `imshow`, `waitKey` et
> `destroyAllWindows`.

## Résultats

- **Haar Cascade** : fonctionne bien sur des images simples (visages de face,
  bonne lumière), mais peut produire des faux positifs. Lors d'un de nos tests,
  il a détecté 5 visages au lieu de 4.
- **CNN (SSD + ResNet-10)** : plus robuste face aux variations de position et
  d'éclairage. Il affiche un score de confiance pour chaque visage détecté
  (seuil utilisé : 0,5).

Cette comparaison est qualitative, basée sur quelques images de test. Elle
n'a pas encore fait l'objet d'une évaluation chiffrée.

## Limites actuelles

- Le projet **détecte** des visages, il ne **reconnaît** pas encore les
  personnes : il compte des visages, il ne sait pas qui est présent.
- Pas d'évaluation chiffrée (faux positifs, faux négatifs).
- Un seul traitement d'image à la fois (pas de traitement par lot ni de flux
  vidéo).

## Améliorations prévues

- Reconnaissance faciale pour identifier chaque étudiant (à l'aide
  d'embeddings de visages).
- Export de la liste de présence au format CSV.
- Traitement d'un dossier d'images ou d'une capture webcam.
- Évaluation sur un jeu de test, avec faux positifs et faux négatifs pour
  chaque méthode.

## Crédits

**Images** : photo provenant de [Pexels](https://www.pexels.com/fr-fr/photo/etudiants-universitaires-diversifies-dans-une-salle-de-conference-31367502/),
utilisée selon la [licence Pexels](https://www.pexels.com/license/).


**Modèles et bibliothèques** :
- [OpenCV](https://opencv.org/) (Haar Cascade et module `dnn`)
- Détecteur de visages SSD + ResNet-10, fourni avec les exemples d'OpenCV