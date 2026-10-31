import cv2

# 1. Charger le classificateur Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# 2. Charger l'image et la convertir en niveaux de gris
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Détecter les visages
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# 4. Vérifier la présence et encadrer les visages
if len(faces) > 0:
    print(f'Presence détectée : {len(faces)} visage(s)')
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, 'Present', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
else:
    print('Aucune présence détectée')
    cv2.putText(img, 'Absent', (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# 5. Afficher et sauvegarder le résultat

cv2.imshow('Detection de presence', img)
cv2.imwrite('resultat.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()