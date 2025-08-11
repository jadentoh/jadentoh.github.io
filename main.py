import generate_portfolio
import sys

def main():
    print("Hello from portfolio-generator!")
    if len(sys.argv) == 1:
        print("Generating portfolio from default file portfolio.json...")
        generate_portfolio.generate_html_cv()
        print("Portfolio generated successfully!")
    elif len(sys.argv) == 2  and ".json" in sys.argv[1]:
        print(f"Generating portfolio from the argument json file {sys.argv[1]}...")
        generate_portfolio.generate_html_cv()
        print("Portfolio generated successfully!")
    else:
        print(f"The argument {sys.argv[1]} is not a valid json file...")
    


if __name__ == "__main__":
    main()
