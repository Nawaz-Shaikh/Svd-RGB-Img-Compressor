******* SVD Image Compressor (Custom Implementation) ********

This project demonstrates an image compression technique using Singular Value Decomposition (SVD) — implemented entirely from scratch without using high-level SVD functions. The compression is applied separately on each RGB channel to preserve color details effectively.

------ Features
  Fully custom SVD algorithm (no use of NumPy’s svd).

  Compresses images by applying SVD to each RGB channel independently.

  Includes a sample image (high.jpg) to test the compression.
  
  Educational and lightweight — great for learning linear algebra and image processing.

------ Repository Contents
   - svd_compressor.py — Main script containing:
       
       - RGB channel separation and recombination.
        
       - Image compression logic.
         
   - my_svd.py — Custom Svd using mathematical functions
    
   - high.jpg — Sample image used for compression testing.
    
   - README.md — Project documentation.

------- How It Works
The input image (high.jpg) is loaded and split into Red, Green, and Blue channels.

A custom SVD is applied to each channel matrix.

Each channel is reconstructed using only the top k singular values (you can configure k).

The compressed RGB channels are merged to form the final compressed image.

This method effectively reduces the size of the image data while retaining most of the visual information — especially when using an optimal k value.
