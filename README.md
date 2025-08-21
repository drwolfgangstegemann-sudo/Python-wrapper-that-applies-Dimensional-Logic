# Dimensional Rational Wrapper

This repository provides a **Python wrapper** that applies **Dimensional Logic** (σ₂: systematic derivation, μ₃: reflexivity, κ₄: contextual coherence) to language model outputs.  
The goal is to enhance **rationality, cooperation, and stability** in AI-generated text.

## ✨ Core Idea
Instead of treating each AI output in isolation, the wrapper evaluates multiple candidate responses and selects the one that maximizes **epistemic rationality**:
- **σ₂ (Systematic Derivation):** Ensures logical consistency across the output.
- **μ₃ (Reflexivity):** Models recursive reasoning (considering the rationality of others).
- **κ₄ (Contextual Coherence):** Aligns answers with social, cultural, or conversational context.

This approach extends classical rational choice theory and introduces a dimensional framework for AI reasoning.

## 🚀 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Dimensional-Rational-Wrapper.git
   cd Dimensional-Rational-Wrapper
   ```

2. Place your language model outputs (e.g., from OpenAI, HuggingFace, etc.) into a list of candidate strings.

3. Run the wrapper:
   ```python
   from dim_rational_wrapper import choose_best_response

   candidates = [
       "I refuse to cooperate.",
       "Let’s find a win-win solution.",
       "This is not my responsibility."
   ]

   best = choose_best_response(candidates)
   print("Selected response:", best)
   ```

   Output:
   ```
   Selected response: Let’s find a win-win solution.
   ```

## 📚 Applications
- Game theory simulations (e.g., Prisoner’s Dilemma with cooperation as rational outcome).
- Dialogue systems that require **trust, cooperation, and reflexivity**.
- AI alignment research: making model outputs more consistent and context-sensitive.

## 🔬 Background
The wrapper is based on **Dimensional Logic**, a framework developed by Wolfgang Stegemann.  
It introduces epistemic operators to model rationality beyond classical logic and game theory.  
For more details, see related publications and the [Zenodo project](https://zenodo.org/).

## 🛠️ Next Steps
- Extend the scoring functions with empirical weights (α, β).
- Integrate with HuggingFace transformers for large-scale experiments.
- Explore multi-agent simulations using this wrapper.

## 📄 License
MIT License — free to use, modify, and share.
