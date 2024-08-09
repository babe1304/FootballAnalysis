from ultralytics import YOLO
import supervision as sv

class Tracker:
    def __init__(self, model_path, batch_size=20):
        self.model = YOLO(model_path)
        self.batch_size = batch_size
        self.tracker = sv.ByteTrack()

    def detect_objects(self, frames):
        detections = []
        for i in range(0, len(frames), self.batch_size):
            batch = self.model.predict(frames[i:i + self.batch_size], conf=0.1)
            detections.extend(batch)
        return detections

    def get_object_tracks(self, frames):
        detections = self.detect_objects(frames)
        class_names = detection.names
        class_inv = {v: k for k, v in detection.names.items()}

        for frame_num, detection in enumerate(detections):

            detections_sv = sv.Detections.from_ultralytics(detection)

            for obj_id, class_id in enumerate(detections_sv.class_id):
                if class_names[class_id] == "goalkeeper":
                    detections_sv.class_id[obj_id] = class_inv["player"]

            detections_with_tracks = self.tracker.update_with_detections(detections_sv)