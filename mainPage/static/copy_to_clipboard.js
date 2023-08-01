function copyImageToClipboard(imagePath) {
  // Make an AJAX request to the Django view or function that runs the Python code
  $.ajax({
    type: "POST",
    url: "/copy-image-to-clipboard/",
    data: {
      image_path: imagePath
    },
    success: function(response) {
      // Handle success if needed
      console.log("Image copied to clipboard!");
    },
    error: function(xhr, errmsg, err) {
      // Handle error if needed
      console.log("Error copying image to clipboard:", errmsg);
    }
  });
}