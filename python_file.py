
# r read
# w write
# a append

file_name = 'example.txt'

"""using "with" is better than "try and except" since it would handle except and close the file for you"""
with open(file_name, 'w') as example_file:

    lines = [
        'Happy whale on parade!\n',
        "Red Bee dacing\n",
        "The great gig in the sky!\n"
             ]

    example_file.writelines(lines)

    """ this is redundant as "with" syntax is used"""
    # example_file.close()

file_content = ''
with open(file_name, 'r') as reading_file:

    file_content = reading_file.read()

counter = 0
new_content = []

for character in file_content:

    if counter % 2 == 0:
        new_content.append(character.upper())
    else:
        new_content.append(character.lower())

    counter += 1

    print(character)

# join all character into one string
new_content = ''.join(new_content)
with open(file_name, 'w') as writeable_file:
    writeable_file.write(new_content)

# with open(file_name, 'r') as reading_file:
#     # passing list args will iterate the list item for you
#     text = reading_file.read()
#     print(text)
#     # for line in reading_file.readlines():
#     #     print(line)



# example_file = open(file_name, 'w')
#
# try:
#     example_file.write("Blue Goose on the loose")
#     example_file.write("Honeycomb cereal\n")
#
# except Exception as error:
#     print ("Problem handling file, error was %s") % error
#
# finally:
#     example_file.close()

