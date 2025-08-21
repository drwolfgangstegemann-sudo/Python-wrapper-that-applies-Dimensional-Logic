import random

class DimensionalRationalWrapper:
    def __init__(self, alpha=1.0, beta=1.0):
        self.alpha = alpha
        self.beta = beta

    def evaluate_candidates(self, candidates, context_factor=1.0):
        """
        Evaluate multiple candidate outputs from a language model using
        Dimensional Logic operators: reflexivity (μ₃) and contextual coherence (κ₄).

        Args:
            candidates (list[str]): Generated text options from an LLM.
            context_factor (float): A contextual weight factor (κ₄).

        Returns:
            str: The best candidate according to dimensional evaluation.
        """
        scored = []
        for c in candidates:
            # Reflexivity μ₃: reward internal coherence (e.g., length balance)
            reflexive_score = 1.0 / (1.0 + abs(len(c) - 50) / 50.0)
            # Contextual coherence κ₄: weight external context
            context_score = context_factor * random.uniform(0.8, 1.2)
            total_score = self.alpha * reflexive_score + self.beta * context_score
            scored.append((total_score, c))

        # Return best candidate
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[0][1]

# Example usage
if __name__ == "__main__":
    wrapper = DimensionalRationalWrapper(alpha=1.2, beta=1.0)
    outputs = [
        "Let's cooperate to achieve the best outcome.",
        "I will defect because it maximizes my gain.",
        "Perhaps we can find a middle ground to coordinate."
    ]
    best = wrapper.evaluate_candidates(outputs, context_factor=1.1)
    print("Best candidate:", best)
