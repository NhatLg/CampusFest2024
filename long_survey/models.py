from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from django.utils.translation import ugettext_lazy as _

author = 'Nhat Luong'

doc = """
Just a quick and dirty Otree Experiment For Campus Fest 2024 at Uni Kassel
"""


class Constants(BaseConstants):
    name_in_url = 'long_survey'
    players_per_group = None
    num_rounds = 1
    EMO = ["emo_frustration","emo_satisfaction","emo_guilt","emo_curiosity","emo_stress","emo_enjoyment","emo_boredom"]

class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment_num = models.IntegerField()
    num_campfest = models.IntegerField(
        label=_("Take a guest: Counting also today’s festival, how many Campus Fest have taken place "
                "since the inauguration of the University of Kassel in 1971?"),
        choices=[12, 6, 3],
        widget=widgets.RadioSelect)
    children_percent = models.FloatField(
        label = _("Take a guess: Of the documented global forced labor (modern slavery), what percentage are children?"),
        choices=[
            [3, "3%"],
            [0.9, "0.9%"],
            [12, "12%"]
        ],
        widget=widgets.RadioSelect
    )
    donate_amount = models.IntegerField(
        initial = 0,
        choices = [
            [0, "0€"],
            [1, "1€"],
            [2, "2€"],
            [3, "3€"],
            [4, "4€"],
            [5, "5€"],
        ],
        widget=widgets.RadioSelect
    )
    donate2_amount = models.IntegerField(
        label="",
        initial = 0,
        choices = [
            [0, "0€"],
            [1, "1€"],
            [2, "2€"],
            [3, "3€"],
            [4, "4€"],
            [5, "5€"],
        ],
        widget = widgets.RadioSelect
    )
    filled_code = models.StringField(
        label = _("Sit and play as soon as you see one of the tables with the game available. Once you are done, ask the experimenter for the code to fill in here to continue")
    )
    know_amnesty = models.IntegerField(
        label = _("Did you know Amnesty International from before?"),
        choices = [
            [1, _("Yes")],
            [2, _("No")],
            [3, _("I am not sure")]
        ],
        widget = widgets.RadioSelect
    )
    meaningful_work = models.IntegerField(
        label = _("How meaningful do you find their work on a scale from 1 (not at all) to 10 (very)?"),
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect
    )
    gender = models.IntegerField(
        label = _("With which gender do you identify?"),
        choices = [
            [1, "Female"],
            [2, "Male"],
            [3, "Other"],
            [4, "I prefer not to say."],
        ]
    )
    birth_year = models.IntegerField(
        label = _("Write you year of birth (i.e. 1998):"),
        min = 1904,
        max = 2008,
    )
    uni_relation = models.IntegerField(
        label = _("How do you relate to the university?"),
        choices = [
            [0, "I am a student."],
            [1, "I am a university employee."],
            [2, "I am a guest."]
        ]
    )
    donate_other = models.IntegerField(
        label = _("What do you think most people think is the appropriate amount to donate"),
        choices = [
            [0, "0€"],
            [1, "1€"],
            [2, "2€"],
            [3, "3€"],
            [4, "4€"],
            [5, "5€"],
        ]
    )
    emo_frustration = models.BooleanField(label= _("Frustration"), blank=True)
    emo_satisfaction = models.BooleanField(label= _("Satisfaction"), blank=True)
    emo_guilt = models.BooleanField(label= _("Guilt"), blank=True)
    emo_curiosity = models.BooleanField(label= _("Curiosity"), blank=True)
    emo_stress = models.BooleanField(label= _("Stress"), blank=True)
    emo_enjoyment = models.BooleanField(label= _("Enjoyment"), blank=True)
    emo_boredom = models.BooleanField(label= _("Boredom"), blank=True)

    open_ended = models.StringField(
        label = _("Open-ended question: Share with us any thoughts, feelings, or emotions about the experiment"),
        blank = True
    )
