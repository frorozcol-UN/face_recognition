
import cv2
import face_recognition

imgElon = face_recognition.load_image_file("images/elon_musk.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("images/elon_musk_test.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]

result = face_recognition.compare_faces([encodeElon], encodeTest)
faceDist = face_recognition.face_distance([encodeElon], encodeTest)

print(result, faceDist)
cv2.rectangle(imgTest, (faceTest[3], faceTest[0]), (faceTest[1], faceTest[2]), (255, 0, 255), 2)
cv2.putText(imgTest, f"{result} {round(faceDist[0],2)}", (50,50), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255),2)
#cv2.imshow("Elon musk", imgElon)
cv2.imshow("Elon musk", imgTest)
cv2.waitKey(0)