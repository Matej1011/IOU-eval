#Used to view a NIfTI file, allowing you to scroll through each slice
#May not function for all NIfTI files
#If the file shown is completely black but there is a non-zero sum() value then a different viewer must be used

import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Path to the NIfTI file
nifti_file_path = r""

# Load the NIfTI file
nifti_image = nib.load(nifti_file_path)
nifti_data = nifti_image.get_fdata()
slice_index = 0

print(f"Shape of the NIfTI data: {nifti_data.shape}")
print(f"Data type of the NIfTI data: {nifti_data.dtype}")
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

img = ax.imshow(nifti_data[:, :, slice_index], cmap='gray')
ax.set_title(f"Slice {slice_index}")
ax.axis('off')

def update(val):
    slice_index = int(slice_slider.val)
    img.set_data(nifti_data[:, :, slice_index])
    ax.set_title(f"Slice {slice_index}")
    fig.canvas.draw_idle()

ax_slice = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slice_slider = Slider(ax_slice, 'Slice', 0, nifti_data.shape[2] - 1, valinit=slice_index, valstep=1)

slice_slider.on_changed(update)
# Print out some values of potential interest
print(nifti_data.max())
print(nifti_data.min())
print(nifti_data.sum())
plt.show()
