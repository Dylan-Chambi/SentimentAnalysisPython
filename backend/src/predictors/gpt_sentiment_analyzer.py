from src.utils.functions import sentiment_selector
from src.predictors.general_analyzer import GeneralAnalyzer
from src.predictors.general_predictor import GeneralPredictor
from src.config.config import get_settings
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from src.utils.gpt_template import SENTIMENT_ANALYSIS_TEMPLATE, POS_TAGGING_TEMPLATE, NER_TEMPLATE
from src.schemas.sentiment_score import SentimentScore
from src.schemas.pos_tagging import PosTagging
from src.schemas.ner import NER

SETTINGS = get_settings()


class GPTPredictor(GeneralAnalyzer, GeneralPredictor):
    def __init__(self):
        super().__init__(model_name=SETTINGS.gpt_model)
        self.model = ChatOpenAI(model_name=SETTINGS.gpt_model, openai_api_key=SETTINGS.openai_key)
        self.embeddings_model = OpenAIEmbeddings(openai_api_key=SETTINGS.openai_key)


    def analyze_sentiment(self, text) -> tuple:

        out_parser = PydanticOutputParser(pydantic_object=SentimentScore)


        prompt_tpl = PromptTemplate(
            template=SENTIMENT_ANALYSIS_TEMPLATE,
            input_variables=["text_input"],
            partial_variables={"format_instructions": out_parser.get_format_instructions()}
        )

        llm_input = prompt_tpl.format(text_input=text)

        prediction = self.model.predict(llm_input, seed=42)

        sentiment_score = out_parser.parse(prediction)

        sentiment_category = sentiment_selector(sentiment_score.score)

        return sentiment_category, sentiment_score.score

    def analyze_text(self, text: str):

        pos_tagging_out_parser = PydanticOutputParser(pydantic_object=PosTagging)

        prompt_pos_tagging = PromptTemplate(
            template=POS_TAGGING_TEMPLATE,
            input_variables=["text_input"],
            partial_variables={"format_instructions": pos_tagging_out_parser.get_format_instructions()}
        )

        ner_out_parser = PydanticOutputParser(pydantic_object=NER)

        prompt_ner = PromptTemplate(
            template=NER_TEMPLATE,
            input_variables=["text_input"],
            partial_variables={"format_instructions": ner_out_parser.get_format_instructions()}
        )


        llm_input_pos_tagging = prompt_pos_tagging.format(text_input=text)
        llm_input_ner = prompt_ner.format(text_input=text)

        prediction_pos_tagging = self.model.predict(llm_input_pos_tagging)
        prediction_ner = self.model.predict(llm_input_ner)
        
        try:
            pos_tagging = pos_tagging_out_parser.parse(prediction_pos_tagging)
        except:
            pos_tagging = PosTagging(pos_tagging=[])
        
        try:
            ner = ner_out_parser.parse(prediction_ner)
        except:
            ner = NER(ner=[])

        embeddings = self.embeddings_model.embed_documents([text])[0]

        return pos_tagging.pos_tagging, ner.ner, embeddings
