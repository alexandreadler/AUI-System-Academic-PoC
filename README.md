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

How It Works:
-------------
### User Profile
- Users register by providing details such as:
  - **Age**
  - **Gender**
  - **Disability**
  - **Device**
  - **Context of Use** (e.g., luminosity and time of day)
- The system calculates **UI adaptations** dynamically based on the user's profile using the operational ontology.

### Profile Page
- Displays user information and dynamically determined **UI adaptations**:
  - **Theme** (e.g., light or dark mode)
  - **Interaction Mode** (e.g., standard or gesture interaction)
  - **Layout** (e.g., mobile-optimized or desktop-optimized)
- Users can update their profile through an **editable interface**.

### Academic Content
- Provides a curated list of **academic subjects** relevant to ontology and accessibility.
- Adapts the interface to ensure better **readability** and **usability** based on the user's profile and context.

### Ontology Integration
- The operational ontology (`ontoOADAPT.owl`) is:
  - Loaded and queried using the **Owlready2** library.
  - Used to determine the most suitable adaptations for the user.
- Adaptation logic is implemented in **Python**, applying rules derived from the ontology to adapt the UI at runtime.

## Code Snippets

### Loading the Operational Ontology
```python
from owlready2 import get_ontology

ontology_path = "ontology/ontoOADAPT_PoC.owl"  #Path to the ontology file
ontology = get_ontology(ontology_path).load()  #Load the ontology

