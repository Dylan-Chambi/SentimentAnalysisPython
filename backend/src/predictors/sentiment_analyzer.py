from transformers import AutoTokenizer, AutoConfig, AutoModelForSequenceClassification
from src.utils.functions import sentiment_selector
from src.predictors.general_analyzer import GeneralAnalyzer
from src.config.config import get_settings

SETTINGS = get_settings()

class SentimentAnalyzer(GeneralAnalyzer):
    def __init__(self):
        self.config = AutoConfig.from_pretrained(SETTINGS.sentiment_model)
        self.model = AutoModelForSequenceClassification.from_pretrained(SETTINGS.sentiment_model, config=self.config)
        self.tokenizer = AutoTokenizer.from_pretrained(SETTINGS.sentiment_model)
        super().__init__(model_name=SETTINGS.sentiment_model)

    def predict(self, text) -> list:
        tokens = self.tokenizer(text, return_tensors="pt", padding=True)
        logits = self.model(**tokens).logits

        probabilidades = logits.softmax(dim=1).tolist()[0]

        return [
            {"label": key, "score": probabilidades[value]}
            for key, value in self.model.config.label2id.items()
        ]

    def analyze_sentiment(self, text) -> tuple:

        prediction = self.predict(text)
        
        positive_index = next((i for i, item in enumerate(prediction) if item['label'] == 'positive'), None)
        negative_index = next((i for i, item in enumerate(prediction) if item['label'] == 'negative'), None)

        positive_score = prediction[positive_index]["score"]
        negative_score = prediction[negative_index]["score"]

        sentiment_score = positive_score - negative_score

        sentiment_category = sentiment_selector(sentiment_score)

        return sentiment_category, sentiment_score

