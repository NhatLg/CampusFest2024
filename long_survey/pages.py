from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils import translation

class TransMixin:
    def get_context_data(self, **context):
        user_language = self.session.config.get('language', 'en')
        translation.activate(user_language)
        return super().get_context_data(**context)

class _1_WelcomePage(TransMixin, Page):
    pass

class _2_CampusFestPage(TransMixin, Page):
    form_model = 'player'
    form_fields = ["num_campfest"]

    def is_displayed(player):
        return player.treatment_num == 1 or player.treatment_num == 2 # Treatment A

class _2_SlaveryPage(TransMixin, Page):
    form_model = 'player'
    form_fields = ["children_percent"]
    def is_displayed(player):
        return player.treatment_num == 3 or player.treatment_num == 4 # Treatment C

class _3_ResultPage(TransMixin, Page):
    pass

class _4_DonateTask(TransMixin, Page):
    form_model = 'player'
    form_fields = ["donate_amount", "filled_code"]
    def is_displayed(player):
        return player.treatment_num == 1 or player.treatment_num == 3  # Treatment A1, C1

class _4_NoDonateTask(TransMixin, Page):
    form_model = 'player'
    form_fields = ["filled_code"]
    def is_displayed(player):
        return player.treatment_num == 2 or player.treatment_num == 4  # Treatment A2, C2

class _5_SurveyDonateAfter(TransMixin, Page):
    form_model = 'player'
    form_fields = ["donate2_amount", "know_amnesty", "meaningful_work", "gender", "birth_year", "uni_relation", "donate_other"]
    def is_displayed(player):
        return player.treatment_num == 2 or player.treatment_num == 4  # Treatment A2, C2

class _5_SurveyNoDonate(TransMixin, Page):
    form_model = 'player'
    form_fields = ["know_amnesty", "meaningful_work", "gender", "birth_year", "uni_relation", "donate_other"]
    def is_displayed(player):
        return player.treatment_num == 1 or player.treatment_num == 3  # Treatment A1, C1

class _6_SurveyEmo(TransMixin, Page):
    form_model = 'player'
    form_fields = ["emo_frustration", "emo_satisfaction", "emo_guilt", "emo_curiosity",
                   "emo_stress", "emo_enjoyment", "emo_boredom", "open_ended"]

class ResultsWaitPage(TransMixin, WaitPage):
    pass


class Results(TransMixin, Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
