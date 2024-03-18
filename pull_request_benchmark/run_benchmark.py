import llms
from evaluations_collection import load_evaluation_samples

def initialize_llm(api_key, model='gpt-4'):
    """
    Initializes and returns a language model instance using PyLLMs.
    """
    return llms.init(api_key=api_key, model=model)

def evaluate_model(model, evaluation_samples):
    """
    Sends evaluation prompts to the LLM and checks if responses contain the specified review outcomes.
    """
    correct_responses = 0
    for sample in evaluation_samples:
        prompt = sample.get_prompt()
        response = model.complete(prompt)
        review_outcome = sample.review_outcome # Adjusted to access the review_outcome field
        # Check if the review_outcome is contained within the response
        if review_outcome.strip().lower() in response.text.strip().lower():
            correct_responses += 1
    
    success_rate = correct_responses / len(evaluation_samples) * 100
    return success_rate

def main():
    # Load your pull request evaluation entries
    evaluation_samples = load_evaluation_samples()
    
    # Initialize your preferred LLM
    model = initialize_llm('your_api_key_here', 'gpt-4')
    
    # Evaluate the model
    success_rate = evaluate_model(model, evaluation_samples)
    
    # Output the benchmark results
    print(f"Model success rate: {success_rate}%")

if __name__ == "__main__":
    main()