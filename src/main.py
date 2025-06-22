import flet as ft
from GPA import calculate_gpa # Corrected import

def main(page: ft.Page):
    page.title = "GPA Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 650 # Increased height slightly to accommodate more padding
    page.padding = ft.padding.only(top=60) # Increased top padding

    subjects_data = [] # Store subjects data

    # Define grade options from GPA.py's Scale
    # Ensure GPA.py's Scale is accessible or redefine it here if preferred
    # For this example, let's assume Scale is accessible or we redefine its keys
    grade_options_keys = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
    grade_dropdown_options = [ft.dropdown.Option(key) for key in grade_options_keys]

    def handle_calculate_gpa_button_click(e): # Renamed for clarity
        if not subjects_data:
            gpa_display.value = "Please add subjects first!"
            gpa_display.color = ft.Colors.ERROR # Optional: add color for emphasis
            page.update()
            return

        # The calculate_gpa function from GPA.py now does all the work
        final_gpa = calculate_gpa(subjects_data)

        if final_gpa == 0.0 and not any(item['credits'] > 0 for item in subjects_data): # Check if actually no credits or all were invalid
             gpa_display.value = "No valid credits to calculate GPA."
             gpa_display.color = ft.Colors.ORANGE # Optional: color for warning
        else:
            gpa_display.value = f"Your GPA: {final_gpa:.2f}"
            gpa_display.color = ft.Colors.GREEN # Optional: color for success
        page.update()

    def add_subject_clicked(e):
        grade = grade_input.value # Directly get value from dropdown
        credits_str = credits_input.value.strip()

        if not grade: # Check if a grade is selected from dropdown
            gpa_display.value = "Please select a grade."
            gpa_display.color = ft.Colors.ERROR
            page.update()
            return
        if not credits_str:
            gpa_display.value = "Grade and Credits cannot be empty."
            gpa_display.color = ft.Colors.ERROR
            page.update()
            return

        try:
            credits = float(credits_str)
            if credits <= 0:
                gpa_display.value = "Credits must be a positive number."
                gpa_display.color = ft.Colors.ERROR
                page.update()
                return
        except ValueError:
            gpa_display.value = "Invalid credits value. Must be a number."
            gpa_display.color = ft.Colors.ERROR
            page.update()
            return

        # Basic validation for grade format (e.g., A, B+, C-) can be added here if desired
        # For now, GPA.calculate_gpa handles unknown grades by skipping them.

        subjects_data.append({"grade": grade, "credits": credits})

        subjects_view.controls.append(
            ft.Text(f"Grade: {grade}, Credits: {credits}")
        )

        grade_input.value = None # Clear dropdown selection
        credits_input.value = ""
        gpa_display.value = ""
        gpa_display.color = None # Reset color
        page.update()
        grade_input.focus()

    def clear_all_clicked(e):
        subjects_data.clear()
        subjects_view.controls.clear()
        gpa_display.value = "All entries cleared."
        gpa_display.color = ft.Colors.BLUE_GREY # Optional: color for info
        grade_input.value = None # Clear dropdown selection
        credits_input.value = ""
        page.update()

    grade_input = ft.Dropdown(
        label="Select Grade",
        options=grade_dropdown_options,
        width=200,
        # text_align isn't a direct property for Dropdown, alignment is handled by container/layout
        # hint_text="Choose a grade" # Alternative to label
    )
    credits_input = ft.TextField(label="Credits (e.g., 3)", keyboard_type=ft.KeyboardType.NUMBER, width=200, text_align=ft.TextAlign.CENTER)

    add_button = ft.ElevatedButton(text="Add Subject", on_click=add_subject_clicked, width=200)

    subjects_view = ft.Column(scroll=ft.ScrollMode.AUTO, height=200, width=400, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    calculate_button = ft.ElevatedButton(text="Calculate GPA", on_click=handle_calculate_gpa_button_click, width=200) # Corrected handler
    clear_button = ft.ElevatedButton(text="Clear All", on_click=clear_all_clicked, width=200)
    gpa_display = ft.Text("Enter grades and credits then press 'Calculate GPA'", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    page.add(
        ft.Column(
            [
                # Content starts here
                grade_input,
                credits_input,
                add_button,
                ft.Container(
                    content=subjects_view,
                    border=ft.border.all(1, ft.Colors.OUTLINE),
                    margin=ft.margin.symmetric(vertical=10), # Added vertical margin
                    padding=10,
                    width=380 # Fixed width for the container
                ),
                calculate_button,
                clear_button,
                gpa_display
            ], # Content ends here
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10 # Reduced spacing
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
