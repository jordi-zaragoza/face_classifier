# Face classifier
This repository is used for face classification. It can detect:

- open-closed eyes
- sunglasses
- profile/frontal
- blurry image.

You can find the repository on [github](https://github.com/jordi-zaragoza/face_classifier).

If you want to use the library directly, go to [pypi](https://test.pypi.org/project/face_classifier/).


## Use Examples
### Closed eyes:

```python
from face_classifier import classifier

classifier(name='face1', path='face_classifier/data/open_test/closed5.jpg')
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classifier/data/readme/TRY_IT_2_2.png?raw=true)

    {'name': 'face1',
     'blurry': 0.0,
     'profile': 0.0,
     'sunglasses': 0.002,
     'eyes': (0.009, 0.011)}

### Open eyes:

```python
classifier(name='face2', path='face_classifier/data/open_test/open2.jpg')
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classifier/data/readme/TRY_IT_3_2.png?raw=true)

    {'name': 'face2',
     'blurry': 0.0,
     'profile': 0.0,
     'sunglasses': 0.0,
     'eyes': (0.763, 0.782)}

### Profile image

```python
classifier(name='face3', path='face_classifier/data/profile_test/profile2.jpg')
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classifier/data/readme/TRY_IT_4_2.png?raw=true)

    {'name': 'face3',
     'blurry': 0.0,
     'profile': 1.0,
     'sunglasses': None,
     'eyes': None}

### Sunglasses image

```python
classifier(name='face4', path='face_classifier/data/sunglasses_test/sunglass1.jpg')
```

![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classifier/data/readme/TRY_IT_5_2.png?raw=true)

    {'name': 'face4',
     'blurry': 0.0,
     'profile': 0.093,
     'sunglasses': 0.93,
     'eyes': None}

### Blurry image

```python
classifier(name='face5', path='face_classifier/data/blurry_test/blurry12.jpg')
```
![png](https://github.com/jordi-zaragoza/face_classifier/blob/main/face_classifier/data/readme/TRY_IT_6_2.png?raw=true)

    {'name': 'face5',
     'blurry': 0.998,
     'profile': None,
     'sunglasses': None,
     'eyes': None}


# Requirements
- matplotlib==3.3.4
- numpy==1.19.5
- tensorflow==2.9.1

# Models
These models have been trained separately using the code from [this other repository](https://github.com/jordi-zaragoza/pictures_classifier) that I created for 'weddings' pictures classification. Specially bad pictures with closed eyes.

I used a pretrained model MobilenetV2. And then retrained using my own dataset.

The models have been trained with around 10k pictures each.

I cannot upload the datasets as they are mostly from weddings of a friend photographer.

# How it works
The program will check conditions and then continue or not depending on the result:
1) Blurry picture
2) Profile/Frontal
3) Sunglasses
4) Open-Closed eyes




    



