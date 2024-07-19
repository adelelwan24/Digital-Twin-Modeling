from PIL import Image

def concat_images_side_by_side(border_width=10):
    """
    Concatenate three images side by side with borders between them.
    
    Parameters
    ----------
    border_width : int, optional
        The width of the border between the images in pixels. Default is 10.
    
    Returns
    -------
    None
    
    Notes
    -----
    - The images '1.png', '2.png', and '3.png' must be present in the same directory as the script.
    - The images are resized to the same height while maintaining their aspect ratios.
    - The concatenated image is saved as 'concatenated_image_with_borders.png'.
    
    Examples
    --------
    >>> concat_images_side_by_side(border_width=15)
    Images concatenated successfully with borders and saved as 'concatenated_image_with_borders.png'.
    """
    # Load the images
    image1 = Image.open('1.png')
    image2 = Image.open('2.png')
    image3 = Image.open('3.png')
    
    # Get the maximum height of the three images
    max_height = max(image1.height, image2.height, image3.height)
    
    # Resize images to the same height using the LANCZOS resampling filter
    image1 = image1.resize((int(image1.width * max_height / image1.height), max_height), Image.Resampling.LANCZOS)
    image2 = image2.resize((int(image2.width * max_height / image2.height), max_height), Image.Resampling.LANCZOS)
    image3 = image3.resize((int(image3.width * max_height / image3.height), max_height), Image.Resampling.LANCZOS)
    
    # Calculate the total width including borders
    total_width = image1.width + image2.width + image3.width + 2 * border_width
    
    # Create a new blank image with the total width and max height, with black background
    new_image = Image.new('RGB', (total_width, max_height), "black")
    
    # Paste the images into the new image with border offsets
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1.width + border_width, 0))
    new_image.paste(image3, (image1.width + image2.width + 2 * border_width, 0))
    
    # Save the new image
    new_image.save('concatenated_image_with_borders.png')
    print("Images concatenated successfully with borders and saved as 'concatenated_image_with_borders.png'.")

concat_images_side_by_side()
