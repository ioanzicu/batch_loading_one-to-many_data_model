import csv  # https://docs.python.org/3/library/csv.html
from collections import namedtuple

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import State, Site, Region, Iso, Category


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Category.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name, description, justification, year, longitude, latitude, area_hectares, category, state,       region, iso
    # Cult, "<p>The</p>, "<p>Bamiyan.", 2003, 67.82525,  34.84694, 158.9265,      Cultural, Afghanistan, Asia,   af

    Row = namedtuple('Row', ['name', 'description', 'justification', 'year', 'longitude',
                     'latitude', 'area_hectares', 'category', 'state', 'region', 'iso'])
    for row in reader:
        r = Row(row[0], row[1], row[2], row[3], row[4], row[5],
                row[6], row[7], row[8], row[9], row[10])
        print(r)

        try:
            area_hectares = int(r.area_hectares)
        except:
            area_hectares = None

        state, state_created = State.objects.get_or_create(
            name=r.state,
            longitude=r.longitude,
            latitude=r.latitude,
            area_hectares=area_hectares)
        region, redion_created = Region.objects.get_or_create(name=r.region)
        iso, iso_created = Iso.objects.get_or_create(name=r.iso)
        category, category_created = Category.objects.get_or_create(
            name=r.category)

        try:
            year = int(r.year)
        except:
            year = None

        site, site_created = Site.objects.get_or_create(
            name=r.name,
            year=r.year,
            description=r.description,
            justification=r.justification,
            category=category,
            state=state,
            region=region, iso=iso)
        site.save()

        # p, created = Person.objects.get_or_create(email=row[0])
        # c, created = Course.objects.get_or_create(title=row[2])

        # r = Membership.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Membership(role=r, person=p, course=c)
        # m.save()
