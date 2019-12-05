from genclf import __version__
from genclf import GenderClassifier



def test_version():
    assert __version__ == '0.1.0'


def test_genclf_for_male():
	g = GenderClassifier()
	g.name = 'Jess'
	result = g.predict()
	assert result == 'male'

def test_genclf_for_female():
	g = GenderClassifier()
	g.name = 'Mary'
	result = g.predict()
	assert result == 'female'

def test_genclf_for_is_female():
	g = GenderClassifier()
	result = g.is_female('Rose')
	assert result == True

def test_genclf_for_is_male():
	g = GenderClassifier()
	result = g.is_male('Jesus')
	assert result == True


