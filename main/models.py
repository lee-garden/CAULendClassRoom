from django.db import models

class Building(models.Model):
    building_no = models.CharField(max_length=3, primary_key=True)
    building_name = models.CharField(max_length=10)
    min_floor = models.IntegerField(default=-8)
    max_floor = models.IntegerField(default=12)
    new_request_reservation = models.IntegerField(default=0)
    change_request_reservation = models.IntegerField(default=0)

    def __str__(self):
        return self.building_name

    def add_new_request(self):
        self.new_request_reservation+=1
        self.save()

    def add_change_request(self):
        self.change_request_reservation+=1
        self.save()

    def sub_new_request(self):
        self.new_request_reservation-=1
        self.save()

    def sub_change_request(self):
        self.change_request_reservation-=1
        self.save()

class ClassRoom(models.Model):
    building_no = models.ForeignKey(Building, db_column='building_no_id', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=4)
    floor = models.IntegerField(default=1)
    capacity = models.IntegerField(default=0)

    class Meta:
        unique_together = (("building_no", "room_no"),)

    def __str__(self):
        return self.building_no.building_no + "관" + self.room_no + "호"