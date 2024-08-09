from ultralytics import YOLO

model = YOLO('models/best.pt')

r = model.predict('./input/C35bd9041_0(27).mp4', save=True)

print(r[0])

for box in r[0].boxes:
    print(box)
