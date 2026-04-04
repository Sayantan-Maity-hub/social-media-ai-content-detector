from typing import Dict

def clamp_score(score: float) -> float: # Ensure the score is between 0 and 1.
    return max(0.0, min(1.0, score))

def get_risk_labels(score: float) -> str: # Determine AI generated content risk lavel based on the score.
    if score < 0.35:
        return "likely human"
    if score < 0.65:
        return "possibly AI-generated"
    return "likely AI-generated"

def fuse_scores(
        artifact_score: float,
        hyperrealism_score: float,
        text_score: float,
        artifact_weight: float = 0.45,
        hyperrealism_weight: float = 0.25,
        text_weight: float = 0.35
) -> Dict[str, float | str]: # combine the score of artifact, hyperrealism, and text to get a final AI probablity. All score should be between 0 and 1.
    artifact_score = clamp_score(artifact_score)
    hyperrealism_score = clamp_score(hyperrealism_score)
    text_score = clamp_score(text_score)

    total_weight = artifact_weight + hyperrealism_weight + text_weight

    if total_weight <=0:
        raise ValueError("Total fusion weight must be greater than zero")

    final_score = (artifact_score * artifact_weight + hyperrealism_score * hyperrealism_weight + text_score * text_weight) / total_weight
    final_score = clamp_score(final_score)
    human_score = clamp_score(1.0 - final_score)

    return {
        "final_score": round(final_score, 2),
        "human_score": round(human_score, 2),
        "risk_label": get_risk_labels(final_score),
        "artifact_score": round(artifact_score, 4),
        "hyperrealism_score": round(hyperrealism_score, 4),
        "text_score": round(text_score, 4)
    }

    
    