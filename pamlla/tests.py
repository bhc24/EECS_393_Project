from django.test import TestCase
from models import User, Patient, Doctor, Prediction, ExpectancyData, HazardFunction, Logit, MutatedGenes, SurvivalFactors

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username= "stephhippo", passphrase="eecs393rules")

    def test_user_creation(self):
        steph = User.objects.get(username="stephhippo")
        self.assertTrue(isinstance(steph, User))

class PatientTestCase(TestCase):
    def setUp(self):
        steph = User.objects.create(username= "stephhippo", passphrase="eecs393rules")
        Patient.objects.create(name="stephhippo",patient = steph)

    def test_patient_creation(self):
        steph = Patient.objects.get(name="stephhippo")
        self.assertTrue(isinstance(steph, Patient))

class DoctorTestCase(TestCase):
    def setUp(self):
        ben = User.objects.create(username="bencook", passphrase="glennan is home")
        Doctor.objects.create(name="Dr. Ben Cook MD", doctor = ben)

    def test_doctor_creation(self):
        ben = Doctor.objects.get(name="Dr. Ben Cook MD")
        self.assertTrue(isinstance(ben, Doctor))

class PredictionTest(TestCase):
    def setUp(self):
        steph = User.objects.create(username= "stephhippo", passphrase="eecs393rules")
        steph_patient = Patient.objects.create(name="stephhippo",patient = steph)
        Prediction.objects.create(patient= steph_patient)

    def test_prediction_creation(self):
        steph_patient = Patient.objects.get(name="stephhippo")
        predict = Prediction.objects.get(patient=steph_patient)
        self.assertTrue(isinstance(predict, Prediction))

class ExpectancyDataTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username= "testuser", passphrase="testing123")
        test_patient = Patient.objects.create(name="Test User",patient = test_user)
        test_prediction = Prediction.objects.create(patient=test_patient)
        self.test_hazard = HazardFunction.objects.create(prediction=test_prediction)
        ExpectancyData.objects.create(hazard=self.test_hazard,percentage_survival=0.80, num_weeks=5)
        ExpectancyData.objects.create(hazard=self.test_hazard,percentage_survival=0.70, num_weeks=4)
        ExpectancyData.objects.create(hazard=self.test_hazard,percentage_survival=0.60, num_weeks=3)
        ExpectancyData.objects.create(hazard=self.test_hazard,percentage_survival=0.50, num_weeks=1)

    def test_expectancy_creation(self):
        data = ExpectancyData.objects.filter(hazard=self.test_hazard)
        for pt in data:
            self.assertTrue(isinstance(pt, ExpectancyData))

class LogitTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username= "testuser", passphrase="testing123")
        test_patient = Patient.objects.create(name="Test User",patient = test_user)
        self.predict_test = Prediction.objects.create(patient=test_patient)

    def test_logit_creation(self):
        test_logit = Logit(prediction=self.predict_test)
        self.assertTrue(isinstance(test_logit, Logit))

class HazardFunctionTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username= "testuser", passphrase="testing123")
        test_patient = Patient.objects.create(name="Test User",patient = test_user)
        test_prediction = Prediction.objects.create(patient=test_patient)
        self.test_hazard = HazardFunction(prediction=test_prediction)

    def test_hazard_function_creation(self):
        self.assertTrue(isinstance(self.test_hazard, HazardFunction))

class MutatedGenesTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username= "testuser", passphrase="testing123")
        test_patient = Patient.objects.create(name="Test User",patient = test_user)
        predict_test = Prediction.objects.create(patient=test_patient)
        self.test_logit = Logit(prediction=predict_test)
        self.test_mutated_gene = MutatedGenes(gene_name="TestGene", meth_score=0.452)

    def test_mutated_genes(self):
        self.assertTrue(isinstance(self.test_mutated_gene, MutatedGenes))

class SurvivalFactorsTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username= "testuser", passphrase="testing123")
        test_patient = Patient.objects.create(name="Test User",patient = test_user)
        test_prediction = Prediction.objects.create(patient=test_patient)
        self.test_logit = Logit(prediction=test_prediction)
        self.test_hazard = HazardFunction(prediction=test_prediction)
        self.test_factor = SurvivalFactors(logit=self.test_logit, hazard=self.test_hazard)

    def test_survival_factor_creation(self):
        self.assertTrue(isinstance(self.test_factor, SurvivalFactors))