import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

def detect_faces(rectangle_color,scale_factor,min_neighbors):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    while True:
        # Read the frames from the webcam
        ret, frame = cap.read()
        # Convert the frames to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect the faces using the face cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            rectangle_color_rgb = st.color_picker(rectangle_color)
            cv2.rectangle(frame, (int(x),int(y)), (int(x) + int(w), int(y) + int(h)), rectangle_color_rgb, 2)
        # Display the frames
        cv2.imshow('Déection de visage', frame)
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

def app():
    st.title("Détection de visage")
    # Ajouter des instructions pour guider l'utilisateur
    st.write("Cliquez sur le bouton 'Démarrer la webcam' pour commencer la détection de visage en temps réel.")
    st.write("Appuyez sur la touche 'q' pour arrêter la détection.")
    st.write("Utilisez les curseurs pour ajuster les paramètres de détection et choisissez la couleur des rectangles.")

    # Paramètres de détection
    min_neighbors = st.slider("Min Neighbors", min_value=3, max_value=10, value=5)
    scale_factor = st.slider("Scale Factor", min_value=1.01, max_value=1.5, value=1.1)

    # Couleur des rectangles
    rectangle_color = st.color_picker("Couleur des rectangles", "#00FF00")

    # Add a button to start detecting faces
    if st.button("Détection"):
        # Call the detect_faces function
        detect_faces(rectangle_color,scale_factor,min_neighbors)
if __name__ == "__main__":
    app()