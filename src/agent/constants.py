from pydantic import BaseModel, Field
from typing import List, Union

"""Set of constants."""
DEFAULT_CANDIDATE_COUNT = 1
DEFAULT_TEMPERATURE = 1.
DEFAULT_TOP_K = 20
DEFAULT_TOP_P = 0.8
DEFAULT_NUM_OUTPUTS = 5096  # tokens

FOCUSED_CRITERIA = """
Criteria:
1. Brand Logos: Identify any brand logos mentioned in the description or OCR results.
2. Products: Mention any products such as beer kegs and bottles.
3. Customers: Describe the number of customers, their activities, and emotions.
4. Promotional Materials: Identify any posters, banners, and billboards.
5. Setup Context: Determine the scene context (e.g., bar, restaurant, grocery store, or supermarket).
"""

# Define your schema
class DetectedObject(BaseModel):
    object: str=Field(description="The name of the detected objected")
    count: int=Field(description="Detect the number of objects in the image.")
    bbox: Union[List[int], None]=Field(description="The information about the bouding box of the detected object.")