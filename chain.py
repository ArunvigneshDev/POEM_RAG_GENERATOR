from model import create_chat_groq
import prompt

def generate_poem(topic):
    """ 
    Function to generate poem

    Args:
        topic (str) - topic of the poem
    
    Returns:
        Response string
    """

    prompt_template = prompt.poem_generator_prompt()
    llm = create_chat_groq()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic" : topic
    })
    return response.content