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

        state, state_created = State.objects.get_or_create(name=r.state)
        region, redion_created = Region.objects.get_or_create(name=r.region)
        iso, iso_created = Iso.objects.get_or_create(name=r.iso)
        category, category_created = Category.objects.get_or_create(
            name=r.category)

        try:
            year = int(r.year)
        except:
            year = None

        try:
            area_hectares = float(r.area_hectares)
        except:
            area_hectares = None

        print(year, area_hectares)

        site, site_created = Site.objects.get_or_create(
            name=r.name,
            year=year,
            description=r.description,
            justification=r.justification,
            longitude=r.longitude,
            latitude=r.latitude,
            area_hectares=area_hectares,
            category=category,  # one to many
            state=state,  # one to many
            region=region,  # one to many
            iso=iso)  # one to many

        site.save()
