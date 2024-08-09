from utils import read_video, save_video
from trackers import Tracker

def main():
    frames = read_video("input/C35bd9041_0(27).mp4")

    tracker = Tracker("models/best.pt")

    tracker.get_object_tracks(frames[:20])

    save_video("output/output.mp4", frames)

if __name__ == "__main__":
    main()