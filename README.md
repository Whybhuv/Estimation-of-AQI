# Estimation of Air Quality Index from Images

This is an Machine Learining Model which uses images of clean and polluted air to estimate the AQI of air in new image.

First, images are scrapped from the web using Bing Image Dowloader module of python (refer files Scraping_Clean_Air.py and Scrapping_Polluted_Air.py).

The images are then classified into training and validation folders manually (generally we use 80% of the images to train the model and the rest to validate).

The model is then built and tested through non-supervised learning.

Sample images are stored in a new file and can be used to manualy test the model.
