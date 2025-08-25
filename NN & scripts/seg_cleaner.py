import slicer

# Zostawiamy T1–T12, L1–L4 z dopiskiem " vertebra"
ALLOWED_NAMES = [
    "T1 vertebra","T2 vertebra","T3 vertebra","T4 vertebra","T5 vertebra","T6 vertebra",
    "T7 vertebra","T8 vertebra","T9 vertebra","T10 vertebra","T11 vertebra","T12 vertebra",
    "L1 vertebra","L2 vertebra","L3 vertebra","L4 vertebra"
]

# Weź pierwszy węzeł segmentacji w scenie (lub podaj nazwę, jeśli wolisz)
segNode = slicer.util.getNodesByClass("vtkMRMLSegmentationNode")[0]
seg = segNode.GetSegmentation()

# Zbierz ID segmentów do usunięcia (nie usuwaj w trakcie iteracji!)
to_delete = []
for i in range(seg.GetNumberOfSegments()):
    seg_id = seg.GetNthSegmentID(i)
    name = seg.GetSegment(seg_id).GetName()
    if name not in ALLOWED_NAMES:
        to_delete.append(seg_id)

for seg_id in to_delete:
    seg.RemoveSegment(seg_id)

print(f"✅ Usunięto {len(to_delete)} segment(ów) spoza listy.")
