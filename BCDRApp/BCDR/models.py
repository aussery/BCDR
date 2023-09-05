from django.db import models

class Assets(models.Model):
    assetid = models.AutoField(primary_key=True)
    assetname = models.CharField(max_length=255, blank=True, null=True)
    assettype = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets'

class BusinessProcesses(models.Model):
    processid = models.AutoField(primary_key=True)
    processname = models.CharField(max_length=255, blank=True, null=True)
    system = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    criticalitylevel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businessprocesses'

class EmergencyContacts(models.Model):
    contactid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencycontacts'

class Incidents(models.Model):
    incidentid = models.AutoField(primary_key=True)
    incidentname = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    incidentdate = models.DateField(blank=True, null=True)
    responseactions = models.TextField(blank=True, null=True)
    strategy = models.ForeignKey('RecoveryStrategies', models.DO_NOTHING, db_column='strategy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidents'

class RecoveryStrategies(models.Model):
    strategyid = models.AutoField(primary_key=True)
    strategyname = models.CharField(max_length=255, blank=True, null=True)
    process = models.ForeignKey(BusinessProcesses, models.DO_NOTHING, db_column='process', blank=True, null=True)
    asset = models.ForeignKey(Assets, models.DO_NOTHING, db_column='asset', blank=True, null=True)
    risk = models.ForeignKey('Risks', models.DO_NOTHING, db_column='risk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recoverystrategies'

class Risks(models.Model):
    riskid = models.AutoField(primary_key=True)
    riskname = models.CharField(max_length=255, blank=True, null=True)
    likelihood = models.CharField(max_length=255, blank=True, null=True)
    impacttype = models.CharField(max_length=255, blank=True, null=True)
    impactscale = models.CharField(max_length=255, blank=True, null=True)
    risklevel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risks'

class TestPlans(models.Model):
    testplanid = models.AutoField(primary_key=True)
    testplanname = models.CharField(max_length=255, blank=True, null=True)
    testdate = models.DateField(blank=True, null=True)
    testresult = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    strategy = models.ForeignKey(RecoveryStrategies, models.DO_NOTHING, db_column='strategy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testplans'
