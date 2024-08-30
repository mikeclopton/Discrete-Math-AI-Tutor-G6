from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# Prompt template for the Tutor Agent
template = """
You are a math tutor. Solve the following math problem: {problem}
"""

# Chain using the new ChatOpenAI interface
llm = ChatOpenAI(temperature=0, model_name="gpt-4")
prompt = PromptTemplate(template=template, input_variables=["problem"])
tutor_chain = LLMChain(llm=llm, prompt=prompt)

# Sample problem
problem = "2x + 3 = 7"

# Running the chain
result = tutor_chain.run({"problem": problem})
print("Solution:", result)

# Prompt template for the Math Validator Agent
validation_template = """
You are a math validator. Verify if the solution to the following problem is correct.
Problem: {problem} 
Solution: {solution}
"""

validation_prompt = PromptTemplate(template=validation_template, input_variables=["problem", "solution"])
validation_chain = LLMChain(llm=llm, prompt=validation_prompt)

# Function to validate the solution
def validate_solution(problem, solution):
    validation_result = validation_chain.run({"problem": problem, "solution": solution})
    return validation_result

validation_feedback = validate_solution(problem, result)
print("Validation Feedback:", validation_feedback)
