import nibabel as nib
import numpy as np

# Wczytaj maskę segmentacyjną
seg = nib.load("7 Vol. Kr Kosci segmentation.nii")
data = seg.get_fdata()

# Wyciągnij unikalne etykiety (label ID)
labels = np.unique(data)
print("Unikalne ID segmentów:", labels)
