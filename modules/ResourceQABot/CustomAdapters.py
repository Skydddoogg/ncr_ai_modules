from chatterbot.logic import LogicAdapter

class GoogleSearchAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'search' and 'for'.
        """
        words = ['search', 'for']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        from googlesearch import search

        search_keyword = input_statement.text.split('search for')[1]

        top_results = search(search_keyword, stop=5)
        count = 1
        for url in top_results:
            print(str(count) + '.', url)
            count += 1

        confidence = 1

        response_statement = Statement(text='Here is the top five results for {0}'.format(search_keyword))
        response_statement.confidence = confidence
        return response_statement

