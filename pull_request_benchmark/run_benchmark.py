import llms
from evaluations_collection import *

def initialize_llm(api_key, model='gpt-4'):
    """
    Initializes and returns a language model instance using PyLLMs.
    """
    return llms.init(api_key=api_key, model=model)

def calculate_score_for_sample(review_outcome, rejection_reason, response_text):
    score = 0
    predicted_outcome_correct = review_outcome.strip().lower() in response_text.strip().lower()
    predicted_rejection_correct = review_outcome.strip().lower() == 'rejected' and rejection_reason is not None and rejection_reason.strip().lower() in response_text.strip().lower()

    # Reward for correct outcome prediction
    if predicted_outcome_correct:
        score += 5  # Correct outcome prediction
        if predicted_rejection_correct:
            score += 1  # Correct rejection reason
    else:
        # Penalty for incorrect outcome prediction
        score -= 2  # Apply a penalty for incorrect prediction

    return score

def evaluate_model_with_scoring(model, evaluation_samples):
    """
    Sends evaluation prompts to the LLM and scores responses based on correct review outcomes and rejection reasons.
    """
    total_score = 0
    for sample in evaluation_samples:
        prompt = sample.get_prompt()
        response = model.complete(prompt)
        review_outcome = sample.review_outcome # This contains 'approved' or 'rejected'
        rejection_reason = sample.rejection_reason if 'rejection_reason' in sample else None # Assuming this field exists for rejected PRs
        
        # Calculate the score for the current sample
        sample_score = calculate_score_for_sample(review_outcome, rejection_reason, response.text)
        total_score += sample_score
    
    # Calculate the final average score
    final_score = total_score / len(evaluation_samples)
    return final_score

def main():
    # Load your pull request evaluation entries
    evaluation_samples = load_evaluation_samples()
    
    # Initialize your preferred LLM
    model = initialize_llm('your_api_key_here', 'gpt-4')
    
    # Evaluate the model
    success_rate = evaluate_model_with_scoring(model, evaluation_samples)
    
    # Output the benchmark results
    print(f"Model success rate: {success_rate}%")

if __name__ == "__main__":
    main()