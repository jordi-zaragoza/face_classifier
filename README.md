# Face classifier
This repository is used for face classification. It can detect:

- open-closed eyes
- sunglasses
- profile/frontal
- blurry image.

You can find the repository on [github](https://github.com/jordi-zaragoza/face_classifier).

If you want to use the library directly, go to [pypi](https://pypi.org/project/face-classify).

## Disclaimer
The classifier works better with face cropped pictures, the models have been trained using [this face recognition repossitory](https://pypi.org/project/face-recognition/) on group pictures.

Better use them in combination or crop the face picture yourself.

This repository comes with absolutely no guarantees. 

## Use Examples

- for face classifier refer to [Try_IT_face.ipynb](https://github.com/jordi-zaragoza/face_classifier/blob/main/TRY_IT_face.ipynb)
- for group face classifier refer to [Try_IT_group.ipynb](https://github.com/jordi-zaragoza/face_classifier/blob/main/TRY_IT_group.ipynb)

### Closed eyes

```python
from face_classify import classifier
classifier(image_or_path='face_classify/data/open_test/closed5.jpg')
```
![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classify/data/readme_files/TRY_IT_3_2.png?raw=true)

Output:

    {'name': 'face1',
     'blurry': 0.0,
     'profile': 0.0,
     'sunglasses': 0.002,
     'eyes': (0.009, 0.011)}

#### with crop face

```python
classifier(image_or_path='face_classify/data/open_test/closed5.jpg', crop_face = True)
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classify/data/readme_files/TRY_IT_5_2.png?raw=true)

Output:

    {'name': 'face1',
     'blurry': 0.0,
     'profile': 0.0,
     'sunglasses': 0.0,
     'eyes': (0.0, 0.0)}



### Open eyes


```python
classifier(image_or_path='face_classify/data/open_test/open2.jpg', crop_face = True)
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classify/data/readme_files/TRY_IT_7_2.png?raw=true)

Output:   

    {'name': 'face2',
     'blurry': 0.0,
     'profile': 0.0,
     'sunglasses': 0.0,
     'eyes': (0.918, 0.924)}


### Profile


```python
classifier(image_or_path='face_classify/data/profile_test/profile2.jpg', crop_face = True)
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classify/data/readme_files/TRY_IT_9_2.png?raw=true)

Output:

    {'name': 'face3',
     'blurry': 0.001,
     'profile': 1.0,
     'sunglasses': None,
     'eyes': None}


### Sunglasses

```python
classifier(image_or_path='face_classify/data/sunglasses_test/sunglass1.jpg', crop_face = True)
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classify/data/readme_files/TRY_IT_11_2.png?raw=true)

Output:

    {'name': 'face4',
     'blurry': 0.0,
     'profile': 0.0,
     'sunglasses': 0.313,
     'eyes': (0.0, 0.0)}

### Blurry

```python
classifier(image_or_path='face_classify/data/blurry_test/blurry12.jpg', crop_face = True)
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classify/data/readme_files/TRY_IT_13_2.png?raw=true)

Output:

    {'name': 'face5',
     'blurry': 1.0,
     'profile': None,
     'sunglasses': None,
     'eyes': None}


## Requirements
- matplotlib==3.3.4
- numpy==1.19.5
- tensorflow==2.9.1
- face_recognition==1.3.0

## Models
These models have been trained separately using the code from [this other repository](https://github.com/jordi-zaragoza/pictures_classifier) that I created for 'weddings' pictures classification. Specially bad pictures with closed eyes.

I used a pretrained model MobilenetV2. And then retrained using my own dataset.

The models have been trained with around 10k pictures each.

I cannot upload the datasets as they are mostly from weddings of a friend photographer.

## How it works
The main goal is to find if a face has opened or closed eyes. 
For this purpose the program will check a condition and then continue to the next one depending on the result, the order is as follows:

1) Check if Blurry picture -> Continues if its not blurry
2) Profile/Frontal picture -> Continues if its frontal
3) Wearing Sunglasses -> Continue if not sunglasses detected
4) Check Open-Closed eyes




    



