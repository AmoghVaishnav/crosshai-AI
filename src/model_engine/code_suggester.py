import json
from fuzzywuzzy import fuzz

class CodeSuggester:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = self.LoadDB()

    def LoadDB(self):
        """Load the prompt database from a JSON file."""
        try:
            with open(self.db_path, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print(f"Error: The file {self.db_path} was not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: The file {self.db_path} could not be decoded. Please check the file format.")
            return []
    
    def AnalyzeCode(self, user_code):
        """Basic analysis of user code (this can be expanded for optimization checks)."""
        # Example of basic analysis: check for performance bottlenecks or redundant code
        if "for i in range" in user_code and "len()" in user_code:
            return "Consider using 'enumerate()' for better readability and performance in loops."
        if "while True" in user_code:
            return "Avoid infinite loops without break conditions for better control flow."

        # For now, return an empty string
        return ""

    def MatchPrompt(self, user_prompt, user_code):
        """
        Use fuzzy matching to match the user prompt to the stored prompts in the database.
        Also incorporate `user_code` into the suggestion process.
        """
        best_match = None
        best_score = 0

        # Analyze the user code for potential improvements
        code_analysis = self.AnalyzeCode(user_code)

        for entry in self.db:
            score = fuzz.partial_ratio(user_prompt.lower(), entry["prompt"].lower())
            if score > best_score:
                best_score = score
                best_match = entry

        
        if best_score >= 80:  
            
            return best_match["answer"], best_match["sample_code"], code_analysis

        return "No suggestions found.", "", code_analysis
