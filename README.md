# duplicateDetection
Image Duplicate detection using Imagehash 


* Using imagehash which converts the images into hash string and then futher compares.
* Image hashes tell whether two images look nearly identical. This is different from cryptographic hashing algorithms (like MD5, SHA-1) where tiny changes in the image give completely different hashes. In image fingerprinting, we actually want our similar inputs to have similar output hashes as well.
* The image hash algorithms (average, perceptual, difference, wavelet) analyse the image structure on luminance (without color information). The color hash algorithm      analyses the color distribution and black & gray fractions (without position information).
