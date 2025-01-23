from flask import Flask, render_template, request, redirect, url_for, session, flash
from owlready2 import get_ontology, Thing

app = Flask(__name__)
app.secret_key = "adaptive_education_secret"

# Carregar a ontologia operacional
ontology_path = "ontology/ontoOADAPT1.1.owl"  # Atualize o caminho correto
ontology = get_ontology(ontology_path).load()

# Simulação de banco de dados de usuários
users = {}

# Função para determinar adaptações com base no perfil e contexto de uso do usuário
def get_adaptations(user_profile):
    adaptations = {}

    # Verificar contexto de luminosidade e hora do dia
    if user_profile["luminosity"] == "Low_Light" and user_profile["time_of_day"] == "Nighttime":
        adaptations["theme"] = "dark"
    if user_profile["luminosity"] == "Low_Light" and user_profile["time_of_day"] == "Daytime":
        adaptations["theme"] = "dark"
    elif user_profile["luminosity"] == "High_Light" and user_profile["time_of_day"] == "Nighttime":
        adaptations["theme"] = "light"
    elif user_profile["luminosity"] == "High_Light" and user_profile["time_of_day"] == "Daytime":
        adaptations["theme"] = "light"

    # Verificar deficiência
    if user_profile["disability"] == "RSI":
        adaptations["interaction"] = "Gesture Interaction Enabled"
    else:
        adaptations["interaction"] = "Standard Interaction"

    # Adaptação para dispositivo
    if user_profile["device"] == "Mobile":
        adaptations["layout"] = "Mobile-Optimized Layout"
    elif user_profile["device"] == "Desktop":
        adaptations["layout"] = "Desktop-Optimized Layout"

    return adaptations

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        gender = request.form["gender"]
        disability = request.form["disability"]
        luminosity = request.form["luminosity"]
        time_of_day = request.form["time_of_day"]
        device = request.form["device"]

        # Verifica se o usuário já existe
        if username in users:
            return "User already exists!", 400

        # Armazena o perfil do usuário
        users[username] = {
            "username": username,
            "age": age,
            "gender": gender,
            "disability": disability,
            "luminosity": luminosity,
            "time_of_day": time_of_day,
            "device": device,
        }

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]

        if username not in users:
            return "User not found!", 404

        # Armazena o usuário na sessão
        session["username"] = username
        return redirect(url_for("academic_content"))
    return render_template("login.html")

@app.route("/academic")
def academic_content():
    # Dados de exemplo sobre assuntos acadêmicos
    academic_contents = [
        {
            "title": "Understanding Ontologies in AI",
            "description": "A comprehensive guide to the use of ontologies in artificial intelligence systems.",
            "link": "https://example.com/understanding-ontologies"
        },
        {
            "title": "Adaptive Systems and User Interfaces",
            "description": "Learn how adaptive systems customize user experiences dynamically.",
            "link": "https://example.com/adaptive-systems"
        },
        {
            "title": "Introduction to Semantic Reasoning",
            "description": "Explore how semantic reasoning engines work in AI applications.",
            "link": "https://example.com/semantic-reasoning"
        },
        {
            "title": "Designing for Accessibility",
            "description": "Guidelines for creating accessible user interfaces for diverse users.",
            "link": "https://example.com/designing-accessibility"
        }
    ]

    # Adaptações dinâmicas com base no perfil do usuário
    username = session["username"]
    user_profile = users[username]
    adaptations = get_adaptations(user_profile)

    return render_template(
        "academic_content.html", academic_contents=academic_contents,
        adaptations=adaptations, user_profile=user_profile)

@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]
    user_profile = users[username]
    adaptations = get_adaptations(user_profile)

    return render_template("profile.html", adaptations=adaptations, user_profile=user_profile)

@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]
    user_profile = users.get(username, {})

    if request.method == "POST":
        # Atualizar os dados do perfil do usuário
        user_profile["age"] = int(request.form["age"])
        user_profile["gender"] = request.form["gender"]
        user_profile["device"] = request.form["device"]
        user_profile["disability"] = request.form["disability"]
        user_profile["time_of_day"] = request.form["time_of_day"]
        user_profile["luminosity"] = request.form["luminosity"]

        flash("Profile updated successfully!", "success")
        return redirect(url_for("profile"))
    
    # Gere adaptações com base no perfil
    adaptations = get_adaptations(user_profile)

    return render_template("edit_profile.html", user_profile=user_profile, adaptations=adaptations)


if __name__ == "__main__":
    app.run(debug=True)
