from os import environ

SESSION_CONFIGS = [
    dict(
       name='campus_fest_survey_en',
       display_name="Campus Fest Survey EN",
       num_demo_participants=5,
       app_sequence=['long_survey'],
       language='en'
    ),
    dict(
        name='campus_fest_survey_de',
        display_name="Campus Fest Survey DE",
        num_demo_participants=5,
        app_sequence=['long_survey'],
        language='de'
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

LANGUAGE_SESSION_KEY = '_language'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'vazfjgc-btf(1_ab4q9spn+82)h@yc18j2=k)uu^use@t3f^(8'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
