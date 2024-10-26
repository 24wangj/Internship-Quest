import openai
import PyPDF2


openai.api_key = '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'

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def makeResponse(input):
    # Make a request to the ChatGPT API
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
        messages=[
            {"role": "user", "content": "Based on the inputted resume output information exactly in the format with no deviation Major - GPA - Feild of interest - Skills where each word is replaced and removed by the information and the dashes are used as seperators. Seperate each skill with a comma and each skill should be one or two words. Here is the resume: "+input}
     ]
    
    )

def createListInfo(filePath):
    input = makeResponse(extract_text_from_pdf(filePath))['choices'][0]['message']['content']
    words = input.split(" - ")
    return [words[0], words[1], words[2], words[3].split(",")]

print(createListInfo("C:/Users/keega/Documents/Internship-Quest/InternshipQuest/InternshipQuest/testResume.pdf"))

