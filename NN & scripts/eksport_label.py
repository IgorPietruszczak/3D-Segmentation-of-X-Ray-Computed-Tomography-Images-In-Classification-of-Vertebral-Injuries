import slicer
import json

# Pobierz pierwszy znaleziony węzeł segmentacji
segmentation = slicer.util.getNodesByClass("vtkMRMLSegmentationNode")[0]

# Pobierz liczbę segmentów
num_segments = segmentation.GetSegmentation().GetNumberOfSegments()

# Przygotuj słownik: {ID: nazwa}
segment_map = {}

for i in range(num_segments):
    segment_id = segmentation.GetSegmentation().GetNthSegmentID(i)
    segment_name = segmentation.GetSegmentation().GetSegment(segment_id).GetName()
    segment_map[i + 1] = segment_name  # i+1 bo etykiety zaczynają się od 1 w labelmapie

# Ścieżka zapisu JSON
output_path = "D:/Skany/Dataset/Nowy folder/segment_labels_auto.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(segment_map, f, indent=4)

print(f"✅ Zapisano mapę etykiet do {output_path}")
