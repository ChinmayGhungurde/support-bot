from utils.generate_dataframe import generate_dataframe

# Utility class for sequential prompt chain
class SeqPrompt:

    @staticmethod
    def get_template():
        reviews_df = generate_dataframe()
        reviews = '\n\n'.join([f'Review: {row.content}\nSentiment: {row.score}' for _, row in reviews_df.iterrows()])

        inference_slice = "Here is a review to perform the operations on: '{review}'"

        return f""" 
        You are a sentiment analysis chatbot. Your job is to read and analyze the sentiment of a user review and reply in a polite manner.
        You'll be given a series of app reviews for a streaming platform application along with their respective sentiment scores in the following format under the ('''):

        '''
        Review: <the review text>
        Sentiment: <the sentiment score from 1 to 5. 1 being the most negative possible sentiment, 5 being the most positive sentiment and 3 being neutral sentiment>
        '''

        This will be your knowledge base context (or training data) for an upcoming task. You'll have to keep this in mind. NOTE: Some reviews may have a positive sounding text (e.g: "The app crashed wonderfully"), but observe that this is obviously sarcasm,
        since the user said that the app crashed which is a negative occurence. Also such reviews will most likely be accompanied by negative sentiment (score less than 3), these sarcastic comments should be classified as negative, irrespective of what they say.

        Here are the training reviews for you, under the ('''):

        '''
        {reviews}
        '''

        Now here is the task. Based on the context provided before, you'll be given a review in the following format:

        '''
        Review: <the review text>
        '''
        Your task is this: You have to return the output as given below
        This entire response should be output in the following format:

        '''
        Sentiment: <The sentiment score of the review (from -1 i.e most negative to +1 i.e most positive and 0 being neutral. The score should be in floating range between -1 to +1 to indicate the strength of the sentiment))>
        Category: <If the sentiment is negative (less than 0), only then identify and return the category of the service in the review text which the user did not like or was offended by. The classes can be one or more out of the following: Customer Service, Streaming performance & Quality, App performance, Content Objection, Security Problem, Account Problem.
        Only when no category is found in the review, simply return "NA">
        Reply: <If the sentiment is negative (less than 0), only then write a brief polite and personalized reply tailored to the user's review, stating that the team has received the review and acknowledged it, you are supposed to be politically, culturally and socially neutral at all times and handle these reviews diplomatically.
        Remember that we are a streaming platform, we do not create the content for streaming though. The content is not out responsibility.
        The reply should be in the format like this: "\n\nDear User,\n\n<content of the reply>\n\nThanks for your patience, Support Team" and it should be around 300 words.>
        '''

        {inference_slice}
        """
