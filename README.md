AUI System Academic - Proof of Concept (PoC)
============================================

This project is a Proof of Concept (PoC) demonstrating an Adaptive User Interface (AUI) system using an operational ontology to 
customize the user experience dynamically. The system focuses on dynamically adapting the UI based on user profiles (age, gender, disability) and contexts
of use (device, luminosity, time of day).

The PoC was implemented using Python, chosen for its flexibility and extensive collection of libraries and tools. The web interface was developed with Flask, a lightweight web framework in Python, to develop the user interface and manage routing, requests, and responses. Flask enables the creation of dynamic web applications by integrating HTML templates with back-end logic. In this system, Flask makes available functionalities such as user registration, login, profile management, and dynamic interface adaptation based on user-specific data. To interact with the ontology, the Owlready2 library was utilized, designed for working with OWL ontologies in Python, enabling navigation, querying, and reasoning over the ontology.


Features:
---------
- User Registration
- User Login
- Profile Page: Displays user details and adaptations applied.
- Academic Content Page: Shows example academic topics dynamically adapted to the user.
- Editable User Profile: Users can update their details to adjust UI adaptations.

Technologies Used:
------------------
- Flask: Web framework for routing, requests, and rendering templates.
- Owlready2: Library for loading, querying, and reasoning over OWL ontologies.
- Python: Core programming language for logic implementation.
- HTML + Jinja2: Templates for rendering dynamic pages.
- Ontology: Operational ontology (`ontoOADAPT.owl`) developed for UI adaptations.

Installation:
-------------
1. Clone this repository:
   ```bash
   git clone https://github.com/alexandreadler/AUI-System-Academic-PoC.git
   cd AUI-System-Academic-PoC
   
Install Dependencies:
-------------
2. Run:
   ```bash
   pip install -r requirements.txt
   
Run the Application:
-------------
3. Run:
   ```bash
   python app.py

