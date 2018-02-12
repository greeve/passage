# Reference category choices
SCRIPTURE = 'S'
HYMN = 'H'
CONFERENCE = 'C'
CATEGORY_CHOICES = (
    (SCRIPTURE, 'Scripture'),
    (HYMN, 'Hymn'),
    (CONFERENCE, 'Conference Address'),
)

# Reference scripture choices
OT = 'ot'
NT = 'nt'
BOM = 'bom'
DC = 'dc'
PGP = 'pgp'
VOLUME_CHOICES = (
    (OT, 'Old Testament'),
    (NT, 'New Testament'),
    (BOM, 'Book of Mormon'),
    (DC, 'Doctrine and Covenants'),
    (PGP, 'Pearl of Great Price'),
)

# Reference conference choices
APRIL = 4
OCTOBER = 10
MONTH_CHOICES = (
    (APRIL, 'April'),
    (OCTOBER, 'October'),
)

SAT_AM = 'sat-am'
SAT_PM = 'sat-pm'
SAT_PR = 'sat-pr'
SAT_WO = 'sat-wo'
SUN_AM = 'sun-am'
SUN_PM = 'sun-pm'
SESSION_CHOICES = (
    (SAT_AM, 'Saturday Morning'),
    (SAT_PM, 'Saturday Afternoon'),
    (SAT_PR, 'General Priesthood'),
    (SAT_WO, 'General Womens'),
    (SUN_AM, 'Sunday Morning'),
    (SUN_PM, 'Sunday Afternoon'),
)
