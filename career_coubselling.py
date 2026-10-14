def ask(question):
    answer = input(question)
    if answer.strip() == "":
        print("ALL QUESTIONS ARE TO BE ANSWERED!")
        exit()   # stop the program if blank
    return answer
def collect_data():
    filename = "career_counselling_data.txt"
    data = {}

    print("=== CAREER COUNSELLING FORM ===\n")

    # PERSONAL INFORMATION
    data["name"] = ask("Full Name: ")
    data["age"] = ask("Age: ")
    data["gender"] = ask("Gender: ")
    data["address"] = ask("Address: ")

    # ACADEMIC BACKGROUND
    data["edu_level"] = ask("Current Educational Level: ")
    data["strong_sub"] = ask("Strong Subjects: ").lower()
    data["weak_sub"] = ask("Weak Subjects: ").lower()

    # CAREER PREFERENCES
    data["sector"] = ask("Preferred Sector: ").lower()
    data["work_env"] = ask("Work Environment (self/team, indoor/outdoor, etc.): ").lower()
    data["salary"] = ask("Expected Salary: ")

    # SKILLS & EXTRACURRICULARS
    data["hobbies"] = ask("Hobbies and Interests: ")
    data["achievements"] = ask("Key Achievements or   Learnings: ")

    # MISCELLANEOUS
    data["inspiration"] = ask("Who is your inspiration? ")
    data["pressure"] = ask("Does anyone pressurise you to opt for a career choice? ")
    data["society_change"] = ask("How does the society need to change? ")

    # Save raw responses
    with open(filename, "a") as file:
        file.write(str(data) + "\n")
        return data
   
def generate_career_report(data):
    """Generate career recommendations based on user input."""

    recommendations = []
    pathways = []
    market_insights = []

    # Simple rule-based suggestions
    if "math" in data["strong_sub"] or "physics" in data["strong_sub"]:
        recommendations.append("Engineer (Mechanical, Civil, Software, etc.)")
        pathways.append("B.Tech/B.E in chosen field, followed by internships")
        market_insights.append("Average Salary: ₹4-10 LPA, High Demand in India")

    if "biology" in data["strong_sub"] :
        recommendations.append("Doctor / Biotechnologist / Pharmacist")
        pathways.append("MBBS, BDS, B.Sc. in Biotechnology, or Pharmacy courses")
        market_insights.append("Average Salary: ₹6-20 LPA, Growing Demand in Healthcare")

    if "english" in data["strong_sub"] or "arts" in data["strong_sub"]:
        recommendations.append("Journalist / Writer / Teacher")
        pathways.append("B.A. in English, Journalism, or B.Ed for teaching")
        market_insights.append("Average Salary: ₹3-8 LPA, Steady Demand")

    if "computer" in data["strong_sub"] or "coding" in data["hobbies"].lower():
        recommendations.append("Software Developer / Data Analyst / AI Engineer")
        pathways.append("B.Tech/BCA + Certifications in Python, Data Science, AI")
        market_insights.append("Average Salary: ₹5-20 LPA, Very High Demand in IT Sector")

    if "business" in data["sector"]:
        recommendations.append("Business Analyst / Entrepreneur / Marketing Manager")
        pathways.append("BBA, MBA, Digital Marketing Certifications")
        market_insights.append("Average Salary: ₹4-15 LPA, High Demand in Management")

    # Default suggestion if none matched
    if not recommendations:
        recommendations.append("Career Counsellor Needed for Further Assessment")
        pathways.append("Take psychometric tests and career aptitude assessments")
        market_insights.append("Salary & demand depend on chosen career")

    # Display Report
    print("\n" + "="*40)
    print("CAREER RECOMMENDATION REPORT")
    print("="*40)
    for i, rec in enumerate(recommendations):
        print(f"{i+1}. {rec}")

    print("\nEDUCATIONAL PATHWAYS")
    print("="*40)
    for path in pathways:
        print(f"- {path}")

    print("\nJOB MARKET INSIGHTS")
    print("="*40)
    for insight in market_insights:
        print(f"- {insight}")

    print("\nNOTE: These recommendations are based on your inputs and general industry trends.\n")
    
# MAIN PROGRAM
while True:
    print("\n=== CAREER COUNSELLING SYSTEM ===")
    print("1. Fill Career Form & Get Recommendations")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        user_data = collect_data()
        generate_career_report(user_data)
    elif choice == "2":
        print("Thank you for using the Career Counselling System!")
        break
    else:
        print("Invalid choice. Try again.")
