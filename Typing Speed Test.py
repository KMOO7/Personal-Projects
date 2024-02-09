import time
import faker #generates fake data, here generating phrases 


def generate_random_paragraph():
    fake = faker.Faker()
    return fake.paragraph(nb_sentences=3)

print("Welcome to Test Typing Speed.... Software ","\n")
print("Type the below sentence with accuracy:")
generated_text=str(generate_random_paragraph())
generated_text=generated_text.lower()
print(generated_text,"\n")
try:
    input("Press Enter to start typing:")
    start_time = time.time()    
    user_input=str(input())
    user_input=user_input.lower()
    end_time=time.time()

    print("\nGenerated Text:", generated_text)
    print("User Input:", user_input)
    
    if(user_input == generated_text):
        total_time_taken=end_time-start_time
        total_time_taken/=60 #(in minutes)
        total_words=len(user_input.split())
        words_per_minute=(total_words/5)/total_time_taken
        print("\nYour typing speed is: ",words_per_minute,"WPM")
    
    else:
        raise ValueError("\nInaccuracy found in your typing, Please try again! ")

except ValueError as e:
    print(e)



