import flet as ft
from GPA import calculate_gpa # Corrected import

def main(page: ft.Page):
    page.title = "GPA Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 450
    page.window_height = 700

    subjects_data = [] # Store subjects data

    def handle_calculate_gpa_button_click(e): # Renamed for clarity
        if not subjects_data:
            gpa_display.value = "Please add subjects first!"
            page.update()
            return

        # The calculate_gpa function from GPA.py now does all the work
        final_gpa = calculate_gpa(subjects_data)

        if final_gpa == 0.0 and not any(item['credits'] > 0 for item in subjects_data): # Check if actually no credits or all were invalid
             gpa_display.value = "No valid credits to calculate GPA."
        else:
            gpa_display.value = f"Your GPA: {final_gpa:.2f}"
        page.update()

    def add_subject_clicked(e):
        grade = grade_input.value.strip().upper()
        credits_str = credits_input.value.strip()

        if not grade or not credits_str:
            gpa_display.value = "Grade and Credits cannot be empty."
            page.update()
            return

        try:
            credits = float(credits_str)
            if credits <= 0:
                gpa_display.value = "Credits must be a positive number."
                page.update()
                return
        except ValueError:
            gpa_display.value = "Invalid credits value. Must be a number."
            page.update()
            return

        # Basic validation for grade format (e.g., A, B+, C-) can be added here if desired
        # For now, GPA.calculate_gpa handles unknown grades by skipping them.

        subjects_data.append({"grade": grade, "credits": credits})

        subjects_view.controls.append(
            ft.Text(f"Grade: {grade}, Credits: {credits}")
        )

        grade_input.value = ""
        credits_input.value = ""
        gpa_display.value = ""
        page.update()
        grade_input.focus()

    def clear_all_clicked(e):
        subjects_data.clear()
        subjects_view.controls.clear()
        gpa_display.value = "All entries cleared."
        grade_input.value = ""
        credits_input.value = ""
        page.update()

    grade_input = ft.TextField(label="Grade (e.g., A+, B, C-)", width=200, text_align=ft.TextAlign.CENTER)
    credits_input = ft.TextField(label="Credits (e.g., 3)", keyboard_type=ft.KeyboardType.NUMBER, width=200, text_align=ft.TextAlign.CENTER)

    add_button = ft.ElevatedButton(text="Add Subject", on_click=add_subject_clicked, width=200)

    subjects_view = ft.Column(scroll=ft.ScrollMode.AUTO, height=200, width=400, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    calculate_button = ft.ElevatedButton(text="Calculate GPA", on_click=handle_calculate_gpa_button_click, width=200) # Corrected handler
    clear_button = ft.ElevatedButton(text="Clear All", on_click=clear_all_clicked, width=200)
    gpa_display = ft.Text("Enter grades and credits then press 'Calculate GPA'", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    page.add(
        ft.Column(
            [
                grade_input,
                credits_input,
                add_button,
                ft.Container(
                    content=subjects_view,
                    border=ft.border.all(1, ft.colors.OUTLINE),
                    margin=ft.margin.symmetric(vertical=10), # Added vertical margin
                    padding=10,
                    width=380 # Fixed width for the container
                ),
                calculate_button,
                clear_button,
                gpa_display
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10 # Reduced spacing
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
