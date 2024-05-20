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
    form_model = 'player'
    form_fields = ["treatment_num"]

class _2_CampusFestPage(TransMixin, Page):
    form_model = 'player'
    form_fields = ["num_campfest"]

    def is_displayed(self):
        return self.player.treatment_num == 1 or self.player.treatment_num == 2 # Treatment A

class _2_SlaveryPage(TransMixin, Page):
    form_model = 'player'
    form_fields = ["children_percent"]
    def is_displayed(self):
        return self.player.treatment_num == 3 or self.player.treatment_num == 4 # Treatment C

class _3_ResultPage(TransMixin, Page):
    
    def vars_for_template(self):
        return dict(
            is_treatment_A = (self.player.treatment_num == 1) or (self.player.treatment_num == 2),
            is_treatment_C = (self.player.treatment_num == 3) or (self.player.treatment_num == 4),
            is_correct_answer_slavery = self.player.children_percent == 12, 
            is_correct_answer_fest = self.player.num_campfest == 6,
        )

class _4_DonateTask(TransMixin, Page):
    form_model = 'player'
    form_fields = ["donate_amount", "filled_code"]
    def is_displayed(self):
        return self.player.treatment_num == 1 or self.player.treatment_num == 3  # Treatment A1, C1

class _4_NoDonateTask(TransMixin, Page):
    form_model = 'player'
    form_fields = ["filled_code"]
    def is_displayed(self):
        return self.player.treatment_num == 2 or self.player.treatment_num == 4  # Treatment A2, C2

class _5_SurveyDonateAfter(TransMixin, Page):
    form_model = 'player'
    form_fields = ["donate2_amount", "know_amnesty", "meaningful_work", "gender", "birth_year", "uni_relation", "donate_other"]
    def is_displayed(self):
        return self.player.treatment_num == 2 or self.player.treatment_num == 4  # Treatment A2, C2

class _5_SurveyNoDonate(TransMixin, Page):
    form_model = 'player'
    form_fields = ["know_amnesty", "meaningful_work", "gender", "birth_year", "uni_relation", "donate_other"]
    def is_displayed(self):
        return self.player.treatment_num == 1 or self.player.treatment_num == 3  # Treatment A1, C1

class _6_SurveyEmo(TransMixin, Page):
    form_model = 'player'
    form_fields = ["emo_frustration", "emo_satisfaction", "emo_guilt", "emo_curiosity",
                   "emo_stress", "emo_enjoyment", "emo_boredom", "open_ended"]

class _7_Thankyou(TransMixin, Page):
    pass

class ResultsWaitPage(TransMixin, WaitPage):
    pass



page_sequence = [_1_WelcomePage, _2_CampusFestPage, _2_SlaveryPage,
                 _3_ResultPage, _4_DonateTask, _4_NoDonateTask,
                 _5_SurveyDonateAfter, _5_SurveyNoDonate, ]
# 
#                   _6_SurveyEmo, _7_Thankyou