
# Information Theory based UI Analysis

The [dataset](http://interactionmining.org/rico) is comprised of over 72k unique free app UI screens mined from the Android app store. Below is a sample of a few of these UI images:

![sample UIs](readme_imgs/sample_uis.png)

These apps span across 28 different categories:

![app categories](readme_imgs/app_cat.png)

These UIs were analyzed by examining pixel intensity distributions (histograms), entropy, KL divergence, and information gain:

![histograms](readme_imgs/histos.png)

![entropy](readme_imgs/ent.png)

The goal of this project was to determine if entropy is a good proxy for app category and app rating:

![entropy_category](readme_imgs/ent_cat.png)

![entropy_rating](readme_imgs/ent_rating.png)
