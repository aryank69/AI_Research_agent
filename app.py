from agent import build_agent
from report_generator import generate_pdf
import os

def main():
    agent = build_agent()

    print("🔍 AI Research Agent")
    print("Type 'exit' to quit\n")

    os.makedirs("outputs/reports", exist_ok=True)

    counter = 1

    while True:
        query = input("Enter your research query: ")
        if query.lower() == "exit":
            break

        print("\nGenerating report...\n")
        response = agent.run(query)

        print("\n📄 Research Report:\n")
        print(response)

        # Save PDF
        pdf_path = f"outputs/reports/report_{counter}.pdf"
        generate_pdf(pdf_path, query, response)

        print(f"\n✅ PDF saved at: {pdf_path}\n")

        counter += 1

if __name__ == "__main__":
    main()