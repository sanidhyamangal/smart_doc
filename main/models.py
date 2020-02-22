from django.db import models
import uuid


# base model
class BaseModel(models.Model):
    """
    A base ORM model to inherit into each classes
    """

    # create a uuid field
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# create a patient model
class Patient(BaseModel):
    """
    A ORM model to deal with patient's profile
    """

    # create patient's name
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=15)
    refered_by = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "patients"


# create doctor model
class Doctor(BaseModel):
    """
    A ORM model to manage doctor table
    """

    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=15)

    class Meta:
        db_table = "doctors"


# Test Class to record all the tests
class TestModel(BaseModel):
    """
    A ORM for managing base test model which could be later inherited
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    test_result = models.BooleanField()

    class Meta:
        abstract = True


class MalariaTest(TestModel):
    """
    A ORM model to manage malaria tests
    """
    class Meta:
        db_table = "malaria_test"


class PneumoniaTest(TestModel):
    """
    A ORM model for managing Pneumonia Tests
    """
    class Meta:
        db_table = "penumonia_test"
