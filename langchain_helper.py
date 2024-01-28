from new_secret_key import huggingface_key1
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = huggingface_key1
llm = HuggingFaceHub(repo_id = "google/flan-t5-xxl", model_kwargs = {'temperature':0.7})

def get_rest_name(cuisine):

    prompt_template_name = PromptTemplate(
                            input_variables=['cuisine'],
                            template="I am planning to open a restaurant with {cuisine} food. Give me a good fancy name for my new restaurant"
    )

    promt_template_menu = PromptTemplate(
                            input_variables=['restaurant_name'],
                            template="Give me 6 good menu names for my {restaurant_name}. Return it as comma separated list"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key='restaurant_name')
    menu_chain = LLMChain(llm=llm, prompt=promt_template_menu,output_key='menu_items')

    new_chain = SequentialChain(chains=[name_chain, menu_chain],
                                input_variables=['cuisine'],
                                output_variables=['restaurant_name','menu_items'])
    
    response = new_chain({'cuisine':cuisine})

    return response

if __name__ == "__main__":
    print(get_rest_name("Italian"))






   