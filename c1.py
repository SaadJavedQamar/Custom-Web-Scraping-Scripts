from bs4 import BeautifulSoup

# Read the HTML content from the file
file_path = 'test.txt'  # Replace with the path to your Notepad file

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all entries containing Name, Address, and Phone
entries = soup.find_all('div', class_='bi-content bi-clic-mobile')

# Extract Name, Address, and Phone from each entry
for entry in entries:
    # Get the Name (in <h3> tag or similar)
    name = entry.find('h3').text if entry.find('h3') else 'No name found'
    
    # Get the Address (in <div class="bi-address small"> or similar)
    address = entry.find('div', class_='bi-address small').text.strip() if entry.find('div', class_='bi-address small') else 'No address found'
    
    # Get the Phone (look for <a> tags with href starting with "tel:")
    phone = entry.find('a', href=True)
    if phone and 'tel:' in phone['href']:
        phone = phone['href'].replace('tel:', '')  # Extract the phone number
    else:
        phone = 'Phone not found'
    
    # Print the extracted data
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone: {phone}")
    print("-" * 50)
