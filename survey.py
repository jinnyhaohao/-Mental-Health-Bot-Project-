class Survey:
    def __init__(self, title, sentiment_analyzer):
        """
        Initializes the Survey with a title, empty questions, responses, and a sentiment analyzer.
        初始化问卷调查，包括标题、空的问题列表、响应数据和情绪分析器。
        :param title: The title of the survey. 问卷调查的标题。
        :param sentiment_analyzer: An instance of SentimentAnalyzer. 情绪分析器的实例。
        """
        self.title = title
        self.questions = []
        self.responses = {}
        self.sentiment_analyzer = sentiment_analyzer

    def add_question(self, question):
        """
        Adds a question to the survey.
        向问卷调查中添加一个问题。
        :param question: The question to add. 要添加的问题。
        """
        if question not in self.questions:
            self.questions.append(question)
            self.responses[question] = []
        else:
            print(f"The question '{question}' already exists in the survey.")
            print(f"问题 '{question}' 已经存在于问卷中。")

    def collect_response(self, question, response):
        """
        Collects a response for a specific question.
        收集用户对特定问题的回答。
        :param question: The question being answered. 用户回答的问题。
        :param response: The response to the question. 用户的回答内容。
        """
        if question in self.questions:
            self.responses[question].append(response)
        else:
            print(f"The question '{question}' is not in the survey.")
            print(f"问题 '{question}' 不在问卷中。")

    def get_user_mood(self):
        """
        Analyzes all user responses and provides a summary of moods.
        分析所有用户的回答，并提供情绪摘要。
        :return: A dictionary with questions and their corresponding moods.
                 包含问题及其对应情绪的字典。
        """
        moods = {}
        for question, responses in self.responses.items():
            if responses:
                analyzed_moods = [self.sentiment_analyzer.analyze(resp) for resp in responses]
                moods[question] = analyzed_moods
            else:
                moods[question] = "No responses yet."
                moods[question] = "暂无回答。"
        return moods

if __name__ == "__main__":
    # Initialize the sentiment analyzer 初始化情绪分析器
    sentiment_analyzer = SentimentAnalyzer()

    # Create a survey with the sentiment analyzer 创建带有情绪分析器的问卷调查
    survey = Survey("AI-Powered Mood Tracker Survey", sentiment_analyzer)

    # Add questions 添加问题
    survey.add_question("How are you feeling today? 今天你的心情如何？")
    survey.add_question("What has been on your mind recently? 最近你在想些什么？")

    # Collect responses 收集回答
    survey.collect_response("How are you feeling today?", "I'm feeling great and optimistic about the future!")
    survey.collect_response("What has been on your mind recently?", "I'm worried about upcoming deadlines.")
    
    # Get and display moods 获取并显示用户情绪
    moods = survey.get_user_mood()
    print("\nUser Mood Analysis 用户情绪分析:")
    for question, mood in moods.items():
        print(f"{question}: {mood}")
