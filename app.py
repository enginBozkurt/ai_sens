import os
from flask import Flask, request, jsonify, send_from_directory
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)


# Get OpenAI API key from environment variables
openai_api_key = ''OPENAI_API_KEY''

# Check if the API key is present
if not openai_api_key:
    raise ValueError("OpenAI API key is missing. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = openai_api_key

# Serve static files (HTML, CSS, JS)
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('static', path)

# Define a route for chatting
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user's message from the request body
        user_message = request.json.get('message')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Make sure to print the user message for debugging
        print(f"User message received: {user_message}")

        # Request OpenAI's response using the ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change this to "gpt-4" if you want to use GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant and a sales representative for Nutrinova, a company specializing in natural supplements. Your name is Sophia. Your goal is to provide information about Nutrinova's products, answer customer questions, and help with sales inquiries in a friendly and professional manner. Please answer the questions related with Nutrinova products, supplement details and healthcare issues. Kindly do not answer other kinds of topics. If the inappropriate questions are asked more than twice, stop the converstion and inform the person."},
                # Product details for all supplements
        {"role": "system", "content": """
        **Product: Black Garlic 400+**
        - Supports cardiovascular health and vitality.
        - Contains aged black garlic bulb powder (800 mg per serving).
        - Benefits:
            1. Promotes healthy cholesterol levels.
            2. Enhances energy and overall well-being.
            3. Provides powerful antioxidants to combat oxidative stress.
        - Usage: Take 2 capsules daily with meals.
        - Features: Non-GMO, gluten-free, no synthetic additives.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Arthrocure**
        - A double-action program for joint health and mobility.
        - Key Ingredients: Boswellia Extract, Devil's Claw, Meadowsweet, Horsetail, Wintergreen, Vitamin C, Manganese.
        - Benefits:
            1. Reduces joint discomfort and swelling.
            2. Promotes cartilage health and flexibility.
            3. Provides a cooling and soothing effect for joints.
        - Usage: Take 2 capsules daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Joint Mobility**
        - Targets freedom of movement and joint nutrition.
        - Key Ingredients: Liquid protein from snail extract, glucosamine, chondroitin, and MSM.
        - Benefits:
            1. Supports cartilage healing and joint function.
            2. Promotes flexibility and alleviates stiffness.
            3. Ideal for active individuals or those experiencing joint discomfort.
        - Usage: Follow instructions on packaging.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Curcumaxe**
        - Crafted for overall health and inflammation reduction.
        - Main Ingredient: High-quality curcumin extract.
        - Benefits:
            1. Enhances joint and immune health.
            2. Reduces inflammation and oxidative stress.
            3. Boosts vitality and wellness.
        - Usage: Take as directed on the packaging.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Sight Saver**
        - Designed to promote eye health and vision.
        - Key Ingredients: Lutein, Blueberry, Zeaxanthin, Vitamin C, Vitamin E, Bamboo Silica.
        - Benefits:
            1. Supports visual wellness and reduces eye fatigue.
            2. Helps combat the effects of aging on eyes.
            3. Nourishes and protects your eyes naturally.
        - Usage: Take 1 capsule twice daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: MoodLife 7**
        - Supports emotional balance and natural stress relief.
        - Key Ingredients: B vitamins, Magnesium, Ashwagandha, L-Theanine.
        - Benefits:
            1. Promotes emotional resilience and stress management.
            2. Enhances mood and relaxation.
            3. Helps maintain a calm, focused state of mind.
        - Usage: Take 1 capsule daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Stomafine 200**
        - Enhances digestive health and gut balance.
        - Key Ingredients: Pylopass™, Ascophyllum, Biotin (Vitamin B8).
        - Benefits:
            1. Promotes gut flora balance and efficient digestion.
            2. Reduces digestive discomfort and bloating.
            3. Supports nutrient absorption and overall digestive wellness.
        - Usage: Take 1 capsule twice daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Body Detox**
        - Promotes weight control and natural detoxification.
        - Key Ingredients: Kaolin, Yerba Mate, Burdock, Psyllium, Probiotic Lactobacillus Acidophilus, Chlorella.
        - Benefits:
            1. Helps eliminate toxins naturally.
            2. Supports healthy digestion and weight management.
            3. Improves gut health and overall vitality.
        - Usage: Take 1 capsule daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Probiotix Plus**
        - Maintains digestive health with 20 billion live probiotics.
        - Key Ingredients: 7 probiotic strains.
        - Benefits:
            1. Balances gut flora for enhanced digestion.
            2. Improves immune system function.
            3. Reduces bloating and supports overall gut health.
        - Usage: Take 1 capsule daily.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Collagen Xpert**
        - Boosts skin elasticity, joint health, and overall vitality.
        - Key Ingredient: Premium collagen peptides.
        - Benefits:
            1. Promotes youthful, radiant skin by reducing wrinkles.
            2. Enhances joint flexibility and mobility.
            3. Supports overall structural health and vitality.
        - Usage: Take 1 capsule daily.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: EroBoost 4x**
        - Enhances male vitality, stamina, and performance.
        - Key Ingredients: Tongkat Ali, Horny Goat Weed, Ginseng, Maca.
        - Benefits:
            1. Boosts energy and endurance naturally.
            2. Supports healthy testosterone levels.
            3. Improves overall physical and mental performance.
        - Usage: Take 2 capsules daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Natural Slim**
        - Aids in natural weight management and appetite control.
        - Key Ingredients: Glucomannan, Chitosan, Artichoke Extract, Guarana Extract, Mate Leaf, Rosemary Extract.
        - Benefits:
            1. Promotes feelings of fullness and reduces cravings.
            2. Supports metabolism and energy levels.
            3. Provides antioxidant benefits for overall wellness.
        - Usage: Take 2 capsules daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Black Nettle**
        - Supports joint health and flexibility.
        - Key Ingredient: Black Nettle extract.
        - Benefits:
            1. Enhances joint mobility and comfort.
            2. Promotes joint flexibility and reduces occasional stiffness.
            3. Supports an active, pain-free lifestyle.
        - Usage: Take 1 capsule daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Brain Wixtra+**
        - Supports cognitive health, focus, and memory.
        - Key Ingredients: Lecithin, Acetyl L-Carnitine, Vinpocetine, Turmeric, Ginkgo Biloba.
        - Benefits:
            1. Enhances concentration and mental clarity.
            2. Supports long-term brain health and memory retention.
            3. Improves brain blood flow and reduces cognitive decline.
        - Usage: Take 1 capsule twice daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Body Detox**
        - Promotes weight control and natural detoxification.
        - Key Ingredients: Kaolin, Yerba Mate, Burdock, Psyllium, Lactobacillus Acidophilus, Chlorella.
        - Benefits:
            1. Detoxifies the body and removes toxins.
            2. Enhances gut health and promotes healthy digestion.
            3. Assists with weight management and energy levels.
        - Usage: Take 1 capsule daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Cordy Boost**
        - Supports natural detoxification and digestive health.
        - Key Ingredient: Cordyceps Mushroom extract (7% Cordycepic Acid).
        - Benefits:
            1. Boosts vitality, physical energy, and endurance.
            2. Enhances immune defenses and slows aging effects.
            3. Supports healthy digestion and detoxification.
        - Usage: Take 1 capsule daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Candi Protect**
        - Promotes gut health and combats Candida imbalances.
        - Key Ingredients: Oleuropein, Silymarin, Chlorophyll, Caprylic Acid, Lithothamnium Algae.
        - Benefits:
            1. Supports a healthy gut environment and digestive balance.
            2. Enhances immunity and overall well-being.
            3. Combats fungal imbalances and promotes detoxification.
        - Usage: Take 1 capsule twice daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Helix Sativa**
        - Full-spectrum hemp extract for relaxation and sleep support.
        - Key Ingredient: Cannabidiol (CBD).
        - Benefits:
            1. Promotes relaxation and reduces stress.
            2. Supports healthy sleep patterns and muscle recovery.
            3. Reduces inflammation and enhances physical recovery.
        - Usage: Take 1 dropper daily under the tongue or as directed.
        - Price : $55.00
        
        """},
        {"role": "system", "content": """
        **Product: Hydro Caps 1000**
        - Enhances energy and natural detoxification.
        - Key Ingredients: Ion-Mag, Aloe Vera, Green Tea extract.
        - Benefits:
            1. Boosts energy levels and cellular function.
            2. Supports detoxification and antioxidant protection.
            3. Improves overall vitality and endurance.
        - Usage: Take 1 capsule daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Marine Body Boost**
        - Promotes vitality with marine-based nutrients.
        - Key Ingredients: Spirulina, Chlorella, Green Lipped Mussel, Vitamin D3.
        - Benefits:
            1. Boosts immune health and energy levels.
            2. Supports joint flexibility and bone health.
            3. Provides anti-inflammatory benefits and skin nourishment.
        - Usage: Take 1 capsule daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Pro Guggul Slim**
        - Supports weight management and fat burning.
        - Key Ingredients: Guggul resin extract, Chicory.
        - Benefits:
            1. Enhances metabolism and promotes fat burning.
            2. Reduces body inflammation and improves digestion.
            3. Supports healthy weight management.
        - Usage: Take 1 capsule twice daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Phyto Revital Lift**
        - Enhances overall wellness with plant-based nutrients.
        - Key Ingredients: Beer Yeast Powder, Shiitake, Centella Asiatica, MSM, Astragalus Root.
        - Benefits:
            1. Boosts energy levels and cognitive health.
            2. Enhances skin vitality and mood balance.
            3. Supports immune function and overall vitality.
        - Usage: Take 1 capsule daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Prostalife 900**
        - Promotes prostate health and function.
        - Key Ingredients: Pomegranate, Boswellia Serrata, Saw Palmetto.
        - Benefits:
            1. Reduces symptoms of an enlarged prostate.
            2. Enhances urinary flow and comfort.
            3. Supports long-term prostate health and well-being.
        - Usage: Take 1 capsule twice daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Regenatin Xtra+**
        - Enhances skin health and reduces aging signs.
        - Key Ingredient: Hyaluronic Acid.
        - Benefits:
            1. Improves skin elasticity and hydration.
            2. Reduces fine lines and wrinkles.
            3. Promotes a youthful, radiant complexion.
        - Usage: Take 1 capsule daily with meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Saffron Gold**
        - Enhances mood, skin health, and vitality.
        - Key Ingredient: Premium saffron extract.
        - Benefits:
            1. Supports emotional balance and cognitive clarity.
            2. Promotes skin radiance and elasticity.
            3. Boosts overall well-being and energy.
        - Usage: Take 1 capsule daily with meals.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Rituel Selkis**
        - Deep hydration and rejuvenation for skin health.
        - Key Ingredients: Hemp Oil, Bitter Orange, Date Palm Oil, Shea Butter, Lotus Extract.
        - Benefits:
            1. Provides deep moisturization and protection.
            2. Reduces signs of aging and environmental stress.
            3. Improves skin texture and radiance.
        - Usage: Apply to skin as needed.
        - Price : $45.00
        """},
        {"role": "system", "content": """
        **Product: Slim Shot**
        - Supports weight loss and metabolism boost.
        - Key Ingredients: Caffeine, Green Tea Extract, L-Carnitine.
        - Benefits:
            1. Boosts metabolism and energy.
            2. Supports fat burning and weight loss.
            3. Reduces appetite naturally.
        - Usage: Take 1 shot daily before meals.
        - Price : $55.00
        """},
        {"role": "system", "content": """
        **Product: Arthropure 500**
        - Supports joint health and bone strength.
        - Key Ingredients: Glucosamine, Chondroitin, MSM, Snail Protein, Boswellia Serrata.
        - Benefits:
            1. Enhances joint flexibility and mobility.
            2. Reduces joint inflammation and stiffness.
            3. Promotes cartilage health and repair.
        - Usage: Take 2 capsules daily with meals.
        - Price : $55.00
        """},
                {"role": "user", "content": user_message}
            ]
        )

        # Log the full response for debugging purposes
        print("OpenAI Response:", response)

        # Extract the assistant's reply
        reply = response['choices'][0]['message']['content'].strip()

        # Return the GPT response to the frontend
        return jsonify({'reply': reply})

    except Exception as e:
        # Handle errors and log them for debugging
        print("Error occurred:", str(e))
        return jsonify({'error': str(e)}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
