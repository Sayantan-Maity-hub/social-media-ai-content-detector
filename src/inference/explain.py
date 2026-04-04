from typing import List

def generate_reasons(
        artifact_score: float,
        hyperrealism_score: float,
        text_score: float,
) -> list[str]: # Generate a list of reasons based on the scores of artifact, hyperrealism, and text.
    reason = []

    if artifact_score > 0.7:
        reason.append("Image contains visual patterns or inconsistencies commonly associated with synthetic genration.")
    elif artifact_score >= 0.5:
        reason.append("Image show moderate visual inregularities that may indicate generated content.")
    if hyperrealism_score > 0.7:
        reason.append("Detected unusually symmetic and idealized features characteristics consistent with hyperrealistic AI faces.")
    elif hyperrealism_score >= 0.5:
        reason.append("Facial structure appears unusually balanced and smooth compared with typical camera-captured portraits.")
    if text_score > 0.7:
        reason.append("captions language resembles templated or AI-generated phrasing.")
    elif text_score >= 0.5:
        reason.append("captions language shows some signs of being AI-generated, such as lack of personal details or overly generic descriptions.")
    if not reason:
        reason.append("No strong indicators of AI generation detected basesd on the current scores, but this does not guarantee the content is human-genrrated.")
    
    return reason  

    