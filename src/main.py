import user
import education
import experience
import institution
import job
import post
import skill
import application

def main_menu():

    while True:
        print("\nWelcome to LinkedIn Dashboard")
        print("\nChoose one option")
        print("1. User")
        print("2. Education")
        print("3. Experience")
        print("4. Institution")
        print("5. Job")
        print("6. Post")
        print("7. Skill")
        print("8. Application")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            user.user_menu()
        elif choice == '2':
            education.education_menu()
        elif choice == '3':
            experience.experience_menu()
        elif choice == '4':
            institution.institution_menu()
        elif choice == '5':
            job.job_menu()
        elif choice == '6':
            post.post_menu()
        elif choice == '7':
            skill.skill_menu()
        elif choice == '8':
            application.application_menu()            
        elif choice == '0':
            print("Exiting Main Menu.")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()