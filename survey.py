class Survey:
    def __init__(self, title):
        """
        Initializes the Survey with a title, empty questions, and responses.
        """
        self.title = title
        self.questions = []
        self.responses = {}

    def add_question(self, question):
        """
        Adds a new question to the survey.
        
        :param question: The question to add.
        """
        if question not in self.questions:
            self.questions.append(question)
            self.responses[question] = []
        else:
            print(f"The question '{question}' already exists in the survey.")

    def collect_response(self, question, response):
        """
        Collects a response for a specific question.
        :param question: The question being answered.
        :param response: The response to the question.
        """
        if question in self.questions:
            self.responses[question].append(response)
        else:
            print(f"The question '{question}' is not in the survey.")

    def get_summary(self):
        """
        Returns a summary of the survey responses.
        :return: A dictionary with questions and their corresponding responses.
        """
        summary = {question: len(responses) for question, responses in self.responses.items()}
        return summary

    def display_questions(self):
        """
        Displays all the questions in the survey.
        """
        print(f"Survey Title: {self.title}")
        print("Questions:")
        for i, question in enumerate(self.questions, start=1):
            print(f"{i}. {question}")

# Example Usage
if __name__ == "__main__":
    survey = Survey("Customer Feedback Survey")
    
    # Add questions
    survey.add_question("How satisfied are you with our service?")
    survey.add_question("Would you recommend our service to others?")
    
    # Collect responses
    survey.collect_response("How satisfied are you with our service?", "Very satisfied")
    survey.collect_response("Would you recommend our service to others?", "Yes")
    survey.collect_response("Would you recommend our service to others?", "No")
    
    # Display questions
    survey.display_questions()
    
    # Display summary
    summary = survey.get_summary()
    print("\nSurvey Summary:")
    for question, count in summary.items():
        print(f"{question}: {count} responses")
