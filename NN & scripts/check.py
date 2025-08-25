import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

# Ścieżki do plików
ct_path = "7 Vol. Kr Kosci.nii"
mask_path = "7 Vol. Kr Kosci segmentation.nii"

# Wczytaj dane
ct_nii = nib.load(ct_path)
mask_nii = nib.load(mask_path)

ct = ct_nii.get_fdata()
mask = mask_nii.get_fdata()

# Wybierz 10 równomiernie rozłożonych slice’y
num_slices = 10
slice_indices = np.linspace(0, ct.shape[2] - 1, num_slices, dtype=int)

plt.figure(figsize=(15, 6))

for i, idx in enumerate(slice_indices):
    # Obraz CT
    plt.subplot(2, num_slices, i + 1)
    plt.imshow(ct[:, :, idx], cmap="gray")
    plt.title(f"Slice {idx}")
    plt.axis("off")

    # CT z maską
    plt.subplot(2, num_slices, i + 1 + num_slices)
    plt.imshow(ct[:, :, idx], cmap="gray")
    plt.imshow(mask[:, :, idx], cmap="jet", alpha=0.4)
    plt.axis("off")

plt.tight_layout()
plt.show()
