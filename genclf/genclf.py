import os
import warnings
warnings.filterwarnings('ignore')
# from sklearn.externals import joblib
import joblib

class GenderClassifier(object):
	"""docstring for GenderClassifier"""
	def __init__(self, name=None):
		super(GenderClassifier, self).__init__()
		self.name = name

	def __repr__(self):
		return 'GenderClassifier(name={})'.format(self.name)

	def predict(self):
		# Load Vectorizers
		gender_vectorizer = open("models/gender_vectorizer.pkl","rb")
		gender_cv = joblib.load(gender_vectorizer)
		# Classification
		gender_nv_model = open("models/gender_nv_model.pkl","rb")
		gender_clf = joblib.load(gender_nv_model)

		# Vectorized Data
		vectorized_data = gender_cv.transform([self.name]).toarray()
		prediction = gender_clf.predict(vectorized_data)
		
		if prediction[0] == 0:
			result = 'female'
		elif prediction[0] == 1:
			result = 'male'
		return result

	def load(self,model_type):
		if model_type == 'nv':
			gender_nv_model = open("/models/gender_nv_model.pkl","rb")
			gender_clf = joblib.load(gender_nv_model)
		elif model_type == 'logit':
			gender_logit_model = open("/models/gender_logit_model.pkl","rb")
			gender_clf = joblib.load(gender_logit_model)
		else:
			print("Pls Load model [nv:naive bayes,logit:logisticregression")

		return gender_clf

	def classify(self,new_name):
		self.name = new_name
		result = self.predict()
		return result

