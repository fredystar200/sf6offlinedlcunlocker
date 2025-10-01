import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Root directory where the script and files are located
ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILES_TO_COPY = [
    "dinput8.dll",
    "SmokeAPI.dll",
    "version.dll",
]
FOLDER_TO_COPY = os.path.join(ROOT_DIRECTORY, "reframework")


def add_files(destination_folder):
    """Copies the required files and folder to the selected folder."""
    try:
        # Copy individual files
        for file_name in FILES_TO_COPY:
            source = os.path.join(ROOT_DIRECTORY, file_name)
            if not os.path.exists(source):
                messagebox.showerror("Error", f"File not found: {file_name} in {ROOT_DIRECTORY}")
                return
            destination = os.path.join(destination_folder, file_name)
            shutil.copy2(source, destination)

        # Copy the entire folder
        if os.path.exists(FOLDER_TO_COPY):
            target_folder = os.path.join(destination_folder, "reframework")
            shutil.copytree(FOLDER_TO_COPY, target_folder, dirs_exist_ok=True)
        else:
            messagebox.showerror("Error", f"Folder not found: {FOLDER_TO_COPY}")
            return

        messagebox.showinfo("Success", "Files and folder added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def remove_files(target_folder):
    """Removes the specified files and folder from the selected folder."""
    try:
        # Remove individual files
        for file_name in FILES_TO_COPY:
            file_path = os.path.join(target_folder, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)

        # Remove the entire folder
        folder_to_remove = os.path.join(target_folder, "reframework")
        if os.path.exists(folder_to_remove):
            shutil.rmtree(folder_to_remove)

        messagebox.showinfo("Success", "Files and folder removed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def select_folder(action):
    """Prompts the user to select a folder and performs the chosen action."""
    folder_selected = filedialog.askdirectory(title="Select a Folder")
    if not folder_selected:
        return

    if action == "add":
        add_files(folder_selected)
    elif action == "remove":
        remove_files(folder_selected)


def main():
    """Main function to create the GUI."""
    # Initialize the customtkinter theme
    ctk.set_appearance_mode("System")  # Options: "System" (default), "Light", "Dark"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    # Create the main application window
    app = ctk.CTk()
    app.title("SF6 Offline DLC Unlocker")
    app.geometry("500x400")

    # Title Label
    title_label = ctk.CTkLabel(app, text="SF6 Offline DLC Unlocker", font=("Roboto", 24, "bold"))
    title_label.pack(pady=20)

    # Buttons
    add_button = ctk.CTkButton(
        app,
        text="Add Files and Folder",
        font=("Roboto", 14),
        command=lambda: select_folder("add"),
        width=200,
        height=40,
        corner_radius=8,
    )
    add_button.pack(pady=10)

    remove_button = ctk.CTkButton(
        app,
        text="Remove Files and Folder",
        font=("Roboto", 14),
        command=lambda: select_folder("remove"),
        width=200,
        height=40,
        corner_radius=8,
    )
    remove_button.pack(pady=10)

    # Backup Reminder
    reminder_label = ctk.CTkLabel(
        app,
        text=(
            "⚠️ Make sure to backup your win64_save folder before use.\n"
            "Located at: <Steam-folder>\\userdata\\<user-id>\\1364780\\remote\\win64_save\\"
        ),
        font=("Roboto", 12),
        text_color="orange",
        wraplength=400,
        justify="center",
    )
    reminder_label.pack(pady=20)

    # Footer
    footer_label = ctk.CTkLabel(app, text="Made by fredystar200 (with community tools)", font=("Roboto", 10), text_color="gray")
    footer_label.pack(side="bottom", pady=10)

    # Run the application
    app.mainloop()


if __name__ == "__main__":
    main()
