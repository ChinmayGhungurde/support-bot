from utils.chains import ChainUtility
from utils.prompts import SeqPrompt

if __name__ == '__main__':

    chains = []
    output_variables = []
    input_variables = ['context']

    chain_utility = ChainUtility(input_variables=input_variables, temperature=0.4)

    template = SeqPrompt.get_template()
    llm_chain = chain_utility.get_chain(template=template, output_key='response')

    review = input("Enter your review: ")
    chain_utility.print_completion(llm_chain, start=review)

    # Create a chain for the training context
    # context_template = SeqPrompt.get_context_template()
    # output_key = 'context_response'
    # output_variables.append(output_key)
    # context_chain = chain_utility.get_chain(template=context_template, output_key=output_key)
    # chains.append(context_chain)

    # # Create a chain for the instruction prompt
    # instruction_template = SeqPrompt.get_instruction_template()
    # output_key = 'instruction_response'
    # output_variables.append(output_key)
    # instruction_chain = chain_utility.get_chain(template=instruction_template, output_key=output_key)
    # chains.append(instruction_chain)

    # # Create a chain for the inference chain
    # review = input('Enter the review: ')

    # inference_template = SeqPrompt.get_inference_template(review)
    # output_key = 'final_response'
    # output_variables.append(output_key)
    # inference_chain = chain_utility.get_chain(template=inference_template, output_key=output_key)
    # chains.append(inference_chain)

    # # Create the overall sequential chain
    # overall_chain = chain_utility.get_overall_chain(chains=chains, output_variables=output_variables)