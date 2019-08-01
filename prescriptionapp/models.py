from django.db import models



class Prescription(models.Model):
    patient_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    prescription_date = models.DateTimeField(auto_now_add=True)
    doctor_Preference = models.CharField(max_length=50)
    description = models.TextField()
    treatment = models.CharField(max_length=100)
    medicine = models.CharField(max_length=200)
    blood_pressure = models.CharField(max_length=20)
    pulse = models.CharField(max_length=20)
    guide  = models.CharField(max_length=30)
    test= models.CharField(max_length=200)


    def __str__(self):
        return self.patient_name


