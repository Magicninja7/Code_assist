# Calendar and Scheduling App using Tkinter

# Features:

# - Monthly calendar view

# - Add, edit, and delete events

# - Save events to a file

# - View events for a specific day

# - Simple and intuitive interface

# 

# Steps:

# 1. Create the main window and calendar display

# 2. Implement event handling functionality

# 3. Create add/edit event dialog

# 4. Save/load events from file

# 5. Add navigation between months



import tkinter as tk








class CalendarApp:

    def __init__(self, root):

        
        self.root.title("Calendar App")

        self.current_date = datetime.datetime.now()

        self.events = {}

        self.load_events()

        

        # Create main frame

        self.main_frame = ttk.Frame(self.root, padding="10")

        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        

        # Navigation frame

        self.nav_frame = ttk.Frame(self.main_frame)

        self.nav_frame.grid(row=0, column=0, columnspan=7, pady=5)

        

        ttk.Button(self.nav_frame, text="<", command=self.prev_month).grid(row=0, column=0)

        self.month_label = ttk.Label(self.nav_frame, text="")

        self.month_label.grid(row=0, column=1, padx=10)

        ttk.Button(self.nav_frame, text=">", command=self.next_month).grid(row=0, column=2)

        

        # Create calendar grid

        self.create_calendar_grid()

        

        # Update calendar display

        self.update_calendar()



    def create_calendar_grid(self):

        # Create weekday labels

        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for i, day in enumerate(weekdays):

            ttk.Label(self.main_frame, text=day).grid(row=1, column=i)

        

        # Create calendar buttons

        self.day_buttons = []

        for week in range(6):

            for day in range(7):

                btn = ttk.Button(self.main_frame, text="", width=8)

                btn.grid(row=week+2, column=day, padx=1, pady=1)

                self.day_buttons.append(btn)



    def update_calendar(self):

        # Update month label

        self.month_label.config(text=f"{self.current_date.strftime('%B %Y')}")

        

        # Get calendar for current month

        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)

        

        # Update day buttons

        for i, button in enumerate(self.day_buttons):

            week = i // 7

            day = i % 7

            

            try:

                day_num = cal[week][day]

                if day_num == 0:

                    button.config(text="", state="disabled")

                else:

                    button.config(text=str(day_num), state="normal")

                    # Check if day has events

                    date_str = f"{self.current_date.year}-{self.current_date.month}-{day_num}"

                    if date_str in self.events:

                        button.config(style="Event.TButton")

                    else:

                        button.config(style="TButton")

                    

                    # Bind click event

                    button.config(command=lambda d=day_num: self.show_day_events(d))

            except IndexError:

                button.config(text="", state="disabled")



    def prev_month(self):

        self.current_date = self.current_# Recipe Manager Application

# Features:

# 1. Store recipes with ingredients, instructions, and cooking time

# 2. Search recipes by available ingredients

# 3. Suggest recipes based on what ingredients user has

# 4. Save and load recipes from a JSON file

# 5. Add, delete, and modify recipes

# 

# Steps:

# 1. Create Recipe class to store recipe information

# 2. Create RecipeManager class to handle operations

# 3. Implement file handling for persistent storage

# 4. Create user interface functions

# 5. Implement search and suggestion algorithms









class Recipe:

    def __init__(self, name: str, ingredients: List[str], instructions: List[str], cooking_time: int):

        
        
        
        
        self.date_added = datetime.now().strftime("%Y-%m-%d")



    def to_dict(self) -> Dict:

        return {

            "name": self.name,
                            
            "ingredients": self.ingredients,

            "instructions": self.instructions,

            "cooking_time": self.cooking_time,

            
        }



    
    def from_dict(cls, data: Dict):

        recipe = cls(

            data["name"],
                            
            data["ingredients"],

            data["instructions"],

            data["cooking_time"]

        )

        recipe.date_added = data["date_added"]

        


class RecipeManager:

    def __init__(self, filename: str = "recipes.json"):

        
        self.recipes = []

        self.load_recipes()



    def load_recipes(self):

        if os.path.exists(self.filename):

            with open(self.filename, "r") as f:

                data = json.load(f)

                self.recipes = [Recipe.from_dict(recipe_data) for recipe_data in data]



    def save_recipes(self):

        with open(self.filename, "w") as f:

            json.dump([recipe.to_dict() for recipe in self.recipes], f, indent=4)



    def add_recipe(self, recipe: Recipe):

        self.recipes.append(recipe)

        self.save_recipes()



    def delete_recipe(self, recipe_name: str):

        self.recipes = [recipe for recipe in self.recipes if recipe.name.lower() != recipe_name.lower()]

        self.save_recipes()



    def find_recipes_by_ingredients(self, available_ingredients: List[str]) -> List[Recipe]:

        available_ingredients = [ing.lower() for ing in available_ingredients]

        matching_recipes = []

        

        for recipe in self.recipes:

            recipe_ingredients = [ing.lower() for ing in recipe.ingredients]

            if all(ing in available_ingredients for ing in recipe_ingredients):

                matching_recipes.append(recipe)

        

        


    def suggest_recipes(self, available_ingredients: List[str]) -> List[Recipe]:

        available_ingredients = [ing.lower() for ing in available_ingredients]

        suggestions = []

        

        for recipe in self.recipes:

            recipe_ingredients = [ing.lower() for ing in recipe.ingredients]

            matching_ingredients = sum(1 for ing in recipe_ingredients if ing in available_ingredients)

            
            

            if missing_ingredients <= 2:  # Suggest recipes missing 2 or fewer ingredients

                suggestions.append((recipe, missing_ingredients))

        

        # Sort by number of missing ingredients

        suggestions.sort(key=lambda x: x[1])

        return [recipe for recipe, _ in suggestions]



def main():

    manager = RecipeManager()

    

    while True:

        print("\n=== Recipe Manager ===")

        print("1. Add Recipe")

        print("2. Delete Recipe")

        print("3. Find Recipes by Ingredients")

        print("4.")