from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict("image.jpg", classes=[15], conf=0.5)

results[0].show()
results[0].save("result_cat.jpg")