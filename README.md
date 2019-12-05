## GenderClassifier Tool
+ Aim: using ML models as packages
+ Purpose: for classifying gender of individuals using their first names

### Installation
```bash
pip install genclf
```

### Usage
#### Basic usage
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.name = 'Jess'
>>> g.predict()
```

#### Loading Different Models
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.name = 'Jessica'
>>> g.load('logit')
>>> g.predict()
```

#### Using the Classify Method
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.load('nb')
>>> g.classify("David")
```

#### Check Gender
```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.is_male("Mark")
```

```python
>>> from genclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.is_female("Mary")
```

#### Requirements
+ Joblib
+ Scikit-learn

#### Maintainer
+ Jesse E.Agbe(JCharis)
+ Jesus Saves@JCharisTech