from django.db import models

GATE1, GATE2 = range(2)
GATE = (
    (GATE1, 'GATE1'),
    (GATE2, 'GATE2')
)

CHECKIN, CHECKOUT = range(2)
STATUS = (
    (CHECKIN, 'CHECKIN'),
    (CHECKOUT, 'CHECKOUT'),
)


class Parkir(models.Model):
    id_card = models.CharField('ID Card', max_length=50)
    gate = models.PositiveSmallIntegerField('Gate', choices=GATE, default=GATE1)
    status = models.PositiveSmallIntegerField('Status', choices=STATUS, default=CHECKIN)
    tanggal = models.DateField('tanggal')
    jam = models.TimeField('jam')
    biaya = models.IntegerField('biaya', choices=list(zip(range(1000, 11000, 1000), range(1000, 11000, 1000))), null=True, blank=True)

    def __unicode__(self):
        return self.id_card

    class Meta:
        verbose_name = ('Parkir')