import cv2
import os
import numpy as np

#Charger le modèle CNN pré-entraîné (SSD + ResNet-10)
prototxt = "deploy.prototxt"
model = "res10_300x300_ssd_iter_140000.caffemodel"

if not os.path.exists(prototxt) or not os.path.exists(model):
    raise FileNotFoundError("Télécharge les fichiers .prototxt et .caffemodel dans le dossier du script !")

net = cv2.dnn.readNetFromCaffe(prototxt, model)

#Charger l'image
img = cv2.imread('old_pic.jpg')
if img is None:
    raise FileNotFoundError("Image inserée introuvable")

h, w = img.shape[:2]

# Prétraitement CNN (blob)
# Le modèle attend du 300x300, avec soustraction des moyennes BGR
blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))

# Inférence
net.setInput(blob)
detections = net.forward()

# Parser & filtrer les détections
faces_found = 0
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    
    # Seuil de confiance CNN (0.5 = 50%)
    if confidence > 0.5:
        # Coordonnées normalisées (0 à 1) → convertir en pixels
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        x1, y1, x2, y2 = box.astype("int")
        
        # Dessiner rectangle & texte
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f'CNN: {confidence:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        faces_found += 1

# Résultat global
if faces_found > 0:
    print(f'Présence détectée : {faces_found} visage(s)')
    cv2.putText(img, 'Present', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
else:
    print('Aucune présence détectée')
    cv2.putText(img, 'Absent', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Afficher & sauvegarder
cv2.imshow('Détection CNN', img)
cv2.imwrite('resultat_cnn.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()