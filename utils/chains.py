from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.llms import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

class ChainUtility:

    def __init__(self, input_variables, temperature=0):
        self.input_variables = input_variables
        self.temperature = temperature

    def get_chain(self, template, output_key):
        llm = AzureOpenAI(temperature=self.temperature, deployment_name="davinci")
        prompt = ChatPromptTemplate.from_template(template)
        chain = LLMChain(llm=llm, prompt=prompt, output_key=output_key)
        return chain
    
    # def get_overall_chain(self, chains, output_variables):
    #     overall_chain = SequentialChain(
    #         chains=chains, 
    #         input_variables=self.input_variables,
    #         output_variables=output_variables,
    #         verbose=True
    #     )
    #     return overall_chain
    
    @staticmethod
    def print_completion(chain, start):
        resp = chain(start)
        print(resp['response'])