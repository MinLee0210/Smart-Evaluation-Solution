# Objects that we want to detect
PREDEFINED_CLASS = """
heineken_logo
tiger_logo
biaviet_logo
larue_logo
bivina_logo
edelweiss_logo
bialacviet_logo
strongbow_logo
biasaigon_logo

heineken_boxes
tiger_boxes
biaviet_boxes
larue_boxes
bivina_boxes
edelweiss_boxes
bialacviet_boxes
strongbow_boxes
biasaigon_boxes

heineken_poster
heineken_banner
heineken_billboard
heineken_table_tent
heineken_digital_screen
heineken_standee
tiger_poster
tiger_banner
tiger_billboard
tiger_table_tent
tiger_digital_screen
tiger_standee
biaviet_poster
biaviet_banner
biaviet_billboard
biaviet_table_tent
biaviet_digital_screen
biaviet_standee
larue_poster
larue_banner
larue_billboard
larue_table_tent
larue_digital_screen
larue_standee
bivina_poster
bivina_banner
bivina_billboard
bivina_table_tent
bivina_digital_screen
bivina_standee
edelweiss_poster
edelweiss_banner
edelweiss_billboard
edelweiss_table_tent
edelweiss_digital_screen
edelweiss_standee
bialacviet_poster
bialacviet_banner
bialacviet_billboard
bialacviet_table_tent
bialacviet_digital_screen
bialacviet_standee
strongbow_poster
strongbow_banner
strongbow_billboard
strongbow_table_tent
strongbow_digital_screen
strongbow_standee
biasaigon_poster
biasaigon_banner
biasaigon_billboard
biasaigon_table_tent
biasaigon_digital_screen
biasaigon_standee

heineken_beer_keg
heineken_beer_bottle
heineken_beer_can
heineken_special_edition_package
tiger_beer_keg
tiger_beer_bottle
tiger_beer_can
tiger_special_edition_package
biaviet_beer_keg
biaviet_beer_bottle
biaviet_beer_can
biaviet_special_edition_package
larue_beer_keg
larue_beer_bottle
larue_beer_can
larue_special_edition_package
bivina_beer_keg
bivina_beer_bottle
bivina_beer_can
bivina_special_edition_package
edelweiss_beer_keg
edelweiss_beer_bottle
edelweiss_beer_can
edelweiss_special_edition_package
bialacviet_beer_keg
bialacviet_beer_bottle
bialacviet_beer_can
bialacviet_special_edition_package
strongbow_beer_keg
strongbow_beer_bottle
strongbow_beer_can
strongbow_special_edition_package
biasaigon_beer_keg
biasaigon_beer_bottle
biasaigon_beer_can
biasaigon_special_edition_package

consumer
promoter
staff
customer_buying
customer_interacting
staff_restocking

bar
restaurant
grocery_store
supermarket
convenience_store
night_club
outdoor_venue
indoor_venue

qr_code
price_tag
inventory_shelf
vehicle_advertisement
ceiling_hanging
branding_placement_compliance
regulatory_compliance_sign
health_and_safety_signage
interior_view
exterior_view
counter_area
seating_area
entrance

consumer_group
consumer_solo
family_group
business_meeting
casual_dining
formal_event
"""

JSON_SAMPLES = """
[
  {
    "object": "heineken_logo",
    "count": 1,
    "bbox": [100, 50, 200, 150]
  },
  {
    "object": "tiger_beer_can",
    "count": 3,
    "bbox": [[50, 100, 100, 150], [150, 120, 200, 170], [220, 80, 270, 130]]
  },
  {
    "object": "promoter",
    "count": 2,
    "bbox": [[300, 200, 400, 300], [10, 350, 80, 450]]
  },
  {
    "object": "edelweiss_digital_screen",
    "count": 1,
    "bbox": [800, 100, 1000, 300]
  },
  {
    "object": "customer_buying",
    "count": 1,
    "bbox": [450, 250, 550, 350]
  },
  {
    "object": "heineken_poster",
    "count": 2,
    "bbox": [[600, 400, 800, 600], [100, 700, 300, 900]]
  },
  {
    "object": "tiger_banner",
    "count": 1,
    "bbox": [500, 10, 700, 200]
  },
  {
    "object": "biaviet_table_tent",
    "count": 0,
    "bbox": None
  },
  {
    "object": "bivina_standee",
    "count": 1,
    "bbox": [200, 500, 350, 700]
  },
  {
    "object": "edelweiss_beer_keg",
    "count": 2,
    "bbox": [[850, 400, 950, 500], [700, 600, 800, 700]]
  },
  {
    "object": "bialacviet_poster",
    "count": 0,
    "bbox": None
  },
  {
    "object": "strongbow_beer_can",
    "count": 1,
    "bbox": [150, 450, 200, 500]
  },
  {
    "object": "heineken_beer_bottle",
    "count": 2,
    "bbox": [[250, 600, 300, 650], [650, 300, 700, 350]]
  },
  {
    "object": "biaviet_staff",
    "count": 1,
    "bbox": [400, 50, 500, 100]
  }]

"""

# Prompt for vision task.
OBJECT_DETECTION = f"""You are an AI assistant that specializes in detecting object in a large space. 
From left to right, your task is to detect everything you see in the provided picture. In addition,  Analyze the image information and provide insights based on the criteria given below:
Here are some objects that you must detect:
{PREDEFINED_CLASS}

The answer must be described in a JSON format. Here is some example: 

{JSON_SAMPLES}
    
It must include the object, and the number of occurrences. You also must give the bounding box information of those objects. If there is no information about the bouding box, leave None value. 

Answer:
"""


# Prompts for story-telling tasks.


FOCUSED_CRITERIA = """
Criteria:
1. Brand Logos: Identify any brand logos mentioned in the description or OCR results.
2. Products: Mention any products such as beer kegs and bottles.
3. Customers: Describe the number of customers, their activities, and emotions.
4. Promotional Materials: Identify any posters, banners, and billboards.
5. Setup Context: Determine the scene context (e.g., bar, restaurant, grocery store, or supermarket).

"""