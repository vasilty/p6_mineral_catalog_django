import json

from peewee import *


DATABASE = SqliteDatabase('minerals.db')


class Mineral(Model):
    name = CharField(max_length=255)
    image_filename = CharField(max_length=255, null=True)
    image_caption = CharField(max_length=255, null=True)
    category = CharField(max_length=255, null=True)
    formula = CharField(max_length=255, null=True)
    strunz_classification = CharField(max_length=255, null=True)
    crystal_system = CharField(max_length=255, null=True)
    unit_cell = CharField(max_length=255, null=True)
    color = CharField(max_length=255, null=True)
    crystal_symmetry = CharField(max_length=255, null=True)
    cleavage = CharField(max_length=255, null=True)
    mohs_scale_hardness = CharField(max_length=255, null=True)
    luster = CharField(max_length=255, null=True)
    streak = CharField(max_length=255, null=True)
    diaphaneity = CharField(max_length=255, null=True)
    optical_properties = CharField(max_length=255, null=True)
    refractive_index = CharField(max_length=255, null=True)
    crystal_habit = CharField(max_length=255, null=True)
    specific_gravity = CharField(max_length=255, null=True)

    class Meta:
        database = DATABASE
        db_table = 'minerals_mineral'


def initialize():
    """Create the database and the table if they don't exist."""
    DATABASE.connect()
    DATABASE.create_tables([Mineral], safe=True)


def get_mineral_data(mineral):
    """Creates the dictionary with all possible fields for a mineral."""
    full_mineral_dict = {
        'name': None,
        'image filename': None,
        'image caption': None,
        'category': None,
        'formula': None,
        'strunz classification': None,
        'crystal system': None,
        'unit cell': None,
        'color': None,
        'crystal symmetry': None,
        'cleavage': None,
        'mohs scale hardness': None,
        'luster': None,
        'streak': None,
        'diaphaneity': None,
        'optical properties': None,
        'refractive index': None,
        'crystal habit': None,
        'specific gravity': None
    }
    for key, value in mineral.items():
        full_mineral_dict[key] = value
    return full_mineral_dict


def json_to_db():
    """Constructs a mineral model instance for each mineral ia n json file and
    saves them to a database"""
    with open('minerals.json') as jsonfile:
        minerals = json.load(jsonfile)
        for mineral in minerals:
            data = get_mineral_data(mineral=mineral)
            Mineral.create(
                name=data['name'],
                image_filename=data['image filename'],
                image_caption=data['image caption'],
                category=data['category'],
                formula=data['formula'],
                strunz_classification=data['strunz classification'],
                crystal_system=data['crystal system'],
                unit_cell=data['unit cell'],
                color=data['color'],
                crystal_symmetry=data['crystal symmetry'],
                cleavage=data['cleavage'],
                mohs_scale_hardness=data['mohs scale hardness'],
                luster=data['luster'],
                streak=data['streak'],
                diaphaneity=data['diaphaneity'],
                optical_properties=data['optical properties'],
                refractive_index=data['refractive index'],
                crystal_habit=data['crystal habit'],
                specific_gravity=data['specific gravity']
            )


if __name__ == '__main__':
    initialize()
    json_to_db()
