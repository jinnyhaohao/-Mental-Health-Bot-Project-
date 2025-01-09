from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self, model_name="j-hartmann/emotion-english-distilroberta-base"):
        """
        Initializes the sentiment analyzer with a pre-trained emotion model.
        初始化情绪分析器，加载预训练的情绪分类模型。
        :param model_name: The name of the pre-trained model. 预训练模型的名称。
        """
        self.analyzer = pipeline("text-classification", model=model_name)

    def analyze(self, text):
        """
        Analyzes the emotion of the given text.
        分析给定文本的情绪。
        :param text: The text to analyze. 需要分析的文本。
        :return: The inferred emotion label (e.g., joy, sadness, anger).
                 返回推断的情绪标签（例如：喜悦、悲伤、愤怒）。
        """
        try:
            result = self.analyzer(text)
            # Return the label with the highest score
            return result[0]['label']
        except Exception as e:
            print(f"Error during emotion analysis: {e}")
            print(f"情绪分析过程中出错: {e}")
            return "Unknown"
