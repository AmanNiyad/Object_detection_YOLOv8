# from ultralytics import YOLO
import pickle
import cv2
# model = YOLO("yolov8n.pt")
# pickle.dump(model, open('model.pkl', 'wb'))

loaded = pickle.load(open('model.pkl', 'rb'))
loaded('000002.jpg', show=True)
if(cv2.waitKey()):
    cv2.destroyAllWindows()
